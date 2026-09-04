# அம்மையப்பன்

Source-led archival work for the supplied screenplay/dialogue booklet `TVA_BOK_0064230_அம்மையப்பன்.pdf`.

The rendered scan is the controlling source for this edition. The PDF is image-only; any OCR or automated text extraction is navigation-only and never canonical.

## Source checkpoint

- source title: `அம்மையப்பன்`;
- printed credit: `கதை வசனம்` / `மு. கருணாநிதி`;
- source identifier from supplied archive filename: `TVA_BOK_0064230`;
- PDF pages: **111**;
- byte size: **154,237,539**;
- SHA-256: `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`;
- publisher: `முரசொலி பதிப்பகம்`, `சென்னை-14`;
- rights line: `[ உரிமை பதிவு செய்யப் பட்டிருக்கிறது ]`;
- edition statement: `முதற் பதிப்பு` / `செப்டம்பர், 1954`;
- price: `விலை எட்டணா`;
- printer line: `முரசொலி அச்சகம். 62 எஸ். பி. சன்னதி தெரு. ராயப்பேட்டை, சென்னை 14.`

## Source structure

- PDF 1: illustrated front cover;
- PDF 2: largely blank verso with a later donor/library label at the bottom; excluded from canonical work text;
- PDF 3: title / author / rights / publisher page;
- PDF 4: first-edition month/year, price and printer imprint;
- PDF 5–109: main screenplay/dialogue body;
- PDF 110–111: unrelated advertisement/back matter; excluded from canonical screenplay text.

The continuous interior pagination supports **logical printed page = PDF page - 2** for PDF 5–109. PDF 5 is therefore logical printed p.3 although its folio is suppressed; PDF 6 visibly carries printed p.4 and PDF 109 printed p.107.

The booklet prints **no numbered scene sequence**. Instead it uses unnumbered location/transition headings, bracketed/parenthetical stage action, continuous dialogue and temporal/location transitions. The whole-scan audit records **58 source-visible structural heading/transition occurrences across 37 distinct printed forms**. These are evidence for later archival segmentation only; they are not source scene numbers.

The detailed occurrence ledger is `notes/scene-heading-audit.md`. The source map is `mapping.md`.

## Canonical Tamil first pass — in progress

- canonical range: **PDF 5–109 / 105 pages**;
- first-pass complete: **PDF 5–54 / logical pp.3–52 — 50/105 pages**;
- current completed-page state: **draft**;
- verified pages: **0**;
- current first-pass uncertainty markers: **39**, documented in `notes/textual-notes.md`;
- next page: **PDF 55 / printed p.53**;
- separate visual fidelity audit: **not-started**.

`transcription/index.json` is the active first-pass progress/assembly authority. `transcription/full-text.md` currently holds the continuous draft through PDF 14; bounded continuation parts hold PDF 15–24, PDF 25–34, PDF 35–44 and PDF 45–54. These parts must be assembled into `full-text.md` before the whole first pass is closed.

The PDF 35–44 batch received a direct scan reconciliation after its initial draft. In particular, source-visible `தனபதி` labels were restored where the first draft had misread them as `தளபதி`; unresolved old-type spans remain marked instead of being repaired from context. The PDF 45–54 batch continues the same source-first uncertainty policy and adds fifteen marked spans for later glyph-level adjudication.

## Current status

| Layer | Status |
|---|---|
| Duplicate-work check | complete — no existing Ammayappan work found on live `main` |
| Source intake | complete |
| Whole-scan inspection | complete — 111/111 pages |
| Structural mapping | **verified** |
| Source-numbered scenes | not applicable — none printed |
| Canonical Tamil first pass | **draft-in-progress — 50/105 pages** |
| Visual fidelity audit | not-started |
| Scene-text derivatives | blocked pending verified Tamil |
| Dialogue index | blocked pending verified Tamil |
| Character/entity index | blocked |
| Song/performance authorship gate | not-started |
| English translation | blocked |
| Reader/export | blocked |

## Source-authority safeguards

- Do not silently modernize or normalize historical/colloquial Tamil.
- Preserve exact printed speaker labels, punctuation, ellipses, repetition and stage directions.
- Do not manufacture source scene numbers.
- Do not infer song lyric authorship from the film-level `கதை வசனம்` / `மு. கருணாநிதி` credit.
- User-reviewed scan verdicts control their reviewed occurrences unless later direct scan evidence reopens them.
- PDF 107 / printed p.105 heading is **`தூக்குமேடை`**; the rejected provisional reading `தாக்குமேடை` must not reappear.

## Exact next activity

**Continue canonical Tamil first-pass transcription from PDF 55 / printed p.53 in a meaningful source-order batch with stable page anchors. Preserve uncertain old-type readings visibly rather than guessing. Do not begin scene/dialogue derivatives until the complete first pass has been assembled and is followed by a separate full visual fidelity audit.**
