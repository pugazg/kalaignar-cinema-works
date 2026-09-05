#!/usr/bin/env python3
"""Synchronize repository-wide Ammayappan status mirrors to the PDF 5-74 closure.

This script is intentionally narrow and idempotent. It does not touch canonical
Tamil. It synchronizes status/progress surfaces after the historical-glyph
retrospective review and occurrence-specific correction synchronization closed.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SYNC_COMMIT = "880978627191a122f55b50522d112d163faa7e10"


def write_if_changed(path: Path, content: str) -> bool:
    old = path.read_text(encoding="utf-8")
    if old == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def sync_registry() -> bool:
    path = ROOT / "data" / "works.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    work = next(item for item in data if item.get("id") == "ammaiyappan")

    work.update({
        "canonical_tamil_verified_pages": 70,
        "canonical_tamil_visual_fidelity_passed_pages": 70,
        "canonical_tamil_historical_glyph_verified_pages": 70,
        "canonical_tamil_review_pages": 0,
        "historical_glyph_guide_path": "docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md",
        "historical_glyph_audit_path": "works/ammaiyappan/notes/historical-glyph-audit.md",
        "historical_glyph_sync_manifest_path": "works/ammaiyappan/notes/historical-glyph-sync-manifest.json",
        "historical_glyph_sync_report_path": "works/ammaiyappan/notes/historical-glyph-sync-report.json",
        "historical_glyph_sync_commit": SYNC_COMMIT,
        "historical_glyph_retrospective_source_review": "complete-70-of-70",
        "historical_glyph_retrospective_sync": "complete",
        "tamil_fidelity_audit": "in-progress-70-of-105",
        "historical_glyph_audit": "in-progress-70-of-105-retrospective-closed",
        "final_tamil_verification": "dual-gate-in-progress-70-of-105",
        "historical_glyph_retrospective_pdf_pages": "5-74",
        "historical_glyph_forward_combined_pdf_pages": "75-109",
        "next_action": "Resume at PDF 75 / logical printed p.73 with visual source-fidelity and historical-Tamil-glyph verification together; PDF 5-74 are closed as dual-gate verified after retrospective source review and occurrence-specific synchronization.",
        "tamil_transcription_verified_pages": 70,
        "tamil_transcription_visual_fidelity_passed_pages": 70,
        "tamil_transcription_historical_glyph_verified_pages": 70,
        "tamil_transcription_review_pages": 0,
        "canonical_range_fidelity_audit_complete": False,
        "canonical_range_historical_glyph_audit_complete": False,
        "total_canonical_pages": 105,
        "total_verified_pages": 70,
        "total_visual_fidelity_passed_pages": 70,
        "total_historical_glyph_verified_pages": 70,
        "total_review_pages": 0,
        "historical_glyph_verified_pdf_pages": "5-74",
        "historical_glyph_verified_logical_printed_pages": "3-72",
        "fidelity_audit_verified_pdf_pages": "5-74",
        "fidelity_audit_verified_logical_printed_pages": "3-72",
        "fidelity_audit_next_pdf_page": 75,
        "historical_glyph_audit_next_pdf_page": 75,
    })
    return write_if_changed(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def sync_master_handover() -> bool:
    path = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
    text = path.read_text(encoding="utf-8")
    marker = "## 16. Ammayappan active checkpoint"
    if marker not in text:
        raise SystemExit(f"master handover marker missing: {marker}")
    prefix = text.split(marker, 1)[0]
    section = f"""## 16. Ammayappan active checkpoint

Work path: `works/ammaiyappan/`  
Source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

