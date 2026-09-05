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

## Dual verification gate — current checkpoint

A page is final Tamil verified only when **visual fidelity = pass** and **historical glyph audit = pass**.

Current durable checkpoint:

- visual-fidelity passed: **80/105 — PDF 5–84 / logical pp.3–72**;
- historical-glyph passed: **80/105 — PDF 5–84 / logical pp.3–72**;
- final dual-gate Tamil verified: **70/105**;
- remaining range: **PDF 85–109 = 35 pages**;
- next source page: **PDF 75 / logical printed p.73**.

### Retrospective PDF 5–74 historical-glyph backfill — CLOSED

The PDF 5–74 range had already passed visual fidelity before the explicit historical-glyph gate was introduced. That entire 70-page range was therefore re-inspected from the rendered scan for historical Tamil typeforms.

- source review: **70/70 complete**;
- correction-free pages: **32**;
- correction-bearing pages: **38**;
- occurrence-specific synchronization: **complete**;
- synchronization commit: `880978627191a122f55b50522d112d163faa7e10`;
- sync report: `notes/historical-glyph-sync-report.json`;
- synchronized logical occurrences across canonical/provenance surfaces: **97**;
- global replacement: **not used**;
- source whitespace/layout: **preserved**;
- genuine same-edition control readings on PDF **48, 62, 64 and 69**: **preserved / PASS**;
- retrospective sync-pending pages: **0**.

Retained first-pass provenance files were synchronized only where the audited phrase actually existed. Older unresolved placeholder passages were not silently filled from the newer canonical layer.


Forward dual-gate verification through PDF 84 is recorded by commit `0da97f94e829bef9b387bf59be580933b97ed122` and `notes/dual-gate-sync-report-pdf-075-084.json`.

## Mandatory historical Tamil glyph gate

`அம்மையப்பன்` contains frequent historical Tamil typeforms. The audit must follow `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` and `notes/historical-glyph-audit.md`.

Minimum known families to inspect on every canonical page:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

This is a minimum set only. Remain alert for other old ligatures, faint vowel marks, worn type, broken ink and edition-specific forms.

Rules:

- identify historical character identity from enlarged/native source pixels;
- prefer same-edition/same-font evidence for doubtful forms;
- OCR, modern spelling expectation and semantic plausibility are not proof;
- no global replacement;
- preserve source wording and change only positively established character identity;
- unresolved character identity keeps the page `needs-review`;
- if a historical-glyph correction changes a page that previously passed visual fidelity, locally recheck that corrected occurrence and record the post-fidelity correction.

## Assembly QA — PASS

- source anchors: **105**;
- exact anchor sequence: **PDF 5 through PDF 109**;
- missing anchors: **0**;
- duplicate anchors: **0**;
- bounded-part boundary presence: **PASS**;
- locked PDF 107 `தூக்குமேடை`: **PASS**;
- rejected `தாக்குமேடை`: **absent**;
- visible unresolved spans in assembled text: **116**.

This closes the **first-pass transcription + assembly gate only**. Final Tamil remains open for PDF 85–109.

## Phase gates

- source intake: complete;
- whole-scan inspection: complete 111/111;
- structural intake map: verified;
- canonical Tamil first pass: **draft-complete — 105/105**;
- full-text assembly: **complete-pass**;
- boundary loss/duplication QA: **PASS**;
- visual fidelity audit: **70/105 passed; next PDF 75 / logical p.73**;
- historical Tamil glyph audit: **70/105 passed; next PDF 75 / logical p.73**;
- final dual-gate Tamil verification: **70/105**;
- PDF 5–74: **dual-gate verified — retrospective backfill and synchronization CLOSED**;
- PDF 85–109: **visual-pending / glyph-pending — run both audits together**;
- scene/dialogue/character derivatives: blocked pending 105/105 dual-gate verified Tamil;
- song/performance authorship gate: not-started;
- English / reader: blocked.

## Exact next activity

> **Resume at PDF 85 / logical printed p.83. Perform visual source-fidelity verification and the full historical-Tamil-glyph audit together on every page from PDF 85–109, adjudicating markers 98–116 occurrence-by-occurrence. Do not reopen PDF 5–74 unless new direct source evidence requires a specific local correction. Do not start scene/dialogue/character derivatives, English translation or reader work until both gates reach 105/105 with no unresolved review pages.**
