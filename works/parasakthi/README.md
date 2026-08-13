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

The detailed transcription and visual audit confirm **46 visible scene headings**. Only `காட்சி-23` and `காட்சி-34` were not observed.

The booklet contains a documented scene-number transposition near the end:

- on PDF 49 / printed p.48 it prints `காட்சி-48`, where the sequence requires **`காட்சி-43`**;
- on PDF 57 / printed p.56 it prints `காட்சி-43`, although this is the final **`காட்சி-48`** after scenes 46 and 47.

The visible canonical transcription corrects those two headings to **43** and **48** respectively. The booklet's printed readings are retained in inline provenance comments and in [`mapping.md`](mapping.md), so the correction is explicit rather than silent.

## Current state

- Structural mapping: **verified**
- Canonical Tamil transcription: **complete and verified** for PDF 4–57 / printed pp. 3–56
- Full canonical visual fidelity audit: **complete**
- Part 01: **32 verified / 0 review**
- Part 02: **22 verified / 0 review**
- Total canonical page status: **54 verified / 0 review**
- Remaining source uncertainties: **none**
- Remaining canonical uncertainty markers: **0**
- The final Part 01 readings were resolved as `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?` on PDF 5 and `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...` on PDF 16
- Part 02's six first-pass uncertainty markers were resolved from the scan and applied
- Nine materially corrupted Part 02 blocks were retranscribed directly from the scan during consolidated application
- A post-rewrite enlarged visual check corrected remaining Part 02 source-form issues before the final durable checkpoint
- Audit ledger: [`notes/fidelity-audit.md`](notes/fidelity-audit.md)
- Structured scene index: **complete — 46 records**
- Individual scene-text derivatives: **complete — 46/46 observed scenes**
- Dialogue index: **pilot verified — 42 records across scenes 1–2**
- Character index: **not-started**
- Per-song authorship mapping: **not-started**
- English translation: **not-started; the verified Tamil source is ready for derivative translation work**

## Canonical transcription

[`transcription/full-text.md`](transcription/full-text.md) is the canonical manifest. The page-order transcription is preserved in two parts:

- [`transcription/parts/part-01-pdf-4-35.md`](transcription/parts/part-01-pdf-4-35.md) — PDF 4–35 / printed pp. 3–34; audited and fully verified
- [`transcription/parts/part-02-pdf-36-57.md`](transcription/parts/part-02-pdf-36-57.md) — PDF 36–57 / printed pp. 35–56; audited, consolidated and post-rewrite verified, plus the PDF 58 back-matter provenance note

The scan controls the textual transcription. Film audio/subtitles, later editions, web quotations, or memory are not used to repair unreadable source text.

## Structured derivatives

The repository is in the post-verification **structured derivatives** stage defined in `docs/ARCHIVAL_WORKFLOW.md`.

[`scenes/index.json`](scenes/index.json) records all **46 observed canonical scenes**, their starting PDF/printed page, canonical part, intended scene-file name, and—where required—the booklet's different printed heading.

[`scenes/README.md`](scenes/README.md) defines the scene-derivative rules. In particular:

- scenes 23 and 34 are not invented because no such headings are observed in the source;
- canonical scene 43 retains source heading 48 as provenance;
- canonical scene 48 retains source heading 43 as provenance;
- derivative scene files copy only from the verified canonical Tamil and retain page anchors;
- a scene boundary follows the next observed scene heading, not an artificial transcription-part boundary.

Five scene extraction batches are complete, covering all **46 / 46 observed scene files**.

### Scene 30 cross-part continuity

Scene 30 begins on PDF 35 / printed p.34 in Part 01 but continues onto PDF 36 / printed p.35, which is stored in the Part 02 canonical file. `scenes/scene-30.md` includes that verified continuation and ends immediately before scene 31 begins on PDF 37. This is intentional and preserves the actual source scene boundary.

### Scene 33 and the absent scene 34

Scene 33 begins on PDF 38 / printed p.37 and continues across PDF 39, 40, 41 and 42. Because no `காட்சி—34` heading is observed, `scenes/scene-33.md` continues uninterrupted until immediately before `காட்சி—35` on PDF 42. No synthetic scene 34 is created.

### Corrected late scene derivatives

- `scenes/scene-43.md` is canonical scene **43** beginning on PDF 49 / printed p.48, while its provenance records that the booklet prints source heading **48**.
- `scenes/scene-48.md` is canonical final scene **48** beginning on PDF 57 / printed p.56, while its provenance records that the booklet prints source heading **43**.
- `scene-48.md` ends with `—சுபம்—` and the printer line and excludes PDF 58 rear advertisement/back matter.

## Dialogue index

[`dialogues/README.md`](dialogues/README.md) and [`dialogues/schema.json`](dialogues/schema.json) define the deterministic dialogue-record layer. [`dialogues/index.json`](dialogues/index.json) currently contains the verified pilot for **scenes 1–2: 42 dialogue records**.

The pilot confirms these rules:

- exact speaker labels are preserved without expansion or normalization;
- only speaker-labelled utterances become dialogue records;
- unlabelled songs and standalone stage directions remain excluded;
- parenthetical text inside a speaker-labelled utterance remains part of the dialogue text;
- a dialogue utterance crossing a page boundary remains one record with all page provenance retained;
- scene 43 / 48 source-heading differences will be carried forward when those scenes are indexed.

The first cross-page record is `parasakthi-s001-d001`: the `தங்கப்பன்` utterance spans PDF 4 / printed p.3 and PDF 5 / printed p.4 and is represented as one dialogue record with two page segments.

## Next dialogue batch

Extract and verify dialogue records for **canonical scenes 3–10** using the fixed pilot schema. Do not modify the schema unless a genuinely new source structure requires a documented change.
