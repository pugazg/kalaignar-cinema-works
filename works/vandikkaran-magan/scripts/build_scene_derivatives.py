#!/usr/bin/env python3
"""Build source-led scene-text derivatives for வண்டிக்காரன் மகன்.

Canonical authority is the closed verified screenplay transcription in
transcription/pages/006.md through 087.md. Source scene headings are preserved
verbatim; scene-NNN filenames are derivative ordinals only.
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

EXPECTED = [
    ("1",6),("2",8),("3",9),("4",9),("4-எ",10),("5",12),("6",13),("7",13),
    ("8",16),("9",17),("10",18),("10-எ",19),("11",20),("12",22),("13",24),
    ("14",25),("14-எ",27),("15",28),("16",29),("16-எ",29),("17",30),("18",31),
    ("19",33),("20",35),("20-எ",37),("21",39),("22",40),("22-எ",40),("23",42),
    ("24",42),("24-எ",44),("24-பி",44),("24-சி",46),("24-டி",47),("25",48),
    ("26",50),("27",51),("28",52),("29",53),("29-எ",55),("30",55),("31",55),
    ("32",56),("33",58),("33-எ",59),("34",59),("35",60),("36",60),("37",61),
    ("38",62),("39",64),("40",65),("41",66),("42",67),("42-எ",68),("43",70),
    ("44",71),("45-46",71),("47",72),("48",72),("49",75),("50",76),("51",76),
    ("52",78),("53",81),("53-எ",81),("53-பி",81),("53-சி",81),("53-டி",83),
    ("54",85),("55",86),("56",87),
]

SOURCE_META_RE = re.compile(r"\A<!-- source: pdf=(\d+).*?status=visual-verified -->\n?")
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


def scene_id_from_heading(heading: str) -> str:
    tail = heading[len("காட்சி"):].replace("—", "-").replace("–", "-").strip()
    tail = tail.rstrip(".… ").strip()
    tail = re.sub(r"\s+", " ", tail)
    tail = re.sub(r"\s*-\s*", "-", tail).strip("- ")
    m = re.fullmatch(r"(\d+(?:-\d+)?)(?:[-\s]+((?:எ|பி|சி|டி)))?", tail)
    if not m:
        raise SystemExit(f"cannot decode scene id from {heading!r}; normalized={tail!r}")
    base, suffix = m.groups()
    return f"{base}-{suffix}" if suffix else base


def location_from_span(span: str) -> str | None:
    values: list[str] = []
    for raw in span.splitlines()[1:]:
        line = raw.strip()
        if not line:
            if not values:
                continue
            continue
        if line.startswith("### "):
            values.append(line[4:].strip())
            continue
        if line.startswith("**") and line.endswith("**") and len(line) > 4:
            values.append(line[2:-2].strip())
            continue
        break
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
    if len(headings) != len(EXPECTED):
        raise SystemExit(f"expected {len(EXPECTED)} source scene headings, found {len(headings)}")

    observed = []
    for m in headings:
        pdf = next(p for p, (a, b) in page_ranges.items() if a <= m.start() < b)
        observed.append((scene_id_from_heading(m.group(1).strip()), pdf))
    if observed != EXPECTED:
        raise SystemExit(f"scene sequence/start-page drift:\nexpected={EXPECTED}\nobserved={observed}")

    pre_scene = stream[:headings[0].start()]
    if pre_scene.strip() != "# வண்டிக்காரன் மகன்":
        raise SystemExit(f"unexpected pre-scene screenplay material: {pre_scene!r}")
    canonical_scene_body = stream[headings[0].start():]

    if SCENES.exists():
        shutil.rmtree(SCENES)
    SCENES.mkdir(parents=True)

    records = []
    spans: list[str] = []
    covered_pages: set[int] = set()

    for ordinal, ((scene_id, expected_pdf), m) in enumerate(zip(EXPECTED, headings), 1):
        start = m.start()
        end = headings[ordinal].start() if ordinal < len(headings) else len(stream)
        span = stream[start:end]
        spans.append(span)

        pages = []
        for pdf, (p_start, p_end) in page_ranges.items():
            a, b = max(start, p_start), min(end, p_end)
            if a < b and stream[a:b].strip():
                pages.append(pdf)
                covered_pages.add(pdf)
        if not pages or pages[0] != expected_pdf:
            raise SystemExit(f"scene {scene_id} start-page drift: {pages[:1]} != [{expected_pdf}]")

        pdf_start, pdf_end = pages[0], pages[-1]
        canonical_paths = [f"transcription/pages/{p:03d}.md" for p in pages]
        span_hash = sha256(span)
        scene_file = f"scene-{ordinal:03d}.md"
        provenance = (
            f"<!-- derivative provenance: work=vandikkaran-magan ordinal={ordinal} "
            f"source_scene_id={scene_id} pdf={pdf_start}-{pdf_end} "
            f"printed={pdf_start-1}-{pdf_end-1} canonical={','.join(canonical_paths)} -->\n"
            f"<!-- derivative span_sha256={span_hash} -->\n\n"
        )
        (SCENES / scene_file).write_text(provenance + span, encoding="utf-8")
        records.append({
            "scene_id": scene_id,
            "ordinal": ordinal,
            "source_heading": m.group(1).strip(),
            "source_heading_markdown": m.group(0),
            "location": location_from_span(span),
            "pdf_start": pdf_start,
            "printed_start": pdf_start - 1,
            "pdf_end": pdf_end,
            "printed_end": pdf_end - 1,
            "pdf_pages": pages,
            "canonical_paths": canonical_paths,
            "scene_path": f"scenes/{scene_file}",
            "span_sha256": span_hash,
            "status": "verified-derivative",
        })

    joined = "".join(spans)
    if joined != canonical_scene_body:
        raise SystemExit("scene spans do not reconstruct canonical scene body exactly")
    expected_pages = set(range(6, 88))
    if covered_pages != expected_pages:
        raise SystemExit(f"page coverage drift: missing={sorted(expected_pages-covered_pages)}")

    for record, span in zip(records, spans):
        raw = (WORK / record["scene_path"]).read_text(encoding="utf-8")
        if not raw.endswith("\n\n" + span):
            raise SystemExit(f"roundtrip mismatch: {record['scene_id']}")

    body_hash = sha256(canonical_scene_body)
    ids = [scene_id for scene_id, _ in EXPECTED]
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
        "total_scenes": len(records),
        "ordered_scene_ids": ids,
        "scene_body_scope": "PDF 6–87 from first source scene heading through screenplay EOF",
        "pre_scene_work_header": "# வண்டிக்காரன் மகன்",
        "canonical_scene_body_sha256": body_hash,
        "joined_scene_spans_sha256": sha256(joined),
        "scenes": records,
        "qa": {
            "continuity": "pass", "duplicates": "none", "loss": "none",
            "scene_heading_count": len(records), "gaps": 0, "overlaps": 0,
            "screenplay_pdf_coverage": "82/82 — PDF 6–87",
            "source_text_policy": "Exact canonical Tamil scene spans; no spelling, punctuation, speaker-label, stage-direction, heading, or performance-text normalization.",
            "location_policy": "Source location captions remain in scene text; index location is derivative navigation metadata only.",
            "span_policy": "Scene begins at its source-visible scene heading and ends immediately before the next source-visible scene heading; the final scene ends at screenplay EOF.",
        },
    }
    (SCENES / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    readme = f"""# வண்டிக்காரன் மகன் — scene-text derivatives

