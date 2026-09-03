# Next Chat Prompt — Raja Rani — Numbered-Song English Translation

Continue directly in:

`pugazg/kalaignar-cinema-works`

Branch: `main`

Active work: `works/raja-rani/` — **ராஜா ராணி**

Controlling full source: `TVA_BOK_0017188_ராஜா_ராணி.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve any newer durable state. Do not reset, repeat or overwrite later work because this prompt contains an older checkpoint.

Source identity:

- PDF pages: **80**
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`
- screenplay/dialogue: PDF **10–79**, printed pp. **9–78**
- numbered front-matter songs: PDF **4–9**
- PDF 80: back cover

## Mandatory startup

Before any write, read completely:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `docs/SOURCE_POLICY.md`
4. `docs/TRANSCRIPTION_GUIDE.md`
5. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
6. `docs/HANDOVER_RAJA_RANI.md`
7. this `docs/NEXT_CHAT_PROMPT_RAJA_RANI.md`
8. `works/raja-rani/README.md`
9. `works/raja-rani/translations/README.md`
10. `works/raja-rani/translations/index.json`
11. `works/raja-rani/translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`
12. `works/raja-rani/songs/index.json`
13. `works/raja-rani/songs/schema.json`
14. `works/raja-rani/songs/inventory.json`
15. `works/raja-rani/songs/credits.json`
16. `works/raja-rani/songs/cross-witness-evidence.json`
17. all 11 verified Tamil song derivatives under the live song directory.

## Source state — fully verified

There are **no blocked/review source pages or screenplay scenes**.

Current source/derivative census:

- source pages: **79/79 verified**;
- screenplay pages: **70/70 verified**;
- scene derivatives: **58/58 verified / 0 blocked**;
- unique dialogue corpus: **1,071 immutable records / 58 scenes / 12 cross-page records**;
- character mapping: **80/80 exact labels / 44 verified entities/roles/collectives**;
- songs/performance: **11 numbered songs + 4 screenplay references = 15 occurrences**;
- song authorship: **5 later-anthology Kalaignar-attributed / 6 unresolved**.

Permanent direct-scan verdicts include:

- PDF 27: `இரவெல்லாம்`;
- PDF 48: `வந்தனா`, `திடீர்னு`;
- PDF 57: `முன்னுக்கு பின் முரணாயிகிட்டே போவது?`;
- PDF 74: `K. N. சங்கரன் ...` is a non-canonical ownership/library stamp; screenplay continues `ஞான: நீ விதவை.` → `ராஜா: விதவை.` → `சாந்: வித்தாரக்கள்ளி! விநாசகாரி`.

`r1.md`–`r4.md`, OCR and parsed PDF text are candidate/navigation aids only; rendered scan and recorded direct user verdicts control source text.

## English screenplay state — COMPLETE

Do **not** reopen screenplay translation production.

Final verified checkpoint:

- scenes: **58/58**;
- English units: **1,236**;
- immutable dialogue links: **1,071/1,071**;
- dialogue-kind units: **1,090**;
- stage-direction units: **137**;
- performance-cue units: **4**;
- written-text units: **5**;
- source-unlabelled spoken units: **19**;
- cross-page English units: **15**;
- draft/review screenplay units: **0**.

Final QA: `works/raja-rani/translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`.

### T055/T056 permanent correction

Final QA removed a duplicate derivative boundary: old scene 55 had repeated the `(முன்)` flashback belonging to scene 56. The canonical pages were unchanged. Final source dialogue counts are scene 55 = **25**, scene 56 = **5**, corpus = **1,071**.

Do not restore deleted duplicate `s055-d026`–`s055-d030` IDs or link English to them.

## EXACT NEXT ACTIVITY — 11 NUMBERED SONGS

Translate the **11 numbered front-matter song bodies**, songs **1 through 11 in source order**, through a dedicated source-linked English song translation layer.

Before creating files, inspect the live Tamil song derivative naming/layout and define the smallest compatible English song schema/index structure. Do not use invented screenplay scene IDs for song bodies.

For each song:

1. use the verified Tamil song derivative as textual authority;
2. preserve exact source page provenance and source song ID;
3. produce a semantic-poetic English translation faithful to imagery, repetition and rhetorical force;
4. preserve source-visible unusual wording rather than silently repairing the Tamil;
5. keep any screenplay performance relationship only when `songs/inventory.json` already supports it;
6. do not infer or upgrade lyricist attribution;
7. never use English fluency as evidence to alter canonical Tamil.

## Authorship gate — preserve exactly

Later-anthology Kalaignar-attributed numbered songs:

- song 3
- song 5
- song 6
- song 7
- song 8

Unresolved lyricist numbered songs:

- song 1
- song 2
- song 4
- song 9
- song 10
- song 11

Original booklet item-level lyricist credits: **0**.

Scene 58's performance occurrence `raja-rani-song-perf-004` → numbered song 11 remains **review-level**, not verified. Translation must not promote it.

## Completion rule

Process all **11 numbered songs** in this phase unless live repository policy requires a smaller safe technical batch. After translation:

1. verify all 11 English song bodies against their verified Tamil derivatives;
2. verify page provenance and song IDs;
3. verify authorship metadata was not changed;
4. verify screenplay performance links were not upgraded;
5. create a dedicated English numbered-song QA/review;
6. synchronize the song-translation index/README, work metadata/README, handover and this prompt;
7. only then mark the overall Raja Rani bilingual archival work complete.
