# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-09-10  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles current repository-wide status mirrors with the authoritative work checkpoints for all **nine registered works**. `data/works.json`, root README, project handover and active work-local metadata/handovers must agree before a major phase is considered closed.

## Result

**PASS for the current repository-wide checkpoint.** Vandikkaran Magan is now closed through the song/performance authorship gate: **9/9 source-visible occurrences / 6 bounded Tamil bodies / 3 cue-only records / QA PASS**, with **0 item-level source-attributed lyricists and 6 unresolved item-level lyric authorships**. The PDF 88 `பாடல்கள்: கவிஞர் வாலி` line remains film-level metadata and was not promoted item-by-item. English translation is READY-NEXT.

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
| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **complete-verified 63/63 / 1,210 units** | reader/export + Reading Room payload **QA PASS**; site not applied |
| Naam / நாம் | canonical Tamil 67/67 complete-verified; 0 unresolved | **45/45 scenes; 590 dialogue records; 28 character/entities; song/performance 7/7 reconciled** | **5/45 verified / 131 units / 99 immutable dialogue links / 1 of 7 performances translated** | not-started |
| Vandikkaran Magan / வண்டிக்காரன் மகன் | **87/87 canonical source pages complete-verified; 0 unresolved** | **72/72 scenes; 744 dialogues / 38 labels; 32 entities; song/performance 9/9 QA PASS** | **READY-NEXT** | not-started |

## Vandikkaran Magan current checkpoint

- canonical Tamil / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- immutable dialogue index: **744 / 38 exact labels / COMPLETE-VERIFIED / QA PASS**;
- character/entity index: **32 entities / 38/38 labels / 744/744 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance layer: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- bounded Tamil bodies: **6**; cue-only non-lyric occurrences: **3**;
- item-level source-attributed lyricists: **0**; unresolved item-level lyric authorships: **6**;
- film-level PDF 88 `பாடல்கள்: கவிஞர் வாலி`: **preserved, not promoted item-by-item**;
- upstream canonical Tamil / scene / dialogue / character mutation from song processing: **0**;
- English translation: **READY-NEXT**.

**Next production phase:** Begin a bounded English-translation pilot from source scene 1 using only closed canonical Tamil plus verified scene/dialogue/character/song-performance derivatives. Preserve exact Tamil source labels and provenance, link immutable dialogue IDs without rewriting them, and keep song/performance authorship unresolved wherever the source gate is unresolved. Run pilot QA before scaling to later scenes.

## Naam current checkpoint

- canonical Tamil: **67/67 COMPLETE-VERIFIED**;
- visual-fidelity / historical-glyph final / dual-gate: **67/67 / 67/67 / 67/67**;
- open source uncertainties: **0**;
- manual controlling-scan verdicts: PDF 5 `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`, PDF 10 `நீ இங்கே வேலை பார்க்கிற வரைக்கும்`, PDF 24 `கெளரவம் தேடி`;
- final audit: `works/naam/notes/canonical-closure-user-manual.md`;
- structured scene derivatives: **45/45 COMPLETE-VERIFIED**; boundary ownership QA **PASS — 0 gaps / 0 overlaps**; canonical PDF pages represented **67/67**.

