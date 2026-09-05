#!/usr/bin/env python3
"""Live-main compatible wrapper for Ammayappan final dual-gate closure."""

from __future__ import annotations

import json
from pathlib import Path

import finalize_dual_gate_closure as base


def sync_status_audit_live() -> None:
    p = base.ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
    t = p.read_text(encoding="utf-8")

    # Current matrix row may contain several blocked columns; replace the whole Ammayappan row.
    lines = t.splitlines()
    replacement_row = "| Ammayappan | canonical Tamil **105/105 dual-gate complete-verified; 0 review; 0 unresolved** | scene-text derivatives READY; dialogue/character blocked by gate order | blocked | blocked |"
    found = False
    for i, line in enumerate(lines):
        if line.startswith("| Ammayappan |"):
            lines[i] = replacement_row
            found = True
            break
    if not found:
        raise SystemExit("Ammayappan matrix row missing")
    t = "\n".join(lines) + "\n"

    candidates = [
        "## Ammayappan dual-gate checkpoint through PDF 94",
        "## Ammayappan dual-gate checkpoint after retrospective glyph closure",
        "## Ammayappan canonical-Tamil first-pass closure checkpoint",
    ]
    start = next((m for m in candidates if m in t), None)
    end = "## Manthiri Kumari reconciliation checkpoint"
    if start is None:
        raise SystemExit("no recognized live Ammayappan status-audit section heading")

    section = f"""## Ammayappan final dual-gate Tamil closure

- canonical range: **PDF 5–109 / logical pp.3–107 — 105 pages**;
- visual source fidelity: **105/105 PASS**;
- historical Tamil glyph audit: **105/105 PASS**;
- final dual-gate Tamil: **105/105 complete-verified**;
- review pages: **0**;
- unresolved canonical markers: **0**;
- assembly: **PASS — 105 anchors / 0 missing / 0 duplicate**;
- final verification commit: `{base.FINAL_VERIFY_COMMIT}`;
- source locks: `பழுதார் வீதி`, `தூக்குமேடை`; `தாக்குமேடை` absent;
- scene-text derivatives: **READY**;
- next gate: scene segmentation/extraction + boundary-ownership QA.

Repository-wide status synchronization for the canonical Tamil closure is **PASS** when this section, the work-local mirrors, `data/works.json`, and the root README all advertise this same 105/105 state.

"""
    t = base.replace_section(t, start, end, section)

    # Bring the top Result and bottom Conclusion to the same live state.
    result_start = "## Result"
    matrix_start = "## Current work matrix"
    result = """## Result

**PASS — Ammayappan canonical Tamil is closed at 105/105 under both visual-fidelity and historical-Tamil-glyph gates, with 0 review pages and 0 unresolved canonical markers. Scene-text derivatives are now the active unblocked phase.**

"""
    t = base.replace_section(t, result_start, matrix_start, result)
    conclusion = "## Conclusion"
    if conclusion not in t:
        raise SystemExit("status audit conclusion missing")
    before = t.split(conclusion, 1)[0]
    t = before + """## Conclusion

Ammayappan canonical Tamil is **complete-verified — 105/105 dual-gate PASS**. The canonical source layer is closed unless new direct scan evidence reopens a specific occurrence. The next repository phase is **scene-text derivatives**, followed by dialogue and character indexing under the normal gate order.
"""
    base.write(p, t)


def main() -> None:
    preflight = base.canonical_preflight()
    base.sync_index()
    base.sync_metadata()
    base.sync_work_readme()
    base.sync_handover()
    base.sync_transcription_readme()
    base.sync_audit_ledgers()
    base.sync_registry()
    base.sync_root_readme()
    base.sync_master_handover()
    sync_status_audit_live()
    base.final_qa(preflight)
    print(json.dumps({"status":"PASS","canonical_tamil":"105/105 dual-gate verified","next":"scene-text derivatives"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
