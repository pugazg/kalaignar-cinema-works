# அம்மையப்பன்

Source-led archival work for `TVA_BOK_0064230_அம்மையப்பன்.pdf`. The rendered scan controls canonical Tamil; OCR, film audio, subtitles, web text and later editions are non-canonical.

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
- verified pages: **59**;
- open first-pass uncertainty markers: **69**;
- final bounded source batch: `transcription/parts/pdf-105-109.md`;
- final uncertainty ledger: `notes/textual-notes-pdf-105-109.md` for markers **115–116**;
- continuous assembled transcription: `transcription/full-text.md`, now through **PDF 109**;
- assembly QA: `transcription/ASSEMBLY_QA.md` — **PASS**;
- visual fidelity audit: **in-progress — PDF 5–63 / logical pp.3–61 verified (59/105); PDF 64 / logical p.62 review**.

The final batch preserves the PDF 104→105 continuation, the source-visible `வேங்கையூர்`, `நகரின் வீதி`, **`தூக்குமேடை`**, and `வெளியே` transitions, and closes the screenplay/dialogue body at PDF 109 / printed p.107. The final two insecure readings remain explicitly marked rather than reconstructed.

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

This closes only the **canonical Tamil first pass and assembly**. It does **not** upgrade any page to verified Tamil.

## Current status

| Layer | Status |
|---|---|
| Source intake | complete |
| Whole-scan inspection | complete — 111/111 |
| Structural mapping | verified intake map |
| Canonical Tamil first pass | **draft-complete — 105/105** |
| Full-text assembly | **complete — PDF 5–109** |
| Boundary loss/duplication QA | **PASS** |
| Visual fidelity audit | **in-progress — 59/105 verified + PDF 64 review** |
| Verified Tamil pages | **59/105; 1 review** |
| Scene/dialogue/character derivatives | blocked pending verified Tamil |
| Song/performance authorship gate | not-started |
| English translation / reader | blocked |

## Exact next activity

**Reopen PDF 64 / logical printed p.62 and resolve marker 47 from the rendered scan.** PDF 5–63 are verified; PDF 64 remains review. Do not advance to PDF 65 or start structured derivatives until PDF 64 is source-clean and ultimately all 105 canonical pages are verified.
