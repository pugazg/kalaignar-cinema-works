# Kalaignar Cinema Works — Master Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Primary branch: `main`  
Purpose: reusable handover for continuing the archive or onboarding a new Kalaignar cinema work

This is the project-level handover. **Live `main` is authoritative** over copied checkpoints and older handovers.

For a new work, read `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`, `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` when older Tamil typeforms occur, `docs/ARCHIVAL_WORKFLOW.md`, `docs/SOURCE_POLICY.md`, `docs/TRANSCRIPTION_GUIDE.md`, `docs/STATUS_CONSISTENCY_AUDIT.md`, and `docs/START_NEW_CINEMA_WORK_PROMPT.md`.

---

## 1. Project purpose and authority

This repository is a source-led archive of cinema writing credited to **Kalaignar M. Karunanidhi**. The scanned publication controls canonical text for the represented edition.

Authority order for textual questions:

1. rendered scan;
2. verified canonical Tamil;
3. verified scene/song/source-structure derivative;
4. immutable dialogue/song/etc. structured record;
5. translation;
6. reader/export/package;
7. website presentation.

A downstream layer must never silently repair an upstream layer. OCR, film audio, subtitles, web quotations, later editions, existing translations and memory are not canonical substitutes.

---

## 2. Reusable workflow

Proceed through these gates as applicable:

1. source intake;
2. structural mapping;
3. canonical Tamil first pass;
4. visual fidelity audit;
5. historical-Tamil-glyph audit where applicable;
6. scene/source-structure derivatives;
7. dialogue index;
8. character/entity index;
9. song/verse/performance authorship gate;
10. Tamil song derivatives only where full source text authorizes them;
11. English translation;
12. whole-work reader QA/export;
13. Reading Room integration;
14. optional standalone packaging only when separately useful/requested.

**Repository-wide status synchronization is a completion gate at every major phase.**

---

## 3. Rules that must survive every handover

- Preserve source-supported spelling, punctuation, exact speaker labels, scene-heading irregularities, repetition, code-switching, stage directions, performance structures and embedded texts.
- Historical Tamil glyph identity must be decoded from source evidence, not modern visual resemblance. Never global-replace historical glyph families.
- Scene numbering may be absent or irregular. Archive navigation IDs must never be presented as printed scene numbers.
- Unlabelled speech may receive downstream context attribution only when evidence supports it; this does not manufacture a printed label.
- Cross-page utterances remain one logical source unit with multi-page provenance.
- Decorative separators such as `★` or `* * *` are structural, not prose.
- Whole-work QA must catch duplicate derivative ownership.
- Story/dialogue credit is not lyric credit. Song authorship requires item-level evidence.
- Source-only performance cues stay source-only in English; absent lyrics must never be reconstructed.
- If a closed dialogue record owns embedded action or irregular internal text, keep that source ownership intact rather than splitting it for schema neatness.
- If a retained occurrence spans a performance cue and a separately labelled spoken token, each distinct printed span may be represented once while linking the same occurrence ID; do not duplicate a source span.

---

## 4. Repository-wide synchronization gate

At the end of each major phase reconcile at minimum:

### Work-local
- `works/<work-id>/metadata.yaml`;
- work README;
- active layer README/index/QA files;
- work-specific handover;
- next-chat prompt.

### Repository-wide
- `data/works.json`;
- root `README.md`;
- this master handover;
- `docs/STATUS_CONSISTENCY_AUDIT.md`;
- any shared guide whose reusable policy changed.

Historical checkpoint files may retain historical counts when clearly labelled historical.

---

## 5. Translation and reader architecture

For screenplay translation:

- use scene-sharded records;
- retain stable unit IDs and exact Tamil speaker labels;
- link explicit speech to immutable dialogue IDs;
- retain source-role origin for context-attributed supplements;
- preserve stage directions, written text, chants/japa, performance cues and other source structures distinctly;
- keep page provenance and cross-page units intact;
- link song/performance occurrence evidence without duplicating source spans;
- preserve source irregularity honestly.

Before declaring translation complete, perform whole-work reconciliation rather than trusting batch counts. Reader/export outputs should be generated from verified structured translation rather than maintained as an independent manual copy.

Non-scene sources must keep their natural model. For example, `மந்திரி குமாரி` uses one story-summary structure plus 15 performance blocks, not synthetic screenplay scenes.

