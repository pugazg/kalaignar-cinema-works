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

## Canonical Tamil checkpoint

Canonical source-order Tamil for PDF **2–13** is stored in `transcription/full-text.md`.

- canonical Tamil first pass: **complete — PDF 2–13**;
- visual fidelity audit: **complete-verified — 12/12 canonical PDF pages**;
- unresolved canonical readings: **0**;
- post-fidelity user scan review: **recorded and applied**;
- later user-approved lexical/spelling campaign: **applied and reconciled**;
- source subdivision form: **`தொகையறா`** wherever printed/applicable.

Correction history is preserved in `notes/fidelity-audit.md` and `notes/post-fidelity-corrections.md`.

## Source-derived Tamil layers

### Credits

`credits/credits.yaml` is **complete-verified from PDF 2**.

The printed `கதை, வசனம் : மு. கருணாநிதி` establishes story/dialogue credit only; it does not automatically establish lyric authorship for the performance blocks.

### Story summary

The continuous PDF **3–5** prose derivative is **complete-verified**:

- `story-summary/full-text.md`;
- `story-summary/index.json`;
- source pages: **3/3**;
- records: **1 continuous-prose record**;
- synthetic screenplay scene IDs: **0**;
- immutable dialogue IDs manufactured from synopsis speech: **0**.

### Songs / performances

The PDF **6–13** source-linked performance layer is **complete-verified**:

- `songs/schema.json`;
- `songs/index.json`;
- `songs/records/001.json` through `015.json`;
- records: **15/15**;
- source pages represented: **8/8 — PDF 6–13**;
- missing / duplicate record IDs: **0 / 0**;
- exact headings, `தொகையறா` / `பாட்டு` subdivisions and source-visible speaker/performance cues: **preserved**;
- current-anthology witness: **1/15** — block 11 `மாட்டுக்கார பையன்` ↔ `kalaignar-song-001`;
- source-only relative to the current anthology: **14/15**;
- booklet item-level lyric authorship: **0 verified / 15 unresolved**;
- canonical Tamil changed by record creation: **no**;
- synthetic screenplay scene IDs created: **0**.

## English translation checkpoint

The source-linked English layer under `translations/` is **complete-verified — QA PASS**.

- story-summary translation: **1/1**, **13** logical prose units, **1** cross-page unit;
- performance translation records: **15/15**;
- performance sections: **52**;
- Tamil / English performance lines-cues: **234 / 234**;
- mapping mismatches: **0**;
- cross-page translated performance records: **7** — `002`, `004`, `006`, `007`, `009`, `011`, `013`;
- authorship upgrades caused by translation: **0**;
- booklet item-level lyricist state after translation: **0 verified / 15 unresolved**;
- canonical Tamil changed by translation: **no**;
- synthetic screenplay scene IDs created: **0**.

The English layer preserves source-visible cues and structural labels rather than flattening them. Performance 13 also preserves the source mismatch between the printed heading `பார்த்திபன்—மந்திரிகுமாரி` and its internal turn labels `பார்த்திபன்` / `அமுதவல்லி`.

## Bilingual reader/export checkpoint

The deterministic source-linked reader under `editions/bilingual/` is **complete-verified — QA PASS**.

- navigation model: **story summary + 15 performance blocks**;
- top-level source structures: **16/16**;
- story-summary logical units: **13/13**;
- performance records: **15/15**;
- performance sections: **52/52**;
- Tamil / English performance line-cues: **234 / 234**;
- line-pair mismatches: **0**;
- cross-page performance records retained: **7/7**;
- current-anthology witness disposition retained: **1 confirmed / 14 source-only**;
- item-level lyric authorship retained: **0 verified / 15 unresolved**;
- synthetic screenplay scene IDs introduced: **0**;
- canonical Tamil changed by reader/export: **no**;
- reader QA: **PASS**.

Reader files:

- `editions/bilingual/reader-edition.json` — machine composition authority;
- `editions/bilingual/reader-edition.md` — human-readable source-order index;
- `editions/bilingual/reader-edition.html` — source-linked bilingual HTML renderer;
- `editions/bilingual/PREFLIGHT_QA_REPORT.md`;
- `editions/bilingual/QA_REPORT.md`;
- `editions/bilingual/manifest.json`;
- `editions/bilingual/build.py` — deterministic validation gate.

The reader remains source-linked to the verified translation records rather than creating another independent textual authority.

## Current status

- duplicate-work check: **complete**;
- source intake: **complete**;
- whole-scan inspection: **complete, 14/14 pages**;
- structural mapping: **verified**;
- canonical Tamil: **complete-verified, PDF 2–13**;
- visual fidelity audit: **complete**;
- post-fidelity correction reconciliation: **complete**;
- credits/cast derivative: **complete-verified**;
- story-summary Tamil derivative: **complete-verified**;
- song/performance structured Tamil layer: **complete-verified — 15/15**;
- song cross-witness comparison: **complete**;
- song booklet-evidence authorship gate: **complete-with-unresolved-item-authorship — 15 unresolved**;
- English translation: **complete-verified**;
- bilingual reader/export: **complete-verified — QA PASS**;
- Reading Room integration: **ready / not-started**;
- scene/dialogue full-work derivatives: **not applicable from this source**.

## Exact next activity

> **Prepare and QA a provenance-safe Reading Room integration payload from the complete-verified bilingual reader. Preserve the booklet's natural `கதைச்சுருக்கம்` + 15-performance navigation, Tamil/English pairing, source/page provenance, source-visible cues, the 1/15 current-anthology witness disposition and the 0 verified / 15 unresolved item-level lyric-authorship state. Do not invent screenplay scenes or upgrade authorship through presentation metadata.**
