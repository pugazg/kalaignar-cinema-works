#!/usr/bin/env python3
"""Synchronize repository-wide current mirrors for the Naam intake/mapping checkpoint."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "works" / "naam"

SOURCE_SHA = "0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad"
NEXT = (
    "Canonical Tamil first-pass transcription from the rendered scan, in source order, "
    "with stable page anchors and page-level historical-glyph checks — followed later "
    "by a separate visual fidelity audit before any structured derivatives."
)

required = [
    WORK / "README.md",
    WORK / "metadata.yaml",
    WORK / "mapping.md",
    WORK / "notes" / "historical-glyph-audit.md",
    WORK / "PROJECT_HANDOVER.md",
    WORK / "NEXT_CHAT_PROMPT.md",
]
for path in required:
    if not path.exists():
        raise SystemExit(f"Missing required Naam intake file: {path.relative_to(ROOT)}")

metadata = (WORK / "metadata.yaml").read_text(encoding="utf-8")
for needle in [
    f'  sha256: "{SOURCE_SHA}"',
    "  structural_mapping: verified",
    "  canonical_tamil_transcription: not-started",
    "  historical_glyph_audit: not-started",
]:
    if needle not in metadata:
        raise SystemExit(f"Naam metadata checkpoint missing: {needle}")

changed: list[str] = []


def write_if_changed(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8")
    if old != text:
        path.write_text(text, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())


# 1. data/works.json — preserve all existing objects/formatting and append Naam only once.
registry_path = ROOT / "data" / "works.json"
registry = registry_path.read_text(encoding="utf-8")
if '"id":"naam"' not in registry and '"id": "naam"' not in registry:
    stripped = registry.rstrip()
    if not stripped.endswith("]"):
        raise SystemExit("data/works.json does not end in a JSON array")
    prefix = stripped[:-1].rstrip()
    if not prefix.endswith("}"):
        raise SystemExit("data/works.json has unexpected final object shape")
    item = f'''  {{
    "id":"naam","title_ta":"நாம்","source_title_ta":"நாம்","work_type":"film","source_type":"printed_screenplay_dialogue_booklet","source_identifier":"TVA_BOK_0064201","source_pdf_pages":72,"source_byte_size":115948588,"source_sha256":"{SOURCE_SHA}","author_as_printed":"மு. கருணாநிதி","story_dialogue_song_credit_as_printed":"கதை, வசனம், பாடல்... மு. கருணாநிதி","source_specific_song_credit":{{"title":"ஆயிரம் தெய்வங்கள்","author":"பாரதியார்","credit_pdf_page":4,"song_body_pdf_page":16}},"publisher_as_printed":"ஆசீர்வாதபுரம் ஆதிதிராவிட நல உரிமைச் சங்கத்தார்","printer_as_printed":"அச்சிட்டது ஆதி பிரஸ், சென்னை—12.","publication_year_as_printed":null,"edition_statement_as_printed":null,"front_matter_pdf_pages":"1-4","main_text_pdf_pages":"5-71","main_text_page_count":67,"back_matter_pdf_pages":"72","visible_printed_page_numbers":"6-71","structural_mapping":"verified","source_numbered_scene_headings":true,"scene_headings_observed":45,"scene_heading_range":"1-45","scene_number_gaps_observed":[],"scene_number_repeats_observed":[],"scene_number_out_of_order_observed":[],"canonical_tamil_transcription":"not-started","historical_glyph_audit":"not-started","historical_glyph_guide_path":"docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md","historical_glyph_audit_path":"works/naam/notes/historical-glyph-audit.md","next_action":"{NEXT}"
  }}'''
    registry = prefix + ",\n" + item + "\n]\n"
    write_if_changed(registry_path, registry)

# Validate registry JSON and preserve critical unrelated checksum.
registry_data = json.loads(registry_path.read_text(encoding="utf-8"))
naam_items = [x for x in registry_data if x.get("id") == "naam"]
if len(naam_items) != 1:
    raise SystemExit(f"Expected exactly one Naam registry object, found {len(naam_items)}")
if naam_items[0].get("source_sha256") != SOURCE_SHA or naam_items[0].get("scene_headings_observed") != 45:
    raise SystemExit("Naam registry object does not match intake authority")
if "17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f" not in registry_path.read_text(encoding="utf-8"):
    raise SystemExit("Critical Tirumbippaar EPUB checksum was not preserved")

# 2. Root README — add active Naam status without changing completed-work text.
root_readme = ROOT / "README.md"
text = root_readme.read_text(encoding="utf-8")
naam_section = f'''## நாம் status

`TVA_BOK_0064201_நாம்.pdf` is the **active newly onboarded cinema source**. Intake and full structural mapping are complete; canonical Tamil has not started.

- source: **72 PDF pages**, image-only; SHA-256 `{SOURCE_SHA}`;
- visible title / author: **நாம் / மு. கருணாநிதி**;
- source-visible organization: **ஆசீர்வாதபுரம் ஆதிதிராவிட நல உரிமைச் சங்கத்தார்**;
- front matter / screenplay / back matter: **PDF 1–4 / 5–71 / 72**;
- visible printed numerals: **6–71** on PDF 6–71; PDF 5 opens the screenplay without a securely visible printed numeral;
- source-numbered scenes: **45 — காட்சி 1–45**, sequential with no observed gap/repeat/out-of-order number;
- PDF 4 credit safeguard: broad `கதை, வசனம், பாடல்... மு. கருணாநிதி`, with the explicit item exception `பாட்டு 'ஆயிரம் தெய்வங்கள்'—பாரதியார்.`;
- canonical Tamil / visual fidelity / historical-glyph audit: **not-started / not-started / not-started**;
- old-type transcription is bound to `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` with page-level dual-gate verification.

**Next:** {NEXT}

'''
if "## நாம் status" not in text:
    marker = "## ராஜா ராணி status\n"
    if marker not in text:
        raise SystemExit("Could not locate root README insertion point")
    text = text.replace(marker, naam_section + marker, 1)
    write_if_changed(root_readme, text)

# 3. Master handover — register Naam and make it the active checkpoint.
handover_path = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
handover = handover_path.read_text(encoding="utf-8")
if "- **Naam / நாம்**" not in handover:
    anchor = "- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **complete-verified 63/63 / 1,210 units**; reader/export QA PASS; Reading Room payload QA PASS; site not applied.\n"
    addition = anchor + f"- **Naam / நாம்** — active new work; 72-page image-only scan; intake complete; 45 source-numbered scenes mapped sequentially; canonical Tamil not-started; historical-glyph dual gate mandatory. Source SHA-256 `{SOURCE_SHA}`.\n"
    if anchor not in handover:
        raise SystemExit("Could not locate master-handover high-level insertion point")
    handover = handover.replace(anchor, addition, 1)

handover = handover.replace(
    "Current active mirrors use the corrected Ammayappan 1,025-unit source authority and complete English checkpoint.",
    "Ammayappan remains closed at its complete-verified checkpoint. The current active production work is **Naam / நாம்**, beginning canonical Tamil only after its completed source-intake and structural-mapping gate.",
    1,
)

if "## 8. Naam active checkpoint" not in handover:
    marker = "## 8. Ammayappan active checkpoint\n"
    if marker not in handover:
        raise SystemExit("Could not locate Ammayappan checkpoint heading")
    naam_handover = f'''## 8. Naam active checkpoint

Work: `works/naam/`  
Source: `TVA_BOK_0064201_நாம்.pdf`

- source intake / whole-scan inspection: **complete / 72/72**;
- source SHA-256: `{SOURCE_SHA}`;
- source is **image-only**;
- source-visible organization: `ஆசீர்வாதபுரம் ஆதிதிராவிட நல உரிமைச் சங்கத்தார்`;
- screenplay range: **PDF 5–71 / 67 pages**; front matter PDF 1–4; back matter PDF 72;
- visible printed numerals: **6–71** on PDF 6–71; no printed numeral is asserted for PDF 5;
- scene map: **காட்சி 1–45**, sequential; no observed gaps/repeats/out-of-order numbers;
- specific source credit safeguard: `பாட்டு 'ஆயிரம் தெய்வங்கள்'—பாரதியார்.` survives the broad `கதை, வசனம், பாடல்... மு. கருணாநிதி` credit;
- canonical Tamil: **not-started**;
- historical-glyph audit: **not-started**, mandatory from the first page using the 13-family source-pixel method;
- structured derivatives / translation / reader: **blocked/not-started**.

**Exact next activity:** {NEXT}

---

'''
    handover = handover.replace(marker, naam_handover + "## 9. Ammayappan closed checkpoint\n", 1)
    handover = handover.replace("## 9. Downstream dispositions for completed works", "## 10. Downstream dispositions for completed works", 1)
write_if_changed(handover_path, handover)

# 4. Repository status audit — advance from seven to eight registered works and add Naam row/checkpoint.
status_path = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
status = status_path.read_text(encoding="utf-8")
status = status.replace("all **seven registered works**", "all **eight registered works**", 1)
old_result = "**PASS for Ammayappan's source/structured authority and complete English translation.** Canonical Tamil is **105/105 dual-gate complete-verified**; scene derivatives are **63/63**; dialogue authority is **1,009 explicit + 16 source-role supplements = 1,025 downstream units**; character/entity coverage is **1,025/1,025** and **62/62 exact labels**. English translation is now **complete-verified at 63/63 archival scenes / 1,210 units**, with whole-work source/linkage reconciliation PASS."
new_result = "**PASS for the current repository-wide checkpoint.** Ammayappan remains complete-verified through its Reading Room payload. **Naam / நாம்** is newly registered with source intake and whole-scan structural mapping complete: 72-page image-only source, 45 sequential source-numbered scenes, canonical Tamil not-started, and a mandatory historical-glyph dual gate before downstream derivatives."
if old_result in status:
    status = status.replace(old_result, new_result, 1)
elif new_result not in status:
    raise SystemExit("Could not locate status-audit Result checkpoint")

naam_row = "| Naam / நாம் | source intake + map complete; canonical Tamil not-started | 45 source-numbered scenes mapped; derivatives blocked | not-started | not-started |\n"
if naam_row not in status:
    row_anchor = "| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **complete-verified 63/63 / 1,210 units** | reader/export + Reading Room payload **QA PASS**; site not applied |\n"
    if row_anchor not in status:
        raise SystemExit("Could not locate status matrix insertion point")
    status = status.replace(row_anchor, row_anchor + naam_row, 1)

if "## Naam current checkpoint" not in status:
    marker = "## Ammayappan current checkpoint\n"
    if marker not in status:
        raise SystemExit("Could not locate status-audit Ammayappan checkpoint")
    section = f'''## Naam current checkpoint

- work: `works/naam/`;
- source: `TVA_BOK_0064201_நாம்.pdf`, **72 pages / image-only**, SHA-256 `{SOURCE_SHA}`;
- source intake / full scan inspection / structural map: **complete / complete / verified**;
- front matter / screenplay / back matter: **PDF 1–4 / 5–71 / 72**;
- scene headings: **45 / காட்சி 1–45**, no observed gap/repeat/out-of-order numbering;
- canonical Tamil / visual fidelity / historical-glyph audit: **not-started / not-started / not-started**;
- the 13 historical glyph families must be checked page-by-page from the rendered source; no global replacements or spelling modernization;
- PDF 4's item-level `ஆயிரம் தெய்வங்கள்` → `பாரதியார்` credit is preserved as a later authorship-gate constraint;
- downstream scene/dialogue/character/song/English layers remain blocked until verified Tamil.

**Next production phase:** {NEXT}

'''
    status = status.replace(marker, section + marker, 1)

old_conclusion = "Ammayappan's canonical Tamil and structured source-derived layers remain **closed at the corrected 1,025-unit authority**. English translation is **complete-verified at 63/63 scenes / 1,210 units**, final source/linkage reconciliation is PASS, and the executable reader/export preflight is now **PASS**. The source-linked Reading Room payload is now **complete-verified / QA PASS**; separate-site application remains **not-applied** and requires explicit authorization."
new_conclusion = f"Ammayappan remains closed through Reading Room payload QA PASS. **Naam / நாம்** is now the active production work with intake and the 45-scene structural map complete and canonical Tamil still not-started. Its next gate is source-order canonical Tamil first pass with mandatory page-level historical-glyph checks; no downstream derivative is authorized before verified Tamil. Source SHA-256 `{SOURCE_SHA}`."
if old_conclusion in status:
    status = status.replace(old_conclusion, new_conclusion, 1)
elif new_conclusion not in status:
    raise SystemExit("Could not locate status-audit conclusion")
write_if_changed(status_path, status)

# Final stale-state assertions for current mirrors.
checks = {
    ROOT / "README.md": ["## நாம் status", SOURCE_SHA, "canonical Tamil / visual fidelity / historical-glyph audit: **not-started / not-started / not-started**"],
    ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md": ["## 8. Naam active checkpoint", SOURCE_SHA, "canonical Tamil: **not-started**"],
    ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md": ["all **eight registered works**", "## Naam current checkpoint", SOURCE_SHA],
    ROOT / "data" / "works.json": ['"id":"naam"', SOURCE_SHA, '"scene_headings_observed":45'],
}
for path, needles in checks.items():
    current = path.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in current:
            raise SystemExit(f"Synchronization assertion failed in {path.relative_to(ROOT)}: {needle}")

print("NAAM INTAKE MIRROR SYNCHRONIZATION")
print("status= PASS")
print("source_sha256=", SOURCE_SHA)
print("registered_works= 8")
print("scenes_mapped= 45")
print("canonical_tamil= not-started")
print("changed_files=", len(changed))
for path in changed:
    print(path)
