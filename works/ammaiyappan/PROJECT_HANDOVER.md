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
15. every bounded part listed by `transcription/index.json`
16. `works/ammaiyappan/notes/textual-notes.md`
17. every supplemental uncertainty ledger listed by `transcription/index.json`.

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

## Canonical Tamil first pass — active

- expected: **105 pages**;
- completed: **100/105**;
- completed range: **PDF 5–104 / printed pp.3–102**;
- state: **draft**, verified pages **0**;
- open uncertainty markers: **114**;
- newest part: `transcription/parts/pdf-095-104.md`;
- newest ledger: `notes/textual-notes-pdf-095-104.md` for markers **108–114**;
- `full-text.md` assembled only through **PDF 14**;
- bounded parts cover **PDF 15–104**;
- next page: **PDF 105 / printed p.103**;
- visual fidelity audit: **not-started**.

PDF 95–104 preserves the source transitions `பாழ் மண்டபம்`, `வேங்கை நாட்டு அவைக்கூடம்`, `பூங்காவனம் அறை`, `முத்தனின் தோழர்கள் பேசிக் கொண்டிருத்தல்`, `சுமதி வீடு`, and `சிறைச்சாலை`. It retains the long political/social denunciation passages as scan-controlled text. **PDF 104 ends inside Muthan's speech; PDF 105 visibly continues it.**

The earlier PDF 65–74 batch remains `draft-high-uncertainty`; no uncertainty marker is verified merely by being carried into assembly.

## Phase gates

- source intake: complete;
- whole-scan inspection: complete 111/111;
- structural intake map: verified;
- canonical Tamil first pass: **draft-in-progress — 100/105**;
- full-text assembly: pending;
- boundary loss/duplication QA: pending;
- visual fidelity audit: not-started;
- scene/dialogue/character derivatives: blocked;
- song/performance authorship gate: not-started;
- English / reader: blocked.

## Exact next activity

> **Complete PDF 105–109 / printed pp.103–107 as the final first-pass batch, beginning with the PDF 104→105 continuation and preserving the locked `தூக்குமேடை` heading on PDF 107. Then assemble every bounded part into `transcription/full-text.md` in exact source order and perform boundary loss/duplication QA. Only after that assembly checkpoint may the canonical first pass be declared closed; the separate full rendered-scan visual fidelity audit comes next. Do not start structured derivatives yet.**
