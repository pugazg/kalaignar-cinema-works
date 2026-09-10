from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "works" / "maruthanattu-ilavarasi"
NOTES = WORK / "notes"
NOTES.mkdir(parents=True, exist_ok=True)

SOURCE_ID = "TVA_BOK_0065774"
SOURCE_FILE = "TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf"
SOURCE_SHA = "8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f"
SOURCE_BYTES = 9330870
NEXT = "Begin canonical Tamil first-pass transcription from PDF 2 onward in five-source-page batches, starting with PDF 2–6. Preserve source order, exact speaker labels, punctuation, stage directions, the unnumbered opening structure, printed scene numbering anomalies and stable PDF/logical-printed page anchors. Inspect all historical-glyph-sensitive families from enlarged source pixels on every page; keep first-pass pages draft, record uncertainty explicitly, and do not begin scene/dialogue/character/song/English derivatives until the later separate full visual-fidelity and historical-glyph verification gates close."

WORK.joinpath("README.md").write_text(f'''# மருதநாட்டு இளவரசி

Source-led archival workspace for the scanned **`மருதநாட்டு இளவரசி`** திரை வசனம் booklet.

## Source authority

Controlling source: `{SOURCE_FILE}` — **22 PDF pages / {SOURCE_BYTES:,} bytes / SHA-256 `{SOURCE_SHA}` / image-only**. The uploaded scan is canonical authority and is not committed to the repository.

Visible source evidence:

- title: **`மருதநாட்டு இளவரசி`**;
- recurring body header: **`மருதநாட்டு இளவரசி—திரை வசனம்`**;
- printed credit on PDF 2: **`வசனம் : மு. கருணாநிதி.`**;
- cover imprint/issuing line: **`வியந்தமிழ்ப் பாசறை, கோவில்பட்டி.`**;
- cover price: **`விலை அணா 3.`**;
- explicit edition statement: **not observed**;
- explicit publication year: **not observed**.

Library/user ownership stamps, handwriting and later marginal marks are non-source and must not enter canonical transcription.

## Intake / mapping checkpoint

- source intake: **COMPLETE**;
- structural mapping: **COMPLETE-VERIFIED**;
- PDF 1: cover, no printed page number;
- PDF 2–22: main திரை வசனம் body;
- visible printed numerals: **2–21 on PDF 3–22**;
- logical body pagination: **PDF 2–22 ↔ printed 1–21**, with logical `printed = PDF - 1`; PDF 2's numeral `1` is not visibly printed and is recorded only as the logical continuation of the uninterrupted sequence;
- source-numbered headings observed: **8** — `காட்சி 2.`, `காட்சி 3.`, `காட்சி 4.`, `காட்சி 5.`, `காட்சி 6.`, `காட்சி 8.`, `காட்சி 9.`, `காட்சி 10.`;
- no printed `காட்சி 1.` heading is visible before `காட்சி 2.`; PDF 2–4 therefore remains an **unnumbered opening source segment**, not an inferred scene 1;
- printed scene-number gap: **`காட்சி 7.` not observed**; do not repair or renumber it;
- scene 8 carries **`(ராஜ தர்பார்)`**;
- scene 10 carries **`பலி பீடம்.`**;
- PDF 4 contains a printed `* * *` structural separator;
- PDF 22 ends with **`நலம்!`** and a decorative star; no separate back-cover scan follows;
- no clearly bounded song/lyric/chant block was observed during the full-scan structural pass;
- historical Tamil typeforms are present and the historical-glyph gate is mandatory.

Canonical Tamil transcription has **not started**. No structured derivative layer is authorized yet.

## Exact next activity

> **{NEXT}**
''', encoding="utf-8")

