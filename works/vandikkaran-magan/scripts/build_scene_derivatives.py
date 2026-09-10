#!/usr/bin/env python3
"""Build source-led scene-text derivatives for வண்டிக்காரன் மகன்.

Canonical authority for this derivative layer is the closed source-verified
transcription in transcription/pages/006.md through 087.md.  The source prints
scene headings, so source scene labels are retained exactly; scene-NNN filenames
are derivative ordinals only.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "works" / "vandikkaran-magan"
PAGES = WORK / "transcription" / "pages"
SCENES = WORK / "scenes"
QA = WORK / "notes" / "scene-boundary-ownership-qa.md"

EXPECTED_IDS = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10-எ",
    "11", "12", "13", "14", "14-எ", "15", "16", "16-எ", "17",
    "18", "19", "20", "20-எ", "21", "22", "22-எ", "23", "24",
    "24-எ", "24-பி", "24-சி", "24-டி", "25", "26", "27", "28",
    "29", "29-எ", "30", "31", "32", "33", "33-எ", "34", "35",
    "36", "37", "38", "39", "40", "41", "42", "42-எ", "43",
    "44", "45-46", "47", "48", "49", "50", "51", "52", "53",
    "53-எ", "53-பி", "53-சி", "53-டி", "54", "55", "56",
]

SOURCE_META_RE = re.compile(
    r"\A<!-- source: pdf=(\d+).*?status=visual-verified -->\n?"
)
SCENE_HEADING_RE = re.compile(r"^##\s+(காட்சி.*)$", re.M)
SUFFIXES = "எபிசிடி"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_page(pdf: int) -> str:
    path = PAGES / f"{pdf:03d}.md"
    raw = path.read_text(encoding="utf-8")
    m = SOURCE_META_RE.match(raw)
    if not m or int(m.group(1)) != pdf:
        raise SystemExit(f"invalid canonical source wrapper: {path}")
    body = raw[m.end():]
    if body.startswith("\n"):
        body = body[1:]
    return body.rstrip("\n")


def heading_scene_id(heading: str) -> str:
    if not heading.startswith("காட்சி"):
        raise SystemExit(f"not a scene heading: {heading!r}")
    tail = heading[len("காட்சி"):].replace("—", "-").replace("–", "-").strip()
    m = re.search(
        rf"(\d+\s*-\s*\d+|\d+)(?:\s*-*\s*([{SUFFIXES}]))?\s*$",
        tail,
    )
    if not m:
        raise SystemExit(f"cannot decode source scene id from {heading!r}")
    base = re.sub(r"\s*-\s*", "-", m.group(1))
    suffix = m.group(2)
    return f"{base}-{suffix}" if suffix else base


def location_from_span(span: str) -> str | None:
    lines = span.splitlines()[1:]
    values: list[str] = []
    started = False
    for raw in lines:
        line = raw.strip()
        if not line:
            if not started:
                continue
            # Permit blank lines between multi-line location captions.
            continue
        value = None
        if line.startswith("### "):
            value = line[4:].strip()
        elif line.startswith("**") and line.endswith("**") and len(line) > 4:
            value = line[2:-2].strip()
        if value is None:
            break
        started = True
        values.append(value)
    return " / ".join(values) if values else None


def main() -> None:
    stream = ""
    page_ranges: dict[int, tuple[int, int]] = {}
    for pdf in range(6, 88):
        body = load_page(pdf)
        if stream:
            stream += "\n\n"
        start = len(stream)
        stream += body
        page_ranges[pdf] = (start, len(stream))

    if "⟦" in stream or "⟧" in stream:
        raise SystemExit("canonical uncertainty markers reappeared")

    headings = list(SCENE_HEADING_RE.finditer(stream))
    if len(headings) != 71:
        raise SystemExit(f"expected 71 source scene headings, found {len(headings)}")

    observed_ids = [heading_scene_id(m.group(1).strip()) for m in headings]
    if observed_ids != EXPECTED_IDS:
        raise SystemExit(
            "source scene-heading sequence drifted:\n"
            f"expected={EXPECTED_IDS}\nobserved={observed_ids}"
        )

    pre_scene = stream[: headings[0].start()]
    if pre_scene.strip() != "# வண்டிக்காரன் மகன்":
        raise SystemExit(f"unexpected pre-scene screenplay material: {pre_scene!r}")
    canonical_scene_body = stream[headings[0].start():]

    if SCENES.exists():
        shutil.rmtree(SCENES)
    SCENES.mkdir(parents=True)

    records = []
    spans: list[str] = []
    covered_pages: set[int] = set()

    for ordinal, (scene_id, m) in enumerate(zip(EXPECTED_IDS, headings), 1):
        start = m.start()
        end = headings[ordinal].start() if ordinal < len(headings) else len(stream)
        span = stream[start:end]
        spans.append(span)

        source_heading = m.group(1).strip()
        markdown_heading = m.group(0)
        included_pages: list[int] = []
        for pdf, (p_start, p_end) in page_ranges.items():
            a, b = max(start, p_start), min(end, p_end)
            if a < b and stream[a:b].strip():
                included_pages.append(pdf)
                covered_pages.add(pdf)
        if not included_pages:
            raise SystemExit(f"scene {scene_id} has no canonical page ownership")

        pdf_start, pdf_end = included_pages[0], included_pages[-1]
        printed_start, printed_end = pdf_start - 1, pdf_end - 1
        canonical_paths = [f"transcription/pages/{p:03d}.md" for p in included_pages]
        scene_file = f"scene-{ordinal:03d}.md"
        span_hash = sha256(span)
        provenance = (
            f"<!-- derivative provenance: work=vandikkaran-magan ordinal={ordinal} "
            f"source_scene_id={scene_id} pdf={pdf_start}-{pdf_end} "
            f"printed={printed_start}-{printed_end} "
            f"canonical={','.join(canonical_paths)} -->\n"
            f"<!-- derivative span_sha256={span_hash} -->\n\n"
        )
        (SCENES / scene_file).write_text(provenance + span, encoding="utf-8")

        records.append(
            {
                "scene_id": scene_id,
                "ordinal": ordinal,
                "source_heading": source_heading,
                "source_heading_markdown": markdown_heading,
                "location": location_from_span(span),
                "pdf_start": pdf_start,
                "printed_start": printed_start,
                "pdf_end": pdf_end,
                "printed_end": printed_end,
                "pdf_pages": included_pages,
                "canonical_paths": canonical_paths,
                "scene_path": f"scenes/{scene_file}",
                "span_sha256": span_hash,
                "status": "verified-derivative",
            }
        )

    joined = "".join(spans)
    if joined != canonical_scene_body:
        raise SystemExit("scene spans do not reconstruct canonical scene-bearing body exactly")

    expected_pages = set(range(6, 88))
    if covered_pages != expected_pages:
        raise SystemExit(
            f"scene page coverage drift: missing={sorted(expected_pages-covered_pages)} "
            f"unexpected={sorted(covered_pages-expected_pages)}"
        )

    for record, span in zip(records, spans):
        raw = (WORK / record["scene_path"]).read_text(encoding="utf-8")
        marker = "\n\n" + span
        if not raw.endswith(marker):
            raise SystemExit(f"scene derivative roundtrip mismatch: {record['scene_id']}")

    index = {
        "work_id": "vandikkaran-magan",
        "status": "complete-verified",
        "source": {
            "filename": "TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf",
            "sha256": "03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253",
            "authority": "attached-pdf-only",
        },
        "canonical_transcription_index": "../transcription/index.json",
        "mapping": "../mapping.md",
        "source_numbered_scenes": True,
        "total_scenes": 71,
        "ordered_scene_ids": EXPECTED_IDS,
        "scene_body_scope": "PDF 6–87 from first source scene heading through screenplay EOF",
        "pre_scene_work_header": "# வண்டிக்காரன் மகன்",
        "canonical_scene_body_sha256": sha256(canonical_scene_body),
        "joined_scene_spans_sha256": sha256(joined),
        "scenes": records,
        "qa": {
            "continuity": "pass",
            "duplicates": "none",
            "loss": "none",
            "scene_heading_count": 71,
            "gaps": 0,
            "overlaps": 0,
            "screenplay_pdf_coverage": "82/82 — PDF 6–87",
            "source_text_policy": "Exact canonical Tamil scene spans; no spelling, punctuation, speaker-label, stage-direction, heading, or performance-text normalization.",
            "location_policy": "Source location captions remain in scene text; index location is derivative navigation metadata only.",
            "span_policy": "Scene begins at its source-visible scene heading and ends immediately before the next source-visible scene heading; the final scene ends at screenplay EOF.",
        },
    }
    (SCENES / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    readme = f"""# வண்டிக்காரன் மகன் — scene-text derivatives

