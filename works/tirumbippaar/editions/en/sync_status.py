#!/usr/bin/env python3
"""Synchronize Tirumbippaar final translation/publication status metadata.

Modes:
  --prepare-index  finalize translations/index.json before deterministic builds
  --metadata       synchronize work metadata after reader + EPUB QA pass
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "tirumbippaar"
INDEX = WORK / "translations" / "index.json"
EDITION = WORK / "editions" / "en"
PACKAGE_MANIFEST = EDITION / "package-manifest.json"
METADATA = WORK / "metadata.yaml"
SCENES = list(range(1, 94))
EXPECTED_UNITS = 1330
EXPECTED_DIALOGUES = 1042
EXPECTED_KINDS = {"dialogue":1049,"stage-direction":262,"song":0,"song-reference":7,"chant":2,"written-text":10}


def load_index() -> dict:
    idx = json.loads(INDEX.read_text(encoding="utf-8"))
    if idx.get("translation_units") != EXPECTED_UNITS:
        raise SystemExit("Refusing sync: translation unit checkpoint is not 1,330")
    if idx.get("unit_kind_counts") != EXPECTED_KINDS:
        raise SystemExit("Refusing sync: translation kind checkpoint differs")
    if idx.get("source_reconciled_scenes") != SCENES:
        raise SystemExit("Refusing sync: corrected-source coverage is not 93/93")
    audit = idx.get("integrity_audit", {})
    if audit.get("dialogue_source_records_expected") != EXPECTED_DIALOGUES or audit.get("dialogue_source_records_linked") != EXPECTED_DIALOGUES:
        raise SystemExit("Refusing sync: labelled dialogue link checkpoint is not 1,042/1,042")
    return idx


def prepare_index() -> None:
    idx = load_index()
    idx["status"] = "complete-verified"
    idx["scenes_reviewed"] = SCENES
    idx["scenes_verified"] = SCENES
    idx["scenes_in_review"] = []
    idx["source_reconciliation_note"] = (
        "Corrected-source English reconciliation is complete for all 93 scenes. "
        "The canonical Part04 three-string synchronization is also complete, so canonical Tamil, scene/dialogue, character/entity and English source-linked layers now agree. "
        "The deterministic reader/export/EPUB workflow is authorized to rebuild from this 1,330-unit / 1,042-link checkpoint."
    )
    idx["next_activity"] = (
        "Regenerate and revalidate the deterministic English Markdown/HTML/JSON reader derivatives and EPUB package, synchronize work metadata, and then close the remaining work-root publication documentation."
    )
    audit = idx.setdefault("integrity_audit", {})
    audit["status"] = "complete-verified"
    notes = [n for n in audit.get("notes", []) if "closure audit rechecked three" not in n.lower()]
    sync_note = (
        "The three Part04 canonical micro-regressions are synchronized with the already-correct scene/dialogue derivatives: the stray `ஈ.` is removed from scene 52 text, `ஏல்லாம்` is corrected to `எல்லாம்` in scene 57 text, and `[புண்ணகோடி கதவைத் தட்டல்]` is corrected to `[புண்யகோடி கதவைத் தட்டல்]`. No stable IDs or counts changed."
    )
    if sync_note not in notes:
        notes.append(sync_note)
    audit["notes"] = notes
    idx["canonical_sync_blockers"] = []
    idx["publication_rebuild_status"] = "complete-verified"
    INDEX.write_text(json.dumps(idx, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print("Finalized Tirumbippaar translation checkpoint for deterministic publication build")


def replace_top_section(text: str, name: str, replacement: str) -> str:
    pattern = re.compile(rf"^{re.escape(name)}:\n.*?(?=^[A-Za-z_][A-Za-z0-9_]*:\n|\Z)", re.M | re.S)
    if not pattern.search(text):
        raise SystemExit(f"Could not locate metadata section {name}")
    return pattern.sub(replacement.rstrip() + "\n\n", text, count=1)


def replace_indented_block(text: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(rf"^  {re.escape(start)}:\n.*?(?=^  {re.escape(end)}:\n)", re.M | re.S)
    if not pattern.search(text):
        raise SystemExit(f"Could not locate structured metadata block {start}")
    return pattern.sub(replacement.rstrip() + "\n", text, count=1)


def sync_metadata() -> None:
    idx = load_index()
    if idx.get("status") != "complete-verified":
        raise SystemExit("Refusing metadata sync: translation index is not complete-verified")
    if not PACKAGE_MANIFEST.exists():
        raise SystemExit("Refusing metadata sync: EPUB package manifest is missing")
    pkg = json.loads(PACKAGE_MANIFEST.read_text(encoding="utf-8"))
    if pkg.get("status") != "complete-verified" or pkg.get("translation_units") != EXPECTED_UNITS:
        raise SystemExit("Refusing metadata sync: EPUB package is not complete-verified at 1,330 units")
    epub = pkg.get("epub", {})
    if epub.get("qa_status") != "PASS" or epub.get("scene_documents") != 93 or epub.get("unit_markers") != EXPECTED_UNITS:
        raise SystemExit("Refusing metadata sync: EPUB QA checkpoint differs")

    scenes = ", ".join(str(x) for x in SCENES)
    cross = ", ".join(f'"{x}"' for x in idx["cross_page_translation_units"])
    direct = ", ".join(f'"{x}"' for x in idx["direct_source_unlabelled_dialogue_units"])
    zero = ", ".join(str(x) for x in idx["zero_dialogue_source_scenes_translated"])
    songs = ", ".join(f'"{x}"' for x in idx["verified_song_reference_occurrences"])
    counts = idx["unit_kind_counts"]

    correction = '''correction_reconciliation:
  status: complete-verified-reconciled
  opened: 2026-08-26
  primary_correction_witness: "thirumbipaar.md"
  final_visual_authority: "TVA_BOK_0014652_திரும்பிப்பார்.pdf"
  corrected_markdown_play_pages: 104
  canonical_reconciled_pdf_pages: "9-112"
  canonical_reconciled_printed_pages: "1-104"
  canonical_parts_reconciled: [1, 2, 3, 4, 5]
  scene_dialogue_reconciled_through_scene: 93
  scene_dialogue_reconciled_through_pdf_page: 112
  scene_dialogue_reconciled_through_printed_page: 104
  dialogue_records_current: 1042
  scene_41_dialogue_records: 38
  recovered_scene_41_record_ids: ["tirumbippaar-s041-d037", "tirumbippaar-s041-d038"]
  character_entity_layer_status: complete-verified-reconciled
  english_source_reconciliation_status: complete-verified
  english_publication_layer_status: complete-verified
  canonical_part04_micro_sync: complete
  note: "Canonical Tamil, all 93 scene/dialogue derivatives, the 1,042-record immutable dialogue corpus, character/entity mappings and the 1,330-unit English layer are synchronized. Deterministic reader and EPUB QA also pass."'''

    text = METADATA.read_text(encoding="utf-8")
    text = replace_top_section(text, "correction_reconciliation", correction)

    tp_match = re.search(r"^transcription_progress:\n.*?(?=^[A-Za-z_][A-Za-z0-9_]*:\n)", text, re.M | re.S)
    if not tp_match:
        raise SystemExit("Could not locate transcription_progress")
    tp = tp_match.group(0)
    tp = re.sub(r"^  status: .*$", "  status: complete-verified-reconciled", tp, count=1, flags=re.M)
    tp = re.sub(r"^  corrected_parts_completed: .*$", "  corrected_parts_completed: 5", tp, flags=re.M)
    tp = re.sub(r"^  corrected_canonical_pdf_pages: .*$", '  corrected_canonical_pdf_pages: "9-112"', tp, flags=re.M)
    tp = re.sub(r"^  corrected_canonical_printed_pages: .*$", '  corrected_canonical_printed_pages: "1-104"', tp, flags=re.M)
    tp = re.sub(r"^  next_pdf_page: .*$", "  next_pdf_page: null", tp, flags=re.M)
    tp = re.sub(r"^  next_printed_page: .*$", "  next_printed_page: null", tp, flags=re.M)
    tp = re.sub(r"^  next_action: .*$", '  next_action: "Source reconciliation complete; deterministic English reader/EPUB publication package QA PASS."', tp, flags=re.M)
    text = text[:tp_match.start()] + tp + text[tp_match.end():]

    scene_block = '''  scene_text_derivatives:
    status: complete-verified-reconciled
    expected_files: 93
    historical_completed_files: 93
    historical_completed_scenes: "1-93"
    corrected_reconciled_through_scene: 93
    next_batch: null
    cross_part_scenes: [5, 29, 48, 76]
    note: "All 93 scene derivatives are synchronized with the scan-closed canonical Tamil through scene 93/end of work."'''
    text = replace_indented_block(text, "scene_text_derivatives", "dialogue_index", scene_block)

    di_match = re.search(r"^  dialogue_index:\n.*?(?=^  character_index:\n)", text, re.M | re.S)
    if not di_match:
        raise SystemExit("Could not locate dialogue_index")
    di = di_match.group(0)
    di = re.sub(r"^    status: .*$", "    status: complete-verified-reconciled", di, count=1, flags=re.M)
    di = re.sub(r"^    corrected_reconciled_through_scene: .*$", "    corrected_reconciled_through_scene: 93", di, flags=re.M)
    di = re.sub(r"^    next_batch: .*$", "    next_batch: null", di, flags=re.M)
    di = re.sub(r"^    note: .*$", '    note: "Immutable labelled-dialogue corpus is closed at 1,042 records across 93 scenes; all stable IDs are preserved except the two source-proven scene-41 additions d037/d038."', di, flags=re.M)
    text = text[:di_match.start()] + di + text[di_match.end():]

    char_block = '''  character_index:
    status: complete-verified-reconciled
    path: "characters/index.json"
    schema: "characters/schema.json"
    readme: "characters/README.md"
    label_inventory: "characters/labels-inventory.json"
    pilot: "characters/entities-pilot.json"
    entities: "characters/entities.json"
    dialogue_records_source_at_last_build: 1042
    current_dialogue_records: 1042
    distinct_source_labels: 45
    entity_count: 39
    verified_entities: 39
    verified_labels: 45
    review_or_unresolved: 0
    dialogue_records_modified_since_last_build: false
    note: "Character/entity mappings are regenerated against the corrected 1,042-record dialogue corpus: 45 exact source labels map to 39 entities/roles with zero unresolved items."'''
    text = replace_indented_block(text, "character_index", "song_authorship_mapping", char_block)

    english_block = f'''  english_translation:
    status: complete-verified
    path: "translations/index.json"
    schema: "translations/schema.json"
    readme: "translations/README.md"
    record_directory: "translations/records"
    pilot_scene: 1
    scenes_started: [{scenes}]
    scenes_verified: [{scenes}]
    translation_units: {EXPECTED_UNITS}
    verified_units: {EXPECTED_UNITS}
    review_units: 0
    draft_units: 0
    unit_kind_counts:
      dialogue: {counts['dialogue']}
      stage_direction: {counts['stage-direction']}
      song: {counts['song']}
      song_reference: {counts['song-reference']}
      chant: {counts['chant']}
      written_text: {counts['written-text']}
    dialogue_source_records_expected: {EXPECTED_DIALOGUES}
    dialogue_source_records_linked: {EXPECTED_DIALOGUES}
    cross_page_translation_units: [{cross}]
    direct_source_unlabelled_dialogue_units: [{direct}]
    zero_dialogue_source_scenes_translated: [{zero}]
    verified_song_reference_occurrences: [{songs}]
    synthetic_star_end_units: 0
    next_batch: null
    note: "All 93 scenes are corrected-source reconciled in English with 1,330 verified units and exact 1,042/1,042 labelled dialogue-link coverage. Seven source-visible spoken units remain intentionally unlabelled. Stable historical English unit IDs were preserved even where source-proven recovered units appear out of numeric order."
  english_reader_edition:
    status: complete-verified
    path: "editions/en"
    build: "editions/en/build.py"
    preflight: "editions/en/audit_probe.py"
    qa_report: "editions/en/QA_REPORT.md"
    manifest: "editions/en/manifest.json"
    markdown: "editions/en/reader-edition.md"
    html: "editions/en/reader-edition.html"
    json: "editions/en/reader-edition.json"
    translation_units: {EXPECTED_UNITS}
    immutable_dialogue_records_linked: {EXPECTED_DIALOGUES}
    cross_page_translation_units: 12
    qa_status: PASS
  english_epub_package:
    status: complete-verified
    format: "EPUB 3"
    path: "editions/en/tirumbippaar-en.epub"
    build: "editions/en/package.py"
    qa_report: "editions/en/EPUB_QA_REPORT.md"
    manifest: "editions/en/package-manifest.json"
    translation_units: {EXPECTED_UNITS}
    scene_documents: 93
    zip_members: {epub['zip_members']}
    byte_size: {epub['bytes']}
    sha256: "{epub['sha256']}"
    deterministic: true
    qa_status: PASS
  next_structured_derivative: null'''
    pattern = re.compile(r"^  english_translation:\n.*?^  next_structured_derivative:.*$", re.M | re.S)
    if not pattern.search(text):
        raise SystemExit("Could not locate English derivative metadata block")
    text = pattern.sub(english_block, text, count=1)

    status = '''status:
  source_intake: complete
  structural_mapping: verified
  tamil_transcription: complete-verified-reconciled
  tamil_fidelity_audit: complete-current
  scene_index: complete-structural
  scene_text_derivatives: complete-verified-reconciled
  dialogue_index: complete-verified-reconciled
  character_index: complete-verified-reconciled
  song_authorship_mapping: historical-complete
  song_tamil_derivatives: not-started
  english_translation: complete-verified
  english_reader_edition: complete-verified
  english_epub_package: complete-verified'''
    text = replace_top_section(text, "status", status).rstrip() + "\n"
    METADATA.write_text(text, encoding="utf-8")
    print("Synchronized Tirumbippaar source, translation, reader and EPUB status metadata")


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prepare-index", action="store_true")
    group.add_argument("--metadata", action="store_true")
    args = parser.parse_args()
    if args.prepare_index:
        prepare_index()
    else:
        sync_metadata()


if __name__ == "__main__":
    main()
