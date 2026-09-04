# மந்திரி குமாரி

Source-led archival work for the supplied film booklet **`மந்திரி குமாரி`**.

This source is **not a full screenplay/dialogue book**. It is a compact film booklet containing production/cast credits, a prose `கதைச்சுருக்கம்`, and a substantial printed song/performance section. It is archived according to the structures the booklet actually prints rather than forced into a scene-based screenplay model.

## Source

- source/archive identifier from supplied filename: `TVA_BOK_0026144`;
- supplied filename: `TVA_BOK_0026144_மந்திரி_குமாரி.pdf`;
- physical PDF pages: **14**;
- byte size: **579,782**;
- SHA-256: `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`;
- scan: **image-only**; rendered page images control all transcription;
- cover title: **`மந்திரி குமாரி`** under the printed `மாடர்ன் தியேட்டர்ஸ்` studio line;
- printed Kalaignar credit on PDF 2: **`கதை, வசனம் : மு. கருணாநிதி`**;
- no explicit publication year or edition statement was observed in this scan.

PDF creation metadata is scan metadata only and is not used as publication evidence.

## Structural checkpoint

- PDF 1: illustrated cover;
- PDF 2: cast, dance, music/playback and production credits;
- PDF 3–5: **`"மந்திரி குமாரி"—கதைச்சுருக்கம்`** — continuous prose story summary;
- PDF 6–13: **`மந்திரி குமாரி—பாடல்கள்`** — **15** separately headed song/performance blocks, including dance, chorus, character-pair and `தொகையறா`/`பாட்டு` structures;
- PDF 14: unrelated back-cover advertisement for **`அமரகவி`** — preserved as paratext/source evidence and excluded from canonical `மந்திரி குமாரி` work text.

There is **no source scene-numbering system** and this booklet does not provide a full dialogue screenplay. Do not manufacture `scenes/` or a film-wide dialogue index from the prose synopsis.

See `mapping.md` for the whole-source map and the exact 15-block heading sequence.

## Canonical Tamil checkpoint

Canonical source-order Tamil for PDF **2–13** is stored in:

`transcription/full-text.md`

Current source status:

- canonical Tamil first pass: **complete — PDF 2–13**;
- visual fidelity audit: **complete-verified — 12/12 canonical PDF pages**;
- canonical page anchors: **12/12 verified**;
- unresolved canonical readings: **0**;
- post-fidelity user scan review: **recorded and applied**;
- later user-approved lexical/spelling campaign across the song/performance section: **applied and reconciled**;
- source subdivision form: **`தொகையறா`** wherever printed/applicable in this work.

The initial audit history is retained in `notes/fidelity-audit.md`. Subsequent source-reviewed corrections are recorded in `notes/post-fidelity-corrections.md`. These later corrections refine verified canonical readings; they do not authorize normalization from OCR, film audio, web text or the later anthology.

## Source-derived layers

### Credits

`credits/credits.yaml` is **complete-verified from PDF 2** for the source-supported credit boundary:

- `கதை, வசனம் : மு. கருணாநிதி` — primary-source verified for story/dialogue;
- item-level lyric authorship — **not assigned from the film-wide credit**.

### Story summary

The continuous PDF **3–5** prose `கதைச்சுருக்கம்` derivative is **complete-verified**.

- derivative text: `story-summary/full-text.md`;
- machine index: `story-summary/index.json`;
- source PDF pages represented: **3/3**;
- continuous story-summary records: **1** — `manthiri-kumari-story-summary-001`;
- synthetic screenplay scene IDs created: **0**;
- immutable dialogue IDs created from synopsis speech: **0**;
- canonical Tamil beneath it: **verified and unchanged by derivative creation**.

### Songs / performances

The PDF **6–13** source-linked performance layer is now **complete-verified**.

- performance inventory: **15/15 classified**;
- structured-record schema: `songs/schema.json`;
- machine index: `songs/index.json`;
- source-linked records: **15/15 complete** — `songs/records/001.json` through `015.json`;
- source PDF pages represented: **8/8 — PDF 6–13**;
- missing / duplicate record IDs: **0 / 0**;
- exact heading reconciliation: **complete**;
- `தொகையறா` / `பாட்டு` subdivisions and source-visible speaker/performance cues: **preserved in the records**;
- later-anthology cross-witness classification: **complete**;
- confirmed existing anthology witness: **1/15** — record 011 `மாட்டுக்கார பையன்` ↔ `kalaignar-song-001` / `ஊருக்கு உழைப்பவண்டி`;
- source-only blocks in the current 54-song anthology corpus: **14/15**;
- duplicate parent anthology records created: **0**;
- existing parent anthology lyrics modified: **0**;
- block-11 line-level witness report: **complete-reconciled**;
- booklet item-level lyricist credits: **0/15**;
- item-level lyric authorship at this evidence tier: **15/15 unresolved**;
- canonical Tamil changed by structured-record creation: **no**;
- synthetic screenplay scene IDs created: **0**.

`source-only` means only that no corresponding record is present in the current anthology corpus; it is not a positive or negative lyric-authorship verdict.

The booklet-level authorship gate is complete at its available evidence tier. Future item-level authorship research may still upgrade individual records if independently supported; unresolved authorship does not block translation.

## Current status

- duplicate-work check: **complete**;
- source intake: **complete**;
- whole-scan inspection: **complete, 14/14 pages**;
- structural mapping: **verified**;
- canonical Tamil: **complete-verified, PDF 2–13**;
- visual fidelity audit: **complete**;
- post-fidelity correction reconciliation: **complete**;
- credits/cast derivative: **complete-verified**;
- story-summary derivative: **complete-verified — 1 continuous record / 3 source pages**;
- song/performance structured layer: **complete-verified — 15/15 records / PDF 6–13**;
- song cross-witness comparison: **complete**;
- song booklet-evidence authorship gate: **complete — 15/15 unresolved item-level lyricists**;
- scene/dialogue derivatives: **not applicable from this source as a full-work model**;
- English translation: **ready / not-started**;
- reader/export and Reading Room integration: **blocked pending English translation**.

## Exact next activity

> **Begin source-linked English translation from the completed verified source structures: the continuous PDF 3–5 story-summary record and the 15 PDF 6–13 song/performance records. Preserve source order, page provenance, performance/speaker cues, `தொகையறா` / `பாட்டு` distinctions and unresolved item-level lyric authorship. Do not convert this booklet into screenplay scenes, and do not use translation to repair canonical Tamil.**
