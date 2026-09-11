# Kalaignar Cinema Works

A source-led archive of screenplay, dialogue, song, and related cinema writing credited to **Kalaignar M. Karunanidhi**.

The repository preserves source provenance, canonical transcription and derivative representations separately.

## Archival principles

1. **Primary source first.** The scanned publication controls canonical transcription.
2. **No silent correction.** Source anomalies stay documented.
3. **Page provenance is mandatory.** Transcribed, indexed and translated units remain traceable to PDF/printed pages.
4. **Uncertainty stays visible.** Interpretive pressure points are reviewed rather than guessed away.
5. **Source and derivatives are separate.** English translation never overwrites Tamil.
6. **Authorship is not inferred.** Mixed-credit material requires item-level evidence.
7. **Rights are not assumed.** No repository-wide public-domain/open-license claim is made.
8. **Current status mirrors must agree.** A major phase is not durably closed until work-local status and repository-wide current mirrors are synchronized.
9. **Historical Tamil glyph identity must be decoded, not visually imitated.** For older-print sources, use `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` where historical typeforms occur.

## Reusable onboarding for new cinema works

Read `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`, `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` when older Tamil typeforms may occur, `docs/ARCHIVAL_WORKFLOW.md`, `docs/SOURCE_POLICY.md`, `docs/TRANSCRIPTION_GUIDE.md`, `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`, and `docs/START_NEW_CINEMA_WORK_PROMPT.md` before starting a new work.

The preferred public reading destination is the **Kalaignar Digital Library / Reading Room at `https://nenjukkuneethi.org/read`**. Preserve each source's natural structure; do not force non-screenplay booklets into screenplay scenes.

## மருதநாட்டு இளவரசி status

- canonical Tamil: **21/21 COMPLETE-VERIFIED**;
- source geometry: **linear PDF 2–22 ↔ logical printed 1–21; no duplicate spreads**;
- visual fidelity / final glyph verification: **21/21 / 21/21 PASS**;
- open uncertainties: **0**;
- structured derivatives: **NOT STARTED / READY-NEXT**.

**Next:** build source-faithful scene-text derivatives while preserving the unnumbered opening and source headings 2–10.

