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
15. `works/ammaiyappan/transcription/ASSEMBLY_QA.md`
16. every bounded part retained by `transcription/index.json`
17. `works/ammaiyappan/notes/textual-notes.md`
18. every supplemental uncertainty ledger listed by `transcription/index.json`.

## Controlling source

`TVA_BOK_0064230_அம்மையப்பன்.pdf`

- PDF pages: **111**;
- bytes: **154,237,539**;
- SHA-256: `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`;
- image-only scan;
- main screenplay/dialogue: **PDF 5–109 / logical printed pp.3–107**;
- PDF 110–111: advertisement/back matter.

Printed identity: `அம்மையப்பன்`; `கதை வசனம்` / `மு. கருணாநிதி`; `முதற் பதிப்பு`, `செப்டம்பர், 1954`; `முரசொலி பதிப்பகம்`, `சென்னை-14`.

## Structural/source locks

- source-numbered scenes: **none**;
- intake structural heading/transition occurrences: **58 / 37 distinct forms**;
- preserve additional source-visible local headings found during transcription even if the intake ledger is narrower;
- PDF 56 / p.54: **`பழுதார் வீதி`**;
- PDF 107 / p.105: **`தூக்குமேடை`** — direct user verdict; reject `தாக்குமேடை`.

## Canonical Tamil first pass — closed as draft coverage

- expected canonical pages: **105**;
- completed: **105/105**;
- completed range: **PDF 5–109 / printed pp.3–107**;
- state: **draft-complete**, verified pages **0**;
- open uncertainty markers: **116**;
- final part: `transcription/parts/pdf-105-109.md`;
- final ledger: `notes/textual-notes-pdf-105-109.md` for markers **115–116**;
- continuous transcription: `transcription/full-text.md` assembled through **PDF 109**;
- assembly QA: `transcription/ASSEMBLY_QA.md` — **PASS**;
- visual fidelity audit: **not-started**.

The final PDF 105–109 batch preserves the PDF 104→105 continuation and the source-visible transitions `வேங்கையூர்`, `நகரின் வீதி`, locked `தூக்குமேடை`, and `வெளியே`. Two final insecure readings remain visibly marked rather than reconstructed.

The earlier PDF 65–74 batch remains `draft-high-uncertainty`; no uncertainty marker is verified merely by being carried into the assembled draft.

## Assembly QA — PASS

- source anchors: **105**;
- exact anchor sequence: **PDF 5 through PDF 109**;
- missing anchors: **0**;
- duplicate anchors: **0**;
- bounded-part boundary presence: **PASS**;
- locked PDF 107 `தூக்குமேடை`: **PASS**;
- rejected `தாக்குமேடை`: **absent**;
- visible unresolved spans in assembled text: **116**.

This closes the **first-pass transcription + assembly gate only**. It is not a source-fidelity verification.

## Phase gates

- source intake: complete;
- whole-scan inspection: complete 111/111;
- structural intake map: verified;
- canonical Tamil first pass: **draft-complete — 105/105**;
- full-text assembly: **complete-pass**;
- boundary loss/duplication QA: **PASS**;
- visual fidelity audit: **not-started — 0/105 verified**;
- scene/dialogue/character derivatives: blocked pending verified Tamil;
- song/performance authorship gate: not-started;
- English / reader: blocked.

## Exact next activity

> **Begin the separate rendered-scan visual fidelity audit at PDF 5 / logical printed p.3 and proceed in source order through PDF 109. Compare every page of `transcription/full-text.md` directly with the controlling scan, adjudicate all 116 explicit uncertainty markers occurrence-by-occurrence, preserve the locked source verdicts, and upgrade pages to verified only after direct page-level visual comparison. Do not start scene/dialogue/character derivatives until all 105 canonical pages pass the audit.**
