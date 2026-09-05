#!/usr/bin/env python3
"""Close Ammayappan canonical Tamil at 105/105 dual-gate verified.

This script updates status mirrors only. Canonical Tamil must already have been
verified by the page-scoped dual-gate workflows. It fails before writing if the
canonical layer is not internally closed.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "works" / "ammaiyappan"
FINAL_VERIFY_COMMIT = "8e8aef9a91dd6222944f81a8d1071f78ecfc5ca3"
SOURCE = "TVA_BOK_0064230_அம்மையப்பன்.pdf"


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def canonical_preflight() -> dict:
    p = WORK / "transcription" / "full-text.md"
    text = p.read_text(encoding="utf-8")
    anchors = re.findall(r"<!-- source: pdf=(\d+).*?status=([^ ]+) -->", text)
    pages = [int(n) for n, _ in anchors]
    statuses = [s for _, s in anchors]
    if pages != list(range(5, 110)):
        raise SystemExit(f"canonical source anchors are not exact PDF 5-109: {pages[:3]}...{pages[-3:]}")
    if len(anchors) != 105 or any(s != "verified" for s in statuses):
        raise SystemExit(f"expected 105 verified anchors; got {len(anchors)}, nonverified={sum(s != 'verified' for s in statuses)}")
    if "⟦" in text or "⟧" in text:
        raise SystemExit("canonical full-text still contains uncertainty markers")
    if "தாக்குமேடை" in text:
        raise SystemExit("rejected heading தாக்குமேடை reappeared")
    if "தூக்குமேடை" not in text or "பழுதார் வீதி" not in text:
        raise SystemExit("locked source heading missing")
    return {"anchors": len(anchors), "verified": len(anchors), "uncertainty_markers": 0}


def sync_index() -> None:
    p = WORK / "transcription" / "index.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    d.update({
        "status": "complete-verified-dual-gate",
        "draft_pages": 105,
        "verified_pages": 105,
        "visual_fidelity_passed_pages": 105,
        "historical_glyph_verified_pages": 105,
        "review_pages": 0,
        "open_uncertainty_markers": 0,
        "next_pdf_page": None,
        "next_printed_page": None,
        "next_action": "Begin scene-text derivatives from the 105/105 dual-gate verified canonical Tamil, using source-visible structural transitions as derivative boundaries and archive-only scene IDs; do not invent printed scene numbers."
    })
    for part in d["assembly"]["parts_retained_for_provenance"]:
        if part["pdf_range"][0] >= 75:
            part["status"] = "verified-dual-gate"
    d["fidelity_audit"].update({
        "status": "complete-pass",
        "canonical_range_audit_complete": True,
        "audited_pages": 105,
        "verified_pages": 105,
        "unresolved_source_readings": 0,
        "review_pages": 0,
        "verified_pdf_range": [5, 109],
        "verified_logical_printed_range": [3, 107],
        "next_pdf_page": None,
        "next_printed_page": None,
    })
    d["historical_glyph_audit"].update({
        "status": "complete-pass-canonical-range",
        "canonical_range_audit_complete": True,
        "audited_pages": 105,
        "reviewed_pdf_range": [5, 109],
        "reviewed_logical_printed_range": [3, 107],
        "verified_pages": 105,
        "verified_pdf_range": [5, 109],
        "verified_logical_printed_range": [3, 107],
        "pending_pages": 0,
        "review_pages": 0,
        "next_forward_pdf_page": None,
        "next_forward_printed_page": None,
    })
    d["final_tamil_verification"].update({
        "verified_pages": 105,
        "verified_pdf_range": [5, 109],
        "verified_logical_printed_range": [3, 107],
        "review_pages": 0,
        "pending_pages": 0,
        "total_pages": 105,
        "status": "complete-verified",
        "verification_commit": FINAL_VERIFY_COMMIT,
    })
    write(p, json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def sync_metadata() -> None:
    p = WORK / "metadata.yaml"
    t = p.read_text(encoding="utf-8")
    replacements = {
        "status: dual-tamil-verification-in-progress": "status: complete-verified-dual-gate",
        "  visual_fidelity_passed_pages: 90": "  visual_fidelity_passed_pages: 105",
        "  historical_glyph_verified_pages: 90": "  historical_glyph_verified_pages: 105",
        "  verified_pages: 90": "  verified_pages: 105",
        "  open_first_pass_uncertainty_markers: 9": "  open_first_pass_uncertainty_markers: 0",
        "  next_pdf_page: 95": "  next_pdf_page: null",
        "  next_logical_printed_page: 93": "  next_logical_printed_page: null",
        "  status: in-progress\n  canonical_range_audit_complete: false\n  audited_pages: 90\n  verified_pages: 90\n  review_pages: 0\n  unresolved_source_readings: 9\n  verified_pdf_pages: \"5-94\"\n  verified_logical_printed_pages: \"3-92\"\n  next_pdf_page: 95\n  next_logical_printed_page: 93": "  status: complete-pass\n  canonical_range_audit_complete: true\n  audited_pages: 105\n  verified_pages: 105\n  review_pages: 0\n  unresolved_source_readings: 0\n  verified_pdf_pages: \"5-109\"\n  verified_logical_printed_pages: \"3-107\"\n  next_pdf_page: null\n  next_logical_printed_page: null",
        "  status: retrospective-complete-forward-combined-pending": "  status: complete-pass-canonical-range",
        "  canonical_range_audit_complete: false": "  canonical_range_audit_complete: true",
        "  formally_verified_pages: 90": "  formally_verified_pages: 105",
        "  verified_pdf_pages: \"5-94\"": "  verified_pdf_pages: \"5-109\"",
        "  verified_logical_printed_pages: \"3-92\"": "  verified_logical_printed_pages: \"3-107\"",
        "  pending_pages: 15": "  pending_pages: 0",
        "  scene_index: blocked-pending-dual-gate-verified-tamil": "  scene_index: ready",
        "  scene_text_derivatives: blocked-pending-dual-gate-verified-tamil": "  scene_text_derivatives: ready",
        "  dialogue_index: blocked-pending-dual-gate-verified-tamil": "  dialogue_index: blocked-pending-scene-text-derivatives",
        "  character_index: blocked": "  character_index: blocked-pending-dialogue-index",
        "  visual_fidelity_audit: in-progress-90-of-105": "  visual_fidelity_audit: complete-verified-105-of-105",
        "  historical_glyph_audit: in-progress-90-of-105-forward-combined": "  historical_glyph_audit: complete-verified-105-of-105",
        "  final_tamil_verification: in-progress-90-of-105-dual-gate": "  final_tamil_verification: complete-verified-105-of-105-dual-gate",
        "  scene_derivatives: blocked": "  scene_derivatives: ready",
        "  dialogue_index: blocked": "  dialogue_index: blocked-pending-scene-text-derivatives",
        "  character_index: blocked": "  character_index: blocked-pending-dialogue-index",
    }
    for old, new in replacements.items():
        t = t.replace(old, new)
    t = re.sub(r'  next_action: ".*?"\n', '  next_action: "Begin scene-text derivatives from verified canonical Tamil; use source-visible transition boundaries and archive-only scene IDs."\n', t, count=1)
    t = re.sub(r'next_action: ".*?"\n?$', 'next_action: "Begin scene-text derivatives from verified canonical Tamil; use source-visible transition boundaries and archive-only scene IDs. Do not invent printed scene numbers."\n', t)
    t = t.replace('      status: draft\n    - path: "transcription/parts/pdf-105-109.md"', '      status: verified-dual-gate\n    - path: "transcription/parts/pdf-105-109.md"')
    t = t.replace('      status: draft\n  visual_fidelity_passed_pages: 105', '      status: verified-dual-gate\n  visual_fidelity_passed_pages: 105')
    if "verified_pages: 105" not in t or "open_first_pass_uncertainty_markers: 0" not in t:
        raise SystemExit("metadata synchronization failed")
    write(p, t)


def replace_section(text: str, start: str, end: str | None, new: str) -> str:
    if start not in text:
        raise SystemExit(f"section start missing: {start}")
    before, rest = text.split(start, 1)
    if end is None:
        return before + new
    if end not in rest:
        raise SystemExit(f"section end missing: {end}")
    _, after = rest.split(end, 1)
    return before + new + end + after


def sync_work_readme() -> None:
    p = WORK / "README.md"
    t = p.read_text(encoding="utf-8")
    t = t.replace("- open first-pass uncertainty markers: **9**;", "- open first-pass uncertainty markers: **0**;")
    t = t.replace("The first-pass draft and assembly are complete, but final Tamil verification remains in progress.", "The first-pass draft, assembly, visual-fidelity audit and historical-glyph audit are complete. Canonical Tamil is **105/105 dual-gate verified**.")
    current = """## Current status

