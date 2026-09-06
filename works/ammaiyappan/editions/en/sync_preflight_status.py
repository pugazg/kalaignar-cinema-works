#!/usr/bin/env python3
"""Record Ammayappan reader preflight PASS and synchronize active status mirrors."""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RUN_ID = os.environ.get("GITHUB_RUN_ID", "unknown")
HEAD_SHA = os.environ.get("GITHUB_SHA", "unknown")
WORKFLOW = ".github/workflows/ammaiyappan-english-reader-preflight.yml"

changed = []


def replace_once(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise SystemExit(f"expected checkpoint text not found in {path}: {old!r}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")
    changed.append(path)


# Durable preflight report. This script runs only after audit_probe.py exits 0.
report_path = ROOT / "works/ammaiyappan/editions/en/PREFLIGHT_QA_REPORT.md"
report = f"""# அம்மையப்பன் — English Reader/Export Preflight QA

Status: **PASS**

This report records the executable whole-work integrity gate run after completion of the source-linked English translation and before generation of publication-facing reader/export derivatives.

## Authority and scope

The preflight reads the repository's frozen verified derivative layers directly:

- `translations/records/scene-001.json` through `scene-063.json`;
- immutable `dialogues/records/scene-001.json` through `scene-063.json`;
- `dialogues/source-role-resolved-records.json`;
- `songs/inventory.json`;
- `translations/index.json`.

It is read-only. Canonical Tamil, scene derivatives, immutable dialogue records, character mappings and song/performance evidence are not altered.

The booklet prints no scene numbers. All `ammaiyappan-sNNN` identifiers remain archival navigation derivatives only.

## Automated run

GitHub Actions workflow: `{WORKFLOW}`  
Preflight implementation: `works/ammaiyappan/editions/en/audit_probe.py`

Passing run checkpoint:

- workflow run: **{RUN_ID}**;
- head commit: `{HEAD_SHA}`;
- Python: **3.12**;
- probe result: **PASS**.

## PASS results

| Check | Result |
|---|---:|
| Translation scene files | **63 / 63** |
| Verified translation units | **1,210 / 1,210** |
| Draft / review units | **0 / 0** |
| Dialogue-kind units | **1,025** |
| Stage-direction units | **181** |
| Song-reference units | **3** |
| Japa units | **1** |
| Literary-verse / written-text units | **0 / 0** |
| Immutable explicit dialogue records | **1,009** |
| Closed source-role supplements | **16** |
| Total dialogue authority | **1,025** |
| Dialogue/source-role links | **1,025 / 1,025 exactly once** |
| Missing / extra / duplicate dialogue links | **0 / 0 / 0** |
| Genuine cross-page translation units | **28** |
| Cross-page provenance/segment errors | **0** |
| Retained occurrence identities | **5 / 5** |
| Occurrence-linked source spans | **7** |
| Synthetic `(Scene ends.)` units | **0** |
| Units derived directly from decorative/structural stars | **0** |
| Page-order regressions | **0** |
| Unit-ID errors | **0** |
| Page-provenance errors | **0** |
| Scene/unit metadata errors | **0** |
| Audit warnings | **0** |
| Audit errors | **0** |

## Exact speaker-label / source-role provenance

The probe independently compared every dialogue-linked English unit against the closed source authority.

- all **1,009** immutable explicit records retain the exact Tamil `speaker_label`, `source-explicit-colon` origin and exact page provenance;
- all **16** source-role supplements retain their exact Tamil label, recorded origin and exact page provenance;
- scene 3 `பூங் ; ...` and scene 5 `திரு; ...` remain `source-explicit-noncolon-delimiter` records rather than being normalized to printed-colon dialogue;
- context-attributed supplements remain `source-context-attributed` and are never promoted into printed labels.

Missing, extra or duplicate source-record links: **0**.

## Cross-page integrity

The probe independently derived **28** genuine cross-page units from the scene records and confirmed that this ordered list exactly matches `translations/index.json`. Every cross-page unit retains multi-page provenance and matching `english_page_segments`; provenance errors and page-order regressions are **0**.

## Song / verse / performance integrity

The five closed source-visible occurrence identities are all represented with their intended source-span multiplicity:

- `ammaiyappan-song-001` — **1** link (`song-reference`);
- `ammaiyappan-song-002` — **1** link (`dialogue`);
- `ammaiyappan-song-003` — **1** link (`song-reference`);
- `ammaiyappan-song-004` — **2** links (`japa` + the separately printed labelled dialogue token);
- `ammaiyappan-song-005` — **2** links (the dialogue request + the separate performance cue).

Thus **5 occurrence identities / 7 intentionally distinct source-span links** are preserved. No absent lyric, title or authorship is introduced.

## Structural and navigation safeguards

PASS:

- source scene numbering remains `null` for all 63 archival scene records;
- archive ordinals remain navigation only;
- synthetic `(Scene ends.)` units: **0**;
- units whose source locator is a decorative/structural star: **0**;
- frozen source layers reported modified by the translation index: **0**.

## Validation scope

This is an **executable Python preflight run in GitHub Actions**, not merely a manual count reconciliation. The probe validates the repository's reader-critical invariants directly. It is not a JSON-Schema-library validation unless such a separate schema validator is later added and recorded.

## Gate disposition

**Reader/export preflight: PASS.**

The complete-verified 63-scene translation is cleared for deterministic publication-facing reader/export generation. The next activity is to generate **Markdown, standalone HTML and machine-readable JSON from the verified structured translation**, then run generated-output QA and produce an integrity manifest before Reading Room integration.
"""
if not report_path.exists() or report_path.read_text(encoding="utf-8") != report:
    report_path.write_text(report, encoding="utf-8")
    changed.append("works/ammaiyappan/editions/en/PREFLIGHT_QA_REPORT.md")

# Work metadata.
replace_once(
    "works/ammaiyappan/metadata.yaml",
    "  reader_export: not-started-pending-preflight\n  reading_room_integration: blocked-pending-reader-export",
    f"  english_reader_preflight: complete-pass\n  english_reader_preflight_report_path: \"editions/en/PREFLIGHT_QA_REPORT.md\"\n  english_reader_preflight_script_path: \"editions/en/audit_probe.py\"\n  english_reader_preflight_workflow_path: \"../../{WORKFLOW}\"\n  english_reader_preflight_workflow_run_id: {RUN_ID}\n  english_reader_preflight_head_commit: \"{HEAD_SHA}\"\n  english_reader_preflight_dialogue_links_missing: 0\n  english_reader_preflight_dialogue_links_extra: 0\n  english_reader_preflight_dialogue_links_duplicate: 0\n  english_reader_preflight_cross_page_errors: 0\n  english_reader_preflight_occurrence_identity_errors: 0\n  english_reader_preflight_synthetic_scene_end_units: 0\n  english_reader_preflight_structural_star_units: 0\n  english_reader_preflight_page_order_regressions: 0\n  english_reader_preflight_unit_id_errors: 0\n  english_reader_preflight_provenance_errors: 0\n  reader_export: ready-after-preflight\n  reading_room_integration: blocked-pending-reader-export-generation-and-qa",
)
replace_once(
    "works/ammaiyappan/metadata.yaml",
    "  reader_export: not-started-pending-preflight\n  reading_room_integration: blocked-pending-reader-export\n\nnext_action: \"Run whole-work English reader/export preflight from the complete-verified 63-scene translation. Generate reader/export from verified structured records rather than an independent manual copy; preserve archival scene IDs as navigation only, exact source provenance, all 1,025 dialogue units, all 28 cross-page units and all five source-visible occurrence links.\"",
    "  reader_export: ready-after-preflight\n  reading_room_integration: blocked-pending-reader-export-generation-and-qa\n\nnext_action: \"Generate deterministic English reader/export derivatives from the complete-verified structured translation in Markdown, standalone HTML and machine-readable JSON; preserve all 1,210 units, 1,025 dialogue/source-role links, 28 cross-page units, five occurrence identities / seven source-span links, exact provenance and archive-only scene numbering. Then run generated-output QA and write an integrity manifest before Reading Room integration.\"",
)

# Work README.
replace_once(
    "works/ammaiyappan/README.md",
    "| Reader/export | **not started — next production phase is reader/export preflight** |",
    "| English reader/export preflight | **complete-pass — 63 scenes / 1,210 units / 1,025 dialogue links** |\n| Reader/export generation | **ready / not started** |",
)
replace_once(
    "works/ammaiyappan/README.md",
    "## Exact next activity\n\n**Run whole-work English reader/export preflight from the complete-verified 63-scene structured translation. Generate reader/export from the verified records rather than maintaining an independent manual copy. Preserve archive scene IDs as navigation only, exact source provenance, all 1,025 dialogue units, all 28 cross-page units and all five source-visible occurrence links.**",
    "## Reader/export preflight — PASS\n\nThe executable whole-work gate passed across **63/63 scene records and 1,210/1,210 verified units**. It independently confirmed all **1,009 explicit dialogue records + 16 source-role supplements = 1,025/1,025 dialogue links exactly once**, all **28** cross-page units, and all **5** retained occurrence identities across **7** intentionally distinct source-span links. Missing/extra/duplicate dialogue links, provenance errors, page regressions, unit-ID errors, structural-star prose units and synthetic scene-end units are all **0**. See `editions/en/PREFLIGHT_QA_REPORT.md`.\n\n## Exact next activity\n\n**Generate deterministic English reader/export derivatives in Markdown, standalone HTML and machine-readable JSON from the verified structured translation. Preserve all 1,210 units, exact Tamil speaker-label/source-role provenance, all 28 cross-page units, the five occurrence identities/seven source-span links, and archive-only scene numbering. Then run generated-output QA and write an integrity manifest before Reading Room integration.**",
)

# Translation README.
replace_once(
    "works/ammaiyappan/translations/README.md",
    "## Next\n\nProceed to **whole-work English reader/export preflight** generated from the complete-verified structured translation. Preserve the full 1,025-unit dialogue authority, all 28 cross-page units, all five source-visible occurrence links, exact Tamil speaker-label provenance and archive-only scene numbering. Do not maintain an independent manual reader copy.",
    "## Reader/export preflight — PASS\n\nThe executable whole-work gate passed across all **63 scene records / 1,210 verified units**. It confirmed **1,025/1,025 dialogue/source-role links exactly once**, all **28** cross-page units with matching page segments, exact Tamil speaker-label/source-role provenance, all **5** retained occurrence identities across **7** intentional source-span links, and archive-only scene numbering. It found **0** missing/extra/duplicate dialogue links, provenance errors, page regressions, unit-ID errors, synthetic scene-end units or direct structural-star prose units. See `../editions/en/PREFLIGHT_QA_REPORT.md`.\n\n## Next\n\nGenerate deterministic publication-facing **Markdown, standalone HTML and machine-readable JSON** directly from the verified structured translation, then run generated-output QA and write an integrity manifest before Reading Room integration. Do not maintain an independent manual reader copy.",
)

# Work handover.
replace_once(
    "works/ammaiyappan/PROJECT_HANDOVER.md",
    "- reader/export: **not started; preflight is the next production phase**.",
    "- reader/export preflight: **complete-pass — executable GitHub Actions gate**;\n- reader/export generation: **ready / not started**.",
)
replace_once(
    "works/ammaiyappan/PROJECT_HANDOVER.md",
    "## Exact next activity\n\n> **Fetch live `main`; confirm English translation is complete-verified at 63/63 scenes and 1,210 units with `FINAL_TRANSLATION_QA.md` PASS. Then run whole-work English reader/export preflight from the verified structured translation. Generate the reader/export from the translation records rather than maintaining an independent manual copy. Preserve archive scene IDs as navigation only, exact Tamil speaker-label provenance, all 1,025 dialogue units, all 28 cross-page units and all five source-visible occurrence links. Do not alter frozen Tamil/dialogue/character/song evidence. After preflight, record its QA and synchronize work/repository status mirrors before building reader outputs.**",
    f"## Reader/export preflight — PASS\n\nExecutable workflow `{WORKFLOW}` passed at run **{RUN_ID}** / head `{HEAD_SHA}`. The probe verified **63/63 scene records, 1,210/1,210 units, 1,025/1,025 dialogue/source-role links exactly once, 28 cross-page units, five occurrence identities across seven intentional source-span links, exact speaker-label/source-role provenance, and archive-only scene numbering**, with zero audit errors or warnings. Full record: `editions/en/PREFLIGHT_QA_REPORT.md`.\n\n## Exact next activity\n\n> **Fetch live `main`; preserve the complete-verified English translation and reader/export preflight PASS. Build deterministic publication-facing English reader/export derivatives from the verified translation records — Markdown, standalone HTML and machine-readable JSON — without maintaining an independent manual copy. Preserve all 1,210 units, all 1,025 dialogue/source-role links, all 28 cross-page units, all five occurrence identities/seven source-span links, exact Tamil speaker-label/source-role provenance and archive-only scene numbering. Then run generated-output QA and write an integrity manifest before Reading Room integration. Do not alter frozen Tamil/dialogue/character/song evidence.**",
)

# Registry: compact targeted updates keep unrelated formatting and checksums untouched.
replace_once(
    "data/works.json",
    '"reader_export":"not-started-pending-preflight","reading_room_integration":"blocked-pending-reader-export","next_structured_derivative":"english-reader-preflight"',
    f'"english_reader_preflight":"complete-pass","english_reader_preflight_report_path":"works/ammaiyappan/editions/en/PREFLIGHT_QA_REPORT.md","english_reader_preflight_script_path":"works/ammaiyappan/editions/en/audit_probe.py","english_reader_preflight_workflow_path":"{WORKFLOW}","english_reader_preflight_workflow_run_id":{RUN_ID},"english_reader_preflight_head_commit":"{HEAD_SHA}","reader_export":"ready-after-preflight","reading_room_integration":"blocked-pending-reader-export-generation-and-qa","next_structured_derivative":"english-reader-export"',
)
replace_once(
    "data/works.json",
    '"next_action":"Run whole-work English reader/export preflight from the complete-verified 63-scene translation. Generate reader/export from verified structured records rather than an independent manual copy; preserve archival scene IDs as navigation only, exact source provenance, all 1,025 dialogue units, all 28 cross-page units and all five source-visible occurrence links."',
    '"next_action":"Generate deterministic English reader/export derivatives from the verified 63-scene translation in Markdown, standalone HTML and machine-readable JSON; preserve all 1,210 units, all 1,025 dialogue/source-role links, all 28 cross-page units, five occurrence identities/seven intentional source-span links, exact provenance and archive-only scene numbering. Then run generated-output QA and write an integrity manifest before Reading Room integration."',
)

# Root README.
replace_once(
    "README.md",
    "- reader/export: **not started; reader/export preflight is next**.",
    "- reader/export preflight: **complete-pass — executable 63-scene / 1,210-unit integrity gate**;\n- reader/export generation: **ready / not started**.",
)
replace_once(
    "README.md",
    "**Next:** run whole-work English reader/export preflight from the complete-verified structured translation. Generate the reader/export from the verified records rather than maintaining an independent manual copy; preserve all 1,025 dialogue units, all 28 cross-page units, all five occurrence links and archive-only scene numbering.",
    "The **Ammayappan English reader/export preflight now passes** across all 63 scene records and 1,210 verified units: 1,025/1,025 dialogue/source-role links exactly once, 28 cross-page units, and all five retained occurrence identities across seven intentional source-span links, with zero missing/extra/duplicate dialogue links, provenance errors, page regressions, unit-ID errors, synthetic scene-end units or direct structural-star prose units.\n\n**Next:** generate deterministic English reader/export derivatives in Markdown, standalone HTML and machine-readable JSON, then run generated-output QA and write an integrity manifest before Reading Room integration.",
)

# Repository status audit.
replace_once(
    "docs/STATUS_CONSISTENCY_AUDIT.md",
    "| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **complete-verified 63/63 / 1,210 units** | reader/export preflight next |",
    "| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **complete-verified 63/63 / 1,210 units** | reader/export preflight **PASS**; generation ready |",
)
replace_once(
    "docs/STATUS_CONSISTENCY_AUDIT.md",
    "This PASS is source/linkage reconciliation. It does not claim an executable JSON-schema validator or CI run unless separately executed and recorded.\n\n**Next production phase:** whole-work English reader/export preflight generated from the complete-verified structured translation.",
    f"The separate **reader/export preflight is now executable and PASS**: workflow `{WORKFLOW}`, run **{RUN_ID}**, head `{HEAD_SHA}`. It directly verified all **63 scene records / 1,210 units / 1,025 dialogue-source links / 28 cross-page units / five occurrence identities across seven intentional links**, with **0** missing/extra/duplicate dialogue links, provenance errors, page regressions, unit-ID errors, synthetic scene-end units, direct structural-star prose units, warnings or errors. See `works/ammaiyappan/editions/en/PREFLIGHT_QA_REPORT.md`. This is not a separate JSON-Schema-library validation.\n\n**Next production phase:** deterministic English reader/export generation in Markdown, standalone HTML and machine-readable JSON, followed by generated-output QA and an integrity manifest.",
)
replace_once(
    "docs/STATUS_CONSISTENCY_AUDIT.md",
    "Ammayappan's canonical Tamil and structured source-derived layers remain **closed at the corrected 1,025-unit authority**. English translation is now **complete-verified at 63/63 scenes / 1,210 units**, with final source/linkage reconciliation PASS. The next bounded activity is **whole-work English reader/export preflight**.",
    "Ammayappan's canonical Tamil and structured source-derived layers remain **closed at the corrected 1,025-unit authority**. English translation is **complete-verified at 63/63 scenes / 1,210 units**, final source/linkage reconciliation is PASS, and the executable reader/export preflight is now **PASS**. The next bounded activity is **deterministic reader/export generation plus generated-output QA/manifest**.",
)

# Master handover.
replace_once(
    "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md",
    "- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **complete-verified 63/63 / 1,210 units**, whole-work reconciliation PASS; reader/export preflight is next.",
    "- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **complete-verified 63/63 / 1,210 units**, whole-work reconciliation PASS; executable reader/export preflight **PASS**; deterministic reader/export generation is next.",
)
replace_once(
    "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md",
    "- reader/export: **not started; preflight next**.",
    "- reader/export preflight: **complete-pass**;\n- reader/export generation: **ready / not started**.",
)
replace_once(
    "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md",
    "**Exact next activity:** run whole-work English reader/export preflight from the verified structured translation. Generate reader/export from the records rather than maintaining an independent manual copy; preserve archive scene IDs as navigation only, exact Tamil speaker-label provenance, all **1,025** dialogue units, all **28** cross-page units and all **5** source-visible occurrence links. Do not modify frozen source evidence.",
    f"### Reader/export preflight — PASS\n\nWorkflow `{WORKFLOW}` passed at run **{RUN_ID}** / head `{HEAD_SHA}`. It verified all **63 scenes / 1,210 units / 1,025 dialogue-source links / 28 cross-page units / five occurrence identities across seven intentional source-span links** with zero errors or warnings.\n\n**Exact next activity:** generate deterministic English reader/export derivatives from the verified structured translation in Markdown, standalone HTML and machine-readable JSON. Preserve archive scene IDs as navigation only, exact Tamil speaker-label/source-role provenance, all **1,210** units, all **1,025** dialogue links, all **28** cross-page units and all **5** occurrence identities / **7** intentional source-span links. Then run generated-output QA and write an integrity manifest before Reading Room integration. Do not modify frozen source evidence.",
)

# Continuation prompt: keep live-main rule, advance downstream gate.
replace_once(
    "works/ammaiyappan/NEXT_CHAT_PROMPT.md",
    "- reader/export: **not started; whole-work reader/export preflight is next**.",
    f"- reader/export preflight: **complete-pass** — workflow run **{RUN_ID}** at `{HEAD_SHA}`;\n- reader/export generation: **ready / not started**.",
)
replace_once(
    "works/ammaiyappan/NEXT_CHAT_PROMPT.md",
    "24. `works/ammaiyappan/translations/FINAL_TRANSLATION_QA.md`\n25. verified translation records `scene-001.json`–`scene-063.json` as needed for the reader/export preflight.",
    "24. `works/ammaiyappan/translations/FINAL_TRANSLATION_QA.md`\n25. `works/ammaiyappan/editions/en/PREFLIGHT_QA_REPORT.md`\n26. `works/ammaiyappan/editions/en/audit_probe.py`\n27. verified translation records `scene-001.json`–`scene-063.json` as needed for reader/export generation and QA.",
)
replace_once(
    "works/ammaiyappan/NEXT_CHAT_PROMPT.md",
    "## EXACT NEXT ACTIVITY\n\n> **Fetch live `main`; confirm English translation is complete-verified at 63/63 scenes and 1,210 units with `translations/FINAL_TRANSLATION_QA.md` PASS. Then run whole-work English reader/export preflight from the verified structured translation. The reader must be generated from the translation records rather than maintained as an independent manual copy. Verify one-to-one preservation of all 1,210 translation units, all 1,025 dialogue units, all 28 cross-page units, all five source-visible occurrence links, exact Tamil speaker-label/source-role provenance, and archive-only scene numbering. Do not alter frozen Tamil/dialogue/character/song evidence. Record the preflight QA before building reader outputs; if preflight passes, synchronize work/repository status mirrors and make reader/export construction the next activity.**",
    "> **Fetch live `main`; confirm English translation remains complete-verified at 63/63 scenes / 1,210 units and `editions/en/PREFLIGHT_QA_REPORT.md` is PASS. Then build deterministic English reader/export derivatives directly from the verified translation records — Markdown, standalone HTML and machine-readable JSON — never an independent manual copy. Preserve every one of the 1,210 translation units, all 1,025 dialogue/source-role links, all 28 cross-page units with page segments, all five occurrence identities across seven intentional source-span links, exact Tamil speaker-label/source-role provenance and archive-only scene numbering. Do not alter frozen Tamil/dialogue/character/song evidence. After generation run whole-work generated-output QA, write an integrity manifest, synchronize all current mirrors, and only then consider Reading Room integration.**",
)

print("AMMAYAPPAN READER PREFLIGHT STATUS SYNC")
print("run_id=", RUN_ID)
print("head_sha=", HEAD_SHA)
print("changed=", changed)
