# ராஜா ராணி — Character / Entity Layer Initialization

## Historical purpose

This note originally opened the character/entity derivative phase when only 50 source-eligible scenes and 892 immutable dialogue records were available. That initialization state is **historical**. Final source review later unblocked every screenplay scene, so the live character layer must be read from `characters/index.json`, `labels-inventory.json`, `entities.json`, and the synchronized final checkpoints.

The character layer remains interpretive metadata only. It never authorizes changes to canonical Tamil, verified scene derivatives or exact dialogue `speaker_label` values.

## Final superseding input state

Authoritative structured input now consists of:

- `dialogues/index.json`
- `dialogues/records/scene-###.json`

Final dialogue state:

- verified scenes: **58/58**
- blocked scenes: **0**
- unique immutable labelled-dialogue records: **1,071**
- zero-record scenes: **16**
- genuine cross-page dialogue records: **12**
- tracked source-label/delimiter anomalies: **3**

The historical 892-record / 50-scene checkpoint must not be used as a current production count.

## Final character-layer result

The initialization sequence was completed successfully:

1. exact source-label inventory completed;
2. final inventory after all source unblocking: **80 exact labels**;
3. evidence-backed entity mapping completed;
4. final mapping: **80/80 labels → 44 verified entities / roles / collectives**;
5. review/unresolved labels and entities: **0**.

Final control files:

- `characters/schema.json`
- `characters/README.md`
- `characters/index.json`
- `characters/labels-inventory.json`
- `characters/entities.json`
- `notes/character-label-inventory.md`
- `notes/character-entity-mapping.md`

## T055 / T056 later correction

Final screenplay QA removed five duplicate records that an earlier scene-55 derivative had copied from scene 56. The corrected dialogue corpus is **1,071** records. This did not add or remove a distinct speaker label/entity; it only changed duplicate derivative ownership. Canonical pages were unchanged.

Any historical count or evidence pointer in older commits must yield to the current live indexes.

## Permanent mapping discipline

- preserve exact source label variants;
- do not merge abbreviations by appearance alone;
- generic labels may remain roles or collectives;
- embedded `சேரன் செங்குட்டுவன்`, `அகல்யா`, and `சாக்ரடீஸ்` identities remain context-aware and distinct from outer-film characters;
- `மனம்` / `நிழல்` remain source-personified roles;
- source-exact `தர்யம்` remains unchanged in dialogue metadata;
- normalization exists downstream only.

## Current production frontier

Character/entity work is complete. The current Raja Rani activity is the **English translation of the 11 verified numbered front-matter song bodies**. That phase must not modify character/dialogue data.
