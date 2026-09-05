# Project handover — அம்மையப்பன்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/ammaiyappan/`

## Live-main rule

Treat live GitHub `main` and the rendered controlling scan as authoritative over copied checkpoints. Preserve newer durable work; do not reset or repeat completed phases because an older prompt says otherwise.

## Mandatory startup

Before changing this work, read completely:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
3. `docs/ARCHIVAL_WORKFLOW.md`
4. `docs/SOURCE_POLICY.md`
5. `docs/TRANSCRIPTION_GUIDE.md`
6. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
7. `docs/STATUS_CONSISTENCY_AUDIT.md`
8. `works/ammaiyappan/README.md`
9. `works/ammaiyappan/metadata.yaml`
10. `works/ammaiyappan/mapping.md`
11. `works/ammaiyappan/notes/INTAKE_AUDIT.md`
12. `works/ammaiyappan/notes/scene-heading-audit.md`
13. `works/ammaiyappan/notes/historical-glyph-audit.md`
14. `works/ammaiyappan/notes/historical-glyph-sync-manifest.json`
15. `works/ammaiyappan/notes/historical-glyph-sync-report.json`
16. `works/ammaiyappan/transcription/README.md`
17. `works/ammaiyappan/transcription/index.json`
18. `works/ammaiyappan/transcription/full-text.md`
19. `works/ammaiyappan/transcription/ASSEMBLY_QA.md`
20. every bounded part retained by `transcription/index.json`
21. `works/ammaiyappan/notes/textual-notes.md`
22. every supplemental uncertainty ledger listed by `transcription/index.json`.

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
- state: **draft-complete**;
- continuous transcription: `transcription/full-text.md` assembled through **PDF 109**;
- assembly QA: `transcription/ASSEMBLY_QA.md` — **PASS**;
- open uncertainty markers: **29**;
- final part: `transcription/parts/pdf-105-109.md`;
- final ledger: `notes/textual-notes-pdf-105-109.md` for markers **115–116**.

The final PDF 105–109 batch preserves the PDF 104→105 continuation and the source-visible transitions `வேங்கையூர்`, `நகரின் வீதி`, locked `தூக்குமேடை`, and `வெளியே`. Two final insecure readings remain visibly marked rather than reconstructed.

## Dual verification gate — CLOSED

A page is final Tamil verified only when **visual fidelity = pass** and **historical glyph audit = pass**.

Final durable checkpoint:

- visual-fidelity passed: **105/105 — PDF 5–109 / logical pp.3–107**;
- historical-glyph passed: **105/105 — PDF 5–109 / logical pp.3–107**;
- final dual-gate Tamil verified: **105/105**;
- review pages: **0**;
- canonical uncertainty markers: **0**;
- final verification commit: `8e8aef9a91dd6222944f81a8d1071f78ecfc5ca3`;
- PDF 95–104 report: `notes/dual-gate-sync-report-pdf-095-104.json` — **10/10 PASS**;
- PDF 105–109 report: `notes/dual-gate-sync-report-pdf-105-109.json` — **5/5 PASS**;
- final canonical range: **PDF 5–109 / logical pp.3–107**.

The retrospective PDF 5–74 historical-glyph backfill and its occurrence-specific synchronization remain part of the audit history. Forward combined verification then closed PDF 75–109. No global historical-glyph replacement was used.

## Phase gates

- source intake: complete;
- whole-scan inspection: complete 111/111;
- structural intake map: verified;
- canonical Tamil first pass: **complete — 105/105**;
- full-text assembly: **complete-pass**;
- boundary loss/duplication QA: **PASS**;
- visual fidelity audit: **complete — 105/105**;
- historical Tamil glyph audit: **complete — 105/105**;
- final dual-gate Tamil verification: **complete-verified — 105/105**;
- scene-text derivatives: **READY — next phase**;
- dialogue index: blocked pending scene-text derivative closure;
- character index: blocked pending dialogue-index closure;
- song/performance authorship gate: not-started;
- English / reader: blocked by derivative gate order.

## Exact next activity

> **Begin scene-text derivatives from `transcription/full-text.md`. Use `notes/scene-heading-audit.md` as the structural transition ledger, assign archive-only navigation IDs because the booklet prints no scene numbers, preserve all page anchors and exact source text, and run boundary-ownership QA before opening the dialogue-index phase.**
