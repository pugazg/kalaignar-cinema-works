# Raja Rani — deterministic bilingual reader/export

This directory is the publication-facing **downstream** reader/export layer for the complete-verified Raja Rani bilingual textual archive.

## Authority

The reader is generated only from verified structured repository data:

- screenplay Tamil: `works/raja-rani/scenes/scene-001.md` through `scene-058.md`;
- screenplay English: `works/raja-rani/translations/records/scene-001.json` through `scene-058.json`;
- immutable dialogue evidence: `works/raja-rani/dialogues/records/`;
- numbered-song Tamil/English pairs: `works/raja-rani/translations/songs/records/song-001.json` through `song-011.json`;
- song/performance evidence: `works/raja-rani/songs/inventory.json` and current song indexes.

The scan and verified canonical Tamil remain upstream authorities. Reader generation never repairs source text.

## Source-structure rule

The source prints **11 numbered front-matter songs**, but it prints **no screenplay scene numbers**.

Therefore the reader preserves two independent navigation structures:

1. **Numbered songs 1–11** — actual source-numbered front-matter song bodies;
2. **Archival scenes 1–58** — repository navigation segments only, never presented as source scene numbers.

The numbered songs must not be converted into synthetic screenplay scenes.

## Fixed input checkpoint

- verified source pages: **79/79**;
- verified screenplay pages: **70/70**;
- screenplay scenes: **58/58**;
- immutable dialogue records: **1,071**;
- screenplay English units: **1,236**;
- source-unlabelled spoken English units: **19**;
- cross-page screenplay English units: **15**;
- screenplay performance occurrence links: **4/4**;
- numbered songs: **11/11**;
- numbered-song translation sections: **67**;
- Tamil/English numbered-song line-cue mappings: **181/181**;
- cross-page numbered-song records: **4**.

The T055/T056 correction is permanent: scene 55 owns 25 immutable dialogue records and scene 56 owns 5; deleted duplicate IDs `raja-rani-s055-d026`–`raja-rani-s055-d030` are invalid.

## Completion checkpoint

Status: **complete-verified — QA PASS**.

- preflight authoritative inputs: **200**;
- screenplay: **58/58 scenes / 1,236 units / 1,071 immutable links**;
- numbered songs: **11/11 / 67 sections / 181 line-cues**;
- generated Markdown SHA-256: `6437a0a39cebbaf17ab63f76f7aef6f9f62eb3c4abbd07864974d47be20902c8`;
- generated HTML SHA-256: `c24ea9ab0f1ee77b3bc795b3134e4ad8bed78f00d6a8f896f9749052ff074ec6`;
- generated JSON SHA-256: `76827d570f3079c04463e3142a9edf32f35c1497e2b820bfa467f8203d7441e2`;
- generated-output QA: `QA_REPORT.md` — **PASS**.

The separate Reading Room payload built from this reader is also QA-PASS under `../../integrations/reading-room/`.

## Outputs

- `audit_probe.py` — whole-work preflight over screenplay + numbered songs;
- `PREFLIGHT_QA_REPORT.md` — generated preflight checkpoint;
- `build.py` — deterministic bilingual reader/export builder and output QA;
- `reader-edition.md` — bilingual Markdown reader;
- `reader-edition.html` — standalone bilingual HTML reader;
- `reader-edition.json` — machine-readable bilingual reader payload;
- `QA_REPORT.md` — generated-output QA;
- `manifest.json` — reproducibility/integrity hashes.

No PDF or EPUB is created by default. The preferred downstream public destination remains the Kalaignar Digital Library / Reading Room.