---

## 6. Working style

When the user says **“Proceed with next activity”** and the next action is already documented:

- fetch live `main` first;
- continue without redundant questions;
- inspect authoritative source/derivative state;
- choose a meaningful bounded batch;
- fetch missing ranges if a large source read is truncated;
- complete source/content reconciliation and status synchronization before claiming completion;
- report exact commits/checkpoints.

A genuine source ambiguity can justify pausing; routine continuation does not.

---

## 7. Current high-level project checkpoint — 2026-09-10

- **Parasakthi** — complete-verified canonical/structured English reader work.
- **Tirumbippaar!** — complete-verified Tamil, structured derivatives, English translation, reader QA and deterministic EPUB QA. EPUB SHA-256 remains `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`.
- **Manohara** — complete-verified Tamil, 57/57 archival scenes, 983 dialogue records, 1,190 English units; reader/export QA PASS; Reading Room ready.
- **Kalaignar Thirai Isai Paadalgal** — 54/54 verified Tamil and English songs; reader/export and Reading Room payload QA PASS; site not applied.
- **Manthiri Kumari** — 12/12 canonical pages; one story-summary derivative + 15 performance records; English 13 story-summary units + 15 performances / 52 sections / 234 paired line-cues; bilingual reader and Reading Room payload QA PASS; item-level lyricist state remains 0 verified / 15 unresolved.
- **Raja Rani** — 79/79 source pages, 70/70 screenplay pages, 58/58 scene derivatives, 1,071 dialogues, 80 labels / 44 entities, 1,236 screenplay English units, 11/11 numbered songs / 181 line-cues; reader and Reading Room payload QA PASS.
- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **complete-verified 63/63 / 1,210 units**; reader/export QA PASS; Reading Room payload QA PASS; site not applied.
- **Naam / நாம்** — canonical Tamil **67/67 COMPLETE-VERIFIED**; scenes **45/45**; dialogues **590**; characters **28 / 45/45 / 590/590**; song/performance gate **7/7 reconciled**; English **5/45 verified / 131 units / 99 immutable dialogue links / 1 of 7 performance records translated**.
- **Vandikkaran Magan / வண்டிக்காரன் மகன்** — canonical Tamil **87/87 COMPLETE-VERIFIED**; scenes **72/72**; dialogues **773 / 38 labels / reconciled QA PASS**; characters **32 / 38/38 / 773/773**; song/performance **9/9 source-only QA PASS**; English **72/72 COMPLETE-VERIFIED / 1,181 units / 773 dialogue links / 27 source-unlabelled / 58 cross-page / 9/9 performance identities**; reader/export **QA PASS**; Reading Room payload **QA PASS — 1,610,402 bytes / `1d1b611c1261eac75577c8c0499123c260406005f26448bb9aac5f6df22339ba`**; site not applied.
- **Maruthanattu Ilavarasi / மருதநாட்டு இளவரசி** — source intake **COMPLETE**, structural mapping **COMPLETE-VERIFIED-CORRECTED**; 22-page image-only booklet / body PDF 2–22; printed credit `வசனம் : மு. கருணாநிதி.`; observed source headings **2,3,4,5,6,7,8,9,10** with unnumbered opening PDF 2–4; PDF 11 directly confirms `காட்சி 7.`; canonical Tamil first pass **10/21 DRAFT through PDF 11**; prospective glyph coverage **10/21**, final visual/glyph **0/21**. Next: PDF 12–16 Tamil T1.

Ammayappan and Naam remain closed at their recorded checkpoints. **Vandikkaran Magan now has no required repository-internal production phase remaining: source/Tamil, structured derivatives, English translation, deterministic reader/export and source-linked Reading Room payload are complete-verified / QA PASS. The separate Reading Room site remains not-applied and requires explicit authorization before modification.**

---

## 8. Naam active checkpoint

Work: `works/naam/`  
Source: `TVA_BOK_0064201_நாம்.pdf`

