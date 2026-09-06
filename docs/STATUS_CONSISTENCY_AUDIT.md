# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-09-06  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles current repository-wide status mirrors with the authoritative work checkpoints for all **seven registered works**. `data/works.json`, root README, project handover and active work-local metadata/handovers must agree before a major phase is considered closed.

## Result

**PASS for Ammayappan's source/structured authority and complete English translation.** Canonical Tamil is **105/105 dual-gate complete-verified**; scene derivatives are **63/63**; dialogue authority is **1,009 explicit + 16 source-role supplements = 1,025 downstream units**; character/entity coverage is **1,025/1,025** and **62/62 exact labels**. English translation is now **complete-verified at 63/63 archival scenes / 1,210 units**, with whole-work source/linkage reconciliation PASS.

The scene-3 post-closure source form `பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......` remains a distinct பூங்காவனம் dialogue unit with its semicolon preserved exactly. Scene 5 `திரு; ...` remains the other source-explicit non-colon speaker delimiter. Neither form is normalized to a colon.

## Current work matrix

| Work | Source/Tamil | Structured text | English | Reader / integration |
|---|---|---|---|---|
| Parasakthi | 54/54 canonical pages verified | 46 observed scenes / 642 dialogue records | 769 verified units | reader/export QA PASS |
| Tirumbippaar! | 104/104 canonical pages verified | 93/93 scenes / 1,040 dialogue records | 1,321 verified units | reader/export + deterministic EPUB QA PASS |
| Manohara | 82/82 canonical pages verified | 57/57 scenes / 983 dialogue records | 1,190 verified units | reader/export QA PASS; Reading Room ready |
| Kalaignar Thirai Isai Paadalgal | 54/54 numbered Tamil songs verified | 54 song records | 54/54 songs / 1,105 line-cues | reader/export + Reading Room payload QA PASS; site not applied |
| Manthiri Kumari | PDF 2–13 canonical Tamil complete-verified; 12/12 pages; 0 unresolved | credits; story summary 1/1; performance records 15/15 | 13 prose units + 15/15 performances / 52 sections / 234 line-cues | bilingual reader + Reading Room payload QA PASS; site not applied |
| Raja Rani | 79/79 source pages; 70/70 screenplay pages verified | 58/58 scenes / 1,071 dialogues / 80 labels / 44 entities | screenplay 1,236 units + 11/11 songs / 181 line-cues | bilingual reader + Reading Room payload QA PASS; site not applied |
| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **complete-verified 63/63 / 1,210 units** | reader/export **QA PASS**; Reading Room ready |

## Ammayappan current checkpoint

### Frozen source/Tamil authority

- canonical Tamil: **105/105 dual-gate complete-verified**;
- PDF 10 post-fidelity correction: `மாடம்` — commit `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`;
- source-visible boundaries / distinct headings: **63 / 41**;
- scene derivatives: **63/63 complete-verified**;
- boundary ownership: **PASS — 0 gaps / 0 overlaps / 105 pages represented**;
- unresolved canonical markers / review pages: **0 / 0**.

### Dialogue / character authority

- explicit colon-labelled records: **1,009**;
- source-role supplements: **16**;
- downstream dialogue units: **1,025**;
- exact source labels: **62**;
- unresolved source-role blocks: **0**;
- source punctuation normalizations: **0**;
- character/entity index: **26/26 verified entities**;
- exact-label / dialogue-unit coverage: **62/62 / 1,025/1,025**;
- `முத்`: **80 முத்தன் / 97 முத்தாயி**;
- `தன`: **1 தனபதி / 9 தனவணிகர்**.

### Song/performance gate

- candidates reviewed: **64/64**;
- retained source-visible occurrences: **5** — scenes **7, 10, 19, 40, 59**;
- unresolved authorship: **3**;
- source-attributed literary quotation: **1**;
- authorship-not-applicable character japa: **1**;
- complete named lyric blocks / standalone Tamil lyric files: **0 / 0**.

### English translation gate — CLOSED

- verified scenes: **63/63**;
- verified units: **1,210**;
- dialogue units: **1,025** = **1,009 explicit + 16 source-role supplements**;
- stage/action units: **181**;
- standalone song-reference units: **3**;
- japa units: **1**;
- standalone literary-verse / written-text units: **0 / 0**;
- cross-page units: **28**;
- unique occurrence links: **5/5** — `ammaiyappan-song-001` through `ammaiyappan-song-005`;
- structural stars translated as prose: **0**;
- canonical Tamil/dialogue/character/song evidence changed by English: **no**;
- whole-work reconciliation: **PASS** — `works/ammaiyappan/translations/FINAL_TRANSLATION_QA.md`.