**Next production phase:** Translate and verify source-numbered scenes 6–10 as the next bounded English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units and stage/narrative ownership; translate only source-visible performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-001` in scene 7 with its specific `பாரதியார்` attribution and `naam-perf-002` in scene 8 with unresolved item-level authorship; and do not alter closed Tamil or structured source layers.

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

**Next production phase:** no repository-internal Ammayappan production phase remains; separate-site application requires explicit authorization and is currently not-applied.

## Ammayappan Reading Room payload — PASS

The deterministic source-linked payload is complete-verified at `works/ammaiyappan/integrations/reading-room/reading-room.json`: **63 Tamil scene texts / 1,210 verified English units / 1,025 dialogue-source links / 28 cross-page units / 5 occurrence identities across 7 source spans**. Payload SHA-256 `f00efb816edf08b43702a3a1a9d71ed9cc54fd1a803b8881bc6e2c6466de1f8c`; QA is PASS. Exact speaker-label/source-role provenance remains **1,009 colon + 2 source-semicolon + 14 context-attributed**. Site application is **not-applied**, and no frozen source layer was modified.

## Stable downstream checkpoints for other works

- **Manthiri Kumari:** 12/12 canonical pages; story summary 1/1; performance records 15/15; English 13 prose units + 15 performances / 52 sections / 234 paired line-cues; bilingual reader and Reading Room payload QA PASS; item-level lyricists 0 verified / 15 unresolved; site not applied.
- **Raja Rani:** 79/79 source pages; 70/70 screenplay pages; 58/58 scenes; 1,071 dialogues; 80 labels / 44 entities; 1,236 screenplay English units; 11/11 songs / 181 line-cues; reader and Reading Room payload QA PASS; site not applied.
- **Tirumbippaar!:** 104/104 canonical pages; 93/93 scenes; 1,040 dialogues; 1,321 English units; deterministic EPUB QA PASS, SHA-256 `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`.

## Repository-wide synchronization rule

A major phase is not complete while an active current-status document still advertises the prior checkpoint. Synchronize work-local metadata/README/index/QA/handover plus `data/works.json`, root README, master handover/status audit and any shared guide changed by reusable lessons. Historical checkpoint files may retain historical numbers when clearly labelled historical.

## Conclusion

Vandikkaran Magan is the active production work. Its canonical Tamil/source gates and **72/72 scene derivatives remain COMPLETE-VERIFIED**; the immutable dialogue index is now **COMPLETE-VERIFIED — 744 records / 38 exact labels / QA PASS**. **Next: bounded English-translation pilot from source scene 1.**

<!-- Naam song gate reconciled 7/7 -->
**Naam current structured checkpoint:** song/performance gate **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED** after the pre-English 45-scene sweep restored scene-1 PDF 6–7 `(பாட்டு)` as append-only `naam-perf-007`; 1 item-level source attribution (`ஆயிரம் தெய்வங்கள்` → `பாரதியார்`), 6 unresolved item-level authorships. **Next:** Begin Phase 9 source-linked English translation from the complete-verified Tamil, scene, dialogue, character/entity and reconciled song/performance layers. Preserve source scene order and exact Tamil speaker labels as metadata; link labelled dialogue to immutable IDs; keep source-unlabelled speech unassigned; translate all seven retained performance records from their source-visible Tamil only, carrying `பாரதியார்` attribution only for `ஆயிரம் தெய்வங்கள்` and leaving the other six item-level authorship states unresolved. Follow `docs/SONG_TRANSLATION_GUIDE.md`, begin with a scene-1 pilot, run source-link/dialogue/performance coverage QA, and do not alter closed Tamil or structured source layers.


<!-- Naam English pilot current -->
**Naam / நாம் current:** English translation **scene 1/45 PILOT-VERIFIED — 21 units / 14 dialogue links / 1 of 7 performance records / 23 song mappings**; song/performance gate **7/7 reconciled**; no source-layer rewrites. **Next:** Translate and verify source-numbered scenes 2–5 as the first bounded post-pilot English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units and stage/narrative ownership; and use only the reconciled seven-record song/performance layer for performance links. Do not alter closed Tamil or structured source layers.


<!-- Naam English scenes 2-5 current -->
**Naam current consistency checkpoint:** source layers remain closed; song/performance gate **7/7 reconciled**; English **5/45 scenes / 131 units / 99 immutable dialogue links / 1 of 7 performances / 23 song mappings**. Scenes 2–5 QA is **PASS** with **85/85** labelled-dialogue links and one unassigned source-unlabelled speech unit. **Next:** Translate and verify source-numbered scenes 6–10 as the next bounded English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units and stage/narrative ownership; translate only source-visible performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-001` in scene 7 with its specific `பாரதியார்` attribution and `naam-perf-002` in scene 8 with unresolved item-level authorship; and do not alter closed Tamil or structured source layers.


<!-- Naam English scenes 6-15 current -->
**Naam English scenes 6-15 current:** English **15/45 verified / 363 units / 279 dialogue links / 3 of 7 performances / 57 mappings**; source-unlabelled speech remains unassigned; upstream rewrites **0**. User cadence: **10 source scenes per iteration**. **Next:** Translate and verify source-numbered scenes 16–25 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units and stage/narrative ownership; translate only source-visible performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-003` in scene 21 with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; only a final remainder may contain fewer scenes.


<!-- Naam English scenes 16-25 current -->
**Naam English scenes 16-25 current:** English **25/45 verified / 501 units / 380 dialogue links / 4 of 7 performances / 74 mappings**; source-unlabelled speech remains unassigned; upstream rewrites **0**. User cadence: **10 source scenes per iteration**. **Next:** Translate and verify source-numbered scenes 26–35 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units and stage/narrative ownership; translate only source-visible performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-004` in scene 31 with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; only a final remainder may contain fewer scenes.


<!-- Naam English scenes 26-35 current -->
**Naam English scenes 26-35 current:** English **35/45 verified / 680 units / 506 dialogue links / 5 of 7 performances / 84 performance mappings / 1 chant (16 mappings)**; source-unlabelled speech remains unassigned; upstream rewrites **0**. **Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.


