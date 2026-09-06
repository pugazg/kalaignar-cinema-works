#!/usr/bin/env python3
"""Synchronize Ammayappan repository mirrors after a passing reader/export build."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "ammaiyappan"
EDITION = WORK / "editions" / "en"
MANIFEST = EDITION / "manifest.json"

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
if manifest.get("status") != "complete-verified" or manifest.get("qa_status") != "PASS":
    raise SystemExit("Refusing sync: reader manifest is not complete-verified/PASS")
if manifest.get("translation_units") != 1210 or manifest.get("dialogue_source_links_total") != 1025:
    raise SystemExit("Refusing sync: reader totals differ from closed authority")
if len(manifest.get("cross_page_units", [])) != 28:
    raise SystemExit("Refusing sync: cross-page total differs")
if manifest.get("occurrence_source_span_links_total") != 7:
    raise SystemExit("Refusing sync: occurrence source-span total differs")

outputs = manifest.get("outputs", {})
required = {"reader-edition.md", "reader-edition.html", "reader-edition.json", "QA_REPORT.md"}
if set(outputs) != required:
    raise SystemExit("Refusing sync: generated reader outputs are incomplete")

MD_SHA = outputs["reader-edition.md"]["sha256"]
HTML_SHA = outputs["reader-edition.html"]["sha256"]
JSON_SHA = outputs["reader-edition.json"]["sha256"]
QA_SHA = outputs["QA_REPORT.md"]["sha256"]
HEAD = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()

changed: list[str] = []


def write_if_changed(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8")
    if old != text:
        path.write_text(text, encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        if rel not in changed:
            changed.append(rel)


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise SystemExit(f"Expected checkpoint not found in {path.relative_to(ROOT)}: {old!r}")
    write_if_changed(path, text.replace(old, new, 1))


# Translation index: keep translation authority intact and add downstream reader checkpoint.
index_path = WORK / "translations" / "index.json"
index = json.loads(index_path.read_text(encoding="utf-8"))
index.update({
    "reader_export": "complete-verified",
    "reader_export_directory": "works/ammaiyappan/editions/en",
    "reader_export_build_script": "works/ammaiyappan/editions/en/build.py",
    "reader_export_qa_report": "works/ammaiyappan/editions/en/QA_REPORT.md",
    "reader_export_manifest": "works/ammaiyappan/editions/en/manifest.json",
    "reader_export_markdown_sha256": MD_SHA,
    "reader_export_html_sha256": HTML_SHA,
    "reader_export_json_sha256": JSON_SHA,
    "reader_export_qa_sha256": QA_SHA,
    "reader_export_dialogue_source_links": 1025,
    "reader_export_cross_page_units": 28,
    "reader_export_occurrence_identities": 5,
    "reader_export_occurrence_source_span_links": 7,
    "reader_export_qa_status": "PASS",
    "reader_export_deterministic": True,
    "next_activity": "Create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures; preserve archive-only scene numbering, exact source provenance, dialogue/source-role distinctions and all five occurrence identities without reconstructing absent lyrics, titles or authorship.",
})
write_if_changed(index_path, json.dumps(index, ensure_ascii=False, separators=(",", ":")) + "\n")

# Work metadata.
metadata = WORK / "metadata.yaml"
replace_once(
    metadata,
    "  reader_export: ready-after-preflight\n  reading_room_integration: blocked-pending-reader-export-generation-and-qa",
    f'''  reader_export: complete-verified
  english_reader_edition_path: "editions/en"
  english_reader_build_script_path: "editions/en/build.py"
  english_reader_qa_report_path: "editions/en/QA_REPORT.md"
  english_reader_manifest_path: "editions/en/manifest.json"
  english_reader_markdown_path: "editions/en/reader-edition.md"
  english_reader_html_path: "editions/en/reader-edition.html"
  english_reader_json_path: "editions/en/reader-edition.json"
  english_reader_translation_units: 1210
  english_reader_dialogue_source_links: 1025
  english_reader_cross_page_units: 28
  english_reader_occurrence_identities: 5
  english_reader_occurrence_source_span_links: 7
  english_reader_qa_status: PASS
  english_reader_deterministic: true
  english_reader_markdown_sha256: "{MD_SHA}"
  english_reader_html_sha256: "{HTML_SHA}"
  english_reader_json_sha256: "{JSON_SHA}"
  english_reader_qa_sha256: "{QA_SHA}"
  reading_room_integration: ready-after-reader-export-qa''',
)
replace_once(
    metadata,
    "  reader_export: ready-after-preflight\n  reading_room_integration: blocked-pending-reader-export-generation-and-qa",
    "  reader_export: complete-verified\n  reading_room_integration: ready-after-reader-export-qa",
)
replace_once(
    metadata,
    'next_action: "Generate deterministic English reader/export derivatives from the complete-verified structured translation in Markdown, standalone HTML and machine-readable JSON; preserve all 1,210 units, 1,025 dialogue/source-role links, 28 cross-page units, five occurrence identities / seven source-span links, exact provenance and archive-only scene numbering. Then run generated-output QA and write an integrity manifest before Reading Room integration."',
    'next_action: "Create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures. Preserve archive-only scene numbering, exact source provenance, dialogue/source-role distinctions and all five occurrence identities; do not reconstruct absent lyrics, titles or authorship."',
)

# Work README.
work_readme = WORK / "README.md"
replace_once(
    work_readme,
    "| Reader/export generation | **ready / not started** |",
    "| Reader/export generation | **complete-verified — Markdown / HTML / JSON / manifest; generated-output QA PASS** |\n| Reading Room integration | **ready after reader/export QA** |",
)
replace_once(
    work_readme,
    "## Exact next activity\n\n**Generate deterministic English reader/export derivatives in Markdown, standalone HTML and machine-readable JSON from the verified structured translation. Preserve all 1,210 units, exact Tamil speaker-label/source-role provenance, all 28 cross-page units, the five occurrence identities/seven source-span links, and archive-only scene numbering. Then run generated-output QA and write an integrity manifest before Reading Room integration.**",
    f'''## Reader/export package — PASS

The deterministic English reader/export package is now **complete-verified** under `editions/en/`. Markdown, standalone HTML and machine-readable JSON each preserve all **1,210** verified units exactly once. Generated-output QA confirms **1,025/1,025 dialogue/source-role links exactly once**, all **28** cross-page units, and all **5** occurrence identities across **7** intentional source-span links. Source-semicolon records retain semicolon provenance, while context-attributed supplements are visibly contextual rather than presented as printed labels.

Output SHA-256 values:

- Markdown: `{MD_SHA}`;
- HTML: `{HTML_SHA}`;
- JSON: `{JSON_SHA}`;
- QA report: `{QA_SHA}`.

`editions/en/manifest.json` records deterministic authoritative-input and output hashes. Reader generation changed **no** canonical Tamil, scene, dialogue/source-role, character or song/performance evidence.

## Exact next activity

**Create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures. Preserve the 63 scene IDs strictly as archive navigation, exact page/source provenance, all dialogue/source-role distinctions and all five source-visible occurrence identities; do not reconstruct absent lyrics, titles or authorship.**''',
)

# Translation README.
trans_readme = WORK / "translations" / "README.md"
replace_once(
    trans_readme,
    "## Next\n\nGenerate deterministic publication-facing **Markdown, standalone HTML and machine-readable JSON** directly from the verified structured translation, then run generated-output QA and write an integrity manifest before Reading Room integration. Do not maintain an independent manual reader copy.",
    f'''## Reader/export package — PASS

The deterministic publication-facing derivatives are complete under `../editions/en/`: Markdown, standalone HTML and machine-readable JSON each contain all **1,210** verified English units exactly once. Generated-output QA confirms exact **1,025/1,025** dialogue/source-role linkage, all **28** cross-page units, and all **5** occurrence identities across **7** intentional source-span links. Source-context-attributed labels remain explicitly contextual in presentation and the two source-semicolon records are not converted into printed-colon labels.

Output SHA-256 values are `{MD_SHA}` (Markdown), `{HTML_SHA}` (HTML) and `{JSON_SHA}` (JSON). The deterministic integrity manifest and QA report are in `../editions/en/`.

**Next:** create and QA the source-linked Ammayappan Reading Room integration payload from these complete-verified structures; preserve archive-only scene numbering and all source-evidence tiers.''',
)

# Root README.
root_readme = ROOT / "README.md"
replace_once(
    root_readme,
    "- reader/export generation: **ready / not started**.",
    "- reader/export generation: **complete-verified — Markdown / HTML / JSON / manifest; generated-output QA PASS**;\n- Reading Room integration: **ready after reader/export QA**.",
)
replace_once(
    root_readme,
    "The **Ammayappan English reader/export preflight now passes** across all 63 scene records and 1,210 verified units: 1,025/1,025 dialogue/source-role links exactly once, 28 cross-page units, and all five retained occurrence identities across seven intentional source-span links, with zero missing/extra/duplicate dialogue links, provenance errors, page regressions, unit-ID errors, synthetic scene-end units or direct structural-star prose units.\n\n**Next:** generate deterministic English reader/export derivatives in Markdown, standalone HTML and machine-readable JSON, then run generated-output QA and write an integrity manifest before Reading Room integration.",
    f'''The **Ammayappan English reader/export package now passes generated-output QA**. Markdown, standalone HTML and machine-readable JSON each preserve all 1,210 verified units exactly once, all 1,025 dialogue/source-role links, all 28 cross-page units and all five occurrence identities across seven intentional source-span links. The integrity manifest records deterministic authoritative-input and output hashes. Output SHA-256 values are `{MD_SHA}` (Markdown), `{HTML_SHA}` (HTML) and `{JSON_SHA}` (JSON). No frozen Tamil or structured source evidence was modified.

**Next:** create and QA the source-linked Ammayappan Reading Room integration payload; preserve the 63 scene IDs strictly as archive navigation and retain all source-provenance/authorship limits.''',
)

# Registry: surgical string replacements to preserve every unrelated work byte-for-byte.
registry = ROOT / "data" / "works.json"
replace_once(
    registry,
    '"reader_export":"ready-after-preflight","reading_room_integration":"blocked-pending-reader-export-generation-and-qa","next_structured_derivative":"english-reader-export"}',
    f'"reader_export":"complete-verified","english_reader_edition_path":"works/ammaiyappan/editions/en","english_reader_build_script_path":"works/ammaiyappan/editions/en/build.py","english_reader_qa_report_path":"works/ammaiyappan/editions/en/QA_REPORT.md","english_reader_manifest_path":"works/ammaiyappan/editions/en/manifest.json","english_reader_markdown_sha256":"{MD_SHA}","english_reader_html_sha256":"{HTML_SHA}","english_reader_json_sha256":"{JSON_SHA}","english_reader_translation_units":1210,"english_reader_dialogue_source_links":1025,"english_reader_cross_page_units":28,"english_reader_occurrence_identities":5,"english_reader_occurrence_source_span_links":7,"english_reader_qa":"PASS","english_reader_deterministic":true,"reading_room_integration":"ready-after-reader-export-qa","next_structured_derivative":"reading-room-integration"}}',
)
replace_once(
    registry,
    '"next_action":"Generate deterministic English reader/export derivatives from the verified 63-scene translation in Markdown, standalone HTML and machine-readable JSON; preserve all 1,210 units, all 1,025 dialogue/source-role links, all 28 cross-page units, five occurrence identities/seven intentional source-span links, exact provenance and archive-only scene numbering. Then run generated-output QA and write an integrity manifest before Reading Room integration."',
    '"next_action":"Create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures. Preserve archive-only scene numbering, exact source provenance, dialogue/source-role distinctions and all five occurrence identities; do not reconstruct absent lyrics, titles or authorship."',
)

# Status consistency audit.
status_audit = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
replace_once(
    status_audit,
    "| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **complete-verified 63/63 / 1,210 units** | reader/export preflight **PASS**; generation ready |",
    "| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **complete-verified 63/63 / 1,210 units** | reader/export **QA PASS**; Reading Room ready |",
)
replace_once(
    status_audit,
    "The separate **reader/export preflight is now executable and PASS**: workflow `.github/workflows/ammaiyappan-english-reader-preflight.yml`, run **34025680568**, head `ae554f92faf7a9b0f4005c42cc28c8b3e8e95d36`. It directly verified all **63 scene records / 1,210 units / 1,025 dialogue-source links / 28 cross-page units / five occurrence identities across seven intentional links**, with **0** missing/extra/duplicate dialogue links, provenance errors, page regressions, unit-ID errors, synthetic scene-end units, direct structural-star prose units, warnings or errors. See `works/ammaiyappan/editions/en/PREFLIGHT_QA_REPORT.md`. This is not a separate JSON-Schema-library validation.\n\n**Next production phase:** deterministic English reader/export generation in Markdown, standalone HTML and machine-readable JSON, followed by generated-output QA and an integrity manifest.",
    f'''The separate **reader/export preflight is executable and PASS**: workflow `.github/workflows/ammaiyappan-english-reader-preflight.yml`, run **34025680568**, head `ae554f92faf7a9b0f4005c42cc28c8b3e8e95d36`. It directly verified all **63 scene records / 1,210 units / 1,025 dialogue-source links / 28 cross-page units / five occurrence identities across seven intentional links**, with **0** missing/extra/duplicate dialogue links, provenance errors, page regressions, unit-ID errors, synthetic scene-end units, direct structural-star prose units, warnings or errors. See `works/ammaiyappan/editions/en/PREFLIGHT_QA_REPORT.md`. This is not a separate JSON-Schema-library validation.

The deterministic **reader/export package is complete-verified with generated-output QA PASS**. Markdown, standalone HTML and machine-readable JSON each preserve all **1,210** verified units exactly once; all **1,025** dialogue/source-role links, **28** cross-page units and **5 occurrence identities / 7 source-span links** reconcile to the structured translation. Output SHA-256 values: Markdown `{MD_SHA}`, HTML `{HTML_SHA}`, JSON `{JSON_SHA}`. `works/ammaiyappan/editions/en/manifest.json` records deterministic input/output hashes. Frozen source layers modified by reader generation: **0**.

**Next production phase:** create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures.''',
)
replace_once(
    status_audit,
    "The next bounded activity is **deterministic reader/export generation plus generated-output QA/manifest**.",
    "The next bounded activity is **source-linked Reading Room payload construction and QA**.",
)

# Master handover.
master = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
replace_once(
    master,
    "- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **complete-verified 63/63 / 1,210 units**, whole-work reconciliation PASS; executable reader/export preflight **PASS**; deterministic reader/export generation is next.",
    "- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **complete-verified 63/63 / 1,210 units**; reader/export **complete-verified with generated-output QA PASS**; Reading Room payload is next.",
)
replace_once(
    master,
    "- reader/export preflight: **complete-pass**;\n- reader/export generation: **ready / not started**.",
    "- reader/export preflight: **complete-pass**;\n- reader/export generation: **complete-verified — generated-output QA PASS**;\n- Reading Room integration: **ready for payload construction/QA**.",
)
replace_once(
    master,
    "**Exact next activity:** generate deterministic English reader/export derivatives from the verified structured translation in Markdown, standalone HTML and machine-readable JSON. Preserve archive scene IDs as navigation only, exact Tamil speaker-label/source-role provenance, all **1,210** units, all **1,025** dialogue links, all **28** cross-page units and all **5** occurrence identities / **7** intentional source-span links. Then run generated-output QA and write an integrity manifest before Reading Room integration. Do not modify frozen source evidence.",
    f'''### Reader/export package — PASS

`works/ammaiyappan/editions/en/` contains deterministic Markdown, standalone HTML and machine-readable JSON plus `QA_REPORT.md` and `manifest.json`. Generated-output QA confirms all **1,210** verified units exactly once in each export, all **1,025** dialogue/source-role links, all **28** cross-page units and all **5 occurrence identities / 7 source-span links**. Output SHA-256 values are `{MD_SHA}` (Markdown), `{HTML_SHA}` (HTML) and `{JSON_SHA}` (JSON). No frozen source evidence was modified.

**Exact next activity:** create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures. Preserve the 63 scene IDs strictly as archive navigation, exact source/page provenance, all speaker-label/source-role distinctions and all five occurrence identities; never reconstruct absent lyrics, titles or authorship.''',
)

# Work handover.
project = WORK / "PROJECT_HANDOVER.md"
replace_once(
    project,
    "## Exact next activity\n\n> **Fetch live `main`; preserve the complete-verified English translation and reader/export preflight PASS. Build deterministic publication-facing English reader/export derivatives from the verified translation records — Markdown, standalone HTML and machine-readable JSON — without maintaining an independent manual copy. Preserve all 1,210 units, all 1,025 dialogue/source-role links, all 28 cross-page units, all five occurrence identities/seven source-span links, exact Tamil speaker-label/source-role provenance and archive-only scene numbering. Then run generated-output QA and write an integrity manifest before Reading Room integration. Do not alter frozen Tamil/dialogue/character/song evidence.**",
    f'''## Reader/export package — PASS

The deterministic reader/export package is complete-verified under `editions/en/`. Markdown, standalone HTML and machine-readable JSON each preserve all **1,210** units exactly once. `QA_REPORT.md` records generated-output PASS and `manifest.json` records deterministic input/output hashes. Exact **1,025/1,025** dialogue/source-role linkage, all **28** cross-page units and all **5 occurrence identities / 7 source-span links** are preserved. Output SHA-256 values: Markdown `{MD_SHA}`, HTML `{HTML_SHA}`, JSON `{JSON_SHA}`. Frozen source layers modified: **0**.

## Exact next activity

> **Fetch live `main`; preserve the complete-verified Tamil/structured/English/reader layers. Create and QA the source-linked Ammayappan Reading Room integration payload from the verified reader/translation structures. Preserve the 63 scene IDs as archive-only navigation, exact page/source provenance, all dialogue/source-role distinctions and all five source-visible occurrence identities; do not reconstruct absent lyrics, titles or authorship. Synchronize all mirrors after payload QA before any separate-site application.**''',
)

# Next-chat prompt.
prompt = WORK / "NEXT_CHAT_PROMPT.md"
prompt_text = prompt.read_text(encoding="utf-8")
old_checkpoint_line_start = "Last confirmed live checkpoint immediately before this prompt refresh:\n\n`"
if old_checkpoint_line_start in prompt_text:
    after = prompt_text.split(old_checkpoint_line_start, 1)[1]
    old_line = after.split("\n", 1)[0]
    prompt_text = prompt_text.replace(
        old_checkpoint_line_start + old_line,
        old_checkpoint_line_start + f"{HEAD}` — **`Reader/export build workflow checkpoint before status synchronization`**",
        1,
    )
    write_if_changed(prompt, prompt_text)
replace_once(
    prompt,
    "- reader/export generation: **ready / not started**.",
    "- reader/export generation: **complete-verified — Markdown / HTML / JSON / manifest; generated-output QA PASS**;\n- Reading Room integration: **ready for payload construction/QA**.",
)
replace_once(
    prompt,
    "27. verified translation records `scene-001.json`–`scene-063.json` as needed for reader/export generation and QA.",
    "27. `works/ammaiyappan/editions/en/build.py`\n28. `works/ammaiyappan/editions/en/QA_REPORT.md`\n29. `works/ammaiyappan/editions/en/manifest.json`\n30. `works/ammaiyappan/editions/en/reader-edition.json`\n31. verified translation records `scene-001.json`–`scene-063.json` as needed for Reading Room payload construction and QA.",
)
replace_once(
    prompt,
    "> **Fetch live `main`; confirm English translation remains complete-verified at 63/63 scenes / 1,210 units and `editions/en/PREFLIGHT_QA_REPORT.md` is PASS. Then build deterministic English reader/export derivatives directly from the verified translation records — Markdown, standalone HTML and machine-readable JSON — never an independent manual copy. Preserve every one of the 1,210 translation units, all 1,025 dialogue/source-role links, all 28 cross-page units with page segments, all five occurrence identities across seven intentional source-span links, exact Tamil speaker-label/source-role provenance and archive-only scene numbering. Do not alter frozen Tamil/dialogue/character/song evidence. After generation run whole-work generated-output QA, write an integrity manifest, synchronize all current mirrors, and only then consider Reading Room integration.**",
    "> **Fetch live `main`; confirm English translation remains complete-verified at 63/63 scenes / 1,210 units, `editions/en/PREFLIGHT_QA_REPORT.md` is PASS, and the deterministic reader/export package is complete-verified with `editions/en/QA_REPORT.md` + `manifest.json` PASS. Then create and QA the source-linked Ammayappan Reading Room integration payload from the verified reader/translation structures. Preserve all 1,210 units, all 1,025 dialogue/source-role links, all 28 cross-page units, all five occurrence identities across seven intentional source-span links, exact Tamil speaker-label/source-role provenance, page provenance and archive-only scene numbering. Do not alter frozen Tamil/dialogue/character/song evidence and do not reconstruct absent lyrics, titles or authorship. Synchronize all current mirrors after payload QA; separate-site application remains a later explicit step.**",
)

print("AMMAYAPPAN READER STATUS SYNC")
print("changed=", changed)
print("markdown_sha256=", MD_SHA)
print("html_sha256=", HTML_SHA)
print("json_sha256=", JSON_SHA)