Final batch **61–63** reconciliation is **PASS**:

| Scene | Explicit dialogue | Source-role supplements | Stage/action | Other | Total |
|---|---:|---:|---:|---:|---:|
| 61 | 0 | 0 | 1 | 0 | 1 |
| 62 | 4 | 0 | 3 | 0 | 7 |
| 63 | 12 | 0 | 2 | 0 | 14 |
| **Total** | **16** | **0** | **6** | **0** | **22** |

Final-batch safeguards:

- scene 61 remains action-only; no speech is invented and the masked substitute is not identified before scene 62 reveals him;
- scene 62 preserves the masked-prisoner reveal, Sukhadev's halting explanation, Maappillaithaasar's atonement speech and the source's final `speech ends; life ends` parallel without external expansion;
- scene 63 preserves exact `முத்` / `முத்தா` provenance, `Aththan` / `Amma` register, mother-recognition and liberation rhetoric;
- scene 63's closing four-line stanza remains inside immutable `ammaiyappan-s063-d012`; no synthetic literary-verse or song occurrence is created;
- frozen `அண்ணலின் விலங்கொடிப்ப ோம்` retains `Annal` as a source term instead of receiving an unsupported stronger gloss or Tamil normalization;
- no frozen Tamil/dialogue/character/song evidence was modified.

Whole-work English reconciliation confirms all **1,009** explicit dialogue records and all **16** source-role supplements are linked exactly once, all **28** cross-page units remain whole, and all **5** retained source-visible occurrences are represented without reconstructing absent lyrics, title or authorship.

The separate **reader/export preflight is executable and PASS**: workflow `.github/workflows/ammaiyappan-english-reader-preflight.yml`, run **34025680568**, head `ae554f92faf7a9b0f4005c42cc28c8b3e8e95d36`. It directly verified all **63 scene records / 1,210 units / 1,025 dialogue-source links / 28 cross-page units / five occurrence identities across seven intentional links**, with **0** missing/extra/duplicate dialogue links, provenance errors, page regressions, unit-ID errors, synthetic scene-end units, direct structural-star prose units, warnings or errors. See `works/ammaiyappan/editions/en/PREFLIGHT_QA_REPORT.md`. This is not a separate JSON-Schema-library validation.

The deterministic **reader/export package is complete-verified with generated-output QA PASS**. Markdown, standalone HTML and machine-readable JSON each preserve all **1,210** verified units exactly once; all **1,025** dialogue/source-role links, **28** cross-page units and **5 occurrence identities / 7 source-span links** reconcile to the structured translation. Output SHA-256 values: Markdown `50fb3baf33c3b249ce32dba5947fe73871f5ef36d18f41807d2ad3ed3d3fb549`, HTML `c8fba94766a4082d5288bcd5f9ff63bde863d942f7b9aaf824a3a1c5bcc0f22a`, JSON `a72b758d397a909cb9004fd9e34ffedcc4bb72027d29d11aec994df6b4ea4ce3`. `works/ammaiyappan/editions/en/manifest.json` records deterministic input/output hashes. Frozen source layers modified by reader generation: **0**.

**Next production phase:** create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures.

## Stable downstream checkpoints for other works

- **Manthiri Kumari:** 12/12 canonical pages; story summary 1/1; performance records 15/15; English 13 prose units + 15 performances / 52 sections / 234 paired line-cues; bilingual reader and Reading Room payload QA PASS; item-level lyricists 0 verified / 15 unresolved; site not applied.
- **Raja Rani:** 79/79 source pages; 70/70 screenplay pages; 58/58 scenes; 1,071 dialogues; 80 labels / 44 entities; 1,236 screenplay English units; 11/11 songs / 181 line-cues; reader and Reading Room payload QA PASS; site not applied.
- **Tirumbippaar!:** 104/104 canonical pages; 93/93 scenes; 1,040 dialogues; 1,321 English units; deterministic EPUB QA PASS, SHA-256 `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`.

## Repository-wide synchronization rule

A major phase is not complete while an active current-status document still advertises the prior checkpoint. Synchronize work-local metadata/README/index/QA/handover plus `data/works.json`, root README, master handover/status audit and any shared guide changed by reusable lessons. Historical checkpoint files may retain historical numbers when clearly labelled historical.

## Conclusion

Ammayappan's canonical Tamil and structured source-derived layers remain **closed at the corrected 1,025-unit authority**. English translation is **complete-verified at 63/63 scenes / 1,210 units**, final source/linkage reconciliation is PASS, and the executable reader/export preflight is now **PASS**. The next bounded activity is **source-linked Reading Room payload construction and QA**.