## வண்டிக்காரன் மகன் status

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` is now a **complete-verified Tamil + structured + English reader + Reading Room payload archival work**.

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 open uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogues: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**;
- character/entity index: **32 entities / 38/38 labels / 773/773 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance gate: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- item-level lyric authorship: **0 source-attributed / 6 unresolved / 3 not-applicable**; PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only;
- English translation: **72/72 COMPLETE-VERIFIED / WHOLE-WORK QA PASS — 1,181 units / 773 dialogue links / 27 source-unlabelled spoken units / 58 cross-page units / 9/9 performance occurrences**;
- deterministic English reader/export: **COMPLETE-VERIFIED / QA PASS**;
- Reading Room payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS — 1,610,402 bytes / SHA-256 `1d1b611c1261eac75577c8c0499123c260406005f26448bb9aac5f6df22339ba`**;
- Reading Room payload authoritative-input aggregate: **150 files / SHA-256 `f76205e7994d53ce41b8554dc3f5597370e968abdadf43821e99a7e5a6850de0`**;
- site application: **not-applied**.

**Next:** No required repository-internal `வண்டிக்காரன் மகன்` production work remains. Keep canonical Tamil, scene, reconciled immutable dialogue, character/entity, song/performance, English translation, reader/export and Reading Room payload layers closed. Apply `works/vandikkaran-magan/integrations/reading-room/reading-room.json` in the separate Kalaignar Digital Library / Reading Room implementation repository only when that repository is explicitly authorized for modification; fetch its live state first and use a fail-closed importer pinned to this verified payload/manifest. Site application remains not-applied here.
## நாம் status

`TVA_BOK_0064201_நாம்.pdf` now has **complete-verified canonical Tamil**. The user's manual controlling-scan review resolved the three former source-obscuration holds.

- canonical Tamil / visual / glyph-final / dual-gate: **67/67 / 67/67 / 67/67 / 67/67 COMPLETE**;
- open source uncertainties: **0**;
- final manual-source readings: PDF 5 `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`, PDF 10 `நீ இங்கே வேலை பார்க்கிற வரைக்கும்`, PDF 24 `கெளரவம் தேடி`;
- final canonical audit: `works/naam/notes/canonical-closure-user-manual.md`;
- scene derivatives: **45/45 COMPLETE-VERIFIED; boundary ownership QA PASS**;
- dialogue index: **590 immutable records / COMPLETE-VERIFIED / QA PASS**;
- character/entity index: **28 entities / 45/45 labels / 590/590 records / COMPLETE-VERIFIED / QA PASS**;
- dialogue index: **590 immutable records / COMPLETE-VERIFIED / QA PASS**;
- character/entity index: **28 entities / 45/45 labels / 590/590 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance/authorship gate: **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED / QA PASS / 1 source-attributed + 6 unresolved item-level authorships**;
- English translation: **45/45 COMPLETE-VERIFIED — 797 units / 590/590 dialogue links / 7/7 performance records / 138 mappings / 1 chant; whole-work reconciliation PASS; reader/export READY-NEXT**.

**Next:** No required repository-internal processing remains for நாம். Reader/export and the source-linked Reading Room payload are complete-verified with QA PASS. Keep Tamil, scene, dialogue, character, song-source and English records closed. Apply `works/naam/integrations/reading-room/reading-room.json` in the separate Kalaignar Digital Library / Reading Room implementation repository only when that repository is explicitly authorized for modification; before applying it, fetch that repository's live state and use a fail-closed importer pinned to this verified payload/manifest. Site application remains not-applied here. Do not create a PDF, EPUB or other publication package unless separately requested.

## ராஜா ராணி status

`TVA_BOK_0017188_ராஜா_ராணி.pdf` is a **complete-verified bilingual archival work with deterministic reader/export and Reading Room payload QA PASS**.

- source scan: **80 PDF pages**; SHA-256 `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`;
- verified source / screenplay pages: **79/79 / 70/70**;
- scene derivatives: **58/58**;
- immutable dialogue records: **1,071**;
- labels / entities: **80/80 / 44**;
- English screenplay: **1,236 units**;
- numbered songs: **11/11 / 181 Tamil-English line-cues**;
- reader/export: **QA PASS**;
- Reading Room payload: **QA PASS**, `974,510` bytes, SHA-256 `ab1058cb5a22ba78e68938f50efc586cc53eb07ef544bdf3919bb3c4b8c46c9b`;
- site application: **not-applied**.

**Next:** no required Raja Rani repository-internal work remains; apply its payload in the separate Reading Room implementation repository only when explicitly authorized.

## மந்திரி குமாரி status

`TVA_BOK_0026144_மந்திரி_குமாரி.pdf` is a **14-page film story-and-song booklet** whose source-appropriate Tamil, English, bilingual reader and Reading Room integration payload are now complete-verified.

- source classification: **film story-and-song booklet**, not a full screenplay/dialogue book;
- direct printed Kalaignar credit: **`கதை, வசனம் : மு. கருணாநிதி`**;
- source SHA-256: `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`;
- canonical Tamil: **PDF 2–13, 12/12 pages complete-verified, 0 unresolved readings**;
- post-fidelity source corrections: **recorded, applied and reconciled**;
- story-summary Tamil derivative: **1/1 continuous record, PDF 3–5**;
- song/performance Tamil records: **15/15 complete-verified, PDF 6–13**;
- current-anthology relationship: **1 confirmed witness / 14 source-only blocks**;
- booklet item-level lyric authorship: **0 verified / 15 unresolved**;
- English story-summary translation: **1/1 / 13 logical units / 1 cross-page unit**;
- English performance translation: **15/15 / 52 sections / 234 Tamil-English line-cues / 0 mismatches**;
- bilingual reader/export: **complete-verified, QA PASS**;
- reader navigation: **16 natural source structures — 1 story summary + 15 performances**;
- reader performance mapping: **52 sections / 234 Tamil line-cues / 234 English line-cues / 0 mismatches**;
- synthetic screenplay scene IDs created: **0**;
- canonical Tamil changes caused by translation/reader/payload: **0**;
- authorship upgrades caused by downstream layers: **0**;
- Reading Room payload: **payload-complete-verified — QA PASS**;
- payload mode: **`source-linked-composition`**;
- payload source-link targets: **32**;
- payload: `works/manthiri-kumari/integrations/reading-room/reading-room.json`;
- payload bytes: **15,704**;
- payload SHA-256: `20a0db293b936757e7d01def336252f28543337f319dfae6ad7bf5ae886bab43`;
- Reading Room site application: **not-applied**.

The source-linked payload preserves the booklet's natural `கதைச்சுருக்கம்` + 15-performance navigation, PDF-page provenance, source-visible cues, the block-11 anthology witness, and the unresolved item-level lyricist state. Performance 13 retains the printed heading `பார்த்திபன்—மந்திரிகுமாரி` while its internal source labels remain `பார்த்திபன்` / `அமுதவல்லி`.

**Next:** no required repository-internal Manthiri Kumari work remains. Apply the verified payload in the separate Reading Room implementation repository only when that repository is explicitly authorized for modification.

## அம்மையப்பன் status

`TVA_BOK_0064230_அம்மையப்பன்.pdf` now has **closed canonical Tamil, closed structured derivatives, and complete-verified English translation with whole-work reconciliation PASS**.

- canonical Tamil: **105/105 dual-gate complete-verified**;
- visual fidelity / historical-glyph audit: **105/105 / 105/105 PASS**;
- unresolved canonical markers: **0**;
- late PDF 10 heading correction: **`மாடம்`**, commit `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`;
- canonical source-visible scene boundaries: **63**;
- archive-only scene derivatives: **63/63 complete-verified**;
- boundary ownership: **PASS — 0 gaps / 0 overlaps / 105 pages represented**;
- explicit colon-labelled dialogue records: **1,009**;
- source-role supplements: **16**;
- downstream dialogue units: **1,025**;
- character/entity index: **26 entities / 62 exact labels / 1,025/1,025 dialogue-unit coverage**;
- post-closure source delimiter repairs: scene 3 `பூங் ; ...` and scene 5 `திரு; ...` remain exact non-colon source forms;
- song/performance authorship gate: **64/64 candidates reviewed / 5 retained source-visible occurrences / 0 standalone lyric files**;
- English translation: **complete-verified — 63/63 archival scenes / 1,210 units**;
- English dialogue coverage: **1,009 explicit records + 16 source-role supplements = 1,025 dialogue units**;
- English stage/action units: **181**;
- English song-reference units: **3**;
- English japa units: **1**;
- English standalone literary-verse / written-text units: **0 / 0**;
- English cross-page units: **28**;
- retained source-only occurrence links translated: **5/5** — `ammaiyappan-song-001` through `ammaiyappan-song-005`;
- whole-work English reconciliation: **PASS** — `works/ammaiyappan/translations/FINAL_TRANSLATION_QA.md`;
- reader/export preflight: **complete-pass — executable 63-scene / 1,210-unit integrity gate**;
- reader/export generation: **complete-verified — Markdown / HTML / JSON / manifest; generated-output QA PASS**;
- Reading Room payload: **complete-verified — QA PASS; site application not-applied**.

Final batch 61–63 adds **22 verified units**: **16 explicit dialogue links + 6 stage/action units**, with no source-role supplement, retained song/performance occurrence or new cross-page unit. Scene 61 remains action-only and does not identify the masked substitute before scene 62. Scene 62 preserves the masked-prisoner revelation, Sukhadev's halting explanation, Maappillaithaasar's atonement speech and the final `speech ends; life ends` parallel without external expansion. Scene 63 preserves the `Aththan` / `Amma` register, mother-recognition and liberation rhetoric; its closing stanza remains owned by immutable dialogue `ammaiyappan-s063-d012` rather than becoming a synthetic verse occurrence.

The **Ammayappan English reader/export package now passes generated-output QA**. Markdown, standalone HTML and machine-readable JSON each preserve all 1,210 verified units exactly once, all 1,025 dialogue/source-role links, all 28 cross-page units and all five occurrence identities across seven intentional source-span links. The integrity manifest records deterministic authoritative-input and output hashes. Output SHA-256 values are `50fb3baf33c3b249ce32dba5947fe73871f5ef36d18f41807d2ad3ed3d3fb549` (Markdown), `c8fba94766a4082d5288bcd5f9ff63bde863d942f7b9aaf824a3a1c5bcc0f22a` (HTML) and `a72b758d397a909cb9004fd9e34ffedcc4bb72027d29d11aec994df6b4ea4ce3` (JSON). No frozen Tamil or structured source evidence was modified.

The **Ammayappan Reading Room payload now passes QA**: 63 Tamil scene texts, all 1,210 verified English units, 1,025 dialogue/source-role links, 28 cross-page units and all 5 occurrence identities / 7 source-span links. Payload SHA-256 `f00efb816edf08b43702a3a1a9d71ed9cc54fd1a803b8881bc6e2c6466de1f8c`. The separate site repository has not been modified.

**Next:** apply the verified payload in the separate Reading Room implementation repository only when explicitly authorized; site application remains not-applied.

## கலைஞர் திரை இசைப் பாடல்கள் status

The dedicated anthology work `works/kalaignar-thirai-isai-paadalgal/` is complete-verified for its numbered corpus.

- source: `TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`;
- source SHA-256: `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- numbered songs: **54/54 Tamil complete-verified**;
- English translation: **54/54 complete-verified**;
- reader/export: **QA PASS**;
- Reading Room payload: **QA PASS — 23 film groups / 54 songs / 1,105 paired line-cues**;
- site application: **not-applied**.

