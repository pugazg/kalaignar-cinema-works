#!/usr/bin/env python3
"""Synchronize repository-level status after anthology English reader preflight PASS."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK_ID = "kalaignar-thirai-isai-paadalgal"
REPORT_PATH = "works/kalaignar-thirai-isai-paadalgal/editions/en/PREFLIGHT_QA_REPORT.md"

# Central machine registry. This update is naturally idempotent.
registry_path = ROOT / "data" / "works.json"
registry = json.loads(registry_path.read_text(encoding="utf-8"))
entry = next((item for item in registry if item.get("id") == WORK_ID), None)
if entry is None:
    raise SystemExit(f"missing {WORK_ID} in data/works.json")
entry.update({
    "english_reader_preflight": "complete-pass",
    "english_reader_preflight_report_path": REPORT_PATH,
    "english_reader_preflight_translation_records": 54,
    "english_reader_preflight_source_links": 54,
    "english_reader_preflight_mapped_tamil_lines": 1105,
    "english_reader_preflight_mapped_english_lines": 1105,
    "english_reader_preflight_cross_page_records": 8,
    "english_reader_preflight_errors": 0,
    "english_reader_preflight_warnings": 0,
    "reader_export": "not-started",
    "next_action": "Generate deterministic English reader/export Markdown, standalone HTML and machine-readable JSON from all 54 verified translation records, then run generated-output QA and create an integrity manifest."
})
registry_path.write_text(json.dumps(registry, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def replace_idempotent(path: Path, old: str, new: str) -> None:
    """Apply a one-time status transition, but pass cleanly if already transitioned."""
    text = path.read_text(encoding="utf-8")
    if old in text:
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        return
    if new in text:
        return
    raise SystemExit(
        f"neither expected old nor synchronized text found in {path.relative_to(ROOT)}: {old!r} / {new!r}"
    )

# Root README status/continuation.
root_readme = ROOT / "README.md"
replace_idempotent(
    root_readme,
    "- reader/export preflight: **not-started**.",
    "- English reader/export preflight: **complete-pass** — 54/54 records, 1,105/1,105 mapped Tamil/English lines-cues, 8 cross-page records, 0 warnings/errors;"
)
replace_idempotent(
    root_readme,
    "**Next:** run a whole-corpus **English reader/export preflight** across all 54 source-linked translation records, preserving anthology order, source/page provenance, `anthology-attributed` status and the distinction between 3 `pilot-verified` and 51 `verified` records.",
    "**Next:** generate deterministic anthology-order English reader/export Markdown, standalone HTML and machine-readable JSON from all 54 complete-verified translation records, then run generated-output QA and create an integrity manifest before downstream Reading Room integration."
)

# Repository-wide consistency audit.
status_audit = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
replace_idempotent(
    status_audit,
    "| English reader/export | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS | preflight not started |",
    "| English reader/export | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS | preflight complete-pass; reader export not started |"
)
replace_idempotent(
    status_audit,
    "The next repository-internal activity is a **whole-corpus English reader/export preflight across all 54 source-linked song translation records**, preserving anthology order, source/page provenance, `anthology-attributed` status, and the distinction between 3 `pilot-verified` and 51 `verified` records.",
    "The anthology whole-corpus English reader/export preflight is **complete-pass** across 54/54 records, 1,105/1,105 mapped Tamil/English lines-cues and all eight cross-page records, with zero warnings/errors. The next repository-internal activity is deterministic reader/export generation (Markdown, standalone HTML, machine-readable JSON), followed by generated-output QA and an integrity manifest."
)

print("synchronized anthology reader preflight status")
