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
23. all completed `works/ammaiyappan/translations/BATCH_*_REVIEW.md` files through `BATCH_061_063_REVIEW.md`
24. `works/ammaiyappan/translations/FINAL_TRANSLATION_QA.md`
25. verified translation records `works/ammaiyappan/translations/records/scene-001.json`–`scene-063.json`.

Also inspect any newer work-local audit/status or reader/export file added after this handover.

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

## English translation — COMPLETE-VERIFIED

Final whole-work checkpoint:

- scenes: **63/63**;
- verified units: **1,210/1,210**;
- dialogue units: **1,025** = **1,009 explicit immutable dialogue links + 16 source-role supplements**;
- stage/action units: **181**;
- standalone song-reference units: **3**;
- japa units: **1**;
- standalone literary-verse units: **0**;
- written-text units: **0**;
- cross-page units: **28**;
- unique source-visible song/performance occurrence links: **5/5** — `ammaiyappan-song-001` through `ammaiyappan-song-005`;
- canonical Tamil/dialogue/character/song evidence changed by English: **no**;
- whole-work English reconciliation: **PASS** — `translations/FINAL_TRANSLATION_QA.md`;
- reader/export preflight: **complete-pass — executable GitHub Actions gate**;
- reader/export generation: **ready / not started**.

The English dialogue census now exactly equals the closed downstream source authority: **1,009 explicit + 16 supplements = 1,025/1,025**.

## Final batch 61–63 safeguards

Batch 61–63 is **22/22 verified units**:

- 16 explicit dialogue links;
- 0 source-role supplements;
- 6 separate stage/action units;
- 0 song-reference / literary-verse / japa / written-text units;
- 0 new cross-page units;
- 0 retained song/performance occurrences;
- 0 frozen source files modified.

Important decisions:

- scene 61 is action-only; the friends' gesture-based rescue creates no invented dialogue, and English does not identify the black-masked substitute before scene 62 reveals him;
- scene 62 preserves the masked-prisoner revelation, Sukhadev's halting `இப்படி—இது மாதிரி—நடந்து விட்டது` explanation, Maappillaithaasar's Pattinathar / eighteen-Siddhars atonement speech, and the source parallel `பேச்சு முடிகிறது; சாமியாரின் வாழ்க்கை முடிகிறது` without external expansion;
- scene 63 preserves exact `முத்` / `முத்தா` source labels, retains **Aththan**, and preserves the recognition shift `இளவராணி` → `அம்மா` as **Princess** → **Amma**;
- scene 63 keeps `கர்ம வீரனே` as **Karmaveeran** and preserves the source movement from love/motherhood to Pazhuthar and motherland liberation;
- its four-line closing stanza remains inside immutable dialogue `ammaiyappan-s063-d012`; the closed song/performance gate authorizes no separate scene-63 verse/song occurrence;
- frozen `அண்ணலின் விலங்கொடிப்ப ோம்` retains `Annal` as a source term because the immediate referent is not secure enough for a stronger gloss; no Tamil normalization is claimed;
- the compact martial saying remains source-bounded rather than being replaced by an external proverb text.

Earlier safeguards remain active, including exact semicolon provenance in scenes 3/5, source-context-attributed supplements remaining derivative, cross-page ownership, scene-30 Purananuru dialogue ownership, scene-40 japa handling, and scene-59 source-only love-song handling.

## Whole-work English reconciliation result

`translations/FINAL_TRANSLATION_QA.md` records **PASS**:

- all 63 scene records present;
- all **1,009** immutable explicit dialogue records linked exactly once;
- all **16** closed source-role supplements linked exactly once with their original provenance;
- all **181** separately owned stage/action spans source-bounded;
- all **28** cross-page units retained whole;
- all **5** retained song/performance occurrences represented without reconstructing absent lyrics/title/authorship;
- structural stars translated as prose: **0**;
- frozen Tamil/dialogue/character/song evidence modified: **0**.

This PASS is source/linkage reconciliation. It does not claim an executable JSON-schema validator or CI run unless separately executed and recorded.

## Reader/export preflight — PASS

Executable workflow `.github/workflows/ammaiyappan-english-reader-preflight.yml` passed at run **34025680568** / head `ae554f92faf7a9b0f4005c42cc28c8b3e8e95d36`. The probe verified **63/63 scene records, 1,210/1,210 units, 1,025/1,025 dialogue/source-role links exactly once, 28 cross-page units, five occurrence identities across seven intentional source-span links, exact speaker-label/source-role provenance, and archive-only scene numbering**, with zero audit errors or warnings. Full record: `editions/en/PREFLIGHT_QA_REPORT.md`.

## Reader/export package — PASS

The deterministic reader/export package is complete-verified under `editions/en/`. Markdown, standalone HTML and machine-readable JSON each preserve all **1,210** units exactly once. `QA_REPORT.md` records generated-output PASS and `manifest.json` records deterministic input/output hashes. Exact **1,025/1,025** dialogue/source-role linkage, all **28** cross-page units and all **5 occurrence identities / 7 source-span links** are preserved. Output SHA-256 values: Markdown `50fb3baf33c3b249ce32dba5947fe73871f5ef36d18f41807d2ad3ed3d3fb549`, HTML `c8fba94766a4082d5288bcd5f9ff63bde863d942f7b9aaf824a3a1c5bcc0f22a`, JSON `a72b758d397a909cb9004fd9e34ffedcc4bb72027d29d11aec994df6b4ea4ce3`. Frozen source layers modified: **0**.

## Reading Room payload — PASS

`integrations/reading-room/reading-room.json` is complete-verified with payload QA PASS: **63 Tamil scene texts / 1,210 English units / 1,025 dialogue-source links / 28 cross-page units / 5 occurrence identities across 7 source spans**. Payload SHA-256 `f00efb816edf08b43702a3a1a9d71ed9cc54fd1a803b8881bc6e2c6466de1f8c`. The site application status is **not-applied**; no separate implementation repository was changed.

## Exact next activity

> **Fetch live `main`; preserve all closed Ammayappan source, translation, reader and Reading Room payload layers. No required repository-internal production work remains. Apply the complete-verified payload to the separate Reading Room implementation repository only when explicitly authorized; until then keep site application `not-applied`.**