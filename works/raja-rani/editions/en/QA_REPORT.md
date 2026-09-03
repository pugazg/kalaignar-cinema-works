# Raja Rani bilingual reader/export — QA report

Status: **PASS**

## Input checkpoint

- screenplay scenes: **58/58**
- screenplay English units: **1,236/1,236**
- immutable dialogue links: **1,071/1,071**
- source-unlabelled spoken units: **19/19**
- cross-page screenplay units: **15/15**
- screenplay performance occurrence links: **4/4**
- numbered songs: **11/11**
- numbered-song translation sections: **67/67**
- numbered-song Tamil/English line-cue mappings: **181/181**
- cross-page numbered songs: **4/4**
- song authorship: **5 later-anthology Kalaignar-attributed / 6 unresolved**
- screenplay song relations: **3 verified / 1 review**

## Structural QA

- numbered songs remain separate source-numbered front-matter structures: **PASS**
- screenplay `s001`–`s058` remain archival navigation only, not source scene numbering: **PASS**
- all immutable dialogue links appear exactly once in English: **PASS**
- source-unlabelled speech remains unlabelled: **PASS**
- T055/T056 deleted duplicate IDs absent: **PASS**
- source-page provenance/order checks: **PASS**
- song line/cue mappings complete and unique: **PASS**
- authorship tiers unchanged by translation/reader generation: **PASS**
- scene-58/song-11 relation remains review-level: **PASS**
- synthetic `(Scene ends.)` / placeholder leakage: **0**

## Generated-output QA

- Markdown contains each of the **1,236** screenplay unit IDs exactly once and each of the **181** song line IDs exactly once: **PASS**
- HTML contains each screenplay unit and song line data ID exactly once: **PASS**
- machine JSON round-trips to the validated reader model: **PASS**
- generated outputs contain no deleted T055 duplicate IDs: **PASS**

## Reproducibility

- build version: **1**
- authoritative-input aggregate SHA-256: `35cfc21e70eed9e0fb820c3df6a6a1c41fbddc21594f78b0cb5a799ab6a7efc2`
- Markdown SHA-256: `6437a0a39cebbaf17ab63f76f7aef6f9f62eb3c4abbd07864974d47be20902c8`
- HTML SHA-256: `c24ea9ab0f1ee77b3bc795b3134e4ad8bed78f00d6a8f896f9749052ff074ec6`
- JSON SHA-256: `76827d570f3079c04463e3142a9edf32f35c1497e2b820bfa467f8203d7441e2`

No canonical Tamil, immutable dialogue record, character mapping, song authorship disposition or translation record is modified by reader generation.
