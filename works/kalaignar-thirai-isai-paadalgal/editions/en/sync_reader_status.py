#!/usr/bin/env python3
"""Synchronize repository status after deterministic anthology English reader QA PASS."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "kalaignar-thirai-isai-paadalgal"
EDITION = WORK / "editions" / "en"
WORK_ID = "kalaignar-thirai-isai-paadalgal"

QA_PATH = EDITION / "QA_REPORT.md"
MANIFEST_PATH = EDITION / "manifest.json"

EXPECTED_OUTPUTS = {
    "reader-edition.md": "42e13ad7a171b4304ef4b1b8b424fa7f50ebace8510c7ea864f49c31dc9cc209",
    "reader-edition.html": "d48bd5476ba3cbdc540334abaf743b4481d0a1b7cae37d5bc4198f15adebc034",
    "reader-edition.json": "8e9782ca160e07bd9f45be38931d3d3ad07c3a126a0be6755b67e7e7fdec1ed8",
    "QA_REPORT.md": "1b2c593944530b922d8e93ba010bdf378b98f9b9734a1c13a5706da7af9475b1",
}

if not QA_PATH.exists() or "Status: **PASS**" not in QA_PATH.read_text(encoding="utf-8"):
    raise SystemExit("generated-output QA report is missing or not PASS")
manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
if manifest.get("status") != "complete-verified" or manifest.get("input_count") != 110:
    raise SystemExit("reader manifest is missing the complete-verified 110-input checkpoint")
outputs = {Path(item["path"]).name: item["sha256"] for item in manifest.get("outputs", [])}
if outputs != EXPECTED_OUTPUTS:
    raise SystemExit(f"generated output hash checkpoint drifted: {outputs}")


def replace_idempotent(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old in text:
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        return
    if new in text:
        return
    raise SystemExit(f"status synchronization text not found in {path.relative_to(ROOT)}")


def replace_section(path: Path, start: str, end: str | None, new_section: str) -> None:
    text = path.read_text(encoding="utf-8")
    start_pos = text.find(start)
    if start_pos < 0:
        raise SystemExit(f"section {start!r} not found in {path.relative_to(ROOT)}")
    if end is None:
        end_pos = len(text)
    else:
        end_pos = text.find(end, start_pos + len(start))
        if end_pos < 0:
            raise SystemExit(f"section end {end!r} not found in {path.relative_to(ROOT)}")
    replacement = new_section.rstrip() + "\n\n"
    current = text[start_pos:end_pos]
    if current == replacement:
        return
    path.write_text(text[:start_pos] + replacement + text[end_pos:], encoding="utf-8")


# Machine registry.
registry_path = ROOT / "data" / "works.json"
registry = json.loads(registry_path.read_text(encoding="utf-8"))
entry = next((item for item in registry if item.get("id") == WORK_ID), None)
if entry is None:
    raise SystemExit(f"missing {WORK_ID} in data/works.json")
entry.update({
    "english_reader_preflight": "complete-pass",
    "english_reader_preflight_report_path": "works/kalaignar-thirai-isai-paadalgal/editions/en/PREFLIGHT_QA_REPORT.md",
    "reader_export": "complete-verified",
    "english_reader_edition_directory": "works/kalaignar-thirai-isai-paadalgal/editions/en",
    "english_reader_markdown_path": "works/kalaignar-thirai-isai-paadalgal/editions/en/reader-edition.md",
    "english_reader_html_path": "works/kalaignar-thirai-isai-paadalgal/editions/en/reader-edition.html",
    "english_reader_json_path": "works/kalaignar-thirai-isai-paadalgal/editions/en/reader-edition.json",
    "english_reader_qa": "PASS",
    "english_reader_qa_report_path": "works/kalaignar-thirai-isai-paadalgal/editions/en/QA_REPORT.md",
    "english_reader_manifest_path": "works/kalaignar-thirai-isai-paadalgal/editions/en/manifest.json",
    "english_reader_qa_songs": 54,
    "english_reader_qa_line_cues": 1105,
    "english_reader_qa_cross_page_records": 8,
    "english_reader_qa_errors": 0,
    "english_reader_qa_warnings": 0,
    "english_reader_markdown_sha256": EXPECTED_OUTPUTS["reader-edition.md"],
    "english_reader_html_sha256": EXPECTED_OUTPUTS["reader-edition.html"],
    "english_reader_json_sha256": EXPECTED_OUTPUTS["reader-edition.json"],
    "reading_room_integration": "ready-after-reader-export-qa",
    "next_action": "Downstream Reading Room integration is ready; no required repository-internal transcription, translation, preflight, or reader/export work remains."
})
registry_path.write_text(json.dumps(registry, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

# Work metadata.
metadata = WORK / "metadata.yaml"
old_reader = '''reader_export:
  preflight_status: complete-pass
  preflight_report_path: "editions/en/PREFLIGHT_QA_REPORT.md"
  preflight_workflow: ".github/workflows/kalaignar-song-anthology-english-preflight.yml"
  preflight_probe: "editions/en/audit_probe.py"
  preflight_translation_records: 54
  preflight_source_links: 54
  preflight_mapped_tamil_lines: 1105
  preflight_mapped_english_lines: 1105
  preflight_cross_page_records: 8
  preflight_errors: 0
  preflight_warnings: 0
  status: not-started
  next_action: "Generate deterministic English reader/export derivatives from the 54 complete-verified translation records, then run generated-output QA and create an integrity manifest."
'''
new_reader = '''reader_export:
  preflight_status: complete-pass
  preflight_report_path: "editions/en/PREFLIGHT_QA_REPORT.md"
  preflight_workflow: ".github/workflows/kalaignar-song-anthology-english-preflight.yml"
  preflight_probe: "editions/en/audit_probe.py"
  preflight_translation_records: 54
  preflight_source_links: 54
  preflight_mapped_tamil_lines: 1105
  preflight_mapped_english_lines: 1105
  preflight_cross_page_records: 8
  preflight_errors: 0
  preflight_warnings: 0
  status: complete-verified
  edition_directory: "editions/en"
  build_script: "editions/en/build.py"
  markdown_path: "editions/en/reader-edition.md"
  html_path: "editions/en/reader-edition.html"
  json_path: "editions/en/reader-edition.json"
  qa_report_path: "editions/en/QA_REPORT.md"
  manifest_path: "editions/en/manifest.json"
  generated_songs: 54
  generated_line_cues: 1105
  generated_cross_page_records: 8
  generated_errors: 0
  generated_warnings: 0
  markdown_sha256: "42e13ad7a171b4304ef4b1b8b424fa7f50ebace8510c7ea864f49c31dc9cc209"
  html_sha256: "d48bd5476ba3cbdc540334abaf743b4481d0a1b7cae37d5bc4198f15adebc034"
  json_sha256: "8e9782ca160e07bd9f45be38931d3d3ad07c3a126a0be6755b67e7e7fdec1ed8"
  reading_room_integration: ready-after-reader-export-qa
  next_action: "Downstream Reading Room integration is ready; no required repository-internal transcription, translation, preflight, or reader/export work remains."
'''
replace_idempotent(metadata, old_reader, new_reader)
replace_idempotent(metadata, "  reader_export: not-started", "  reader_export: complete-verified")

# Progress.
progress = WORK / "PROGRESS.md"
replace_section(progress, "## Current phase", "## Source/Tamil checkpoint", '''## Current phase

**English reader/export — complete-verified; generated-output QA PASS.**

Both immutable source-linked content layers remain closed:

- Tamil songs: **54/54 complete-verified**;
- English translations: **54/54 complete-verified**.

The whole-corpus preflight passed, and deterministic Markdown, standalone HTML and machine-readable JSON reader derivatives have now been generated and reconciled without rewriting the verified English.''')
replace_section(progress, "## Next activity", None, '''## Deterministic reader/export package

Generated under `editions/en/`:

- `reader-edition.md` — **124,018 bytes**, SHA-256 `42e13ad7a171b4304ef4b1b8b424fa7f50ebace8510c7ea864f49c31dc9cc209`;
- `reader-edition.html` — **187,842 bytes**, SHA-256 `d48bd5476ba3cbdc540334abaf743b4481d0a1b7cae37d5bc4198f15adebc034`;
- `reader-edition.json` — **354,382 bytes**, SHA-256 `8e9782ca160e07bd9f45be38931d3d3ad07c3a126a0be6755b67e7e7fdec1ed8`;
- `QA_REPORT.md` — generated-output QA **PASS**;
- `manifest.json` — deterministic checkpoint across **110 authoritative inputs** and all publication outputs.

Generated-output QA confirms **54/54 songs**, **1,105/1,105 English lines/cues**, **8/8 cross-page records**, the **3 pilot-verified / 51 verified** distinction, and **54/54 anthology-attributed** states with zero missing/extra/duplicate IDs, zero text drift, and **0 warnings / 0 errors**.

Kalaignar-language English is copied exactly from the verified records; the reader build performs no stylistic smoothing.

## Next activity

No required repository-internal transcription, translation, preflight, or reader/export work remains. The work is ready for **downstream Kalaignar Digital Library / Reading Room integration**, preserving anthology order, provenance, item-status history, attribution discipline and the source-faithful English.''')

# Work audit.
audit = WORK / "AUDIT.md"
replace_section(audit, "## Current gate result", None, '''## Final gate result

- Tamil transcription: **complete-verified — 54/54**;
- Tamil fidelity audit: **complete**;
- English translation: **complete-verified — 54/54**;
- English reader/export preflight: **complete-pass**;
- deterministic reader/export package: **complete-verified**;
- generated-output QA: **PASS**;
- generated songs: **54/54**;
- generated English lines/cues: **1,105/1,105**;
- cross-page records: **8/8**;
- generated-output warnings/errors: **0/0**.

**PASS — the source-linked Tamil and English layers and the deterministic English reader/export derivative are all closed at their verified checkpoints.**

## Generated-output integrity

`editions/en/QA_REPORT.md` confirms that Markdown, standalone HTML and machine-readable JSON each retain the complete 54-song anthology order and all 1,105 English lines/cues. There are zero missing/extra/duplicate song IDs, translation IDs or line IDs, zero source-page/status/attribution drift and zero English text drift in the machine-addressable outputs.

`editions/en/manifest.json` hashes **110 authoritative inputs** and the generated Markdown, HTML, JSON and QA report. Output SHA-256 values are recorded in `metadata.yaml`.

## Next activity

No required repository-internal archival or publication-generation gate remains for this anthology. Downstream Reading Room integration may proceed without reopening or smoothing the verified Tamil or Kalaignar-language English.''')

# Work README.
work_readme = WORK / "README.md"
replace_section(work_readme, "## English reader/export preflight", "## Attribution", '''## English reader/export

**Complete-verified — preflight PASS and generated-output QA PASS.**

Preflight: `editions/en/PREFLIGHT_QA_REPORT.md`  
Generated-output QA: `editions/en/QA_REPORT.md`  
Integrity manifest: `editions/en/manifest.json`  
Builder: `editions/en/build.py`

The deterministic package contains:

- `editions/en/reader-edition.md`;
- `editions/en/reader-edition.html`;
- `editions/en/reader-edition.json`.

QA confirms **54/54 songs** and **1,105/1,105 English lines/cues** exactly once in each machine-addressable output layer, with all **8 cross-page records**, **3 pilot-verified + 51 verified** statuses and **54 anthology-attributed** states intact. There are **0 warnings / 0 errors** and no English-line text drift.

The build treats the source-faithful English as immutable input. It does not smooth Kalaignar's language for publication.''')
replace_section(work_readme, "## Next activity", None, '''## Next activity

Repository-internal work is complete. The verified reader/export package is ready for **downstream Kalaignar Digital Library / Reading Room integration** while preserving anthology order, Tamil/source provenance, item status history, attribution state and the approved Kalaignar-language English.''')

# Translation README.
translation_readme = WORK / "translations" / "README.md"
replace_section(translation_readme, "## Next activity", None, '''## Reader/export derivative

The complete-verified translation corpus now has a deterministic publication derivative under `../editions/en/`:

- `reader-edition.md`;
- `reader-edition.html`;
- `reader-edition.json`;
- `QA_REPORT.md` — **PASS**;
- `manifest.json`.

Generated QA proves that all **54 songs** and **1,105 English lines/cues** survive exactly once with source provenance, the **3 pilot-verified / 51 verified** distinction and `anthology-attributed` state intact. The builder does not edit or smooth these translation records.

## Next activity

No translation-layer or reader/export work remains. Downstream Reading Room integration may consume these verified derivatives without changing the source-linked English.''')

# Tamil song-layer README.
songs_readme = WORK / "songs" / "README.md"
replace_section(songs_readme, "## Next derivative activity", None, '''## Downstream derivative status

The English translation and deterministic English reader/export package are both complete-verified. Generated-output QA passes for **54/54 songs** and **1,105/1,105 English lines/cues** with no alteration to this Tamil source layer.

No further source-layer activity is required. Downstream Reading Room integration may proceed from the verified derivatives.''')

# Work handover.
handover = WORK / "PROJECT_HANDOVER.md"
replace_section(handover, "## Exact next activity", "## Repository boundary", '''## Reader/export package checkpoint

The deterministic English reader/export package is **complete-verified**.

Generated files under `editions/en/`:

1. `reader-edition.md`;
2. `reader-edition.html`;
3. `reader-edition.json`;
4. `QA_REPORT.md` — **PASS**;
5. `manifest.json`;
6. `build.py` — deterministic builder/QA implementation.

Generated-output QA confirms:

- anthology order `001–054` exactly once;
- **54/54** songs;
- **1,105/1,105** English lines/cues;
- **3 pilot-verified + 51 verified** item statuses;
- **54/54 anthology-attributed** items;
- all **8** cross-page source arrays;
- **0** missing/extra/duplicate song IDs, translation IDs or line IDs;
- **0** source-page/status/attribution drift;
- **0** English-line text drift;
- **0 warnings / 0 errors**.

The manifest hashes **110 authoritative inputs** and all generated publication outputs. Do not manually edit generated reader files; rerun `editions/en/build.py` through the workflow when authoritative inputs change.

## Exact next activity

No required repository-internal transcription, fidelity, translation, preflight or reader/export gate remains. The next activity is **downstream Kalaignar Digital Library / Reading Room integration**. Preserve anthology order, page provenance, `anthology-attributed` status, the 3 `pilot-verified` / 51 `verified` history, and the source-faithful Kalaignar-language English. Do not reopen or smooth the verified source-linked layers for UI convenience.''')

# Root README.
root_readme = ROOT / "README.md"
replace_idempotent(
    root_readme,
    "- English reader/export preflight: **complete-pass** — 54/54 records, 1,105/1,105 mapped Tamil/English lines-cues, 8 cross-page records, 0 warnings/errors;",
    "- English reader/export: **complete-verified, QA PASS** — 54/54 songs, 1,105/1,105 English lines-cues, 8 cross-page records, deterministic Markdown/HTML/JSON + manifest;"
)
replace_idempotent(
    root_readme,
    "**Next:** generate deterministic anthology-order English reader/export Markdown, standalone HTML and machine-readable JSON from all 54 complete-verified translation records, then run generated-output QA and create an integrity manifest before downstream Reading Room integration.",
    "**Next:** repository-internal anthology work is complete; downstream Kalaignar Digital Library / Reading Room integration may proceed from the verified reader/export package."
)

# Repository-wide consistency audit.
status_audit = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
replace_idempotent(
    status_audit,
    "| English reader/export | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS | preflight complete-pass; reader export not started |",
    "| English reader/export | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS — 54 songs / 1,105 lines-cues |"
)
replace_idempotent(
    status_audit,
    "The anthology whole-corpus English reader/export preflight is **complete-pass** across 54/54 records, 1,105/1,105 mapped Tamil/English lines-cues and all eight cross-page records, with zero warnings/errors. The next repository-internal activity is deterministic reader/export generation (Markdown, standalone HTML, machine-readable JSON), followed by generated-output QA and an integrity manifest.",
    "The anthology English reader/export is **complete-verified with QA PASS**: 54/54 songs, 1,105/1,105 English lines-cues, all eight cross-page records, deterministic Markdown/HTML/JSON and an integrity manifest, with zero warnings/errors or text drift. No required repository-internal anthology activity remains; downstream Reading Room integration is ready."
)

print("synchronized complete anthology English reader/export status")
