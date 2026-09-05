# அம்மையப்பன்

Source-led archival work for `TVA_BOK_0064230_அம்மையப்பன்.pdf`. The rendered scan controls canonical Tamil; OCR, film audio, subtitles, web text and later editions are non-canonical.

Because this 1954 source contains frequent historical Tamil typeforms, canonical Tamil now requires **two independent verification gates**:

1. complete visual source-fidelity comparison; and
2. historical-Tamil-glyph verification under `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.

A page is final Tamil verified only when both gates pass. Work-level tracking is in `notes/historical-glyph-audit.md`.

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
- visual-fidelity-passed pages: **70/105**;
- historical-glyph-cleared pages under the explicit new gate: **0/105** at gate introduction;
- final dual-gate Tamil verified pages: **0/105** at gate introduction;
- open first-pass uncertainty markers: **29**;
- final bounded source batch: `transcription/parts/pdf-105-109.md`;
- final uncertainty ledger: `notes/textual-notes-pdf-105-109.md` for markers **115–116**;
- continuous assembled transcription: `transcription/full-text.md`, now through **PDF 109**;
- assembly QA: `transcription/ASSEMBLY_QA.md` — **PASS**;
- visual fidelity audit: **in-progress — PDF 5–74 / logical pp.3–72 passed (70/105)**;
- historical Tamil glyph audit: **required for all 105 canonical pages**.

The existing PDF 5–74 visual-fidelity result remains valid as visual evidence, but those 70 pages require a retrospective historical-glyph pass before they can be considered final Tamil verified. For PDF 75–109, visual fidelity and historical-glyph verification must be performed together.

The final batch preserves the PDF 104→105 continuation, the source-visible `வேங்கையூர்`, `நகரின் வீதி`, **`தூக்குமேடை`**, and `வெளியே` transitions, and closes the screenplay/dialogue body at PDF 109 / printed p.107. The final two insecure readings remain explicitly marked rather than reconstructed.

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

This closes only the **canonical Tamil first pass and assembly**. It does **not** close the dual verification gate.

## Current status

| Layer | Status |
|---|---|
| Source intake | complete |
| Whole-scan inspection | complete — 111/111 |
| Structural mapping | verified intake map |
| Canonical Tamil first pass | **draft-complete — 105/105** |
| Full-text assembly | **complete — PDF 5–109** |
| Boundary loss/duplication QA | **PASS** |
| Visual fidelity audit | **in-progress — 70/105 passed** |
| Historical Tamil glyph audit | **required — 0/105 formally cleared at gate introduction** |
| Final dual-gate Tamil verification | **0/105 at gate introduction** |
| PDF 5–74 | visual-pass / glyph-pending — retrospective glyph backfill required |
| PDF 75–109 | visual-pending / glyph-pending — run both together |
| Scene/dialogue/character derivatives | blocked pending dual-gate verified Tamil |
| Song/performance authorship gate | not-started |
| English translation / reader | blocked |

## Exact next activity

**Continue at PDF 75 / logical printed p.73, but from this point every rendered-scan visual fidelity check must simultaneously perform the full historical-Tamil-glyph audit.** Adjudicate markers 88–116 occurrence-by-occurrence and inspect the complete known historical family set on every page. Before Tamil closure, perform the mandatory retrospective historical-glyph backfill for PDF 5–74. No structured derivative or English/reader work may treat the Tamil layer as verified until both gates reach **105/105**.