| Layer | Status |
|---|---|
| Source intake | complete |
| Whole-scan inspection | complete — 111/111 |
| Structural mapping | verified intake map |
| Canonical Tamil first pass | **complete — 105/105** |
| Full-text assembly | **complete — PDF 5–109** |
| Boundary loss/duplication QA | **PASS** |
| Visual fidelity audit | **complete — 105/105, PDF 5–109** |
| Historical Tamil glyph audit | **complete — 105/105, PDF 5–109** |
| Final dual-gate Tamil verification | **complete-verified — 105/105** |
| Open canonical uncertainty markers | **0** |
| Scene-text derivatives | **READY — next phase** |
| Dialogue index | blocked until scene-text derivatives close |
| Character index | blocked until dialogue index closes |
| Song/performance authorship gate | not-started |
| English translation / reader | blocked by derivative gate order |

## Exact next activity

**Begin scene-text derivatives.** Build archive-only scene/segment IDs from the verified canonical Tamil using the source-visible transitions in `notes/scene-heading-audit.md`. Preserve source order, page anchors, exact headings, stage directions and speaker labels. Do **not** invent printed scene numbers. Run boundary-ownership QA before opening the dialogue-index phase.
"""
    t = replace_section(t, "## Current status", None, current)
    if "105/105" not in t or "Scene-text derivatives | **READY" not in t:
        raise SystemExit("work README synchronization failed")
    write(p, t)


def sync_handover() -> None:
    p = WORK / "PROJECT_HANDOVER.md"
    t = p.read_text(encoding="utf-8")
    final = f"""## Dual verification gate — CLOSED

