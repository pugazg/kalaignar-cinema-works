#!/usr/bin/env python3
"""Synchronize Manohara metadata/readmes after a successful reader preflight."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "manohara"


def replace_once(path: Path, old: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return False
    if old not in text:
        raise SystemExit(f"expected checkpoint text not found in {path.relative_to(ROOT)}: {old!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    return True

changed = []

def do(path, old, new):
    p = ROOT / path
    if replace_once(p, old, new):
        changed.append(path)

# Work metadata.
do(
    "works/manohara/metadata.yaml",
    '  next_action: "Run whole-work English reader/export preflight and integrity QA across all 57 verified archival scene records before generating publication-facing derivatives."',
    '  next_action: "Generate deterministic English reader/export derivatives in Markdown, standalone HTML and machine-readable JSON; run generated-output QA and write an integrity manifest before Reading Room integration."',
)
do(
    "works/manohara/metadata.yaml",
    "  english_translation_integrity_state: translation-complete-pre-reader-qa\n  reader_export: not-started\n  reading_room_integration: blocked\n  next_structured_derivative: reader-export",
    "  english_translation_integrity_state: preflight-complete-pass\n  english_reader_preflight: complete-pass\n  english_reader_preflight_report_path: \"editions/en/PREFLIGHT_QA_REPORT.md\"\n  english_reader_preflight_script_path: \"editions/en/audit_probe.py\"\n  english_reader_preflight_workflow_path: \"../../.github/workflows/manohara-english-preflight.yml\"\n  english_reader_preflight_workflow_run_id: 31956654990\n  english_reader_preflight_head_commit: \"b2cd2a597a9f2eeb0e8016b78102ec67fe05ae7e\"\n  english_reader_preflight_dialogue_links_missing: 0\n  english_reader_preflight_dialogue_links_extra: 0\n  english_reader_preflight_dialogue_links_duplicate: 0\n  english_reader_preflight_synthetic_scene_end_units: 0\n  english_reader_preflight_structural_star_units: 0\n  english_reader_preflight_page_order_regressions: 0\n  english_reader_preflight_unit_id_errors: 0\n  reader_export: ready-after-preflight\n  reading_room_integration: blocked-pending-reader-export-generation-and-qa\n  next_structured_derivative: reader-export",
)

# Translation-layer handoff.
do(
    "works/manohara/translations/README.md",
    "## Next gate\n\nThe **translation layer itself is complete**. The next activity is a separate **whole-work reader/export preflight and integrity QA** across all 57 scene records. That gate should check source order, unit IDs, exact 983/983 dialogue linkage, cross-page provenance, absence of synthetic star-derived endings, song-reference integrity and publication-reader structure before any Markdown/HTML/JSON or Reading Room derivative is generated.",
    "## Reader/export preflight — PASS\n\nThe whole-work automated preflight passed across all **57** scene records and **1,190** verified units. It independently confirmed **983/983 immutable dialogue links exactly once**, all **27** null-speaker spoken units, all **17** cross-page units, and all **6/6** song/performance occurrence links. Diagnostics found **0** missing/extra/duplicate dialogue links, **0** synthetic `(Scene ends.)` units, **0** units derived directly from decorative stars, **0** page-order regressions, **0** unit-ID errors and **0** provenance/scene-metadata errors. See `../editions/en/PREFLIGHT_QA_REPORT.md`.\n\n**Next:** generate deterministic publication-facing Markdown, standalone HTML and machine-readable JSON; then run generated-output QA and write an integrity manifest before Reading Room integration.",
)

# Work-level checkpoint.
do(
    "works/manohara/README.md",
    "| English reader/export preflight | **not-started** |\n| Reading Room integration | blocked pending reader/export QA |",
    "| English reader/export preflight | **complete-pass — 57 scenes / 1,190 units / 983 dialogue links** |\n| English reader/export generation | **ready / not-started** |\n| Reading Room integration | blocked pending generated reader/export QA |",
)
do(
    "works/manohara/README.md",
    "## Next activity\n\nRun a **whole-work English reader/export preflight and integrity QA** across all 57 verified translation records before producing publication-facing Markdown/HTML/JSON or Reading Room data. The preflight should verify source order, unit IDs, exact **983/983** dialogue linkage, the **17** cross-page units, the **27** null-speaker spoken units, song-reference integrity, and absence of synthetic prose derived only from decorative `★` separators.",
    "## Reader/export preflight — PASS\n\nThe automated whole-work gate passed across **57/57 scene records and 1,190/1,190 verified units**. It confirmed **983/983 immutable dialogue links exactly once**, **27** null-speaker spoken units, **17** genuine cross-page units and **6/6** song/performance links, with **0** missing/extra/duplicate dialogue links, **0** synthetic scene-end units, **0** direct structural-star units, **0** page-order regressions, **0** unit-ID errors and **0** provenance/scene-metadata errors. The reproducible diagnostic and full disposition are under `editions/en/`.\n\n## Next activity\n\nGenerate the deterministic **English reader/export package** in Markdown, standalone HTML and machine-readable JSON, then run generated-output QA and write an integrity manifest before Reading Room integration.",
)

# Repository-level checkpoint.
do(
    "README.md",
    "**Next:** run **whole-work English reader/export preflight and integrity QA** across all 57 verified scene records before generating publication-facing Markdown/HTML/JSON or Reading Room data.",
    "The **Manohara English reader/export preflight now passes** across all 57 scene records and 1,190 verified units: 983/983 immutable dialogue links exactly once, 27 null-speaker spoken units, 17 cross-page units and all 6 song/performance links, with zero missing/extra/duplicate dialogue links, synthetic scene-end units, direct structural-star units, page-order regressions, unit-ID errors or provenance/scene-metadata errors.\n\n**Next:** generate deterministic Manohara English reader/export derivatives in Markdown, standalone HTML and machine-readable JSON; run generated-output QA and write an integrity manifest before Reading Room integration.",
)

print("MANOHARA PREFLIGHT STATUS SYNC")
print("changed=", changed)