- intake / map / first pass: **complete / verified / 67/67 COMPLETE**;
- canonical Tamil: **67/67 COMPLETE-VERIFIED**;
- visual-fidelity / historical-glyph final / dual-gate: **67/67 / 67/67 / 67/67**;
- open source uncertainties: **0**;
- user manual source verdicts: PDF 5 `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`, PDF 10 `நீ இங்கே வேலை பார்க்கிற வரைக்கும்`, PDF 24 `கெளரவம் தேடி`;
- final audit: `works/naam/notes/canonical-closure-user-manual.md`;
- scene derivatives: **45/45 COMPLETE-VERIFIED**; boundary ownership QA **PASS — 0 gaps / 0 overlaps**; dialogue index **590 records COMPLETE-VERIFIED / QA PASS**; character/entity index **28 entities COMPLETE-VERIFIED / QA PASS**; song/performance **7/7 reconciled**; English **scene 1/45 PILOT-VERIFIED / 21 units**.

**Exact next activity:** Translate and verify source-numbered scenes 2–5 as the first bounded post-pilot English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units and stage/narrative ownership; and use only the reconciled seven-record song/performance layer for performance links. Do not alter closed Tamil or structured source layers.

## 9. Ammayappan closed checkpoint

Work: `works/ammaiyappan/`  
Source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

### Frozen source layers

- canonical Tamil: **105/105 dual-gate complete-verified**;
- PDF 10 source correction: `மாடம்`, commit `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`;
- source-visible boundaries / distinct heading forms: **63 / 41**;
- archive-only scene derivatives: **63/63**;
- boundary ownership: **PASS — 0 gaps / 0 overlaps / 105 pages**;
- dialogue index: **1,009 explicit + 16 supplements = 1,025 downstream units**;
- exact source speaker labels: **62**;
- unresolved source-role blocks / source punctuation normalizations: **0 / 0**;
- character/entity layer: **26 entities / 62/62 labels / 1,025/1,025 units**;
- song/performance gate: **5 retained occurrences**, scenes **7, 10, 19, 40, 59**; no full named lyric bodies and no standalone Tamil lyric files.

Post-closure delimiter authority remains unchanged: scene 3 `பூங் ; ...` and scene 5 `திரு; ...` are exact non-colon source forms.

### English translation — complete

- verified scenes: **63/63**;
- verified units: **1,210**;
- dialogue: **1,025** = **1,009 explicit + 16 source-role supplements**;
- stage/action: **181**;
- standalone song-reference: **3**;
- japa: **1**;
- standalone literary-verse / written-text: **0 / 0**;
- cross-page: **28**;
- unique occurrence links: **5/5** — `ammaiyappan-song-001` through `ammaiyappan-song-005`;
- frozen Tamil/dialogue/character/song files modified by English: **no**;
- whole-work source/linkage reconciliation: **PASS** — `works/ammaiyappan/translations/FINAL_TRANSLATION_QA.md`;
- reader/export preflight: **complete-pass**;
- reader/export generation: **complete-verified — generated-output QA PASS**;
- Reading Room payload: **complete-verified — QA PASS; site application not-applied**.

### Final batch 61–63 safeguards

Batch 61–63 is **22/22 verified units**: **16 explicit dialogue + 0 supplements + 6 stage/action**. It adds no cross-page unit and encounters no retained song/performance occurrence.

- Scene 61 remains action-only; the rescue/masked-substitute sequence creates no invented speech and does not identify the substitute before scene 62.
- Scene 62 preserves Sukhadev's halting explanation, Maappillaithaasar's atonement speech and the source's `speech ends; life ends` parallel without external expansion.
- Scene 63 preserves exact `முத்` / `முத்தா` provenance, **Aththan**, the recognition shift **Princess → Amma**, **Karmaveeran**, and the movement from family reunion to Pazhuthar / motherland liberation.
- Scene 63's closing four-line stanza remains inside immutable dialogue `ammaiyappan-s063-d012`; no synthetic literary-verse or song occurrence is created.
- Frozen `அண்ணலின் விலங்கொடிப்ப ோம்` retains `Annal` as a source term rather than receiving an unsupported stronger gloss or silent Tamil normalization.
- The compact martial saying is kept source-bounded and is not replaced by an external proverb text.
- No frozen Tamil/dialogue/character/song evidence was modified.

### Final English reconciliation

`translations/FINAL_TRANSLATION_QA.md` records **PASS**:

