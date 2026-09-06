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

## 7. Current high-level project checkpoint — 2026-09-06

- **Parasakthi** — complete-verified canonical/structured English reader work.
- **Tirumbippaar!** — complete-verified Tamil, structured derivatives, English translation, reader QA and deterministic EPUB QA. EPUB SHA-256 remains `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`.
- **Manohara** — complete-verified Tamil, 57/57 archival scenes, 983 dialogue records, 1,190 English units; reader/export QA PASS; Reading Room ready.
- **Kalaignar Thirai Isai Paadalgal** — 54/54 verified Tamil and English songs; reader/export and Reading Room payload QA PASS; site not applied.
- **Manthiri Kumari** — 12/12 canonical pages; one story-summary derivative + 15 performance records; English 13 story-summary units + 15 performances / 52 sections / 234 paired line-cues; bilingual reader and Reading Room payload QA PASS; item-level lyricist state remains 0 verified / 15 unresolved.
- **Raja Rani** — 79/79 source pages, 70/70 screenplay pages, 58/58 scene derivatives, 1,071 dialogues, 80 labels / 44 entities, 1,236 screenplay English units, 11/11 numbered songs / 181 line-cues; reader and Reading Room payload QA PASS.
- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **complete-verified 63/63 / 1,210 units**; reader/export **complete-verified with generated-output QA PASS**; Reading Room payload is next.

Current active mirrors use the corrected Ammayappan 1,025-unit source authority and complete English checkpoint.

---

## 8. Ammayappan active checkpoint

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
- Reading Room integration: **ready for payload construction/QA**.

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

**Exact next activity:** create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures. Preserve the 63 scene IDs strictly as archive navigation, exact source/page provenance, all speaker-label/source-role distinctions and all five occurrence identities; never reconstruct absent lyrics, titles or authorship.

---

## 9. Downstream dispositions for completed works

- **Raja Rani:** no required repository-internal production work remains; its verified Reading Room payload should be applied only in the separate implementation repository when explicitly authorized.
- **Manthiri Kumari:** no required repository-internal production work remains; preserve its natural story-summary + 15-performance navigation and unresolved item-level authorship tiers when integrating externally.
- **Tirumbippaar!:** no required repository-internal translation/reader/package work remains.

The preferred public destination remains **`https://nenjukkuneethi.org/read` — Kalaignar Digital Library / Reading Room**.