WORK.joinpath("metadata.yaml").write_text(f'''id: maruthanattu-ilavarasi
title_ta: "மருதநாட்டு இளவரசி"
work_type: film
source_type: printed_screenplay_dialogue_booklet
source_identifier: {SOURCE_ID}
source_filename: "{SOURCE_FILE}"
source_pdf_pages: 22
source_byte_size: {SOURCE_BYTES}
source_sha256: {SOURCE_SHA}
source_embedded_text: false
source_image_only: true
credit_as_printed: "வசனம் : மு. கருணாநிதி."
recurring_header_as_printed: "மருதநாட்டு இளவரசி—திரை வசனம்"
cover_imprint_as_printed: "வியந்தமிழ்ப் பாசறை, கோவில்பட்டி."
cover_price_as_printed: "விலை அணா 3."
publication_year_as_printed: null
edition_statement_as_printed: null
cover_pdf_pages: "1"
main_text_pdf_pages: "2-22"
main_text_logical_printed_pages: "1-21"
visible_printed_page_numbers: "2-21"
body_pagination_formula: "logical printed = PDF - 1"
source_intake: complete
structural_mapping: complete-verified
mapping_path: works/maruthanattu-ilavarasi/mapping.md
source_numbered_scene_headings: true
scene_headings_observed: 8
scene_ids_observed: ["2", "3", "4", "5", "6", "8", "9", "10"]
scene_number_gaps_observed: [7]
source_scene_1_heading_observed: false
opening_unnumbered_segment_pdf_pages: "2-4"
opening_unnumbered_segment_logical_printed_pages: "1-3"
historical_glyph_policy: required
historical_glyph_guide_path: docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md
historical_glyph_audit_path: works/maruthanattu-ilavarasi/notes/historical-glyph-audit.md
canonical_tamil_transcription: not-started
canonical_tamil_first_pass_pages_completed: 0
canonical_tamil_total_body_pages: 21
visual_fidelity_audit: not-started
historical_glyph_audit: required-not-started
structured_derivatives: blocked
next_action: "{NEXT}"
''', encoding="utf-8")

WORK.joinpath("mapping.md").write_text('''# மருதநாட்டு இளவரசி — structural mapping

Status: **COMPLETE-VERIFIED for source intake / structural mapping**.

The scan is image-only. Mapping was established from the rendered source, not OCR. Canonical transcription is not started.

## Pagination and content map

| PDF | Printed / logical page | Source structure |
|---:|:---:|---|
| 1 | — | Front cover: `மருதநாட்டு இளவரசி`; cover imprint `வியந்தமிழ்ப் பாசறை, கோவில்பட்டி.`; `விலை அணா 3.`; ownership/library stamps overlay the cover. |
| 2 | logical 1 | Title/credit box with `வசனம் : மு. கருணாநிதி.`; beginning of the unnumbered opening source segment. The numeral `1` is not visibly printed. |
| 3 | 2 | Unnumbered opening segment continues. |
| 4 | 3 | Unnumbered opening segment continues; printed `* * *` separator occurs mid-page. |
| 5 | 4 | `காட்சி 2.` begins. |
| 6 | 5 | `காட்சி 2.` continues; `காட்சி 3.` begins mid-page. |
| 7 | 6 | `காட்சி 3.` continues. |
| 8 | 7 | `காட்சி 3.` closes; `காட்சி 4.` begins and closes; `காட்சி 5.` begins near page foot. |
| 9 | 8 | `காட்சி 5.` continues; `காட்சி 6.` begins near page foot. |
| 10 | 9 | `காட்சி 6.` continues. |
| 11 | 10 | `காட்சி 6.` continues. |
| 12 | 11 | `காட்சி 6.` continues. |
| 13 | 12 | `காட்சி 6.` closes; `காட்சி 8.` begins with `(ராஜ தர்பார்)`. No `காட்சி 7.` is printed between them. |
| 14 | 13 | `காட்சி 8.` continues. |
| 15 | 14 | `காட்சி 8.` continues. |
| 16 | 15 | `காட்சி 8.` continues. |
| 17 | 16 | `காட்சி 8.` continues. |
| 18 | 17 | `காட்சி 8.` closes; `காட்சி 9.` begins near page foot. |
| 19 | 18 | `காட்சி 9.` continues/closes; `காட்சி 10.` begins with `பலி பீடம்.`. |
| 20 | 19 | `காட்சி 10.` continues. |
| 21 | 20 | `காட்சி 10.` continues. |
| 22 | 21 | `காட்சி 10.` concludes; `நலம்!` and decorative star; library stamp below. |

For PDF 3–22 the visible printed numerals are 2–21. PDF 2 is retained as **logical printed page 1** only because it is the immediately preceding body page in the uninterrupted PDF/printed sequence; no visible `1` is claimed.

## Observed source-heading sequence

| Order | PDF | Printed/logical | Exact heading / attached source marker |
|---:|---:|:---:|---|
| 1 | 5 | 4 | `காட்சி 2.` |
| 2 | 6 | 5 | `காட்சி 3.` |
| 3 | 8 | 7 | `காட்சி 4.` |
| 4 | 8 | 7 | `காட்சி 5.` |
| 5 | 9 | 8 | `காட்சி 6.` |
| 6 | 13 | 12 | `காட்சி 8.` + `(ராஜ தர்பார்)` |
| 7 | 18 | 17 | `காட்சி 9.` |
| 8 | 19 | 18 | `காட்சி 10.` + `பலி பீடம்.` |

### Numbering disposition

- no source-visible `காட்சி 1.` heading is present in PDF 2–4;
- PDF 2–4 is therefore mapped as an **unnumbered opening segment**;
- `காட்சி 7.` is not observed; printed numbering jumps directly from `காட்சி 6.` to `காட்சி 8.`;
- the archive must preserve these facts and must not synthesize scene 1 or scene 7.

## Other structures

- recurring running header: `மருதநாட்டு இளவரசி—திரை வசனம்`;
- PDF 4 has a `* * *` structural separator;
- no clearly bounded printed song, lyric or chant block was identified during intake mapping;
- PDF 22 closes with `நலம்!` and a decorative star;
- no separately scanned back matter/back cover follows PDF 22.

## Scan condition / non-source marks

- heavy ownership/library stamps overlay the cover and the PDF 2 title/credit area;
- handwritten brackets, strokes and other later marginal marks appear on several body pages;
- some pages show skew, gutter shadow and edge wear/cropping, but the visible printed numbering is continuous from 2 through 21;
- these later marks are not canonical text;
- the older typeface requires enlarged source-pixel review for the known historical Tamil glyph families.

## Gate state

- source intake: **complete**;
- structural mapping: **complete-verified**;
- canonical Tamil: **not-started**;
- visual fidelity: **not-started**;
- historical-glyph audit: **required / not-started**;
- scene/dialogue/character/song/English/reader layers: **blocked**.
''', encoding="utf-8")

