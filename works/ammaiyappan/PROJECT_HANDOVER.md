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

## Canonical Tamil and scene-text derivatives — CLOSED

Canonical Tamil:

- visual fidelity: **105/105 PASS**;
- historical glyph audit: **105/105 PASS**;
- final dual-gate Tamil: **105/105 complete-verified**;
- unresolved canonical markers: **0**;
- post-fidelity direct-scan correction: PDF 10 heading `மாடம்`, commit `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`.

Scene layer:

- segmentation preflight: **PASS — 63 source-visible canonical boundaries**;
- earlier intake ledger: **58/58 reconciled**;
- canonical additions beyond intake: **5**;
- archive-only scene files: **63/63 complete-verified**;
- source scene numbers invented: **0**;
- boundary ownership QA: **PASS — 0 gaps, 0 overlaps**;
- canonical page representation: **105/105 — PDF 5–109**;
- scene derivative commit: `6a764137616879d08f5a1ff14431caafa87b11eb`.

## Phase gates

- source/canonical Tamil gates: **closed**;
- scene-text derivatives: **closed-verified**;
- dialogue index: **READY — next phase**;
- character index: blocked pending dialogue-index closure;
- song/performance authorship gate: not-started;
- English / reader: blocked by derivative gate order.

## Exact next activity

> **Build the dialogue index from the 63 verified scene-text derivatives. Preserve the exact printed speaker label for every dialogue turn, attach archive scene ID and source PDF provenance, do not normalize aliases/character identities in this phase, and run dialogue coverage/ownership QA before opening character indexing.**


## Dialogue-index closure — FINAL QA PASS

- explicit colon-labelled records: **1009**;
- exact source speaker-label strings: **62**;
- reviewed cross-page continuation candidates: **20/20 PASS**;
- source-role residual review: **20/20 complete**;
- source-role-resolved dialogue supplements: **15**;
- non-dialogue resolved source units: **6**;
- downstream dialogue units: **1024**;
- unresolved source-role blocks: **0**;
- source scene numbers invented: **0**;
- alias normalization: **0**;
- source punctuation normalization: **0**;
- exceptional source delimiter `திரு; ...`: preserved exactly;
- final QA: `notes/dialogue-final-qa.json` — **PASS**;
- character/entity index gate: **UNLOCKED**.

### Exact next activity

> **Build the character/entity index from `dialogues/final-index.json`, the 1009 explicit dialogue records, the 15 source-role-resolved dialogue supplements, and the 63 verified scene derivatives. Preserve every exact speaker label as provenance; perform alias/entity reconciliation only in the new character/entity layer, never by rewriting the dialogue records.**
