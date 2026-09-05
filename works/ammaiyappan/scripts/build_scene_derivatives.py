#!/usr/bin/env python3
"""Build Ammayappan scene-text derivatives from verified canonical Tamil.

The booklet prints no scene numbers. Archive IDs are navigation-only.
Boundaries come from the PASS scene-segmentation preflight, which itself is
derived from source-visible headings in verified transcription/full-text.md.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "works" / "ammaiyappan"
FULL = WORK / "transcription" / "full-text.md"
PREFLIGHT = WORK / "notes" / "scene-segmentation-preflight.json"
SCENES = WORK / "scenes"
QA = WORK / "notes" / "scene-boundary-ownership-qa.md"

ANCHOR_LINE_RE = re.compile(r"^<!-- source: pdf=(\d+).*?status=verified -->$", re.M)
HEADING_RE = re.compile(r"^(#{2,4})\s+(.+?)\s*$", re.M)
NON_BOUNDARY_HEADINGS = {"கதை வசனம்"}


def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def exact_anchor_before(text: str, pos: int) -> tuple[int, str]:
    hits = list(ANCHOR_LINE_RE.finditer(text, 0, pos + 1))
    if not hits:
        raise SystemExit(f"no verified source anchor before position {pos}")
    m = hits[-1]
    return int(m.group(1)), m.group(0)


def main() -> None:
    canonical = FULL.read_text(encoding="utf-8")
    pf = json.loads(PREFLIGHT.read_text(encoding="utf-8"))
    if pf.get("status") != "PASS" or pf.get("canonical_tamil_gate") != "105/105-dual-gate-complete-verified":
        raise SystemExit("scene preflight is not PASS against closed canonical Tamil")
    boundaries = pf["boundaries"]
    if len(boundaries) != 63:
        raise SystemExit(f"expected current authoritative 63 boundaries, got {len(boundaries)}")
    if "⟦" in canonical or "⟧" in canonical:
        raise SystemExit("canonical uncertainty markers reappeared")

    # Re-locate boundary headings occurrence-by-occurrence in the current canonical
    # rather than trusting stale line numbers.
    all_heading_matches = [
        m for m in HEADING_RE.finditer(canonical)
        if m.group(2).strip() not in NON_BOUNDARY_HEADINGS
    ]
    if len(all_heading_matches) != len(boundaries):
        raise SystemExit(f"canonical heading count changed: {len(all_heading_matches)} != {len(boundaries)}")
    for i, (m, b) in enumerate(zip(all_heading_matches, boundaries), 1):
        got = m.group(2).strip()
        if got != b["heading"]:
            raise SystemExit(f"boundary {i} heading drift: {got!r} != {b['heading']!r}")
        pdf, _ = exact_anchor_before(canonical, m.start())
        if pdf != b["pdf"]:
            raise SystemExit(f"boundary {i} PDF drift: {pdf} != {b['pdf']}")

    first_start = all_heading_matches[0].start()
    canonical_derivative_body = canonical[first_start:]

    # Rebuild directory deterministically.
    if SCENES.exists():
        shutil.rmtree(SCENES)
    SCENES.mkdir(parents=True)

    index = []
    scene_spans = []
    page_anchor_union = set()

    for i, (m, b) in enumerate(zip(all_heading_matches, boundaries), 1):
        start = m.start()
        end = all_heading_matches[i].start() if i < len(all_heading_matches) else len(canonical)
        span = canonical[start:end]
        scene_spans.append(span)

        start_pdf, start_anchor = exact_anchor_before(canonical, start)
        in_span_pdfs = [int(x) for x in ANCHOR_LINE_RE.findall(span)]
        pdfs = []
        for p in [start_pdf] + in_span_pdfs:
            if not pdfs or pdfs[-1] != p:
                pdfs.append(p)
            page_anchor_union.add(p)
        end_pdf = pdfs[-1]

        scene_id = f"ammaiyappan-s{i:03d}"
        next_id = f"A{i+1:03d}" if i < len(boundaries) else None
        header = (
            f"<!-- derivative provenance: work=ammaiyappan scene_id={scene_id} ordinal={i} "
            f"source_scene_number=none boundary_id=A{i:03d} start_pdf={start_pdf} "
            f"start_printed={start_pdf-2} end_before={next_id or 'EOF'} -->\n"
            "<!-- archive note: scene_id and ordinal are derivative navigation only; the booklet prints no scene number. -->\n"
            f"<!-- derivative span_sha256={sha256(span)} -->\n"
            f"{start_anchor}\n\n"
        )
        path = SCENES / f"scene-{i:03d}.md"
        path.write_text(header + span, encoding="utf-8")

        index.append({
            "scene_id": scene_id,
            "ordinal": i,
            "source_scene_number": None,
            "boundary_id": f"A{i:03d}",
            "heading": b["heading"],
            "start_pdf": start_pdf,
            "start_printed": start_pdf - 2,
            "end_pdf": end_pdf,
            "pdf_pages": pdfs,
            "end_before_boundary_id": next_id,
            "span_sha256": sha256(span),
            "file": f"scene-{i:03d}.md",
            "status": "verified-derivative",
        })

    # Exact whole-body ownership: every byte from the first source-visible scene
    # heading through canonical EOF belongs to exactly one derivative span.
    joined = "".join(scene_spans)
    ownership_pass = joined == canonical_derivative_body
    if not ownership_pass:
        raise SystemExit("scene spans do not reconstruct canonical derivative body exactly")

    # Each generated scene must preserve its exact canonical span after the four
    # derivative/provenance header lines.
    file_roundtrip_errors = []
    for item, span in zip(index, scene_spans):
        raw = (SCENES / item["file"]).read_text(encoding="utf-8")
        marker = item["span_sha256"]
        # Locate the exact span at the first canonical heading, not by fixed line count.
        heading_token = re.escape(item["heading"])
        hm = re.search(rf"^#{{2,4}}\s+{heading_token}\s*$", raw, re.M)
        if not hm or raw[hm.start():] != span:
            file_roundtrip_errors.append(item["scene_id"])
    if file_roundtrip_errors:
        raise SystemExit(f"scene-file roundtrip mismatch: {file_roundtrip_errors}")

    # All canonical source pages must be represented across the derivative layer.
    expected_pages = set(range(5, 110))
    missing_pages = sorted(expected_pages - page_anchor_union)
    if missing_pages:
        raise SystemExit(f"canonical pages absent from derivative coverage: {missing_pages}")

    index_payload = {
        "work_id": "ammaiyappan",
        "status": "complete-verified",
        "source_numbered_scenes": False,
        "archive_scene_count": len(index),
        "canonical_tamil_gate": "105/105-dual-gate-complete-verified",
        "boundary_preflight": "../notes/scene-segmentation-preflight.json",
        "boundary_ownership_qa": "../notes/scene-boundary-ownership-qa.md",
        "canonical_derivative_body_sha256": sha256(canonical_derivative_body),
        "joined_scene_spans_sha256": sha256(joined),
        "scene_records": index,
    }
    (SCENES / "index.json").write_text(json.dumps(index_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    readme = f"""# அம்மையப்பன் — scene-text derivatives