NOTES.joinpath("source-intake.md").write_text(f'''# மருதநாட்டு இளவரசி — source intake

Status: **COMPLETE**.

## Binary identity

- original filename: `{SOURCE_FILE}`;
- archive identifier: `{SOURCE_ID}` (from supplied archive filename);
- PDF pages: **22**;
- bytes: **{SOURCE_BYTES:,}**;
- SHA-256: `{SOURCE_SHA}`;
- embedded text: **none detected**; image-only source.

## Printed identity

- title: `மருதநாட்டு இளவரசி`;
- recurring header: `மருதநாட்டு இளவரசி—திரை வசனம்`;
- credit: `வசனம் : மு. கருணாநிதி.` on PDF 2;
- cover imprint/issuing line: `வியந்தமிழ்ப் பாசறை, கோவில்பட்டி.`;
- cover price: `விலை அணா 3.`;
- edition statement: not observed;
- publication year: not observed.

No year or edition is inferred from film history, file metadata, price, library stamps or outside knowledge.

## Scan boundaries

- PDF 1: cover;
- PDF 2–22: main திரை வசனம் body;
- visible printed pagination: 2–21 on PDF 3–22;
- PDF 2 retained as logical printed 1 for reversible sequence mapping only;
- PDF 22 ends the text with `நலம்!`; no separate back-cover scan follows.

## Source-condition notes

Ownership stamps and later handwriting/marginal marks are present and must be excluded from canonical transcription. The historical typeface requires the repository historical-glyph workflow from the first canonical batch onward.
''', encoding="utf-8")

NOTES.joinpath("historical-glyph-audit.md").write_text('''# மருதநாட்டு இளவரசி — historical Tamil glyph audit

Status: **REQUIRED / NOT STARTED**.

The rendered scan uses older Tamil typeforms. Canonical first pass must prospectively inspect every source page at enlarged resolution and explicitly check the known families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Rules:

- source pixels control character identity;
- OCR/parsed text is not authority;
- encode proven historical character identity in modern Unicode without modernizing wording;
- never global-replace a glyph family;
- preserve occurrence-specific source forms;
- unresolved glyphs remain explicit and prevent page verification;
- first-pass pages remain draft until the later independent visual-fidelity and historical-glyph closure gate.

Coverage at intake: **0/21 body pages**.
''', encoding="utf-8")

WORK.joinpath("PROJECT_HANDOVER.md").write_text(f'''# மருதநாட்டு இளவரசி — Project Handover

Repository: `pugazg/kalaignar-cinema-works`
Branch: `main`
Work: `works/maruthanattu-ilavarasi/`

**LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`{SOURCE_FILE}` — **22 PDF pages / {SOURCE_BYTES:,} bytes / SHA-256 `{SOURCE_SHA}` / image-only**. Do not commit the source PDF.

## Durable intake state

- source intake: **COMPLETE**;
- structural mapping: **COMPLETE-VERIFIED**;
- PDF 1 cover; PDF 2–22 body;
- logical body pages: **PDF 2–22 ↔ printed 1–21**, visible printed numerals 2–21 on PDF 3–22;
- exact printed credit: **`வசனம் : மு. கருணாநிதி.`**;
- edition/year: **not observed / not observed**;
- source headings observed: **8 — 2, 3, 4, 5, 6, 8, 9, 10**;
- no printed scene-1 heading; PDF 2–4 is unnumbered opening structure;
- source numbering gap: **7 not observed**;
- historical-glyph workflow: **required**;
- canonical Tamil: **NOT STARTED**;
- all structured/English/reader derivatives: **BLOCKED**.

## Exact next activity

> **{NEXT}**
''', encoding="utf-8")