**Stage:** **COMPLETE-VERIFIED**  
**Source-visible scene-heading occurrences:** **71**  
**Generated scene-text derivatives:** **71/71**  
**Boundary ownership:** **PASS — 0 gaps / 0 overlaps / 0 duplicate text ownership**

This directory is a source-led derivative layer built only from the closed canonical Tamil screenplay in `../transcription/pages/006.md` through `087.md`. It does not replace or normalize the canonical source layer.

## Source-scene policy

The booklet prints its own scene labels. `scene-001.md` through `scene-071.md` are derivative filenames only; the authoritative source labels remain the 71-item sequence recorded in `index.json` and `../notes/scene-heading-audit.md`, including suffix inserts and the combined `45-46` heading.

## Boundary policy

Each derivative begins at one source-visible `காட்சி` heading and ends immediately before the next source-visible `காட்சி` heading, or at screenplay EOF for scene `56`. Cross-page continuations stay with their owning scene. Decorative stars, song/performance blocks, source location captions, spelling, punctuation, speaker labels and stage directions are preserved inside the exact canonical span.

PDF 4–5 foreword and PDF 88–90 credit/back-cover matter are not synthetic scenes. The work-title line before scene 1 on PDF 6 is work-level metadata, not scene body.

## QA

- source-heading count: **71/71**;
- screenplay page coverage represented by scene spans: **82/82 — PDF 6–87**;
- canonical scene-bearing body reconstructed by ordered scene spans: **PASS**;
- gaps / overlaps: **0 / 0**;
- derivative roundtrip errors: **0**;
- canonical scene-body SHA-256: `{sha256(canonical_scene_body)}`;
- joined derivative-span SHA-256: `{sha256(joined)}`.