The anthology attribution tier remains separate from original-film primary-source verification.

**Next:** apply the verified payload in the separate Reading Room implementation repository only when explicitly authorized.

## மனோகரா status

`TVA_BOK_0010102_மனோகரா.pdf` has complete-verified Tamil, structured derivatives, English translation and reader/export.

- canonical Tamil: **82/82 pages**;
- archival scenes: **57/57**;
- dialogue records: **983**;
- character labels/entities: **111 / 37**;
- English: **1,190/1,190 units**;
- reader/export: **QA PASS**;
- Reading Room integration: ready.

**Next:** integrate the verified Manohara reader into the Reading Room while preserving its archival scene IDs as navigation rather than printed source numbering.

## Parasakthi status

Parasakthi has complete-verified canonical Tamil and source-linked English reader work.

- canonical Tamil: **54/54 pages**;
- scene layer: **46/46**;
- dialogue index: **642 records**;
- song/verse authorship: **14/14 verified**;
- English: **769/769 units**;
- reader/export: **QA PASS**.

**Next:** no required translation/reader activity remains; future public access should prioritize Reading Room integration.

## திரும்பிப்பார்! status

`TVA_BOK_0014652_திரும்பிப்பார்.pdf` is complete-verified through deterministic reader/export and EPUB packaging.