WORK.joinpath("NEXT_CHAT_PROMPT.md").write_text(f'''# Next Chat Prompt — மருதநாட்டு இளவரசி / canonical Tamil PDF 2–6

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/maruthanattu-ilavarasi/`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`{SOURCE_FILE}` — **22 PDF pages / {SOURCE_BYTES:,} bytes / SHA-256 `{SOURCE_SHA}` / image-only**. Do not commit it.

## Durable state

- intake **COMPLETE**;
- mapping **COMPLETE-VERIFIED**;
- body PDF **2–22**, logical printed **1–21**;
- source headings: **2,3,4,5,6,8,9,10**;
- PDF 2–4 is an unnumbered opening segment; do not invent source scene 1;
- no source `காட்சி 7.` observed; do not repair numbering;
- canonical Tamil first pass **0/21 / NOT STARTED**;
- visual-fidelity and historical-glyph final verification **NOT STARTED**;
- later derivatives **BLOCKED**.

## Next batch

> **Canonical Tamil first-pass transcription for PDF 2–6 as one five-source-page batch. Visually transcribe each whole page once from the rendered source, preserve exact wording/punctuation/speaker labels/scene headings/stage directions and page boundaries, and keep pages draft. Prospectively inspect the historical-glyph families on every page; use crops/enhancement only when an actual reading is uncertain. Synchronize controls and commit immediately after the five pages. Do not start visual-fidelity verification or structured derivatives in the same batch.**
''', encoding="utf-8")

registry_path = ROOT / "data" / "works.json"
registry = json.loads(registry_path.read_text(encoding="utf-8"))
if not any(x.get("id") == "maruthanattu-ilavarasi" for x in registry):
    registry.append({
        "id": "maruthanattu-ilavarasi",
        "title_ta": "மருதநாட்டு இளவரசி",
        "source_title_ta": "மருதநாட்டு இளவரசி",
        "work_type": "film",
        "source_type": "printed_screenplay_dialogue_booklet",
        "source_identifier": SOURCE_ID,
        "source_pdf_pages": 22,
        "source_byte_size": SOURCE_BYTES,
        "source_sha256": SOURCE_SHA,
        "credit_as_printed": "வசனம் : மு. கருணாநிதி.",
        "cover_imprint_as_printed": "வியந்தமிழ்ப் பாசறை, கோவில்பட்டி.",
        "cover_price_as_printed": "விலை அணா 3.",
        "publication_year_as_printed": None,
        "edition_statement_as_printed": None,
        "cover_pdf_pages": "1",
        "main_text_pdf_pages": "2-22",
        "main_text_logical_printed_pages": "1-21",
        "visible_printed_page_numbers": "2-21",
        "body_pagination_formula": "logical printed = PDF - 1",
        "structural_mapping": "complete-verified",
        "source_numbered_scene_headings": True,
        "scene_headings_observed": 8,
        "scene_ids_observed": ["2", "3", "4", "5", "6", "8", "9", "10"],
        "scene_number_gaps_observed": [7],
        "opening_unnumbered_segment_pdf_pages": "2-4",
        "canonical_tamil_transcription": "not-started",
        "canonical_tamil_first_pass_pages_completed": 0,
        "canonical_tamil_total_body_pages": 21,
        "historical_glyph_audit": "required-not-started",
        "structured_derivatives": {
            "scene_index": "not-started",
            "dialogue_index": "not-started",
            "character_index": "not-started",
            "song_performance_gate": "not-started",
            "english_translation": "not-started",
            "reader_export": "not-started",
            "reading_room_integration": "not-started"
        },
        "next_action": NEXT
    })
registry_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

