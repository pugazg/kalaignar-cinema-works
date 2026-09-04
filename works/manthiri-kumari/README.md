# மந்திரி குமாரி

Source-led archival work for the supplied film booklet **`மந்திரி குமாரி`**.

This source is **not a full screenplay/dialogue book**. It is a compact film booklet containing production/cast credits, a prose `கதைச்சுருக்கம்`, and a substantial printed song/performance section. It is archived according to the structures the booklet actually prints rather than forced into a scene-based screenplay model.

## Source

- source/archive identifier: `TVA_BOK_0026144`;
- supplied filename: `TVA_BOK_0026144_மந்திரி_குமாரி.pdf`;
- physical PDF pages: **14**;
- byte size: **579,782**;
- SHA-256: `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`;
- scan: **image-only**; rendered page images control all transcription;
- cover title: **`மந்திரி குமாரி`** under `மாடர்ன் தியேட்டர்ஸ்`;
- printed Kalaignar credit on PDF 2: **`கதை, வசனம் : மு. கருணாநிதி`**;
- no explicit publication year or edition statement was observed.

## Natural source structure

- PDF 1: illustrated cover;
- PDF 2: cast/music/production credits;
- PDF 3–5: continuous **`"மந்திரி குமாரி"—கதைச்சுருக்கம்`**;
- PDF 6–13: **`மந்திரி குமாரி—பாடல்கள்`** — **15** separately headed song/performance blocks;
- PDF 14: unrelated `அமரகவி` advertisement / paratext.

There is **no source scene-numbering system** and this booklet does not provide a full dialogue screenplay. Do not manufacture screenplay scenes or a film-wide dialogue index from it.

## Canonical Tamil

Canonical Tamil for PDF **2–13** is `transcription/full-text.md`.

- first pass: **complete**;
- visual fidelity audit: **complete-verified — 12/12 canonical PDF pages**;
- unresolved readings: **0**;
- direct user post-fidelity scan corrections: **recorded, applied and reconciled**;
- later user-approved lexical/spelling corrections: **applied and reconciled**;
- source subdivision form: **`தொகையறா`** where printed/applicable.

Correction history is preserved in `notes/fidelity-audit.md` and `notes/post-fidelity-corrections.md`.

## Source-derived Tamil layers

- credits: `credits/credits.yaml` — **complete-verified**;
- story summary: `story-summary/full-text.md` + `story-summary/index.json` — **1/1 continuous record, PDF 3–5**;
- song/performance records: `songs/records/001.json`–`015.json` — **15/15 complete-verified, PDF 6–13**;
- synthetic screenplay scene IDs: **0**;
- immutable dialogue IDs manufactured from synopsis speech: **0**.

### Authorship / cross-witness boundary

The printed `கதை, வசனம் : மு. கருணாநிதி` is primary-source evidence for story/dialogue credit only.

- booklet item-level lyricists verified: **0/15**;
- item-level lyricists unresolved: **15/15**;
- confirmed current-anthology witness: **1/15** — block 11 `மாட்டுக்கார பையன்` ↔ `kalaignar-song-001`;
- source-only against the current anthology: **14/15**;
- later anthology used to repair this booklet: **no**.

## English translation

The source-linked English layer under `translations/` is **complete-verified — QA PASS**.

- story summary: **1/1**, **13** logical prose units, **1** cross-page unit;
- performances: **15/15**;
- performance sections: **52**;
- Tamil / English performance lines-cues: **234 / 234**;
- mapping mismatches: **0**;
- cross-page performance records: **7** — `002`, `004`, `006`, `007`, `009`, `011`, `013`;
- authorship upgrades: **0**;
- canonical Tamil changed: **no**;
- synthetic screenplay scenes: **0**.

Performance 13 retains the evidence distinction between the printed heading `பார்த்திபன்—மந்திரிகுமாரி` and internal turn labels `பார்த்திபன்` / `அமுதவல்லி`.

## Bilingual reader/export

`editions/bilingual/` is **complete-verified — QA PASS**.

- navigation: **1 story summary + 15 performance blocks**;
- top-level source structures: **16/16**;
- story-summary logical units: **13/13**;
- performance sections: **52/52**;
- Tamil / English performance line-cues: **234 / 234**;
- mapping mismatches: **0**;
- cross-page performance records retained: **7/7**;
- item-level lyric authorship retained: **0 verified / 15 unresolved**;
- synthetic screenplay scenes: **0**;
- canonical Tamil changed: **no**.

The reader is source-linked to verified translation records and does not become a competing textual authority.

## Reading Room integration payload

`integrations/reading-room/` is now **payload-complete-verified — QA PASS**.

- payload: `integrations/reading-room/reading-room.json`;
- payload mode: **`source-linked-composition`**;
- payload validator: `integrations/reading-room/build.py`;
- QA report: `integrations/reading-room/QA_REPORT.md`;
- manifest: `integrations/reading-room/manifest.json`;
- expected source-link targets: **32** — 16 Tamil/source + 16 English translation records;
- story-summary units represented: **13**;
- performance blocks / sections / line-cues: **15 / 52 / 234**;
- payload bytes: **15,704**;
- payload SHA-256: `20a0db293b936757e7d01def336252f28543337f319dfae6ad7bf5ae886bab43`;
- current-anthology disposition preserved: **1 confirmed / 14 source-only**;
- item-level lyricists preserved: **0 verified / 15 unresolved**;
- synthetic screenplay scenes: **0**;
- canonical Tamil changes: **0**;
- authorship upgrades: **0**;
- site application: **not-applied**.

The payload does **not** deploy or modify the separate public Reading Room implementation repository.

## Current status

- source intake / whole-scan inspection / structural mapping: **complete / verified**;
- canonical Tamil: **complete-verified**;
- credits/story-summary/performance Tamil derivatives: **complete-verified**;
- English translation: **complete-verified**;
- bilingual reader/export: **complete-verified — QA PASS**;
- Reading Room integration payload: **payload-complete-verified — QA PASS**;
- Reading Room site application: **not-applied**;
- screenplay scene/dialogue full-work derivatives: **not applicable**.

## Next activity / disposition

> **No required repository-internal Manthiri Kumari transcription, translation, reader/export, or Reading Room-payload work remains. Apply the verified source-linked payload in the separate Reading Room implementation repository only when that repository is explicitly authorized for modification. Preserve the natural story-summary + 15-performance navigation and all evidence tiers.**