- canonical Tamil: **104/104 pages**;
- scenes: **93/93**;
- dialogue records: **1,040**;
- English: **1,321 verified units**;
- reader/export: **QA PASS**;
- EPUB 3: **QA PASS**, SHA-256 `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`.

**Next:** no required Tirumbippaar repository-internal translation/reader/package work remains.

## Status vocabulary

`not-started` · `draft` · `draft-complete` · `review` · `verified` · `pilot-verified` · `complete-verified` · `unresolved`

Translation status is independent of source-transcription verification status.

<!-- Naam song gate reconciled 7/7 -->
**Naam current structured checkpoint:** song/performance gate **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED** after the pre-English 45-scene sweep restored scene-1 PDF 6–7 `(பாட்டு)` as append-only `naam-perf-007`; 1 item-level source attribution (`ஆயிரம் தெய்வங்கள்` → `பாரதியார்`), 6 unresolved item-level authorships. **Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.


<!-- Naam English pilot current -->
**Naam current English checkpoint:** source scene **1/45 PILOT-VERIFIED**, **21 units**, **14/14 immutable dialogue links**, **`naam-perf-007` 1/7 performance occurrence translated**, **23/23 song role/line mappings**, and **0 upstream rewrites**. Song/performance gate is **7/7 reconciled**. **Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.


<!-- Naam English scenes 6-15 current -->
**Naam current English checkpoint:** **15/45 source scenes VERIFIED**, **363 units**, **279 immutable dialogue links**, **3/7 performance records translated**, **57 performance mappings**, **0 upstream rewrites**. Iteration size is now **10 source scenes**. **Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.