See `../notes/scene-boundary-ownership-qa.md` for the durable QA record.

## Downstream gate

Scene-text derivatives are **COMPLETE-VERIFIED**. Dialogue indexing may now open. Character/entity indexing remains blocked until dialogue indexing closes.
"""
    (SCENES / "README.md").write_text(readme, encoding="utf-8")

    qa = f"""# வண்டிக்காரன் மகன் — scene boundary ownership QA

Status: **PASS**

## Inputs

- closed canonical Tamil screenplay: `transcription/pages/006.md`–`087.md`;
- source-heading authority: `notes/scene-heading-audit.md` — **71 observed occurrences**;
- generated source-led scene derivatives: **71**.

## Assertions

- source-visible scene headings used as boundaries: **71/71**;
- generated scene files: **71/71**;
- source scene labels normalized or renumbered: **0**;
- source-text corrections performed by derivative builder: **0**;
- gaps between consecutive scene spans: **0**;
- overlaps between consecutive scene spans: **0**;
- ordered scene spans reconstruct the canonical scene-bearing body exactly: **PASS**;
- canonical scene-body SHA-256: `{sha256(canonical_scene_body)}`;
- joined scene-span SHA-256: `{sha256(joined)}`;
- derivative file roundtrip errors: **0**;
- screenplay PDF pages represented: **82/82 — PDF 6–87**;
- missing screenplay PDF pages: **0**;
- excluded non-scene matter: PDF 4–5 foreword, PDF 88–90 credits/back cover, and the work-title line preceding scene 1 on PDF 6.

## Boundary ownership rule

A scene begins at its source-visible `காட்சி` heading and owns every canonical character until immediately before the next source-visible `காட்சி` heading. Page breaks are not boundaries. Multiple scene starts on one source page are allowed. A single source page may therefore be referenced by more than one scene without duplicate text ownership.

## Disposition

**PASS — 71/71 source-led scene-text derivatives are complete-verified. Dialogue indexing is unblocked.**
"""
    QA.write_text(qa, encoding="utf-8")

    print(
        json.dumps(
            {
                "status": "PASS",
                "scenes": 71,
                "pages_covered": len(covered_pages),
                "gaps": 0,
                "overlaps": 0,
                "next": "dialogue-index",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