**Stage:** **COMPLETE-VERIFIED**  
**Source-visible scene-heading occurrences:** **{len(records)}**  
**Generated scene-text derivatives:** **{len(records)}/{len(records)}**  
**Boundary ownership:** **PASS — 0 gaps / 0 overlaps / 0 duplicate text ownership**

This directory is built only from the closed canonical Tamil screenplay in `../transcription/pages/006.md` through `087.md`. It does not replace or normalize the canonical source layer.

## Source-scene policy

The booklet prints its own scene labels. `scene-001.md` through `scene-{len(records):03d}.md` are derivative filenames only. The authoritative labels are the {len(records)}-item sequence in `index.json`, including source-visible `4-எ` at PDF 10, later suffix inserts, and combined `45-46`.

## Boundary policy

Each derivative begins at a source-visible `காட்சி` heading and ends immediately before the next such heading, or at screenplay EOF for scene `56`. Cross-page continuations, decorative stars, songs, location captions, spelling, punctuation, speaker labels and stage directions remain inside their exact canonical span.

PDF 4–5 foreword and PDF 88–90 credit/back-cover matter are excluded. The work-title line before scene 1 on PDF 6 is work-level metadata, not scene body.

## QA

- source-heading count: **{len(records)}/{len(records)}**;
- screenplay page coverage: **82/82 — PDF 6–87**;
- ordered spans reconstruct canonical scene body: **PASS**;
- gaps / overlaps: **0 / 0**;
- derivative roundtrip errors: **0**;
- canonical scene-body SHA-256: `{body_hash}`;
- joined derivative-span SHA-256: `{sha256(joined)}`.