A page is final Tamil verified only when **visual fidelity = pass** and **historical glyph audit = pass**.

Final durable checkpoint:

- visual-fidelity passed: **105/105 — PDF 5–109 / logical pp.3–107**;
- historical-glyph passed: **105/105 — PDF 5–109 / logical pp.3–107**;
- final dual-gate Tamil verified: **105/105**;
- review pages: **0**;
- canonical uncertainty markers: **0**;
- final verification commit: `{FINAL_VERIFY_COMMIT}`;
- PDF 95–104 report: `notes/dual-gate-sync-report-pdf-095-104.json` — **10/10 PASS**;
- PDF 105–109 report: `notes/dual-gate-sync-report-pdf-105-109.json` — **5/5 PASS**;
- final canonical range: **PDF 5–109 / logical pp.3–107**.

The retrospective PDF 5–74 historical-glyph backfill and its occurrence-specific synchronization remain part of the audit history. Forward combined verification then closed PDF 75–109. No global historical-glyph replacement was used.

## Phase gates

- source intake: complete;
- whole-scan inspection: complete 111/111;
- structural intake map: verified;
- canonical Tamil first pass: **complete — 105/105**;
- full-text assembly: **complete-pass**;
- boundary loss/duplication QA: **PASS**;
- visual fidelity audit: **complete — 105/105**;
- historical Tamil glyph audit: **complete — 105/105**;
- final dual-gate Tamil verification: **complete-verified — 105/105**;
- scene-text derivatives: **READY — next phase**;
- dialogue index: blocked pending scene-text derivative closure;
- character index: blocked pending dialogue-index closure;
- song/performance authorship gate: not-started;
- English / reader: blocked by derivative gate order.

## Exact next activity

> **Begin scene-text derivatives from `transcription/full-text.md`. Use `notes/scene-heading-audit.md` as the structural transition ledger, assign archive-only navigation IDs because the booklet prints no scene numbers, preserve all page anchors and exact source text, and run boundary-ownership QA before opening the dialogue-index phase.**
"""
    t = replace_section(t, "## Dual verification gate — current checkpoint", None, final)
    write(p, t)


def sync_transcription_readme() -> None:
    p = WORK / "transcription" / "README.md"
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"## Current dual-gate checkpoint.*?## Retrospective historical-glyph synchronization — CLOSED", """## Current dual-gate checkpoint

