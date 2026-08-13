# பராசக்தி

Archival record for the scanned booklet **`பராசக்தி — முழு வசனம் + பாடல்கள்`**.

## Source-supported identification

The title page shows `பராசக்தி`, `முழு வசனம் + பாடல்கள்`, `திரைக்கதை, வசனம்`, `கலைஞர் மு. கருணாநிதி`, and `விலை ரூபாய் 1-00.` The following credits page also prints `கதை-வசனம் — கலைஞர் மு. கருணாநிதி` and lists multiple contributors under the song/lyric credits, so individual songs are **not** attributed automatically to Kalaignar.

## Scan

- Source file: `TVA_BOK_0062968_பராசக்தி.pdf`
- PDF pages: **58**
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- Type: image-only scan
- Printed dialogue/song pagination: **3–56**, corresponding to PDF **4–57**
- PDF 58: rear advertisement / back matter

See [`mapping.md`](mapping.md) for the corrected complete structural page map.

## Scene numbering

The detailed transcription and visual audit confirm **46 visible scene headings**. `காட்சி-23` and `காட்சி-34` are not observed and are not invented.

The booklet contains a documented scene-number transposition near the end:

- PDF 49 / printed p.48 prints `காட்சி-48`, where the canonical sequence is **`காட்சி-43`**;
- PDF 57 / printed p.56 prints `காட்சி-43`, although this is the final **`காட்சி-48`** after scenes 46 and 47.

The visible canonical transcription corrects those two headings to 43 and 48 respectively while retaining the booklet readings in provenance.

## Current state

- Structural mapping: **verified**
- Canonical Tamil transcription: **complete and verified** for PDF 4–57 / printed pp.3–56
- Full canonical visual fidelity audit: **complete**
- Part 01: **32 verified / 0 review**
- Part 02: **22 verified / 0 review**
- Total canonical status: **54 verified / 0 review**
- Remaining source uncertainties: **none**
- Remaining canonical uncertainty markers: **0**
- Scene index: **complete — 46 records**
- Individual scene-text derivatives: **complete — 46/46 observed scenes**
- Dialogue index: **in progress and verified through scenes 1–10 — 117 records**
- Character index: **not-started**
- Per-song authorship mapping: **not-started**
- English translation: **not-started**

The final Part 01 readings resolved from the scan are `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?` on PDF 5 and `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...` on PDF 16.

## Canonical transcription

[`transcription/full-text.md`](transcription/full-text.md) is the canonical manifest. The page-order transcription is preserved in two parts:

- [`transcription/parts/part-01-pdf-4-35.md`](transcription/parts/part-01-pdf-4-35.md) — PDF 4–35 / printed pp.3–34; fully verified.
- [`transcription/parts/part-02-pdf-36-57.md`](transcription/parts/part-02-pdf-36-57.md) — PDF 36–57 / printed pp.35–56; audited, consolidated and post-rewrite verified, plus the PDF 58 back-matter provenance note.

The scan controls the textual transcription. Film audio/subtitles, later editions, web quotations, or memory are not used to repair source text.

## Scene derivatives

[`scenes/index.json`](scenes/index.json) records all **46 observed canonical scenes** and their PDF/printed-page provenance. [`scenes/README.md`](scenes/README.md) defines the scene-derivative rules.

Important boundaries:

- scene 30 crosses the transcription-file boundary from PDF 35 into PDF 36;
- scene 33 continues through PDF 42 because scene 34 is absent;
- canonical scene 43 records booklet source heading 48;
- canonical final scene 48 records booklet source heading 43 and ends before PDF 58 back matter.

## Dialogue index

[`dialogues/schema.json`](dialogues/schema.json) is the fixed dialogue-record schema. [`dialogues/index.json`](dialogues/index.json) is now a compact manifest/checkpoint; actual records are sharded by canonical scene under [`dialogues/records/`](dialogues/records/).

Dialogue extraction is verified through **scenes 1–10**, producing **117 records**:

- scene 1: 1
- scene 2: 41
- scene 3: 8
- scene 4: 8
- scene 5: 5
- scene 6: 19
- scene 7: 22
- scene 8: 5
- scene 9: 1
- scene 10: 7

The original scenes 1–2 pilot was migrated losslessly into `dialogues/records/scene-01.json` and `scene-02.json`; the record schema itself was not changed.

Dialogue rules remain strict:

- exact speaker labels are preserved without expansion or normalization;
- only explicitly speaker-labelled utterances become dialogue records;
- standalone stage directions and unlabelled songs remain excluded;
- parenthetical text inside a speaker-labelled utterance remains part of the dialogue;
- explicitly labelled sung/verse lines, such as scene 4's `தங்` / `கல்` / `இரு` exchange, are retained;
- a cross-page utterance stays one record with all page provenance and exact page segments.

Verified cross-page records so far are `parasakthi-s001-d001` (PDF 4→5) and `parasakthi-s009-d001` (PDF 12→13).

## Next dialogue batch

Extract and verify canonical **scenes 11–20** using the same fixed schema and scene-sharded storage.
