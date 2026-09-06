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
- dialogue index: **complete-source-role-resolved — 1,024/1,024 downstream units**;
- character/entity index: **complete-verified-reconciled — 26 entities / 62 exact labels / 1,024 units**;
- song/performance authorship gate: **complete-verified-source-only — 64/64 candidates reviewed; 5 retained occurrences; 0 standalone lyric files**;
- English / reader: **READY — next phase**.

## Exact next activity

> **Begin English translation/reconciliation from the closed Tamil/scene/dialogue/character evidence layers. Keep exact Tamil provenance and source structure; do not reopen canonical Tamil or dialogue evidence without new scan-backed authority.**


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

> **Begin English translation/reconciliation from the closed Tamil/scene/dialogue/character evidence layers. Use `characters/index.json` only as a derivative identity aid; exact Tamil/dialogue labels remain the provenance authority.**

## Character/entity closure — FINAL QA PASS

- downstream dialogue units dispositioned: **1,024/1,024**;
- exact source speaker labels dispositioned: **62/62**;
- stable entities / role categories: **26**;
- verified entities: **26**;
- review entities: **0**;
- unresolved entities: **0**;
- record-aware exact labels: **2** — `முத்`, `தன`;
- record-aware units: **187**;
- `முத்`: **80 → முத்தன் / 97 → முத்தாயி**;
- `தன`: **1 → தனபதி / 9 → தனவணிகர்**;
- dialogue records modified by character reconciliation: **no**;
- character index: `characters/index.json`;
- complete entities: `characters/entities.json`;
- exact-label disposition: `characters/labels-inventory.json`;
- record-aware assignments: `characters/record-aware-dispositions.json`;
- character/entity build commit: `e670816876c4f02c0bebe283c2c9bfc0de93fcc9`.

### Exact next activity

> **Begin English translation/reconciliation. Translate only from the frozen verified Tamil evidence, preserve scene/dialogue provenance, and use the character/entity layer to resolve identity without normalizing the Tamil source.**

## Song / verse / performance authorship closure — FINAL SOURCE GATE

- preflight candidate hits reviewed: **64/64**;
- retained source-visible occurrences: **5**;
- unresolved authorship occurrences: **3**;
- source-attributed literary quotation occurrences: **1**;
- authorship-not-applicable japa occurrences: **1**;
- complete named song lyric bodies printed by the booklet: **0**;
- standalone Tamil lyric files authorized / created: **0 / 0**;
- external item-level evidence used: **no**;
- canonical Tamil changed by this gate: **no**;
- source inventory: `songs/index.json`, `songs/inventory.json`, `songs/candidate-disposition.json`, `songs/credits.json`;
- gate commit: `d51e3151a3fff218d8e942fc91e6eb837c1d487c`.

The booklet's printed `கதை வசனம் / மு. கருணாநிதி` credit is not promoted into lyric authorship. English may translate only the source-visible performance references, literary fragment, japa token and cues; absent song lyrics must not be reconstructed from film audio, websites, subtitles, later editions or memory.

### Exact next activity

> **Begin source-linked English translation/reconciliation from the frozen Tamil and completed derivative evidence layers. Preserve scene/dialogue/character provenance and translate only source-visible song/performance material.**