- canonical screenplay range: **PDF 5–109 / logical printed pp.3–107**;
- canonical pages expected: **105**;
- first-pass pages completed: **105/105**;
- visual-fidelity-passed pages: **105/105**;
- historical-glyph-passed pages: **105/105**;
- final dual-gate verified pages: **105/105**;
- review pages: **0**;
- open uncertainty markers: **0**;
- assembly QA: `ASSEMBLY_QA.md` — **PASS**;
- canonical Tamil state: **complete-verified**;
- final verification commit: `""" + FINAL_VERIFY_COMMIT + """`.

## Retrospective historical-glyph synchronization — CLOSED""", t, flags=re.S)
    t = t.replace("- PDF 95–104: draft complete, 7 batch markers numbered 108–114; dual-gate verification pending.", "- PDF 95–104: **dual-gate verified**; markers 108–114 resolved; report `../notes/dual-gate-sync-report-pdf-095-104.json`.")
    t = t.replace("- PDF 105–109: final draft batch complete, 2 batch markers numbered **115–116**; dual-gate verification pending; preserves the PDF 104→105 continuation and locked `தூக்குமேடை` heading.", "- PDF 105–109: **dual-gate verified**; markers 115–116 resolved; preserves the PDF 104→105 continuation and locked `தூக்குமேடை` heading; report `../notes/dual-gate-sync-report-pdf-105-109.json`.")
    t = re.sub(r"## Exact next activity.*$", """## Exact next activity

Begin **scene-text derivatives** from `full-text.md`, using source-visible transitions as derivative boundaries and archive-only scene IDs. Preserve canonical text exactly and run boundary-ownership QA before the dialogue-index phase.
""", t, flags=re.S)
    write(p, t)


def sync_audit_ledgers() -> None:
    p = WORK / "notes" / "fidelity-audit.md"
    t = p.read_text(encoding="utf-8")
    banner = f"""<!-- current-checkpoint: PDF 5-109 dual-gate verified; canonical Tamil CLOSED; final verification commit {FINAL_VERIFY_COMMIT} -->
# அம்மையப்பன் — canonical Tamil visual fidelity audit

Status: **complete-pass — 105/105 canonical pages verified**.

Controlling source: `{SOURCE}`  
Canonical range: **PDF 5–109 / logical printed pp.3–107 — 105 pages**

## Final closure — 2026-09-05

- visual source fidelity: **105/105 PASS**;
- historical-glyph companion gate: **105/105 PASS**;
- review pages: **0**;
- unresolved canonical readings: **0**;
- final verification commit: `{FINAL_VERIFY_COMMIT}`;
- PDF 95–104 batch report: `dual-gate-sync-report-pdf-095-104.json`;
- PDF 105–109 batch report: `dual-gate-sync-report-pdf-105-109.json`;
- structured scene-text derivative gate: **unblocked**.

The historical batch sections below are retained as audit history. Earlier progress counts in those sections are historical checkpoints, not the current status.

"""
    # Drop existing checkpoint comments/title/status preamble but retain audit rules onward.
    idx = t.find("## Audit rules")
    if idx < 0:
        raise SystemExit("fidelity audit rules marker missing")
    write(p, banner + t[idx:])

    p = WORK / "notes" / "historical-glyph-audit.md"
    t = p.read_text(encoding="utf-8")
    banner = f"""<!-- current-checkpoint: PDF 5-109 dual-gate verified; historical-glyph gate CLOSED; final verification commit {FINAL_VERIFY_COMMIT} -->
# அம்மையப்பன் — Historical Tamil Glyph Audit

## Final canonical-range closure — 2026-09-05

- historical-Tamil-glyph audit: **105/105 PASS — PDF 5–109 / logical pp.3–107**;
- visual-fidelity companion gate: **105/105 PASS**;
- final dual-gate verified: **105/105**;
- review pages: **0**;
- unresolved canonical markers: **0**;
- global historical-glyph replacement used: **no**;
- final verification commit: `{FINAL_VERIFY_COMMIT}`;
- final batch reports: `dual-gate-sync-report-pdf-095-104.json`, `dual-gate-sync-report-pdf-105-109.json`;
- next phase: **scene-text derivatives**.

Older checkpoint sections below are retained as audit history and must not be used as the current production status.

"""
    idx = t.find("## Purpose")
    if idx < 0:
        raise SystemExit("glyph audit purpose marker missing")
    write(p, banner + t[idx:])


