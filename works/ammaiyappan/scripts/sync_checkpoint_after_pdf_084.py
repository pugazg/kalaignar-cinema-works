#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "works" / "ammaiyappan"
VERIFY_COMMIT = "0da97f94e829bef9b387bf59be580933b97ed122"


def replace_required(path: Path, old: str, new: str, count: int = 1) -> bool:
    text = path.read_text(encoding="utf-8")
    actual = text.count(old)
    if actual < count:
        raise SystemExit(f"{path}: expected at least {count} occurrence(s) of {old!r}, found {actual}")
    updated = text.replace(old, new, count)
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def sync_index() -> bool:
    path = WORK / "transcription" / "index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data.update({
        "verified_pages": 80,
        "visual_fidelity_passed_pages": 80,
        "historical_glyph_verified_pages": 80,
        "review_pages": 0,
        "open_uncertainty_markers": 19,
        "next_pdf_page": 85,
        "next_printed_page": 83,
        "next_action": "Resume at PDF 85 / printed p.83. Perform visual source-fidelity verification and the historical-Tamil-glyph audit together on every page, adjudicating markers 98-116 occurrence-by-occurrence. PDF 5-84 are closed as dual-gate verified; PDF 5-74 remain the completed retrospective glyph-backfill range."
    })
    data["fidelity_audit"].update({
        "audited_pages": 80,
        "verified_pages": 80,
        "unresolved_source_readings": 19,
        "verified_pdf_range": [5,84],
        "verified_logical_printed_range": [3,82],
        "next_pdf_page": 85,
        "next_printed_page": 83,
    })
    hg = data["historical_glyph_audit"]
    hg.update({
        "status": "in-progress-forward-combined-through-pdf-84",
        "audited_pages": 80,
        "reviewed_pdf_range": [5,84],
        "reviewed_logical_printed_range": [3,82],
        "verified_pages": 80,
        "verified_pdf_range": [5,84],
        "verified_logical_printed_range": [3,82],
        "pending_pages": 25,
        "next_forward_pdf_page": 85,
        "next_forward_printed_page": 83,
    })
    data["final_tamil_verification"].update({
        "verified_pages": 80,
        "verified_pdf_range": [5,84],
        "verified_logical_printed_range": [3,82],
        "pending_pages": 25,
    })
    for part in data["assembly"]["parts_retained_for_provenance"]:
        if part["pdf_range"] == [75,84]:
            part["status"] = "verified-dual-gate"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return True