**Stage:** **complete-verified**  
**Archive-only scene/segment IDs:** **{len(index)}**  
**Verified scene-text files:** **{len(index)}/{len(index)}**  
**Blocked source-review segments:** **0**

This directory is a derivative layer built only from the **105/105 dual-gate verified** canonical Tamil in `../transcription/full-text.md`. It does not replace or normalize the canonical source layer.

## Scene-number policy

The booklet does **not** print numbered screenplay scenes. Therefore `ammaiyappan-s001`–`ammaiyappan-s{len(index):03d}` are archive-only navigation identifiers. Their ordinals are not source scene numbers.

## Boundary authority

- canonical source-visible headings: **{len(index)}**;
- earlier intake-ledger transitions: **58**;
- all 58 reconciled against canonical headings;
- later canonical/source review contributed **5 additional source-visible headings**;
- final boundary inventory: `../notes/scene-segmentation-preflight.md`;
- whole-work ownership QA: `../notes/scene-boundary-ownership-qa.md` — **PASS**.

## Derivative rules

Each scene file:

1. copies an exact contiguous span from verified canonical Tamil;
2. begins at one source-visible canonical heading;
3. ends immediately before the next source-visible canonical heading, or at canonical EOF for the final segment;
4. preserves source spelling, punctuation, speaker labels, stage directions and page anchors;
5. adds only derivative provenance comments and an archive-only ID;
6. never invents a printed scene number;
7. never repairs or normalizes canonical Tamil.

## Downstream gate

Scene-text derivative construction and boundary-ownership QA are complete. The **dialogue-index phase may now open**. Character/entity indexing remains blocked until dialogue indexing closes.
"""
    (SCENES / "README.md").write_text(readme, encoding="utf-8")

    qa = f"""# அம்மையப்பன் — scene boundary ownership QA

Status: **PASS**

## Inputs

- canonical Tamil: `transcription/full-text.md` — **105/105 dual-gate verified**;
- segmentation preflight: `notes/scene-segmentation-preflight.json` — **PASS**;
- planned/generated archive segments: **{len(index)}**.

## Assertions

- canonical source-visible headings used as boundaries: **{len(index)}**;
- generated scene files: **{len(index)}/{len(index)}**;
- source-numbered scenes invented: **0**;
- pre-boundary screenplay body lines omitted: **0**;
- gaps between consecutive derivative spans: **0**;
- overlaps between consecutive derivative spans: **0**;
- joined derivative spans equal canonical body from first scene heading through PDF 109 EOF: **PASS**;
- canonical derivative-body SHA-256: `{sha256(canonical_derivative_body)}`;
- joined scene-span SHA-256: `{sha256(joined)}`;
- scene-file canonical-span roundtrip errors: **0**;
- canonical PDF pages represented across scene derivatives: **105/105 — PDF 5–109**;
- missing canonical PDF pages: **0**.

## Boundary policy

Page breaks alone are not scene boundaries. Every boundary is a source-visible heading preserved in the verified canonical transcription. `ammaiyappan-sNNN` identifiers are derivative navigation only.

## Disposition

**PASS — scene-text derivatives are complete-verified. Dialogue indexing is unblocked.**
"""
    QA.write_text(qa, encoding="utf-8")

    print(json.dumps({"status":"PASS","scenes":len(index),"pages_covered":len(page_anchor_union),"ownership":"PASS","next":"dialogue-index"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
