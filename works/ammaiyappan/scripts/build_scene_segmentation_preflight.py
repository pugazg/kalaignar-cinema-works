#!/usr/bin/env python3
"""Build a source-derived scene/segment preflight for Ammayappan.

Authority order:
1. verified canonical transcription/full-text.md;
2. source-visible transition intake ledger for reconciliation/history.

This does not create scene files. It establishes the complete boundary candidate
inventory after canonical Tamil closure, including headings discovered during
transcription that were absent from the earlier intake ledger.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "works" / "ammaiyappan"
FULL = WORK / "transcription" / "full-text.md"
LEDGER = WORK / "notes" / "scene-heading-audit.md"
OUT_MD = WORK / "notes" / "scene-segmentation-preflight.md"
OUT_JSON = WORK / "notes" / "scene-segmentation-preflight.json"

ANCHOR_RE = re.compile(r"<!-- source: pdf=(\d+)(?:\s+logical_printed=(\d+)|\s+printed=(\d+))?.*?status=verified -->")
HEADING_RE = re.compile(r"^(#{2,4})\s+(.+?)\s*$")
LEDGER_RE = re.compile(r"^\|\s*\d+\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|")

# Document-level wrapper, not a screenplay transition.
NON_BOUNDARY_HEADINGS = {"கதை வசனம்"}


def logical_printed(pdf: int) -> int:
    return pdf - 2


def main() -> None:
    text = FULL.read_text(encoding="utf-8")
    if "⟦" in text or "⟧" in text:
        raise SystemExit("canonical text is not uncertainty-free")

    current_pdf = None
    candidates = []
    first_candidate_offset = None
    offset = 0
    for line_no, line in enumerate(text.splitlines(keepends=True), 1):
        m = ANCHOR_RE.search(line)
        if m:
            current_pdf = int(m.group(1))
        hm = HEADING_RE.match(line.rstrip("\n"))
        if hm and hm.group(2).strip() not in NON_BOUNDARY_HEADINGS:
            if current_pdf is None:
                raise SystemExit(f"heading before canonical page anchor at line {line_no}: {hm.group(2)}")
            title = hm.group(2).strip()
            candidates.append({
                "ordinal": len(candidates) + 1,
                "boundary_id": f"A{len(candidates)+1:03d}",
                "pdf": current_pdf,
                "printed": logical_printed(current_pdf),
                "heading": title,
                "markdown_level": len(hm.group(1)),
                "line": line_no,
            })
            if first_candidate_offset is None:
                first_candidate_offset = offset
        offset += len(line)

    ledger = []
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        m = LEDGER_RE.match(line)
        if m:
            ledger.append({"pdf": int(m.group(1)), "printed": int(m.group(2)), "heading": m.group(3)})

    # Occurrence-aware reconciliation. Match each ledger occurrence to the first
    # unused canonical candidate with the same PDF + heading.
    unused = set(range(len(candidates)))
    ledger_matches = []
    ledger_missing = []
    for item in ledger:
        hit = next((i for i in sorted(unused) if candidates[i]["pdf"] == item["pdf"] and candidates[i]["heading"] == item["heading"]), None)
        if hit is None:
            ledger_missing.append(item)
        else:
            unused.remove(hit)
            ledger_matches.append({**item, "boundary_id": candidates[hit]["boundary_id"]})
    canonical_additions = [candidates[i] for i in sorted(unused)]

    # Ensure the first body transition owns the opening action. Before the first
    # boundary, only title/wrapper/ornament material may appear after PDF 5 anchor.
    first_anchor_pos = text.find("<!-- source: pdf=5")
    pre = text[first_anchor_pos:first_candidate_offset] if first_candidate_offset is not None else ""
    pre_lines = [x.strip() for x in pre.splitlines() if x.strip()]
    permitted = {
        "<!-- source: pdf=5 logical_printed=3 printed_folio=suppressed status=verified -->",
        "# அம்மையப்பன்",
        "★",
        "## கதை வசனம்",
    }
    unexpected_preboundary = [x for x in pre_lines if x not in permitted]

    if ledger_missing:
        raise SystemExit(f"intake-ledger transitions missing from verified canonical headings: {ledger_missing}")
    if unexpected_preboundary:
        raise SystemExit(f"unexpected screenplay text before first boundary: {unexpected_preboundary}")
    if not candidates or candidates[0]["pdf"] != 5:
        raise SystemExit("first canonical boundary is not on PDF 5")

    # Every candidate will become one archive-only segment, starting at its heading
    # and ending immediately before the next candidate (or canonical EOF).
    for i, c in enumerate(candidates):
        nxt = candidates[i+1] if i + 1 < len(candidates) else None
        c["segment_id"] = f"ammaiyappan-s{i+1:03d}"
        c["source_scene_number"] = None
        c["end_before_boundary_id"] = nxt["boundary_id"] if nxt else None
        c["end_before_heading"] = nxt["heading"] if nxt else None
        c["end_before_pdf"] = nxt["pdf"] if nxt else None

    payload = {
        "work_id": "ammaiyappan",
        "status": "PASS",
        "canonical_tamil_gate": "105/105-dual-gate-complete-verified",
        "source_numbered_scenes": False,
        "segmentation_policy": "one archive-only segment per source-visible canonical heading; segment begins at heading and ends immediately before next canonical heading; final segment ends at canonical EOF",
        "canonical_boundary_candidates": len(candidates),
        "intake_ledger_occurrences": len(ledger),
        "intake_ledger_matched": len(ledger_matches),
        "intake_ledger_missing_from_canonical": ledger_missing,
        "canonical_heading_additions_beyond_intake": canonical_additions,
        "unexpected_preboundary_body_text": unexpected_preboundary,
        "segments_planned": len(candidates),
        "boundaries": candidates,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    rows = "\n".join(
        f"| {c['ordinal']} | `{c['segment_id']}` | {c['boundary_id']} | {c['pdf']} | {c['printed']} | `{c['heading']}` | "
        f"{('EOF' if c['end_before_boundary_id'] is None else c['end_before_boundary_id'])} |"
        for c in candidates
    )
    additions = "\n".join(
        f"- {c['boundary_id']} — PDF {c['pdf']} / logical p.{c['printed']}: `{c['heading']}`"
        for c in canonical_additions
    ) or "- none"

    md = f"""# அம்மையப்பன் — scene segmentation preflight