- all 63 scene records present;
- all **1,009** immutable explicit dialogue records linked exactly once;
- all **16** closed source-role supplements linked exactly once with original provenance;
- all **181** separately owned stage/action spans retained source-bounded;
- all **28** cross-page units remain whole;
- all **5** retained source-visible occurrences represented without reconstructing absent lyrics/title/authorship;
- structural stars translated as prose: **0**;
- frozen source layers modified: **0**.

The PASS is source/linkage reconciliation; it does not claim an executable JSON-schema validator or CI run unless separately executed and recorded.

### Reader/export preflight — PASS

Workflow `.github/workflows/ammaiyappan-english-reader-preflight.yml` passed at run **34025680568** / head `ae554f92faf7a9b0f4005c42cc28c8b3e8e95d36`. It verified all **63 scenes / 1,210 units / 1,025 dialogue-source links / 28 cross-page units / five occurrence identities across seven intentional source-span links** with zero errors or warnings.

### Reader/export package — PASS

`works/ammaiyappan/editions/en/` contains deterministic Markdown, standalone HTML and machine-readable JSON plus `QA_REPORT.md` and `manifest.json`. Generated-output QA confirms all **1,210** verified units exactly once in each export, all **1,025** dialogue/source-role links, all **28** cross-page units and all **5 occurrence identities / 7 source-span links**. Output SHA-256 values are `50fb3baf33c3b249ce32dba5947fe73871f5ef36d18f41807d2ad3ed3d3fb549` (Markdown), `c8fba94766a4082d5288bcd5f9ff63bde863d942f7b9aaf824a3a1c5bcc0f22a` (HTML) and `a72b758d397a909cb9004fd9e34ffedcc4bb72027d29d11aec994df6b4ea4ce3` (JSON). No frozen source evidence was modified.

**Exact next activity:** no required repository-internal Ammayappan production work remains. Apply the complete-verified Reading Room payload in the separate implementation repository only when explicitly authorized; site application remains not-applied.

### Reading Room payload — complete-verified

`works/ammaiyappan/integrations/reading-room/reading-room.json` is QA PASS with **63 Tamil scene texts / 1,210 English units / 1,025 dialogue-source links / 28 cross-page units / 5 occurrence identities / 7 source-span links**. Payload SHA-256 `f00efb816edf08b43702a3a1a9d71ed9cc54fd1a803b8881bc6e2c6466de1f8c`. The source booklet's 63 archival scene ordinals remain derivative navigation only. Site application is **not-applied** and requires separate explicit authorization.

---

## 10. Downstream dispositions for completed works

- **Raja Rani:** no required repository-internal production work remains; its verified Reading Room payload should be applied only in the separate implementation repository when explicitly authorized.
- **Manthiri Kumari:** no required repository-internal production work remains; preserve its natural story-summary + 15-performance navigation and unresolved item-level authorship tiers when integrating externally.
- **Tirumbippaar!:** no required repository-internal translation/reader/package work remains.

The preferred public destination remains **`https://nenjukkuneethi.org/read` — Kalaignar Digital Library / Reading Room**.

<!-- Naam song gate reconciled 7/7 -->
**Naam current structured checkpoint:** song/performance gate **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED** after the pre-English 45-scene sweep restored scene-1 PDF 6–7 `(பாட்டு)` as append-only `naam-perf-007`; 1 item-level source attribution (`ஆயிரம் தெய்வங்கள்` → `பாரதியார்`), 6 unresolved item-level authorships. **Next:** Begin Phase 9 source-linked English translation from the complete-verified Tamil, scene, dialogue, character/entity and reconciled song/performance layers. Preserve source scene order and exact Tamil speaker labels as metadata; link labelled dialogue to immutable IDs; keep source-unlabelled speech unassigned; translate all seven retained performance records from their source-visible Tamil only, carrying `பாரதியார்` attribution only for `ஆயிரம் தெய்வங்கள்` and leaving the other six item-level authorship states unresolved. Follow `docs/SONG_TRANSLATION_GUIDE.md`, begin with a scene-1 pilot, run source-link/dialogue/performance coverage QA, and do not alter closed Tamil or structured source layers.


<!-- Naam English pilot current -->
**Naam / நாம் current:** English translation **scene 1/45 PILOT-VERIFIED — 21 units / 14 dialogue links / 1 of 7 performance records / 23 song mappings**; song/performance gate **7/7 reconciled**; no source-layer rewrites. **Next:** Translate and verify source-numbered scenes 2–5 as the first bounded post-pilot English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units and stage/narrative ownership; and use only the reconciled seven-record song/performance layer for performance links. Do not alter closed Tamil or structured source layers.