root_readme = ROOT / "README.md"
text = root_readme.read_text(encoding="utf-8")
section = f'''## மருதநாட்டு இளவரசி status

`{SOURCE_FILE}` is a newly initialized **22-page image-only திரை வசனம் source** with source intake and structural mapping complete-verified.

- printed credit: **`வசனம் : மு. கருணாநிதி.`**;
- cover imprint: **`வியந்தமிழ்ப் பாசறை, கோவில்பட்டி.`**; price **`விலை அணா 3.`**;
- explicit edition/year: **not observed / not observed**;
- body: **PDF 2–22 / logical printed 1–21**; visible numerals 2–21 on PDF 3–22;
- opening PDF 2–4 remains **unnumbered**; no source `காட்சி 1.` heading is invented;
- numbered headings observed: **8 — 2,3,4,5,6,8,9,10**; source `காட்சி 7.` not observed;
- historical Tamil glyph gate: **required**;
- canonical Tamil: **NOT STARTED**; later derivatives **BLOCKED**.

**Next:** {NEXT}

'''
if "## மருதநாட்டு இளவரசி status" not in text:
    text = text.replace("## வண்டிக்காரன் மகன் status\n", section + "## வண்டிக்காரன் மகன் status\n", 1)
root_readme.write_text(text, encoding="utf-8")

master = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
text = master.read_text(encoding="utf-8")
if "- **Maruthanattu Ilavarasi / மருதநாட்டு இளவரசி**" not in text:
    needle = "- **Vandikkaran Magan / வண்டிக்காரன் மகன்** —"
    pos = text.find(needle)
    if pos >= 0:
        end = text.find("\n", pos)
        line = "- **Maruthanattu Ilavarasi / மருதநாட்டு இளவரசி** — source intake **COMPLETE**, structural mapping **COMPLETE-VERIFIED**; 22-page image-only booklet / body PDF 2–22; printed credit `வசனம் : மு. கருணாநிதி.`; observed source headings 2,3,4,5,6,8,9,10 with unnumbered opening PDF 2–4 and missing source heading 7; canonical Tamil not started; historical-glyph gate required.\n"
        text = text[:end+1] + line + text[end+1:]
marker = "## 11. மருதநாட்டு இளவரசி active checkpoint"
if marker not in text:
    text += f'''\n\n---\n\n{marker}\n\nWork: `works/maruthanattu-ilavarasi/`\nSource: `{SOURCE_FILE}`\n\n- intake: **COMPLETE**;\n- mapping: **COMPLETE-VERIFIED**;\n- source: **22 PDF pages / {SOURCE_BYTES:,} bytes / SHA-256 `{SOURCE_SHA}` / image-only**;\n- body: **PDF 2–22 / logical printed 1–21**;\n- printed credit: **`வசனம் : மு. கருணாநிதி.`**;\n- source headings: **2,3,4,5,6,8,9,10**;\n- opening PDF 2–4 unnumbered; `காட்சி 7.` not observed;\n- historical-glyph gate: **required**;\n- canonical Tamil: **NOT STARTED**;\n- later derivatives: **BLOCKED**.\n\n**Exact next activity:** {NEXT}\n'''
master.write_text(text, encoding="utf-8")

audit = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
text = audit.read_text(encoding="utf-8")
text = text.replace("all **nine registered works**", "all **ten registered works**")
row = "| Maruthanattu Ilavarasi / மருதநாட்டு இளவரசி | **intake + mapping complete-verified; canonical Tamil not started** | headings **2,3,4,5,6,8,9,10**; opening unnumbered; scene 7 absent | not-started | not-started |\n"
if row not in text:
    anchor = "| Vandikkaran Magan / வண்டிக்காரன் மகன் |"
    pos = text.find(anchor)
    if pos >= 0:
        text = text[:pos] + row + text[pos:]
marker = "## Maruthanattu Ilavarasi current checkpoint"
if marker not in text:
    text += f'''\n\n{marker}\n\n- source: `{SOURCE_FILE}` — **22 pages / {SOURCE_BYTES:,} bytes / SHA-256 `{SOURCE_SHA}` / image-only**;\n- source intake / structural mapping: **COMPLETE / COMPLETE-VERIFIED**;\n- body: **PDF 2–22 / logical printed 1–21**; visible printed numerals 2–21;\n- credit: **`வசனம் : மு. கருணாநிதி.`**;\n- observed numbered scene headings: **8 — 2,3,4,5,6,8,9,10**;\n- PDF 2–4 unnumbered opening; no synthetic scene 1; source `காட்சி 7.` not observed;\n- historical-glyph workflow: **required**;\n- canonical Tamil / visual fidelity / final glyph audit: **NOT STARTED / NOT STARTED / NOT STARTED**;\n- later derivatives: **BLOCKED**.\n\n**Next production phase:** {NEXT}\n'''
audit.write_text(text, encoding="utf-8")

print("MARUTHANATTU ILAVARASI INTAKE: PASS")
print("source=22 PDF / 9,330,870 bytes /", SOURCE_SHA)
print("body=PDF 2-22 / logical printed 1-21")
print("headings=2,3,4,5,6,8,9,10; scene 7 not observed; opening unnumbered")
print("canonical_tamil=not-started")