def sync_registry() -> None:
    p = ROOT / "data" / "works.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    w = next(x for x in d if x.get("id") == "ammaiyappan")
    w.update({
        "canonical_tamil_verified_pages": 105,
        "canonical_tamil_visual_fidelity_passed_pages": 105,
        "canonical_tamil_historical_glyph_verified_pages": 105,
        "canonical_tamil_review_pages": 0,
        "tamil_transcription_verified_pages": 105,
        "tamil_transcription_visual_fidelity_passed_pages": 105,
        "tamil_transcription_historical_glyph_verified_pages": 105,
        "tamil_transcription_review_pages": 0,
        "canonical_range_fidelity_audit_complete": True,
        "canonical_range_historical_glyph_audit_complete": True,
        "total_canonical_pages": 105,
        "total_verified_pages": 105,
        "total_visual_fidelity_passed_pages": 105,
        "total_historical_glyph_verified_pages": 105,
        "total_review_pages": 0,
        "historical_glyph_verified_pdf_pages": "5-109",
        "historical_glyph_verified_logical_printed_pages": "3-107",
        "fidelity_audit_verified_pdf_pages": "5-109",
        "fidelity_audit_verified_logical_printed_pages": "3-107",
        "fidelity_audit_next_pdf_page": None,
        "historical_glyph_audit_next_pdf_page": None,
        "tamil_fidelity_audit": "complete-verified-105-of-105",
        "historical_glyph_audit": "complete-verified-105-of-105",
        "final_tamil_verification": "complete-verified-dual-gate-105-of-105",
        "open_uncertainty_markers": 0,
        "final_tamil_verification_commit": FINAL_VERIFY_COMMIT,
        "scene_text_derivatives": "ready",
        "dialogue_index": "blocked-pending-scene-text-derivatives",
        "character_index": "blocked-pending-dialogue-index",
        "next_action": "Begin scene-text derivatives from the 105/105 dual-gate verified canonical Tamil; use source-visible transition boundaries and archive-only IDs, then run boundary-ownership QA."
    })
    write(p, json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def sync_root_readme() -> None:
    p = ROOT / "README.md"
    t = p.read_text(encoding="utf-8")
    start, end = "## அம்மையப்பன் status", "## கலைஞர் திரை இசைப் பாடல்கள் status"
    section = f"""## அம்மையப்பன் status

`{SOURCE}` has **complete-verified canonical Tamil under the mandatory dual gate**.

- canonical screenplay: **PDF 5–109 / logical pp.3–107 — 105/105 pages**;
- assembly QA: **PASS — 105 anchors / 0 missing / 0 duplicate**;
- visual source fidelity: **105/105 PASS**;
- historical Tamil glyph audit: **105/105 PASS**;
- final dual-gate Tamil: **105/105 complete-verified**;
- review pages: **0**;
- unresolved canonical markers: **0**;
- final verification commit: `{FINAL_VERIFY_COMMIT}`;
- final batch reports: `works/ammaiyappan/notes/dual-gate-sync-report-pdf-095-104.json`, `works/ammaiyappan/notes/dual-gate-sync-report-pdf-105-109.json`;
- scene-text derivatives: **READY**;
- dialogue/character layers: blocked by normal derivative gate order;
- English / reader: blocked by normal derivative gate order.

**Next:** build scene-text derivatives from verified canonical Tamil using source-visible transitions and archive-only navigation IDs; do not invent printed scene numbers.

"""
    t = replace_section(t, start, end, section)
    write(p, t)


def sync_master_handover() -> None:
    p = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
    t = p.read_text(encoding="utf-8")
    marker = "## 16. Ammayappan active checkpoint"
    section = f"""## 16. Ammayappan active checkpoint

Work path: `works/ammaiyappan/`  
Source: `{SOURCE}`

- source intake / whole-scan map: **complete**;
- canonical first pass / assembly: **105/105 complete; assembly QA PASS**;
- visual source fidelity: **105/105 PASS — PDF 5–109 / logical pp.3–107**;
- historical-Tamil-glyph audit: **105/105 PASS**;
- final dual-gate Tamil: **105/105 complete-verified**;
- review pages / unresolved canonical markers: **0 / 0**;
- final verification commit: `{FINAL_VERIFY_COMMIT}`;
- locked headings: `பழுதார் வீதி` and `தூக்குமேடை`; rejected `தாக்குமேடை` absent;
- scene-text derivatives: **READY — next phase**;
- dialogue index: blocked pending scene-text closure;
- character index: blocked pending dialogue-index closure;
- song/performance authorship: not-started;
- English / reader: blocked by derivative gate order.

**Exact next activity:** build source-order scene-text derivatives from the verified canonical Tamil. Use `works/ammaiyappan/notes/scene-heading-audit.md` as the transition ledger, use archive-only scene/segment IDs because no printed scene numbers exist, preserve page anchors and exact source text, and run boundary-ownership QA before dialogue indexing.
"""
    t = replace_section(t, marker, None, section)
    write(p, t)


def sync_status_audit() -> None:
    p = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"\| Ammayappan \|.*?\| blocked \|", "| Ammayappan | canonical Tamil **105/105 dual-gate complete-verified; 0 review; 0 unresolved** | scene-text derivatives READY; dialogue/character blocked by gate order | blocked | blocked |", t, count=1)
    start = "## Ammayappan dual-gate checkpoint after retrospective glyph closure"
    if start not in t:
        start = "## Ammayappan canonical-Tamil first-pass closure checkpoint"
    end = "## Manthiri Kumari reconciliation checkpoint"
    section = f"""## Ammayappan final dual-gate Tamil closure

- canonical range: **PDF 5–109 / logical pp.3–107 — 105 pages**;
- visual source fidelity: **105/105 PASS**;
- historical Tamil glyph audit: **105/105 PASS**;
- final dual-gate Tamil: **105/105 complete-verified**;
- review pages: **0**;
- unresolved canonical markers: **0**;
- assembly: **PASS — 105 anchors / 0 missing / 0 duplicate**;
- final verification commit: `{FINAL_VERIFY_COMMIT}`;
- source locks: `பழுதார் வீதி`, `தூக்குமேடை`; `தாக்குமேடை` absent;
- scene-text derivatives: **READY**;
- next gate: scene segmentation/extraction + boundary-ownership QA.

Repository-wide status synchronization for the canonical Tamil closure is **PASS** when this section, the work-local mirrors, `data/works.json`, and the root README all advertise this same 105/105 state.

"""
    t = replace_section(t, start, end, section)
    write(p, t)