def sync_metadata() -> bool:
    path = WORK / "metadata.yaml"
    text = path.read_text(encoding="utf-8")
    replacements = [
        ("  visual_fidelity_passed_pages: 70\n  historical_glyph_verified_pages: 70\n  verified_pages: 70", "  visual_fidelity_passed_pages: 80\n  historical_glyph_verified_pages: 80\n  verified_pages: 80"),
        ("  open_first_pass_uncertainty_markers: 29", "  open_first_pass_uncertainty_markers: 19"),
        ("  next_pdf_page: 75\n  next_logical_printed_page: 73", "  next_pdf_page: 85\n  next_logical_printed_page: 83"),
        ("  next_action: \"Resume at PDF 75 / logical printed p.73 with visual source-fidelity and historical-Tamil-glyph verification together; PDF 5-74 are closed as dual-gate verified after retrospective source review and occurrence-specific synchronization.\"", "  next_action: \"Resume at PDF 85 / logical printed p.83 with visual source-fidelity and historical-Tamil-glyph verification together; PDF 5-84 are closed as dual-gate verified, while PDF 5-74 remain the completed retrospective glyph-backfill range.\""),
        ("  audited_pages: 70\n  verified_pages: 70\n  review_pages: 0\n  unresolved_source_readings: 29\n  verified_pdf_pages: \"5-74\"\n  verified_logical_printed_pages: \"3-72\"\n  next_pdf_page: 75\n  next_logical_printed_page: 73", "  audited_pages: 80\n  verified_pages: 80\n  review_pages: 0\n  unresolved_source_readings: 19\n  verified_pdf_pages: \"5-84\"\n  verified_logical_printed_pages: \"3-82\"\n  next_pdf_page: 85\n  next_logical_printed_page: 83"),
        ("  formally_verified_pages: 70\n  verified_pdf_pages: \"5-74\"\n  verified_logical_printed_pages: \"3-72\"\n  pending_pages: 35", "  formally_verified_pages: 80\n  verified_pdf_pages: \"5-84\"\n  verified_logical_printed_pages: \"3-82\"\n  pending_pages: 25"),
        ("  next_pdf_page: 75\n  next_logical_printed_page: 73\n  preserve_controls_passed", "  next_pdf_page: 85\n  next_logical_printed_page: 83\n  preserve_controls_passed"),
        ("  verified_pages: 70\n  verified_pdf_pages: \"5-74\"\n  verified_logical_printed_pages: \"3-72\"\n  pending_pages: 35", "  verified_pages: 80\n  verified_pdf_pages: \"5-84\"\n  verified_logical_printed_pages: \"3-82\"\n  pending_pages: 25"),
        ("  visual_fidelity_audit: in-progress-70-of-105\n  historical_glyph_audit: in-progress-70-of-105-retrospective-closed\n  final_tamil_verification: in-progress-70-of-105-dual-gate", "  visual_fidelity_audit: in-progress-80-of-105\n  historical_glyph_audit: in-progress-80-of-105-forward-combined\n  final_tamil_verification: in-progress-80-of-105-dual-gate"),
        ("next_action: \"Resume at PDF 75 / logical printed p.73 with visual source-fidelity and historical-Tamil-glyph verification together; adjudicate markers 88-116 occurrence-by-occurrence. PDF 5-74 are closed unless new direct source evidence requires a specific local correction. Structured derivatives remain blocked until both gates reach 105/105.\"", "next_action: \"Resume at PDF 85 / logical printed p.83 with visual source-fidelity and historical-Tamil-glyph verification together; adjudicate markers 98-116 occurrence-by-occurrence. PDF 5-84 are closed unless new direct source evidence requires a specific local correction. Structured derivatives remain blocked until both gates reach 105/105.\""),
        ('      pdf_pages: "75-84"\n      printed_pages: "73-82"\n      status: draft', '      pdf_pages: "75-84"\n      printed_pages: "73-82"\n      status: verified-dual-gate'),
    ]
    for old,new in replacements:
        if old not in text:
            raise SystemExit(f"metadata replacement source missing: {old[:80]!r}")
        text = text.replace(old,new,1)
    path.write_text(text,encoding="utf-8")
    return True


def sync_readme(path: Path, handover: bool=False) -> bool:
    text = path.read_text(encoding="utf-8")
    reps = [
        ("70/105 — PDF 5–74", "80/105 — PDF 5–84"),
        ("70/105 passed — PDF 5–74", "80/105 passed — PDF 5–84"),
        ("70/105 — PDF 5–74 closed", "80/105 — PDF 5–84 closed"),
        ("35 pages pending — visual fidelity + glyph audit together", "25 pages pending — visual fidelity + glyph audit together"),
        ("29 — markers 88–116", "19 — markers 98–116"),
        ("PDF 75–109", "PDF 85–109"),
        ("Resume at PDF 75 / logical printed p.73", "Resume at PDF 85 / logical printed p.83"),
        ("markers **88–116**", "markers **98–116**"),
        ("markers 88–116", "markers 98–116"),
    ]
    for old,new in reps:
        text = text.replace(old,new)
    if "verification commit" not in text:
        insert = f"\nForward dual-gate verification through PDF 84 is recorded by commit `{VERIFY_COMMIT}` and `notes/dual-gate-sync-report-pdf-075-084.json`.\n"
        marker = "## Historical Tamil glyph gate" if "## Historical Tamil glyph gate" in text else "## Mandatory historical Tamil glyph gate"
        if marker in text:
            text = text.replace(marker, insert + "\n" + marker,1)
    path.write_text(text,encoding="utf-8")
    return True


