# நாம் — English translation layer

**Canonical authority:** 67/67 dual-gate verified Tamil, 45/45 verified source-numbered scenes, 590 immutable dialogue records, complete 28-entity character layer, and reconciled 7/7 source-visible song/performance records  
**Target language:** English (`en`)  
**Status:** **COMPLETE-VERIFIED / whole-work reconciliation PASS**

This is a source-linked English derivative. It does not repair, normalize, expand or overwrite the verified Tamil.

## Translation principles

1. Preserve source scene order and printed scene numbers.
2. Preserve exact Tamil speaker labels as metadata; character/entity aliases never rewrite them.
3. Every explicitly labelled utterance links to its immutable dialogue ID exactly once.
4. Source-unlabelled speech remains unassigned.
5. Narrative, stage directions, performance cues and songs remain distinct unit kinds.
6. Cross-page source units remain one logical translation unit with complete page provenance.
7. Songs use `semantic-poetic-source-faithful` translation and explicit Tamil→English line/cue mapping.
8. Do not import soundtrack, subtitle, web or remembered lyric wording.
9. Translation never upgrades authorship. `ஆயிரம் தெய்வங்கள்` alone carries the source-printed `பாரதியார்` attribution; the other six retained performance records remain unresolved at item level.
10. Verified Tamil irregularities are interpreted conservatively in English and never silently repaired upstream.

## Pilot — source scene 1

Scene 1 covers PDF 5–7 and includes the source-visible PDF 6–7 `(பாட்டு)` restored during the pre-English song-gate reconciliation as append-only `naam-perf-007`.

- translation units: **21**;
- immutable dialogue links: **14/14**;
- narrative units: **4**;
- stage-direction units: **1**;
- performance-cue units: **1**;
- full song units: **1**;
- song/performance occurrence links: **1/1 — `naam-perf-007`**;
- Tamil→English song role/line mappings: **23/23**;
- cross-page translation units: **1 — `naam-en-s001-u021` across PDF 6–7**;
- invented speaker assignments: **0**;
- canonical Tamil / scene / dialogue / character / song-source changes caused by translation: **0 / 0 / 0 / 0 / 0**.

The pilot establishes the initial English voice: preserve rationalist satire, colloquial address, rhetorical repetition and concrete imagery before optimizing smoothness. Deity names and culturally loaded terms are transliterated where a generic substitute would flatten the source.

Detailed pilot decisions and integrity checks are in `PILOT_REVIEW.md`; machine-readable checks are in `pilot-qa.json`.

## Next gate

Begin Phase 10 whole-work reader/export generation from the complete-verified Tamil and English structured layers. Build deterministic Markdown, standalone HTML, machine-readable JSON, reader QA, and an integrity manifest; verify all 45 source scenes appear exactly once in canonical order and all 797 verified English units render exactly once; preserve all 590 immutable dialogue links, the seven retained performance records, the distinct scene-34 chant, written text, source-unlabelled speech, exact cross-page provenance, and source-page linkage; prohibit duplicate source-span ownership, synthetic scene-end prose, placeholder/editorial leakage, or upstream source-layer mutation. After reader QA passes, prepare structured data for Kalaignar Digital Library / Reading Room integration. Do not create a PDF, EPUB, or other publication package unless separately requested.

## Batch — source scenes 2–5

Scenes 2–5 are **VERIFIED** as **110 units** with **85/85 immutable dialogue links**, **1 deliberately unassigned source-unlabelled speech unit**, **0 performance occurrences**, and **0 cross-page units**. Detailed decisions are in `BATCH_002_005_REVIEW.md`; machine QA is `batch-002-005-qa.json`.

Cumulative English state is now **5/45 verified scenes / 131 units / 99 immutable dialogue links / 1 of 7 performance records translated / 23 song mappings**.

## Next gate

Begin Phase 10 whole-work reader/export generation from the complete-verified Tamil and English structured layers. Build deterministic Markdown, standalone HTML, machine-readable JSON, reader QA, and an integrity manifest; verify all 45 source scenes appear exactly once in canonical order and all 797 verified English units render exactly once; preserve all 590 immutable dialogue links, the seven retained performance records, the distinct scene-34 chant, written text, source-unlabelled speech, exact cross-page provenance, and source-page linkage; prohibit duplicate source-span ownership, synthetic scene-end prose, placeholder/editorial leakage, or upstream source-layer mutation. After reader QA passes, prepare structured data for Kalaignar Digital Library / Reading Room integration. Do not create a PDF, EPUB, or other publication package unless separately requested.

## Verified batch — scenes 6–15

- source scenes: **10 / scenes 6–15**;
- units: **232**;
- immutable dialogue links: **180/180**;
- source-unlabelled speech: **3 / inferred speakers 0**;
- performance occurrences: **2/2 — `naam-perf-001`, `naam-perf-002`**;
- new line/cue mappings: **34**;
- upstream rewrites: **0**.

The continuing production cadence is **10 source scenes per iteration**.

## Verified batch — scenes 16–25

- source scenes: **10 / scenes 16–25**;
- units: **138**;
- immutable dialogue links: **101/101**;
- source-unlabelled speech: **6 / inferred speakers 0**;
- performance occurrences: **1/1 — `naam-perf-003`**;
- new lyric-line mappings: **17**;
- upstream rewrites: **0**.

Production cadence remains **10 source scenes per iteration**.

## Verified batch — scenes 26–35

- source scenes: **10 / scenes 26–35**;
- units: **179**;
- immutable dialogue links: **126/126**;
- source-unlabelled speech: **9 / inferred speakers 0**;
- performance occurrence: **1/1 — `naam-perf-004`**;
- new song/performance mappings: **10**;
- scene-local chant: **1 unit / 16 mappings / no song occurrence or authorship inference**;
- upstream rewrites: **0**.

## Verified final batch — scenes 36–45

- source scenes: **10 / scenes 36–45**;
- units: **117**;
- immutable dialogue links: **84/84**; cumulative **590/590**;
- source-unlabelled speech: **1 / inferred speakers 0**; cumulative **20**;
- performance occurrences: **2/2 — `naam-perf-005`, `naam-perf-006`**; cumulative **7/7**;
- new performance mappings: **54**; cumulative **138**;
- written text: **2 units**;
- upstream rewrites: **0**.

The scene-sharded English layer is **45/45 complete**. Whole-work translation reconciliation must PASS before final `complete-verified` status or reader/export generation.

## Whole-work English closure

- **45/45 scenes / 797 units / 590/590 dialogue links / 20 source-unlabelled with 0 inferred speakers / 7/7 performances / 138 mappings / 1 chant (16 mappings) / 12 cross-page units**;
- duplicate source ownership / placeholders / synthetic scene ends / upstream rewrites: **0 / 0 / 0 / 0**;
- reconciliation: `whole-work-reconciliation.json` — **PASS**.

**Next:** Begin Phase 10 whole-work reader/export generation from the complete-verified Tamil and English structured layers. Build deterministic Markdown, standalone HTML, machine-readable JSON, reader QA, and an integrity manifest; verify all 45 source scenes appear exactly once in canonical order and all 797 verified English units render exactly once; preserve all 590 immutable dialogue links, the seven retained performance records, the distinct scene-34 chant, written text, source-unlabelled speech, exact cross-page provenance, and source-page linkage; prohibit duplicate source-span ownership, synthetic scene-end prose, placeholder/editorial leakage, or upstream source-layer mutation. After reader QA passes, prepare structured data for Kalaignar Digital Library / Reading Room integration. Do not create a PDF, EPUB, or other publication package unless separately requested.