def final_qa(preflight: dict) -> None:
    report = f"""# அம்மையப்பன் — Final canonical Tamil QA

Status: **PASS**  
Source: `{SOURCE}`  
Final verification commit: `{FINAL_VERIFY_COMMIT}`

## Canonical closure

- expected canonical PDF range: **5–109**;
- expected canonical pages: **105**;
- source anchors found: **{preflight['anchors']}**;
- verified anchors: **{preflight['verified']}**;
- missing anchors: **0**;
- duplicate anchors: **0**;
- uncertainty markers remaining in `transcription/full-text.md`: **0**;
- visual fidelity gate: **105/105 PASS**;
- historical-glyph gate: **105/105 PASS**;
- final dual-gate Tamil: **105/105 complete-verified**;
- review pages: **0**.

## Locked source controls

- PDF 56 / p.54: `பழுதார் வீதி` — **present**;
- PDF 107 / p.105: `தூக்குமேடை` — **present**;
- rejected `தாக்குமேடை` — **absent**.

## Final batch evidence

- PDF 95–104: `dual-gate-sync-report-pdf-095-104.json` — **10/10 PASS, 0 markers**;
- PDF 105–109: `dual-gate-sync-report-pdf-105-109.json` — **5/5 PASS, 0 markers**.

## Gate disposition

Canonical Tamil is **closed-verified**. Scene-text derivatives are now unblocked. They must remain downstream derivatives of `transcription/full-text.md`, preserve exact canonical text and page provenance, use archive-only IDs, and pass boundary-ownership QA before dialogue indexing begins.
"""
    write(WORK / "notes" / "FINAL_TAMIL_QA.md", report)


def main() -> None:
    preflight = canonical_preflight()
    sync_index()
    sync_metadata()
    sync_work_readme()
    sync_handover()
    sync_transcription_readme()
    sync_audit_ledgers()
    sync_registry()
    sync_root_readme()
    sync_master_handover()
    sync_status_audit()
    final_qa(preflight)
    print(json.dumps({"status": "PASS", "canonical_tamil": "105/105 dual-gate verified", "next": "scene-text derivatives"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
