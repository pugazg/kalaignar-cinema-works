# Project handover — அம்மையப்பன்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/ammaiyappan/`

## Live-main rule

Treat live GitHub `main` and the rendered controlling scan as authoritative over copied checkpoints. Preserve newer durable work; do not reset or repeat completed phases because an older prompt says otherwise.

## Mandatory startup

Before changing this work, read completely:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `docs/SOURCE_POLICY.md`
4. `docs/TRANSCRIPTION_GUIDE.md`
5. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
6. `docs/STATUS_CONSISTENCY_AUDIT.md`
7. `works/ammaiyappan/README.md`
8. `works/ammaiyappan/metadata.yaml`
9. `works/ammaiyappan/mapping.md`
10. `works/ammaiyappan/notes/INTAKE_AUDIT.md`
11. `works/ammaiyappan/notes/scene-heading-audit.md`
12. `works/ammaiyappan/transcription/README.md`
13. `works/ammaiyappan/transcription/index.json`
14. `works/ammaiyappan/transcription/full-text.md`
15. `works/ammaiyappan/transcription/parts/` as listed by the index
16. `works/ammaiyappan/notes/textual-notes.md`

## Controlling source

`TVA_BOK_0064230_அம்மையப்பன்.pdf`

- PDF pages: **111**;
- bytes: **154,237,539**;
- SHA-256: `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`;
- image-only scan;
- rendered scan controls canonical Tamil.

## Printed source evidence

- title: `அம்மையப்பன்`;
- credit: `கதை வசனம்` / `மு. கருணாநிதி`;
- publisher: `முரசொலி பதிப்பகம்`, `சென்னை-14`;
- rights line: `[ உரிமை பதிவு செய்யப் பட்டிருக்கிறது ]`;
- edition: `முதற் பதிப்பு`;
- publication date: `செப்டம்பர், 1954`;
- price: `விலை எட்டணா`;
- printer: `முரசொலி அச்சகம். 62 எஸ். பி. சன்னதி தெரு. ராயப்பேட்டை, சென்னை 14.`

## Source bounds

- PDF 1 cover;
- PDF 2 blank verso / donor-library label;
- PDF 3 title/author/rights/publisher;
- PDF 4 edition/date/price/printer;
- PDF 5–109 main screenplay/dialogue;
- PDF 110–111 advertisement/back matter.

Pagination: logical printed page = PDF page - 2 across PDF 5–109. PDF 5 is logical p.3 with folio suppressed; PDF 6 visibly p.4; PDF 109 visibly p.107.

## Structural map — complete

- source-numbered scenes: **none**;
- structural heading/transition occurrences: **58**;
- distinct printed forms: **37**;
- occurrence ledger: `notes/scene-heading-audit.md`;
- archive-generated scene numbers: **none at intake**.

Important adjudications:

- PDF 56 / p.54: `பழுதார் வீதி`;
- PDF 107 / p.105: **`தூக்குமேடை`** — direct user scan verdict; reject `தாக்குமேடை`.

## Canonical Tamil first pass — active

- canonical range: **PDF 5–109 / logical pp.3–107 — 105 pages**;
- completed first-pass range: **PDF 5–34 / logical pp.3–32**;
- first-pass pages completed: **30 / 105**;
- current completed-page state: **draft**;
- verified pages: **0**;
- open first-pass uncertainty markers: **19**;
- uncertainty ledger: `notes/textual-notes.md`;
- active progress/assembly authority: `transcription/index.json`;
- assembled `full-text.md` currently reaches **PDF 14**;
- bounded continuation parts: `transcription/parts/pdf-015-024.md`, `transcription/parts/pdf-025-034.md`;
- next page: **PDF 35 / printed p.33**;
- visual fidelity audit: **not-started**.

The PDF 25–34 batch preserves the source-visible transitions and speaker/action structure while keeping eight insecure old-typeface spans explicitly marked. No marked reading was repaired from context or external text.

Before declaring the entire first pass complete, assemble every bounded part into `full-text.md` in exact source order and perform boundary loss/duplication QA.

## Current phase

- source intake: **complete**;
- whole-scan inspection: **complete 111/111**;
- structural mapping: **verified**;
- canonical Tamil first pass: **draft-in-progress — 30/105**;
- visual fidelity audit: **not-started**;
- scene/dialogue/character derivatives: **blocked pending verified Tamil**;
- song/performance authorship gate: **not-started**;
- English translation / reader: **blocked**.

## Source-authority boundaries

- Do not silently normalize old spelling or grammar.
- Preserve exact speaker labels, stage directions, punctuation, repetitions and source transitions.
- OCR/audio/subtitles/web/later editions cannot repair canonical Tamil.
- Story/dialogue credit is not item-level lyric credit.
- User-reviewed scan verdicts control their reviewed occurrences unless direct scan evidence explicitly reopens them.
- Do not resolve the current uncertainty markers by semantic expectation; enlarge the scan during the later fidelity review.

## Exact next activity

> **Continue canonical Tamil first-pass transcription at PDF 35 / printed p.33. Work in a meaningful source-order batch with stable PDF/printed-page anchors. Store later batches in bounded part files and keep `transcription/index.json` authoritative for coverage until final assembly. Do not start scene/dialogue derivatives yet. After the entire PDF 5–109 first pass is assembled, perform a separate full rendered-scan visual fidelity audit before structured derivatives.**