- source intake / whole-scan map: **complete**;
- canonical first pass: **105/105 draft-complete**, continuous `full-text.md` through PDF 109;
- assembly QA: **PASS — 105 anchors / 0 missing / 0 duplicate**;
- visual source-fidelity: **PDF 5–74 / logical pp.3–72 — 70/105 passed**;
- historical-Tamil-glyph audit: **PDF 5–74 / logical pp.3–72 — 70/105 passed**;
- final dual-gate Tamil verified: **70/105**;
- retrospective PDF 5–74 historical-glyph source review: **CLOSED — 70/70**;
- retrospective correction-bearing pages: **38**; correction-free pages: **32**;
- occurrence-specific synchronization: **complete**, commit `{SYNC_COMMIT}`;
- synchronized logical occurrences across canonical/provenance surfaces: **97**;
- global replacement: **not used**; source whitespace/layout preserved;
- genuine same-edition controls on PDF **48, 62, 64, 69**: **preserved / PASS**;
- PDF 75–109 disposition: **35 pages pending — visual fidelity + historical glyph audit together**;
- open first-pass uncertainty markers: **29 — markers 88–116**;
- locked source headings remain `பழுதார் வீதி` (PDF 56) and `தூக்குமேடை` (PDF 107; reject `தாக்குமேடை`);
- historical-glyph authorities: `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `works/ammaiyappan/notes/historical-glyph-audit.md`, `works/ammaiyappan/notes/historical-glyph-sync-manifest.json`, `works/ammaiyappan/notes/historical-glyph-sync-report.json`;
- minimum known audit families: `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- structured derivatives / English / reader: **blocked pending 105/105 dual-gate verified Tamil**.

**Exact next activity:** resume at **PDF 75 / logical printed p.73**, performing rendered-scan visual source-fidelity verification and the historical-Tamil-glyph audit together; adjudicate markers 88–116 only from source evidence. PDF 5–74 are closed unless new direct source evidence requires a specific local correction.
"""
    return write_if_changed(path, prefix + section)


def sync_status_audit() -> bool:
    path = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
    text = path.read_text(encoding="utf-8")

    text = re.sub(
        r"## Result\n\n\*\*PASS.*?\*\*\n",
        "## Result\n\n**PASS — current status mirrors are synchronized to the Ammayappan retrospective historical-glyph closure. The canonical first pass remains 105/105 assembled through PDF 109. PDF 5–74 / logical pp.3–72 have passed both visual source fidelity and the historical-glyph gate, so final dual-gate Tamil verification is 70/105. The retrospective historical-glyph source review and occurrence-specific synchronization are closed; PDF 75–109 are the remaining 35 pages and must receive both audits together.**\n",
        text,
        count=1,
        flags=re.S,
    )

    text = re.sub(
        r"\| Ammayappan \|.*?\| blocked \|",
        "| Ammayappan | source intake 111/111; structural map verified; Tamil first pass **105/105 draft-complete; visual fidelity 70/105; historical-glyph 70/105; final dual-gate verified 70/105** | scene/dialogue/character blocked pending 105/105 dual-gate verified Tamil | blocked | blocked |",
        text,
        count=1,
    )

    start = "## Ammayappan canonical-Tamil first-pass closure checkpoint"
    end = "## Manthiri Kumari reconciliation checkpoint"
    if start not in text or end not in text:
        raise SystemExit("Ammayappan status-audit section markers missing")
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    new_section = f"""## Ammayappan dual-gate checkpoint after retrospective glyph closure