def sync_transcription_readme() -> bool:
    path = WORK / "transcription" / "README.md"
    text = path.read_text(encoding="utf-8")
    reps = [
        ("70/105 — PDF 5–74", "80/105 — PDF 5–84"),
        ("35 — PDF 75–109", "25 — PDF 85–109"),
        ("open first-pass uncertain readings: **29**", "open first-pass uncertain readings: **19**"),
        ("next source page: **PDF 75 / logical printed p.73**", "next source page: **PDF 85 / logical printed p.83**"),
        ("PDF 75–84: draft complete, 10 batch markers; dual-gate verification pending.", "PDF 75–84: **dual-gate verified**; markers 88–97 resolved from the rendered scan; synchronization report `../notes/dual-gate-sync-report-pdf-075-084.json`."),
        ("Resume at **PDF 75 / logical printed p.73**", "Resume at **PDF 85 / logical printed p.83**"),
        ("markers **88–116**", "markers **98–116**"),
        ("PDF 5–74 are closed", "PDF 5–84 are closed"),
    ]
    for old,new in reps:
        text = text.replace(old,new)
    path.write_text(text,encoding="utf-8")
    return True


def sync_resolved_notes() -> bool:
    path = WORK / "notes" / "textual-notes-pdf-075-084.md"
    content = f'''# அம்மையப்பன் — resolved uncertainty supplement — PDF 75–84\n\nControlling source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`\n\nStatus: **CLOSED / dual-gate verified**. Markers **88–97** were adjudicated directly from enlarged rendered-scan evidence during the combined visual-fidelity + historical-glyph pass. Canonical/provenance synchronization is recorded by `dual-gate-sync-report-pdf-075-084.json` and commit `{VERIFY_COMMIT}`.\n\nResolved readings:\n\n- **88 / PDF 76:** `ஆண்பாதி—பெண்பாதி—ஆணும் பெண்ணும் அர்த்தநாரீஸ்வரர்களாகவே சிருஷ்டிக்கப்பட வேண்டுமென்பதே`.\n- **89 / PDF 78:** `களிப்பில் ஆடும் மயிலைப்பார்! காதாரப் பண்பாடும் குயிலைப்பார்! ஆறு பார்!—அருவிபார்!—அதன் அழகுபார்!—கொஞ்சும் அருகே வந்துபார்!`.\n- **90 / PDF 79:** `ஏ!...அழக்கூடாது...அன்புக் காட்சி...அழகு மணி மாளிகையின் அலங்காரத் திரு உருவே...அழித் தெழுதா சித்திரமே...ஆடிவரும் பொன்விளக்கே...ஆராரோ...`.\n- **91 / PDF 80:** `வாழைக்குலை மாதிரி`.\n- **92 / PDF 80:** `ஓலைக்குடிசை`.\n- **93 / PDF 82:** `துன்பம் துணையோடு வரும், இன்பம், தனியாக வரும் என்பார்களே, அது தவறு!`.\n- **94 / PDF 82:** food-chain passage resolved through `குறவன் எமனுக்கு ஆகாரம்—அதே வழிதான் என் வழியும்!`.\n- **95 / PDF 84:** invocation resolved from the rendered scan; canonical text now carries the source-supported deity sequence and corrected following wording.\n- **96 / PDF 84:** `அரண்மணிவாசி`.\n- **97 / PDF 84:** `ஆசிரமத்துவாசியாகி`.\n\nNo `⟦…⟧` uncertainty marker remains in PDF 75–84. Genuine controls, including PDF 80 `உன் பேரு என்னு?`, were preserved.\n'''
    path.write_text(content,encoding="utf-8")
    return True


def sync_fidelity_banner() -> bool:
    path = WORK / "notes" / "fidelity-audit.md"
    text = path.read_text(encoding="utf-8")
    marker = "# "
    banner = f"<!-- current-checkpoint: dual-gate verified PDF 5-84; next PDF 85; commit {VERIFY_COMMIT} -->\n"
    if banner not in text:
        text = banner + text
    path.write_text(text,encoding="utf-8")
    return True