Status: **PASS**

Authority: verified `transcription/full-text.md` after **105/105 dual-gate Tamil closure**.  
Reconciliation reference: `notes/scene-heading-audit.md`.

## Result

- canonical source-visible boundary headings found: **{len(candidates)}**;
- earlier intake-ledger occurrences: **{len(ledger)}**;
- intake occurrences matched in canonical text: **{len(ledger_matches)}/{len(ledger)}**;
- intake occurrences missing from canonical text: **0**;
- canonical heading occurrences discovered beyond the earlier intake ledger: **{len(canonical_additions)}**;
- screenplay text before first canonical boundary: **0 lines** (only title/wrapper/ornament material precedes it);
- planned archive-only segments: **{len(candidates)}**;
- printed source scene numbers: **none**.

The earlier 58-occurrence intake map is not forced as the final derivative count. The verified canonical text controls later source-visible headings discovered during transcription.

## Canonical additions beyond intake ledger

{additions}

## Segmentation policy

Each source-visible canonical heading begins one derivative segment. The segment owns the exact verified canonical span from that heading through immediately before the next canonical heading. The last segment owns the remainder through PDF 109 canonical EOF. IDs such as `ammaiyappan-s001` are **archive-only navigation IDs**, never printed scene numbers.

## Planned segments

| # | Archive ID | Boundary | Start PDF | Logical p. | Exact source heading | Ends before |
|---:|---|---|---:|---:|---|---|
{rows}

## Gate disposition

This preflight establishes boundaries only; it does not alter canonical Tamil. Scene-file generation may proceed deterministically from this inventory. Before dialogue indexing opens, run whole-work boundary-ownership QA to prove that every canonical screenplay span belongs to exactly one intended scene derivative and no adjacent scene duplicates source text.
"""
    OUT_MD.write_text(md, encoding="utf-8")
    print(json.dumps({"status":"PASS","boundaries":len(candidates),"intake":len(ledger),"canonical_additions":len(canonical_additions),"segments":len(candidates)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