- source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`;
- canonical Tamil first pass: **draft-complete — 105/105 pages**;
- continuous assembled transcription: `works/ammaiyappan/transcription/full-text.md` through **PDF 109**;
- assembly QA: **PASS — 105 anchors / exact PDF 5→109 / 0 missing / 0 duplicate**;
- visual source fidelity: **70/105 passed — PDF 5–74 / logical pp.3–72**;
- historical Tamil glyph gate: **70/105 passed — PDF 5–74 / logical pp.3–72**;
- final dual-gate Tamil verification: **70/105**;
- retrospective PDF 5–74 glyph source review: **70/70 complete**;
- correction-bearing pages: **38**; correction-free pages: **32**;
- occurrence-specific synchronization: **complete** — commit `{SYNC_COMMIT}`;
- synchronization report: `works/ammaiyappan/notes/historical-glyph-sync-report.json`;
- synchronized logical occurrences across canonical/provenance surfaces: **97**;
- global replacement: **0**;
- source whitespace/layout preserved: **yes**;
- genuine controls PDF 48 / 62 / 64 / 69: **PASS / preserved**;
- remaining range: **PDF 75–109 = 35 pages**;
- open first-pass uncertainty markers: **29 — markers 88–116**;
- structured derivatives / English / reader: **blocked until 105/105 dual-gate verified**.

The minimum historical/reform-sensitive families remain `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`. This is a minimum set only; source pixels and same-edition evidence control every character-identity decision.

Exact next activity: **resume at PDF 75 / logical printed p.73 with visual source-fidelity and historical-Tamil-glyph verification together**. PDF 5–74 are closed unless new direct source evidence requires a specific local correction.

"""
    text = before + new_section + end + after

    conclusion = "## Conclusion"
    if conclusion not in text:
        raise SystemExit("status audit conclusion marker missing")
    before_conclusion = text.split(conclusion, 1)[0]
    new_conclusion = """## Conclusion

The **Ammayappan retrospective historical-glyph backfill is closed**. PDF 5–74 retain their prior visual-fidelity pass and now also pass the explicit historical-glyph gate after source review and deterministic occurrence-specific synchronization. Final dual-gate Tamil verification is therefore **70/105**. The remaining work is PDF **75–109**, where visual fidelity and historical-glyph verification must continue together before any structured derivative, English or reader release can begin.
"""
    return write_if_changed(path, before_conclusion + new_conclusion)


def sync_glyph_ledger_banner() -> bool:
    path = ROOT / "works" / "ammaiyappan" / "notes" / "historical-glyph-audit.md"
    text = path.read_text(encoding="utf-8")
    marker = "## Current authoritative closure — 2026-09-05"
    if marker in text:
        return False
    insert_before = "## Current checkpoint when this gate was introduced"
    if insert_before not in text:
        raise SystemExit("historical-glyph ledger insertion marker missing")
    banner = f"""## Current authoritative closure — 2026-09-05

The retrospective historical-glyph pass for **PDF 5–74 / 70 canonical pages is CLOSED**.

- visual fidelity: **70/105 — PDF 5–74 passed**;
- historical glyph audit: **70/105 — PDF 5–74 passed**;
- final dual-gate verified: **70/105**;
- correction-bearing retrospective pages: **38**;
- correction synchronization: **complete** — `{SYNC_COMMIT}`;
- sync manifest/report: `historical-glyph-sync-manifest.json` / `historical-glyph-sync-report.json`;
- global replacement used: **no**;
- genuine controls on PDF 48, 62, 64 and 69: **preserved / PASS**;
- next page: **PDF 75 / logical printed p.73**, with visual fidelity + historical glyph audit together.

The older checkpoint sections below are retained as historical audit evidence. Their `sync-pending` language describes the state *before* commit `{SYNC_COMMIT}` and must not be used as the current work status.

"""
    return write_if_changed(path, text.replace(insert_before, banner + insert_before, 1))


def sync_root_typo() -> bool:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    corrected = text.replace("Kalaignar M. Karunanாநிதி", "Kalaignar M. Karunanidhi")
    if "final dual-gate Tamil verified: **70/105**" not in corrected:
        raise SystemExit("root README does not contain current Ammayappan 70/105 checkpoint")
    return write_if_changed(path, corrected)


def main() -> None:
    changed = []
    for label, func in [
        ("data/works.json", sync_registry),
        ("docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md", sync_master_handover),
        ("docs/STATUS_CONSISTENCY_AUDIT.md", sync_status_audit),
        ("works/ammaiyappan/notes/historical-glyph-audit.md", sync_glyph_ledger_banner),
        ("README.md", sync_root_typo),
    ]:
        if func():
            changed.append(label)
    print(json.dumps({"status": "updated" if changed else "already-synchronized", "changed": changed}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