def sync_glyph_banner() -> bool:
    path = WORK / "notes" / "historical-glyph-audit.md"
    text = path.read_text(encoding="utf-8")
    banner = f'''## Forward combined-gate checkpoint through PDF 84 — 2026-09-05\n\n- visual fidelity passed: **80/105 — PDF 5–84 / logical pp.3–82**;\n- historical-glyph passed: **80/105 — PDF 5–84 / logical pp.3–82**;\n- final dual-gate verified: **80/105**;\n- PDF 75–84 combined audit: **10/10 PASS**, commit `{VERIFY_COMMIT}`;\n- markers **88–97 resolved**; open markers now **98–116 (19)**;\n- next page: **PDF 85 / logical printed p.83**;\n- retrospective glyph-backfill range remains **PDF 5–74** and is not redefined by this forward checkpoint.\n\n'''
    if banner not in text:
        text = text.replace("# ", "# ",1)
        first_break = text.find("\n\n")
        text = text[:first_break+2] + banner + text[first_break+2:]
    path.write_text(text,encoding="utf-8")
    return True


def sync_registry() -> bool:
    path = ROOT / "data" / "works.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    work = next(x for x in data if x.get("id") == "ammaiyappan")
    work.update({
        "canonical_tamil_verified_pages": 80,
        "canonical_tamil_visual_fidelity_passed_pages": 80,
        "canonical_tamil_historical_glyph_verified_pages": 80,
        "tamil_transcription_verified_pages": 80,
        "tamil_transcription_visual_fidelity_passed_pages": 80,
        "tamil_transcription_historical_glyph_verified_pages": 80,
        "total_verified_pages": 80,
        "total_visual_fidelity_passed_pages": 80,
        "total_historical_glyph_verified_pages": 80,
        "historical_glyph_verified_pdf_pages": "5-84",
        "historical_glyph_verified_logical_printed_pages": "3-82",
        "fidelity_audit_verified_pdf_pages": "5-84",
        "fidelity_audit_verified_logical_printed_pages": "3-82",
        "fidelity_audit_next_pdf_page": 85,
        "historical_glyph_audit_next_pdf_page": 85,
        "tamil_fidelity_audit": "in-progress-80-of-105",
        "historical_glyph_audit": "in-progress-80-of-105-forward-combined",
        "final_tamil_verification": "dual-gate-in-progress-80-of-105",
        "forward_dual_gate_verified_through_pdf": 84,
        "forward_dual_gate_verification_commit": VERIFY_COMMIT,
        "next_action": "Resume at PDF 85 / logical printed p.83 with visual source-fidelity and historical-Tamil-glyph verification together; adjudicate markers 98-116 occurrence-by-occurrence."
    })
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return True


def sync_root_readme() -> bool:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    start = text.index("## அம்மையப்பன் status")
    end = text.index("## கலைஞர் திரை இசைப் பாடல்கள் status")
    section = f'''## அம்மையப்பன் status\n\n`TVA_BOK_0064230_அம்மையப்பன்.pdf` is an active **111-page image-only screenplay/dialogue booklet** whose canonical Tamil first pass is complete and whose Tamil verification uses a **dual gate: visual source fidelity + historical-Tamil-glyph verification**.\n\n- canonical Tamil first pass: **draft-complete — 105/105 pages**;\n- first-pass assembly QA: **PASS — 105 anchors, exact PDF 5→109 order, 0 missing, 0 duplicate**;\n- visual source-fidelity audit: **80/105 passed — PDF 5–84 / logical pp.3–82**;\n- historical Tamil glyph audit: **80/105 passed — PDF 5–84 / logical pp.3–82**;\n- final dual-gate Tamil verified: **80/105**;\n- retrospective historical-glyph backfill: **PDF 5–74 CLOSED**;\n- forward combined dual-gate batch PDF 75–84: **10/10 PASS**, commit `{VERIFY_COMMIT}`;\n- PDF 85–109: **25 pages pending**;\n- open first-pass uncertainty markers: **19 — markers 98–116**;\n- structured derivatives / English / reader: **blocked pending complete 105/105 dual-gate verified Tamil**.\n\nThe historical-glyph pass follows `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`. No global historical-glyph replacement is permitted; source pixels and same-edition evidence control character identity.\n\n**Next:** resume at **PDF 85 / logical printed p.83** with visual source-fidelity and historical-Tamil-glyph verification together; adjudicate markers 98–116 occurrence-by-occurrence.\n\n'''
    path.write_text(text[:start]+section+text[end:],encoding="utf-8")
    return True


