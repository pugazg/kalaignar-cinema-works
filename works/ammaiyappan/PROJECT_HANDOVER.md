# Project handover — அம்மையப்பன்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/ammaiyappan/`

## Live-main rule

Treat live GitHub `main` and the rendered controlling scan as authoritative over copied checkpoints. Preserve newer durable work; do not reset or repeat completed phases because an older handover says otherwise.

## Controlling source

`TVA_BOK_0064230_அம்மையப்பன்.pdf`

- PDF pages: **111**;
- bytes: **154,237,539**;
- SHA-256: `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`;
- image-only scan;
- main screenplay/dialogue: **PDF 5–109 / logical printed pp.3–107**;
- PDF 110–111: advertisement/back matter.

Printed identity: `அம்மையப்பன்`; `கதை வசனம்` / `மு. கருணாநிதி`; `முதற் பதிப்பு`, `செப்டம்பர், 1954`; `முரசொலி பதிப்பகம்`, `சென்னை-14`.

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
9. this `works/ammaiyappan/PROJECT_HANDOVER.md`
10. `works/ammaiyappan/NEXT_CHAT_PROMPT.md`
11. `works/ammaiyappan/metadata.yaml`
12. `works/ammaiyappan/scenes/index.json`
13. `works/ammaiyappan/dialogues/final-index.json`
14. `works/ammaiyappan/dialogues/source-role-resolved-records.json`
15. `works/ammaiyappan/characters/index.json`
16. `works/ammaiyappan/characters/entities.json`
17. `works/ammaiyappan/songs/index.json`
18. `works/ammaiyappan/songs/inventory.json`
19. `works/ammaiyappan/translations/README.md`
20. `works/ammaiyappan/translations/index.json`
21. `works/ammaiyappan/translations/schema.json`
22. `works/ammaiyappan/translations/PILOT_REVIEW.md`
23. all completed `works/ammaiyappan/translations/BATCH_*_REVIEW.md` files
24. verified translation records through the current checkpoint.

Also inspect any newer work-local audit/status file added after this handover.

## Closed source authority

### Canonical Tamil / scene layer

- visual fidelity: **105/105 PASS**;
- historical-glyph audit: **105/105 PASS**;
- final dual-gate Tamil: **105/105 complete-verified**;
- unresolved canonical markers: **0**;
- PDF 10 direct-scan correction: **`மாடம்`**, commit `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`;
- source-numbered scenes: **none**;
- source-visible structural boundaries: **63**;
- distinct verified heading forms: **41**;
- archive-only scene derivatives: **63/63 complete-verified**;
- boundary ownership: **PASS — 0 gaps / 0 overlaps / 105 pages represented**;
- PDF 56 / printed 54: `பழுதார் வீதி`;
- PDF 107 / printed 105: **`தூக்குமேடை`**; reject `தாக்குமேடை`.

### Dialogue / character layer

The post-closure scene-3 source form `பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......` is a distinct பூங்காவனம் dialogue unit with its semicolon preserved. Scene 5 `திரு; ...` is the other source-explicit non-colon form. Neither may be normalized to a colon.

Current authority:

- explicit colon-labelled dialogue records: **1,009**;
- source-role supplements: **16**;
- downstream dialogue units: **1,025**;
- exact source speaker labels: **62**;
- unresolved source-role blocks: **0**;
- source punctuation normalizations: **0**;
- character entities / role categories: **26**;
- exact-label coverage: **62/62**;
- downstream dialogue coverage: **1,025/1,025**;
- record-aware `முத்`: **80 → முத்தன் / 97 → முத்தாயி**;
- record-aware `தன`: **1 → தனபதி / 9 → தனவணிகர்**.

Character identity is an English aid only; exact Tamil labels remain provenance authority.

### Song / verse / performance gate

- candidates reviewed: **64/64**;
- retained source-visible occurrences: **5** — archival scenes **7, 10, 19, 40, 59**;
- unresolved authorship occurrences: **3**;
- source-attributed literary quotation: **1**;
- authorship-not-applicable character japa: **1**;
- complete named lyric bodies printed: **0**;
- standalone Tamil lyric derivatives: **0**.

Do not promote `கதை வசனம் / மு. கருணாநிதி` into lyric authorship and do not import absent lyrics from film audio, websites, subtitles, later editions or memory.

## English translation — ACTIVE through scene 45

Current verified checkpoint:

- scenes: **45/63**;
- verified units: **1,000/1,000**;
- dialogue units: **853** = **839 explicit immutable dialogue links + 14 source-role supplements**;
- stage/action units: **144**;
- standalone song-reference units: **2**;
- japa units: **1**;
- cross-page units: **23**;
- unique source-visible song/performance occurrence links: **4** — `ammaiyappan-song-001` through `ammaiyappan-song-004`;
- canonical Tamil/dialogue/character/song evidence changed by English: **no**;
- reader/export: **blocked pending complete English**.

Current files include `translations/records/scene-001.json`–`scene-045.json`, all prior batch reviews, `BATCH_041_045_REVIEW.md`, and `translations/index.json`.

## Batch 41–45 safeguards

Batch 41–45 is **21/21 verified units**:

- 13 explicit dialogue links;
- 0 source-role supplements;
- 8 separate stage/action units;
- 1 cross-page unit — scene 41 `ammaiyappan-en-s041-u001` across PDF 85→86 / printed 83→84;
- 0 retained song/performance occurrences;
- 0 frozen source files modified.

Important decisions:

- scene 41 is action-only; the storm/tree-fall sequence remains one cross-page stage unit and no dialogue is invented;
- scene 42's elliptical `பெண்ணை வந்தொரு மாயப் பிசாசு...` line remains immutable Vedalam dialogue; no song/verse occurrence is manufactured;
- scene 42 preserves exact `வணிகர்` / `வணி` labels and does not repair frozen `இல்ல ை` spacing upstream;
- scene 43 preserves exact source label `தன`; record-aware merchant identity does not rewrite provenance;
- scene 44 keeps source-owned `(பார்க்கிறாள்)` inside Sumathi's immutable dialogue rather than splitting it into a separate action;
- scene 45 preserves exact `முத்தன்` / `முத்` / `தனவணிகர்` / `தன` labels and the source's `சீமான் இனம்` class accusation without euphemizing it.

Earlier safeguards remain active, including scene-40 japa occurrence handling: `ammaiyappan-song-004` is a character japa cue, not a soundtrack song, and no title/lyrics/authorship are reconstructed.

Translation must preserve archive scene ID, PDF/printed-page provenance, exact speaker labels, source-role origin, cross-page ownership, source rhetoric/register and the closed song/performance evidence.

## Exact next activity

> **Fetch live `main`; confirm the English checkpoint is 45/63 scenes and 1,000 verified units; then translate and source-review archival scenes 46–50 from the frozen verified derivatives. Inspect the closed source-role layer: scene 50 contains `ammaiyappan-s050-r001`, which must remain `source-context-attributed` provenance and must not become a manufactured printed speaker label. The closed song/performance inventory has no retained occurrence in scenes 46–50. Preserve exact Tamil speaker labels and PDF/printed-page provenance, keep cross-page units whole, and do not modify frozen Tamil/dialogue/character/song evidence. After the batch synchronize translation/work/repository status mirrors and refresh this handover and `NEXT_CHAT_PROMPT.md`.**