See `../notes/scene-boundary-ownership-qa.md`.

## Downstream gate

Scene-text derivatives are **COMPLETE-VERIFIED**. Dialogue indexing may now open. Character/entity indexing remains blocked until dialogue indexing closes.
"""
    (SCENES / "README.md").write_text(readme, encoding="utf-8")

    qa = f"""# வண்டிக்காரன் மகன் — scene boundary ownership QA

Status: **PASS**

## Inputs

- closed canonical Tamil screenplay: `transcription/pages/006.md`–`087.md`;
- source-visible canonical scene headings: **{len(records)}**;
- generated source-led scene derivatives: **{len(records)}**.

## Corrective boundary finding

Derivative construction exposed one stale inventory omission: canonical PDF 10 contains source-visible `காட்சி — 4 எ.`. It is a real scene boundary and is retained as source scene ID `4-எ`. The earlier 71-heading inventory is superseded by the canonical **72-heading** sequence.

## Assertions

- source-visible scene headings used as boundaries: **{len(records)}/{len(records)}**;
- generated scene files: **{len(records)}/{len(records)}**;
- source scene labels normalized or renumbered in scene text: **0**;
- source-text corrections performed by derivative builder: **0**;
- gaps between consecutive scene spans: **0**;
- overlaps between consecutive scene spans: **0**;
- ordered scene spans reconstruct the canonical scene-bearing body exactly: **PASS**;
- canonical scene-body SHA-256: `{body_hash}`;
- joined scene-span SHA-256: `{sha256(joined)}`;
- derivative file roundtrip errors: **0**;
- screenplay PDF pages represented: **82/82 — PDF 6–87**;
- missing screenplay PDF pages: **0**;
- excluded non-scene matter: PDF 4–5 foreword, PDF 88–90 credits/back cover, and the work-title line preceding scene 1 on PDF 6.

## Boundary ownership rule

A scene begins at its source-visible `காட்சி` heading and owns every canonical character until immediately before the next source-visible `காட்சி` heading. Page breaks are not boundaries. Multiple scene starts on one page are allowed without duplicate text ownership.

## Disposition

**PASS — {len(records)}/{len(records)} source-led scene-text derivatives are complete-verified. Dialogue indexing is unblocked.**
"""
    QA.write_text(qa, encoding="utf-8")

    print(json.dumps({"status":"PASS","scenes":len(records),"pages_covered":len(covered_pages),"gaps":0,"overlaps":0,"next":"dialogue-index"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