def sync_master_handover() -> bool:
    path = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
    text = path.read_text(encoding="utf-8")
    marker = "## 16. Ammayappan active checkpoint"
    if marker not in text:
        raise SystemExit("master handover marker missing")
    prefix = text.split(marker,1)[0]
    section = f'''## 16. Ammayappan active checkpoint\n\nWork path: `works/ammaiyappan/`  \nSource: `TVA_BOK_0064230_அம்மையப்பன்.pdf`\n\n- canonical first pass: **105/105 draft-complete**;\n- assembly QA: **PASS — 105 anchors / 0 missing / 0 duplicate**;\n- visual source-fidelity: **80/105 — PDF 5–84 / logical pp.3–82 passed**;\n- historical-Tamil-glyph audit: **80/105 — PDF 5–84 / logical pp.3–82 passed**;\n- final dual-gate Tamil verified: **80/105**;\n- retrospective glyph backfill: **PDF 5–74 CLOSED**;\n- forward PDF 75–84 combined audit: **10/10 PASS**, commit `{VERIFY_COMMIT}`;\n- remaining range: **PDF 85–109 = 25 pages**;\n- open first-pass uncertainty markers: **19 — markers 98–116**;\n- structured derivatives / English / reader: **blocked pending 105/105 dual-gate verified Tamil**.\n\n**Exact next activity:** resume at **PDF 85 / logical printed p.83**, performing rendered-scan visual source-fidelity verification and the historical-Tamil-glyph audit together; adjudicate markers 98–116 only from source evidence.\n'''
    path.write_text(prefix+section,encoding="utf-8")
    return True


def sync_status_audit() -> bool:
    path = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("70/105", "80/105")
    text = text.replace("PDF 5–74 / logical pp.3–72", "PDF 5–84 / logical pp.3–82")
    text = text.replace("PDF 75–109", "PDF 85–109")
    text = text.replace("35 pages", "25 pages")
    text = text.replace("markers 88–116", "markers 98–116")
    text = text.replace("PDF 75 / logical printed p.73", "PDF 85 / logical printed p.83")
    path.write_text(text,encoding="utf-8")
    return True


def main():
    changed=[]
    funcs=[
        ("works/ammaiyappan/transcription/index.json", sync_index),
        ("works/ammaiyappan/metadata.yaml", sync_metadata),
        ("works/ammaiyappan/README.md", lambda: sync_readme(WORK/"README.md")),
        ("works/ammaiyappan/PROJECT_HANDOVER.md", lambda: sync_readme(WORK/"PROJECT_HANDOVER.md", True)),
        ("works/ammaiyappan/transcription/README.md", sync_transcription_readme),
        ("works/ammaiyappan/notes/textual-notes-pdf-075-084.md", sync_resolved_notes),
        ("works/ammaiyappan/notes/fidelity-audit.md", sync_fidelity_banner),
        ("works/ammaiyappan/notes/historical-glyph-audit.md", sync_glyph_banner),
        ("data/works.json", sync_registry),
        ("README.md", sync_root_readme),
        ("docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md", sync_master_handover),
        ("docs/STATUS_CONSISTENCY_AUDIT.md", sync_status_audit),
    ]
    for label,fn in funcs:
        if fn(): changed.append(label)
    print(json.dumps({"status":"updated","verified_pages":80,"next_pdf":85,"changed":changed},ensure_ascii=False,indent=2))

if __name__ == "__main__":
    main()