<!-- Naam English scenes 16-25 current -->
**Naam current English checkpoint:** **25/45 source scenes VERIFIED**, **501 units**, **380 immutable dialogue links**, **4/7 performance records translated**, **74 performance mappings**, **0 upstream rewrites**. Iteration size remains **10 source scenes**. **Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.


<!-- Naam English scenes 26-35 current -->
**Naam current English checkpoint:** **35/45 source scenes VERIFIED**, **680 units**, **506 immutable dialogue links**, **5/7 performance records translated**, **84 performance mappings**, **1 source-local chant / 16 mappings**, **0 upstream rewrites**. **Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.


<!-- Naam English scenes 36-45 current -->
**Naam current English checkpoint:** **45/45 source scenes VERIFIED**, **797 units**, **590/590 immutable dialogue links**, **7/7 performance records translated**, **138 performance mappings**, **1 source-local chant / 16 mappings**, **whole-work reconciliation READY-NEXT**, **0 upstream rewrites**. **Next:** Run whole-work English translation reconciliation and closure QA across source scenes 1–45 before building the reader/export layer. Verify every translated unit is source-ordered and unique; all 590 immutable dialogue records are linked exactly once; source-unlabelled speech remains unassigned; all seven retained song/performance records are translated without authorship upgrades; the scene-34 chant remains a distinct chant; cross-page provenance and written-text/stage ownership are exact; no duplicate source-span ownership, synthetic scene-end prose, placeholder text, or upstream Tamil/scene/dialogue/character/song-source mutation exists. If and only if that whole-work gate passes, mark English translation complete-verified and begin Phase 10 whole-work reader/export generation.


<!-- Naam English whole-work closure current -->
**Naam current:** English **COMPLETE-VERIFIED**, reconciliation **PASS**, **45/45 / 797 / 590/590 / 7/7 / 138 / chant 1/16**, reader/export **READY-NEXT**, upstream rewrites **0**. **Next:** No required repository-internal processing remains for நாம். Reader/export and the source-linked Reading Room payload are complete-verified with QA PASS. Keep Tamil, scene, dialogue, character, song-source and English records closed. Apply `works/naam/integrations/reading-room/reading-room.json` in the separate Kalaignar Digital Library / Reading Room implementation repository only when that repository is explicitly authorized for modification; before applying it, fetch that repository's live state and use a fail-closed importer pinned to this verified payload/manifest. Site application remains not-applied here. Do not create a PDF, EPUB or other publication package unless separately requested.


<!-- Naam Phase 10 current -->
**Naam Phase 10 current:** reader/export **COMPLETE-VERIFIED / QA PASS** — 45 source-numbered scenes / 797 English units / 590 immutable dialogue links / 7 retained performances / 138 performance mappings / 1 distinct chant (16 mappings) / 12 cross-page units. Reading Room payload **PAYLOAD-COMPLETE-VERIFIED / QA PASS**, SHA-256 `9b97493b820ebd42c822b5fbdc53beda8dbe1d61103a1c9d2abb06a552bcf825`, site application **not-applied**. No PDF/EPUB was generated. **Next:** No required repository-internal processing remains for நாம். Reader/export and the source-linked Reading Room payload are complete-verified with QA PASS. Keep Tamil, scene, dialogue, character, song-source and English records closed. Apply `works/naam/integrations/reading-room/reading-room.json` in the separate Kalaignar Digital Library / Reading Room implementation repository only when that repository is explicitly authorized for modification; before applying it, fetch that repository's live state and use a fail-closed importer pinned to this verified payload/manifest. Site application remains not-applied here. Do not create a PDF, EPUB or other publication package unless separately requested.


<!-- Vandikkaran Magan first pass current -->
**வண்டிக்காரன் மகன் current:** canonical Tamil first pass **PDF 4–8 / 5 of 84 DRAFT**, screenplay through PDF 8 / printed 7; open uncertainty markers **0**; prospective historical-glyph check **5/5 PASS**; verified pages **0**; derivatives **blocked**. **Next:** Continue canonical Tamil first-pass transcription with PDF 9–13 (five source pages) in source order. Preserve exact source scene headings, speaker labels, punctuation, stage directions and page boundaries; keep every page draft during first pass; inspect the historical Tamil glyph families prospectively occurrence by occurrence from enlarged source pixels; record any uncertainty explicitly; and do not begin visual-fidelity verification or structured derivatives yet.
