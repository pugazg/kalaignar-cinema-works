#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "works" / "ammaiyappan"
VERIFY_COMMIT = "1911df2c97d45dfe07f1b9073bdf6368378ddf44"
BATCH_REPORT = "works/ammaiyappan/notes/dual-gate-sync-report-pdf-085-094.json"


def write(path: Path, text: str) -> bool:
    old = path.read_text(encoding="utf-8")
    if old == text:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def req(text: str, old: str, new: str, *, count: int = 1) -> str:
    n = text.count(old)
    if n < count:
        raise SystemExit(f"missing expected status text {old!r}; found {n}")
    return text.replace(old, new, count)


def sync_index() -> bool:
    path = WORK / "transcription" / "index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data.update({
        "verified_pages": 90,
        "visual_fidelity_passed_pages": 90,
        "historical_glyph_verified_pages": 90,
        "review_pages": 0,
        "open_uncertainty_markers": 9,
        "next_pdf_page": 95,
        "next_printed_page": 93,
        "next_action": "Resume at PDF 95 / printed p.93 with visual source-fidelity and historical-Tamil-glyph verification together; adjudicate markers 108-116 occurrence-by-occurrence. PDF 5-94 are closed as dual-gate verified."
    })
    data["fidelity_audit"].update({
        "audited_pages": 90,
        "verified_pages": 90,
        "unresolved_source_readings": 9,
        "verified_pdf_range": [5,94],
        "verified_logical_printed_range": [3,92],
        "next_pdf_page": 95,
        "next_printed_page": 93,
    })
    data["historical_glyph_audit"].update({
        "status": "in-progress-forward-combined-through-pdf-94",
        "audited_pages": 90,
        "reviewed_pdf_range": [5,94],
        "reviewed_logical_printed_range": [3,92],
        "verified_pages": 90,
        "verified_pdf_range": [5,94],
        "verified_logical_printed_range": [3,92],
        "pending_pages": 15,
        "next_forward_pdf_page": 95,
        "next_forward_printed_page": 93,
    })
    data["final_tamil_verification"].update({
        "verified_pages": 90,
        "verified_pdf_range": [5,94],
        "verified_logical_printed_range": [3,92],
        "pending_pages": 15,
    })
    for part in data["assembly"]["parts_retained_for_provenance"]:
        if part["pdf_range"] == [85,94]:
            part["status"] = "verified-dual-gate"
    return write(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def sync_metadata() -> bool:
    path = WORK / "metadata.yaml"
    text = path.read_text(encoding="utf-8")
    pairs = [
        ("      pdf_pages: \"85-94\"\n      printed_pages: \"83-92\"\n      status: draft", "      pdf_pages: \"85-94\"\n      printed_pages: \"83-92\"\n      status: verified-dual-gate"),
        ("  visual_fidelity_passed_pages: 80\n  historical_glyph_verified_pages: 80\n  verified_pages: 80", "  visual_fidelity_passed_pages: 90\n  historical_glyph_verified_pages: 90\n  verified_pages: 90"),
        ("  open_first_pass_uncertainty_markers: 19", "  open_first_pass_uncertainty_markers: 9"),
        ("  next_pdf_page: 85\n  next_logical_printed_page: 83", "  next_pdf_page: 95\n  next_logical_printed_page: 93"),
        ("  next_action: \"Resume at PDF 85 / logical printed p.83 with visual source-fidelity and historical-Tamil-glyph verification together; PDF 5-84 are closed as dual-gate verified, while PDF 5-74 remain the completed retrospective glyph-backfill range.\"", "  next_action: \"Resume at PDF 95 / logical printed p.93 with visual source-fidelity and historical-Tamil-glyph verification together; PDF 5-94 are closed as dual-gate verified.\""),
        ("  audited_pages: 80\n  verified_pages: 80\n  review_pages: 0\n  unresolved_source_readings: 19\n  verified_pdf_pages: \"5-84\"\n  verified_logical_printed_pages: \"3-82\"\n  next_pdf_page: 85\n  next_logical_printed_page: 83", "  audited_pages: 90\n  verified_pages: 90\n  review_pages: 0\n  unresolved_source_readings: 9\n  verified_pdf_pages: \"5-94\"\n  verified_logical_printed_pages: \"3-92\"\n  next_pdf_page: 95\n  next_logical_printed_page: 93"),
        ("  formally_verified_pages: 80\n  verified_pdf_pages: \"5-84\"\n  verified_logical_printed_pages: \"3-82\"\n  pending_pages: 25", "  formally_verified_pages: 90\n  verified_pdf_pages: \"5-94\"\n  verified_logical_printed_pages: \"3-92\"\n  pending_pages: 15"),
        ("  next_pdf_page: 85\n  next_logical_printed_page: 83\n  preserve_controls_passed", "  next_pdf_page: 95\n  next_logical_printed_page: 93\n  preserve_controls_passed"),
        ("  verified_pages: 80\n  verified_pdf_pages: \"5-84\"\n  verified_logical_printed_pages: \"3-82\"\n  pending_pages: 25", "  verified_pages: 90\n  verified_pdf_pages: \"5-94\"\n  verified_logical_printed_pages: \"3-92\"\n  pending_pages: 15"),
        ("  visual_fidelity_audit: in-progress-80-of-105\n  historical_glyph_audit: in-progress-80-of-105-forward-combined\n  final_tamil_verification: in-progress-80-of-105-dual-gate", "  visual_fidelity_audit: in-progress-90-of-105\n  historical_glyph_audit: in-progress-90-of-105-forward-combined\n  final_tamil_verification: in-progress-90-of-105-dual-gate"),
        ("next_action: \"Resume at PDF 85 / logical printed p.83 with visual source-fidelity and historical-Tamil-glyph verification together; adjudicate markers 98-116 occurrence-by-occurrence. PDF 5-84 are closed unless new direct source evidence requires a specific local correction. Structured derivatives remain blocked until both gates reach 105/105.\"", "next_action: \"Resume at PDF 95 / logical printed p.93 with visual source-fidelity and historical-Tamil-glyph verification together; adjudicate markers 108-116 occurrence-by-occurrence. PDF 5-94 are closed unless new direct source evidence requires a specific local correction. Structured derivatives remain blocked until both gates reach 105/105.\"")
    ]
    for old,new in pairs:
        text = req(text, old, new)
    return write(path, text)


def simple_forward_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    replacements = [
        ("80/105", "90/105"),
        ("PDF 5–84", "PDF 5–94"),
        ("PDF 85–109", "PDF 95–109"),
        ("25 pages pending", "15 pages pending"),
        ("markers **98–116**", "markers **108–116**"),
        ("markers 98–116", "markers 108–116"),
        ("PDF 85 / logical printed p.83", "PDF 95 / logical printed p.93"),
        ("PDF 85 / printed p.83", "PDF 95 / printed p.93"),
        ("open first-pass uncertainty markers: **29**", "open first-pass uncertainty markers: **9**"),
        ("open first-pass uncertain readings: **19**", "open first-pass uncertain readings: **9**"),
        ("remaining canonical pages: **25", "remaining canonical pages: **15"),
    ]
    for old,new in replacements:
        text = text.replace(old,new)
    if "dual-gate-sync-report-pdf-085-094.json" not in text:
        insert = f"\nForward dual-gate verification through PDF 94 is recorded by commit `{VERIFY_COMMIT}` and `notes/dual-gate-sync-report-pdf-085-094.json`.\n"
        marker = "## Historical Tamil glyph gate" if "## Historical Tamil glyph gate" in text else "## Mandatory historical Tamil glyph gate"
        if marker in text:
            text = text.replace(marker, insert + "\n" + marker, 1)
    return write(path, text)


def sync_transcription_readme() -> bool:
    path = WORK / "transcription" / "README.md"
    text = path.read_text(encoding="utf-8")
    reps = [
        ("80/105 — PDF 5–84", "90/105 — PDF 5–94"),
        ("25 — PDF 85–109", "15 — PDF 95–109"),
        ("open first-pass uncertain readings: **19**", "open first-pass uncertain readings: **9**"),
        ("next source page: **PDF 85 / logical printed p.83**", "next source page: **PDF 95 / logical printed p.93**"),
        ("PDF 85–94: draft complete, 10 batch markers; dual-gate verification pending.", "PDF 85–94: **dual-gate verified**; markers 98–107 closed from the rendered scan; synchronization report `../notes/dual-gate-sync-report-pdf-085-094.json`."),
        ("Resume at **PDF 85 / logical printed p.83**", "Resume at **PDF 95 / logical printed p.93**"),
        ("markers **98–116**", "markers **108–116**"),
        ("PDF 5–84 are closed", "PDF 5–94 are closed"),
    ]
    for old,new in reps:
        text = text.replace(old,new)
    return write(path, text)


def replace_section(text: str, heading: str, replacement: str) -> str:
    pos = text.find(heading)
    if pos < 0:
        raise SystemExit(f"missing section heading: {heading}")
    next_pos = text.find("\n## ", pos + len(heading))
    if next_pos < 0:
        return text[:pos] + replacement.rstrip() + "\n"
    return text[:pos] + replacement.rstrip() + "\n" + text[next_pos+1:]


def sync_root_readme() -> bool:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    section = f'''## அம்மையப்பன் status

`TVA_BOK_0064230_அம்மையப்பன்.pdf` is an active **111-page image-only screenplay/dialogue booklet** using a mandatory dual Tamil gate: visual source fidelity + historical-Tamil-glyph verification.

- canonical Tamil first pass: **105/105 draft-complete**;
- assembly QA: **PASS — PDF 5–109, 105 anchors, 0 missing, 0 duplicate**;
- visual source fidelity: **90/105 passed — PDF 5–94 / logical pp.3–92**;
- historical Tamil glyph audit: **90/105 passed — PDF 5–94 / logical pp.3–92**;
- final dual-gate Tamil verified: **90/105**;
- retrospective historical-glyph backfill PDF 5–74: **CLOSED**;
- forward dual-gate batches PDF 75–84 and PDF 85–94: **CLOSED / PASS**;
- PDF 85–94 verification commit: `{VERIFY_COMMIT}`;
- PDF 85–94 report: `{BATCH_REPORT}` — **10/10 pages, 0 markers remaining, canonical/provenance PASS**;
- remaining: **PDF 95–109 = 15 pages**;
- open first-pass uncertainty markers: **9 — markers 108–116**;
- structured derivatives / English / reader: **blocked pending 105/105 dual-gate Tamil**.

**Next:** resume at **PDF 95 / logical printed p.93** with visual source-fidelity and historical-Tamil-glyph verification together; adjudicate markers 108–116 occurrence-by-occurrence.
'''
    return write(path, replace_section(text, "## அம்மையப்பன் status", section))


def sync_master_handover() -> bool:
    path = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
    text = path.read_text(encoding="utf-8")
    section = f'''## 16. Ammayappan active checkpoint

Work path: `works/ammaiyappan/`  
Source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

- canonical first pass: **105/105 draft-complete**, assembled through PDF 109;
- assembly QA: **PASS — 105 anchors / 0 missing / 0 duplicate**;
- visual source fidelity: **90/105 — PDF 5–94 / logical pp.3–92 passed**;
- historical-Tamil-glyph audit: **90/105 — PDF 5–94 / logical pp.3–92 passed**;
- final dual-gate Tamil verified: **90/105**;
- retrospective PDF 5–74 glyph backfill: **CLOSED**;
- forward PDF 75–84: **PASS**;
- forward PDF 85–94: **PASS**, commit `{VERIFY_COMMIT}`, report `{BATCH_REPORT}`;
- remaining PDF 95–109: **15 pages**;
- unresolved first-pass markers: **9 — markers 108–116**;
- structured derivatives / English / reader: **blocked pending 105/105 dual-gate Tamil**.

**Exact next activity:** resume at **PDF 95 / logical printed p.93** and perform visual source-fidelity + historical-Tamil-glyph verification together; adjudicate markers 108–116 only from source evidence.
'''
    return write(path, replace_section(text, "## 16. Ammayappan active checkpoint", section))


def sync_status_audit() -> bool:
    path = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
    text = path.read_text(encoding="utf-8")
    start = text.find("## Ammayappan")
    if start < 0:
        raise SystemExit("Ammayappan status section missing")
    end = text.find("\n## ", start + 5)
    if end < 0:
        end = len(text)
    section = f'''## Ammayappan dual-gate checkpoint through PDF 94

- canonical Tamil first pass: **105/105 draft-complete**;
- visual source fidelity: **90/105 — PDF 5–94 passed**;
- historical Tamil glyph gate: **90/105 — PDF 5–94 passed**;
- final dual-gate Tamil verification: **90/105**;
- PDF 85–94 verification: **PASS — 10/10**, commit `{VERIFY_COMMIT}`;
- PDF 85–94 uncertainty markers: **98–107 closed; 0 remain in range**;
- canonical/provenance agreement for PDF 85–94: **PASS**;
- remaining: **PDF 95–109 = 15 pages / markers 108–116 = 9**;
- derivatives / English / reader: **blocked until 105/105**.

Exact next activity: **PDF 95 / logical printed p.93** with both gates together.
'''
    return write(path, text[:start] + section.rstrip() + "\n" + text[end+1:])


def sync_registry() -> bool:
    path = ROOT / "data" / "works.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    work = next(item for item in data if item.get("id") == "ammaiyappan")
    work.update({
        "canonical_tamil_verified_pages": 90,
        "canonical_tamil_visual_fidelity_passed_pages": 90,
        "canonical_tamil_historical_glyph_verified_pages": 90,
        "canonical_tamil_review_pages": 0,
        "tamil_transcription_verified_pages": 90,
        "tamil_transcription_visual_fidelity_passed_pages": 90,
        "tamil_transcription_historical_glyph_verified_pages": 90,
        "tamil_transcription_review_pages": 0,
        "tamil_fidelity_audit": "in-progress-90-of-105",
        "historical_glyph_audit": "in-progress-90-of-105-forward-combined",
        "final_tamil_verification": "dual-gate-in-progress-90-of-105",
        "total_verified_pages": 90,
        "total_visual_fidelity_passed_pages": 90,
        "total_historical_glyph_verified_pages": 90,
        "total_review_pages": 0,
        "historical_glyph_verified_pdf_pages": "5-94",
        "historical_glyph_verified_logical_printed_pages": "3-92",
        "fidelity_audit_verified_pdf_pages": "5-94",
        "fidelity_audit_verified_logical_printed_pages": "3-92",
        "fidelity_audit_next_pdf_page": 95,
        "historical_glyph_audit_next_pdf_page": 95,
        "next_action": "Resume at PDF 95 / logical printed p.93 with visual source-fidelity and historical-Tamil-glyph verification together; adjudicate markers 108-116 occurrence-by-occurrence."
    })
    return write(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def add_banner(path: Path, label: str) -> bool:
    text = path.read_text(encoding="utf-8")
    banner = f"<!-- {label}: PDF 5-94 dual-gate verified; next PDF 95; verification commit {VERIFY_COMMIT} -->\n"
    if banner in text:
        return False
    return write(path, banner + text)


def main() -> None:
    changed = []
    actions = [
        ("works/ammaiyappan/transcription/index.json", sync_index),
        ("works/ammaiyappan/metadata.yaml", sync_metadata),
        ("works/ammaiyappan/README.md", lambda: simple_forward_file(WORK / "README.md")),
        ("works/ammaiyappan/PROJECT_HANDOVER.md", lambda: simple_forward_file(WORK / "PROJECT_HANDOVER.md")),
        ("works/ammaiyappan/transcription/README.md", sync_transcription_readme),
        ("README.md", sync_root_readme),
        ("docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md", sync_master_handover),
        ("docs/STATUS_CONSISTENCY_AUDIT.md", sync_status_audit),
        ("data/works.json", sync_registry),
        ("works/ammaiyappan/notes/fidelity-audit.md", lambda: add_banner(WORK / "notes" / "fidelity-audit.md", "current-checkpoint")),
        ("works/ammaiyappan/notes/historical-glyph-audit.md", lambda: add_banner(WORK / "notes" / "historical-glyph-audit.md", "current-checkpoint")),
    ]
    for name, fn in actions:
        if fn():
            changed.append(name)
    print(json.dumps({"status":"updated" if changed else "already-synchronized","changed":changed}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