<!-- Naam English scenes 2-5 current -->
**Naam / நாம் current English checkpoint:** **5/45 scenes VERIFIED / 131 units / 99 immutable dialogue links / 1 of 7 performance records translated / 23 song mappings**. Scenes 2–5 are **110 units / 85/85 labelled-dialogue links**, with one source-unlabelled utterance deliberately unassigned and 0 performance occurrences. No closed source layer changed. **Next:** Translate and verify source-numbered scenes 6–10 as the next bounded English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units and stage/narrative ownership; translate only source-visible performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-001` in scene 7 with its specific `பாரதியார்` attribution and `naam-perf-002` in scene 8 with unresolved item-level authorship; and do not alter closed Tamil or structured source layers.


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
## வண்டிக்காரன் மகன் active checkpoint

- source: `TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`**;
- printed source roles: **`மூலக்கதை அண்ணா` / `திரைக்கதை-வசனம் கலைஞர்`**;
- first edition: **1978**; publisher: **கனி பதிப்பகம், சென்னை-34.**;
- structure: PDF 4–5 foreword; PDF 6–87 screenplay/dialogue; PDF 88–89 film credits; PDF 90 back cover;
- scene-heading mapping: **70/70 observed occurrences**, including 15 suffix insertions and combined `45-46`;
- canonical Tamil: **NOT-STARTED**; later derivatives: **BLOCKED**;
- source film credits include `பாடல்கள்: கவிஞர் வாலி`; item-level occurrence mapping remains deferred to the song gate.

**Exact next activity:** Begin canonical Tamil first-pass transcription from PDF 4 onward in source order, preserving front matter and screenplay exactly with stable PDF/printed-page anchors. Use the historical-glyph guide prospectively on every page, keep uncertain readings explicit, and do not call pages verified during first pass. No structured derivative work begins until the later separate visual-fidelity + historical-glyph verification gate closes.


<!-- Vandikkaran Magan first pass current -->
## வண்டிக்காரன் மகன் active first-pass checkpoint

- intake / structural map: **COMPLETE / COMPLETE-VERIFIED**;
- canonical Tamil first pass: **PDF 4–8 / 5 of 84 DRAFT**;
- screenplay drafted through **PDF 8 / printed 7**;
- historical-glyph prospective check: **5/5 PASS**, final verification **0/84**;
- visual fidelity: **not-started**;
- derivatives: **blocked**.

**Exact next activity:** Continue canonical Tamil first-pass transcription with PDF 9–13 (five source pages) in source order. Preserve exact source scene headings, speaker labels, punctuation, stage directions and page boundaries; keep every page draft during first pass; inspect the historical Tamil glyph families prospectively occurrence by occurrence from enlarged source pixels; record any uncertainty explicitly; and do not begin visual-fidelity verification or structured derivatives yet.


---

## 11. மருதநாட்டு இளவரசி active checkpoint

Work: `works/maruthanattu-ilavarasi/`
Source: `TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf`

- intake: **COMPLETE**;
- mapping: **COMPLETE-VERIFIED**;
- source: **22 PDF pages / 9,330,870 bytes / SHA-256 `8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f` / image-only**;
- body: **PDF 2–22 / logical printed 1–21**;
- printed credit: **`வசனம் : மு. கருணாநிதி.`**;
- source headings: **2,3,4,5,6,8,9,10**;
- opening PDF 2–4 unnumbered; `காட்சி 7.` not observed;
- historical-glyph gate: **required**;
- canonical Tamil: **NOT STARTED**;
- later derivatives: **BLOCKED**.

**Exact next activity:** Begin canonical Tamil first-pass transcription from PDF 2 onward in five-source-page batches, starting with PDF 2–6. Preserve source order, exact speaker labels, punctuation, stage directions, the unnumbered opening structure, printed scene numbering anomalies and stable PDF/logical-printed page anchors. Inspect all historical-glyph-sensitive families from enlarged source pixels on every page; keep first-pass pages draft, record uncertainty explicitly, and do not begin scene/dialogue/character/song/English derivatives until the later separate full visual-fidelity and historical-glyph verification gates close.
