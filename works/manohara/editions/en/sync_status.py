#!/usr/bin/env python3
"""Synchronize Manohara reader/export status after a passing deterministic build."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "manohara"
EDITION = WORK / "editions" / "en"
MANIFEST = EDITION / "manifest.json"
METADATA = WORK / "metadata.yaml"
WORK_README = WORK / "README.md"
TRANS_README = WORK / "translations" / "README.md"
ROOT_README = ROOT / "README.md"

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
if manifest.get("status") != "complete-verified" or manifest.get("qa_status") != "PASS":
    raise SystemExit("Refusing status sync: Manohara reader manifest is not complete-verified/PASS")
if manifest.get("translation_units") != 1190 or manifest.get("immutable_dialogue_records_linked") != 983:
    raise SystemExit("Refusing status sync: Manohara reader checkpoint totals differ")
outputs = manifest.get("outputs", {})
required_outputs = {"reader-edition.md", "reader-edition.html", "reader-edition.json", "QA_REPORT.md"}
if set(outputs) != required_outputs:
    raise SystemExit("Refusing status sync: expected reader outputs are incomplete")

# Metadata: promote the passed preflight into a completed reader/export derivative.
text = METADATA.read_text(encoding="utf-8")
old_action = '  next_action: "Generate deterministic English reader/export derivatives in Markdown, standalone HTML and machine-readable JSON; run generated-output QA and write an integrity manifest before Reading Room integration."'
new_action = '  next_action: "Integrate the complete-verified Manohara English reader derivative into the Reading Room using verified structured data; keep the repository reader package as the reproducible publication/export checkpoint."'
if old_action not in text and new_action not in text:
    raise SystemExit("Could not locate Manohara metadata next_action checkpoint")
text = text.replace(old_action, new_action)
old_tail = '''  reader_export: ready-after-preflight
  reading_room_integration: blocked-pending-reader-export-generation-and-qa
  next_structured_derivative: reader-export'''
new_tail = '''  reader_export: complete-verified
  english_reader_edition_path: "editions/en"
  english_reader_build_script_path: "editions/en/build.py"
  english_reader_qa_report_path: "editions/en/QA_REPORT.md"
  english_reader_manifest_path: "editions/en/manifest.json"
  english_reader_markdown_path: "editions/en/reader-edition.md"
  english_reader_html_path: "editions/en/reader-edition.html"
  english_reader_json_path: "editions/en/reader-edition.json"
  english_reader_translation_units: 1190
  english_reader_dialogue_links: 983
  english_reader_source_unlabelled_spoken_units: 27
  english_reader_cross_page_units: 17
  english_reader_song_occurrence_links: 6
  english_reader_qa_status: PASS
  english_reader_deterministic: true
  reading_room_integration: ready-after-reader-export-qa
  next_structured_derivative: reading-room-integration'''
if old_tail not in text and new_tail not in text:
    raise SystemExit("Could not locate Manohara metadata reader-export checkpoint")
text = text.replace(old_tail, new_tail)
METADATA.write_text(text, encoding="utf-8")

# Work README: reader/export generation is now complete and Reading Room integration is unblocked.
text = WORK_README.read_text(encoding="utf-8")
text = text.replace(
    '| English reader/export generation | **ready / not-started** |\n| Reading Room integration | blocked pending generated reader/export QA |',
    '| English reader/export generation | **complete-verified — Markdown / HTML / JSON / manifest** |\n| Reading Room integration | **ready after reader/export QA** |',
)
old_next = 'Generate the deterministic **English reader/export package** in Markdown, standalone HTML and machine-readable JSON, then run generated-output QA and write an integrity manifest before Reading Room integration.'
new_section = '''The deterministic English reader/export package is now **complete-verified**. `editions/en/reader-edition.md`, `reader-edition.html` and `reader-edition.json` each contain all **1,190** verified English units exactly once. Generated-output QA confirms exact **983/983** immutable dialogue linkage, all **27** source-unlabelled spoken units, all **17** cross-page units and all **6/6** song/performance links. `editions/en/manifest.json` records deterministic input/output hashes and `editions/en/QA_REPORT.md` records the PASS disposition.

No canonical Tamil, scene, dialogue, character or song-inventory layer was modified by reader generation.

## Next activity

Integrate the verified structured Manohara English reader into the **Kalaignar Digital Library / Reading Room**, preserving archival-scene labelling as derivative navigation because the booklet prints no scene numbers.'''
if old_next in text:
    text = text.replace('## Next activity\n\n' + old_next, '## Reader/export package — PASS\n\n' + new_section)
elif '## Reader/export package — PASS' not in text:
    raise SystemExit("Could not locate Manohara work README next activity")
WORK_README.write_text(text, encoding="utf-8")

# Translation README: close the export gate and point to the Reading Room integration step.
text = TRANS_README.read_text(encoding="utf-8")
old = '**Next:** generate deterministic publication-facing Markdown, standalone HTML and machine-readable JSON; then run generated-output QA and write an integrity manifest before Reading Room integration.'
new = '''## Reader/export package — PASS

The deterministic publication-facing derivatives are now complete under `../editions/en/`: Markdown, standalone HTML and machine-readable JSON each contain all **1,190** verified English units exactly once. Generated-output QA and the integrity manifest both pass; exact **983/983** dialogue linkage, **27** null-speaker spoken units, **17** cross-page units and **6/6** song/performance links are preserved.

**Next:** integrate this verified structured derivative into the Reading Room; do not infer source scene numbering from the archive's 57 navigation segments.'''
if old in text:
    text = text.replace(old, new)
elif '## Reader/export package — PASS' not in text:
    raise SystemExit("Could not locate Manohara translation README export checkpoint")
TRANS_README.write_text(text, encoding="utf-8")

# Repository summary: advance the top-level Manohara checkpoint.
text = ROOT_README.read_text(encoding="utf-8")
old = '**Next:** generate deterministic Manohara English reader/export derivatives in Markdown, standalone HTML and machine-readable JSON; run generated-output QA and write an integrity manifest before Reading Room integration.'
new = '''The deterministic **Manohara English reader/export package now passes generated-output QA**: Markdown, standalone HTML and machine-readable JSON each contain all 1,190 verified units exactly once, with an integrity manifest recording reproducible input/output hashes. No canonical Tamil or structured source derivative was changed.

**Next:** integrate the verified Manohara English reader into the Kalaignar Digital Library / Reading Room, preserving the 57 scene IDs strictly as archival navigation rather than source numbering.'''
if old in text:
    text = text.replace(old, new)
elif 'Manohara English reader/export package now passes generated-output QA' not in text:
    raise SystemExit("Could not locate repository Manohara reader-export checkpoint")
ROOT_README.write_text(text, encoding="utf-8")

print("Synchronized Manohara reader/export PASS status and Reading Room readiness")
