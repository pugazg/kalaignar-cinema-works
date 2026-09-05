# அம்மையப்பன்

Source-led archival work for `TVA_BOK_0064230_அம்மையப்பன்.pdf`. The rendered scan controls canonical Tamil; OCR, film audio, subtitles, web text and later editions are non-canonical.

Because this 1954 source contains frequent historical Tamil typeforms, canonical Tamil requires **two independent verification gates**:

1. complete visual source-fidelity comparison; and
2. historical-Tamil-glyph verification under `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.

A page is final Tamil verified only when both gates pass. Work-level tracking is in `notes/historical-glyph-audit.md`; the completed retrospective correction synchronization is recorded by `notes/historical-glyph-sync-manifest.json` and `notes/historical-glyph-sync-report.json`.

## Source checkpoint

- title: `அம்மையப்பன்`;
- printed credit: `கதை வசனம்` / `மு. கருணாநிதி`;
- PDF pages: **111**;
- source SHA-256: `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`;
- first edition: **செப்டம்பர், 1954**;
- publisher: `முரசொலி பதிப்பகம்`, `சென்னை-14`;
- main screenplay/dialogue: **PDF 5–109 / logical printed pp.3–107**;
- PDF 110–111: advertisement/back matter, excluded from canonical screenplay.

The booklet prints no numbered scene sequence. Whole-scan intake mapping records **58 structural heading/transition occurrences / 37 distinct forms**; canonical transcription additionally preserves any local source-visible heading encountered on the rendered page.

Locked source verdicts:

- PDF 56 / printed p.54: **`பழுதார் வீதி`**;
- PDF 107 / printed p.105: **`தூக்குமேடை`**; rejected reading `தாக்குமேடை` must not reappear.

## Canonical Tamil first pass — complete draft coverage

- expected canonical pages: **105**;
- completed first-pass range: **PDF 5–109 / printed pp.3–107**;
- progress: **105/105 pages**;
- first-pass state: **draft-complete**;
- continuous assembled transcription: `transcription/full-text.md`, through **PDF 109**;
- assembly QA: `transcription/ASSEMBLY_QA.md` — **PASS**;
- open first-pass uncertainty markers: **29**;
- final uncertainty ledger: `notes/textual-notes-pdf-105-109.md` for markers **115–116**.

The first-pass draft and assembly are complete, but final Tamil verification remains in progress.

## Retrospective historical-glyph backfill — CLOSED through PDF 74

The previously visual-passed PDF 5–74 range was re-inspected from the source for historical Tamil typeforms before forward verification resumed.

- retrospective source review: **PDF 5–74 = 70/70 pages complete**;
- pages requiring no historical-glyph correction: **32**;
- pages with source-established correction sets: **38**;
- correction synchronization: **complete**;
- synchronization commit: `880978627191a122f55b50522d112d163faa7e10`;
- synchronized logical occurrences across canonical/provenance surfaces: **97**;
- global replacement used: **no**;
- source whitespace/layout preserved by the synchronization pass: **yes**;
- genuine same-edition control readings preserved on PDF **48, 62, 64 and 69**: **PASS**.

The synchronization report is `notes/historical-glyph-sync-report.json`. Retained first-pass provenance was changed only where the matching audited occurrence existed; older unresolved placeholders were not silently filled from the newer canonical layer.

Therefore **PDF 5–74 / logical pp.3–72 are now dual-gate verified: 70/105 pages**.


Forward dual-gate verification through PDF 84 is recorded by commit `0da97f94e829bef9b387bf59be580933b97ed122` and `notes/dual-gate-sync-report-pdf-075-084.json`.

## Historical Tamil glyph gate

The minimum known reform-sensitive families to inspect occurrence-by-occurrence are:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

This list is a minimum, not exhaustive. Old ligatures, faint vowel marks, broken/worn type and edition-specific forms must also be inspected. Character identity must be determined from enlarged source pixels and same-edition evidence where needed; no OCR authority, semantic guessing, spelling modernization or global replacement is permitted.

## First-pass assembly QA

The continuous draft was assembled from the existing PDF 5–14 `full-text.md` plus all bounded parts from PDF 15–109. Automated boundary QA records:

- **105 / 105** page anchors present;
- exact source-anchor order **PDF 5, 6, …, 109**;
- missing anchors: **0**;
- duplicate anchors: **0**;
- bounded-part boundary presence: **PASS**;
- locked `தூக்குமேடை`: **PASS**;
- rejected `தாக்குமேடை`: **absent**;
- visible unresolved first-pass spans: **116**.

This closes only the **canonical Tamil first pass and assembly**. It does not close the remaining PDF 85–109 dual verification.

## Current status

| Layer | Status |
|---|---|
| Source intake | complete |
| Whole-scan inspection | complete — 111/111 |
| Structural mapping | verified intake map |
| Canonical Tamil first pass | **draft-complete — 105/105** |
| Full-text assembly | **complete — PDF 5–109** |
| Boundary loss/duplication QA | **PASS** |
| Visual fidelity audit | **80/105 passed — PDF 5–84** |
| Historical Tamil glyph audit | **80/105 passed — PDF 5–84** |
| Final dual-gate Tamil verification | **80/105 — PDF 5–84 closed** |
| Retrospective PDF 5–74 glyph backfill | **CLOSED — source review + synchronization complete** |
| PDF 85–109 | **25 pages pending — visual fidelity + glyph audit together** |
| Scene/dialogue/character derivatives | blocked pending 105/105 dual-gate Tamil |
| Song/performance authorship gate | not-started |
| English translation / reader | blocked |

## Exact next activity

**Resume at PDF 85 / logical printed p.83.** From PDF 85–109, perform the rendered-scan **visual source-fidelity check and the complete historical-Tamil-glyph audit together on every page**. Adjudicate markers **98–116** occurrence-by-occurrence, preserve genuine old/colloquial forms when the source proves them, and never apply global replacement. Do not start structured derivatives, English translation or reader work until both gates reach **105/105** with no unresolved review pages.