<!-- Naam English scenes 36-45 current -->
**Naam English scenes 36-45 current:** scene-sharded English **45/45 verified / 797 units / 590/590 dialogue links / 7 of 7 performances / 138 performance mappings / 1 chant (16 mappings)**; source-unlabelled speech remains unassigned; whole-work English reconciliation **READY-NEXT**; upstream rewrites **0**. **Next:** Run whole-work English translation reconciliation and closure QA across source scenes 1–45 before building the reader/export layer. Verify every translated unit is source-ordered and unique; all 590 immutable dialogue records are linked exactly once; source-unlabelled speech remains unassigned; all seven retained song/performance records are translated without authorship upgrades; the scene-34 chant remains a distinct chant; cross-page provenance and written-text/stage ownership are exact; no duplicate source-span ownership, synthetic scene-end prose, placeholder text, or upstream Tamil/scene/dialogue/character/song-source mutation exists. If and only if that whole-work gate passes, mark English translation complete-verified and begin Phase 10 whole-work reader/export generation.


<!-- Naam English whole-work closure current -->
**Naam English whole-work closure:** **PASS / COMPLETE-VERIFIED — 45/45 scenes / 797 units / 590/590 dialogue links / 20 unlabelled / 7/7 performances / 138 mappings / chant 1/16 / 12 cross-page units**; duplicate ownership, placeholders, synthetic scene ends, upstream rewrites **0**; reader/export **READY-NEXT**. **Next:** No required repository-internal processing remains for நாம். Reader/export and the source-linked Reading Room payload are complete-verified with QA PASS. Keep Tamil, scene, dialogue, character, song-source and English records closed. Apply `works/naam/integrations/reading-room/reading-room.json` in the separate Kalaignar Digital Library / Reading Room implementation repository only when that repository is explicitly authorized for modification; before applying it, fetch that repository's live state and use a fail-closed importer pinned to this verified payload/manifest. Site application remains not-applied here. Do not create a PDF, EPUB or other publication package unless separately requested.


<!-- Naam Phase 10 current -->
**Naam Phase 10 current:** reader/export **COMPLETE-VERIFIED / QA PASS** — 45 source-numbered scenes / 797 English units / 590 immutable dialogue links / 7 retained performances / 138 performance mappings / 1 distinct chant (16 mappings) / 12 cross-page units. Reading Room payload **PAYLOAD-COMPLETE-VERIFIED / QA PASS**, SHA-256 `9b97493b820ebd42c822b5fbdc53beda8dbe1d61103a1c9d2abb06a552bcf825`, site application **not-applied**. No PDF/EPUB was generated. **Next:** No required repository-internal processing remains for நாம். Reader/export and the source-linked Reading Room payload are complete-verified with QA PASS. Keep Tamil, scene, dialogue, character, song-source and English records closed. Apply `works/naam/integrations/reading-room/reading-room.json` in the separate Kalaignar Digital Library / Reading Room implementation repository only when that repository is explicitly authorized for modification; before applying it, fetch that repository's live state and use a fail-closed importer pinned to this verified payload/manifest. Site application remains not-applied here. Do not create a PDF, EPUB or other publication package unless separately requested.


<!-- Vandikkaran Magan intake current -->
**Current active work:** **வண்டிக்காரன் மகன்**. Source intake and structural mapping are synchronized **COMPLETE-VERIFIED**: 90-page image-only 1978 first-edition source, screenplay PDF 6–87 / printed pp.5–86, and **70 observed source scene-heading occurrences** including suffix insertions and combined `45-46`. Canonical Tamil is **NOT-STARTED** and every downstream derivative remains blocked/not-started. The source-visible film-level lyric credit `பாடல்கள்: கவிஞர் வாலி` is metadata only until the item-level song/performance gate. **Next:** Begin canonical Tamil first-pass transcription from PDF 4 onward in source order, preserving front matter and screenplay exactly with stable PDF/printed-page anchors. Use the historical-glyph guide prospectively on every page, keep uncertain readings explicit, and do not call pages verified during first pass. No structured derivative work begins until the later separate visual-fidelity + historical-glyph verification gate closes.


<!-- Vandikkaran Magan first pass current -->
**Current active work:** **வண்டிக்காரன் மகன்** — canonical Tamil first pass now **PDF 4–8 / 5 of 84 DRAFT**, screenplay through PDF 8 / printed 7, **0** uncertainty markers, historical-glyph prospective check **5/5 PASS**, verified pages **0**, derivatives blocked. **Next:** Continue canonical Tamil first-pass transcription with PDF 9–13 (five source pages) in source order. Preserve exact source scene headings, speaker labels, punctuation, stage directions and page boundaries; keep every page draft during first pass; inspect the historical Tamil glyph families prospectively occurrence by occurrence from enlarged source pixels; record any uncertainty explicitly; and do not begin visual-fidelity verification or structured derivatives yet.
