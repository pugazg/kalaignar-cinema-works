# Raja Rani — character / entity mapping checkpoint

## Scope

This checkpoint now records the **final fully unblocked character/entity derivative** for all exact non-empty speaker labels preserved in the corrected dialogue layer.

Controlling inputs:

- `works/raja-rani/characters/labels-inventory.json`
- `works/raja-rani/dialogues/index.json`
- `works/raja-rani/dialogues/records/scene-###.json`
- verified scene text under `works/raja-rani/scenes/`
- source-visible PDF-9 cast roster as an outer-film identity anchor only

There are no source-review-blocked scenes remaining.

## Final completion result

- immutable dialogue records considered: **1,071/1,071**
- verified dialogue scenes: **58/58**
- distinct exact source labels: **80**
- exact labels dispositioned: **80/80**
- entities / role categories / collectives: **44**
- verified entities: **44**
- review entities: **0**
- unresolved entities: **0**
- verified labels: **80**
- review labels: **0**
- unresolved labels: **0**
- dialogue records modified by entity mapping: **none**
- output: `works/raja-rani/characters/entities.json`

## Additions after final source unblocking

The fully verified scenes added exact source labels that were absent from the original 50-scene mapping checkpoint:

- `மனம்` — source-personified Rani internal role;
- `நிழல்` — source-personified shadow / Leela role;
- `ஞானக்கண் குரல்` — mapped to Gnanakannu using explicit remembered-voice context;
- `ராஜாவின் குரல்` — mapped to Raja using explicit remembered-voice context;
- `சமரசம் குரல்` — mapped to Samarasam using explicit voice label/context.

The preceding source-correction campaign also preserved the one-off exact label `தர்யம்`, mapped to Thayammal without normalizing the immutable source string.

## Important context-sensitive decisions

### `ரா` is Rani, not Raja

In scene 45 the exact label `ரா` answers Raja's flower/pottu offer and belongs to Rani. Raja's distinct exact source forms are `ராஜா`, `ராசா`, `ராஜ`, plus remembered-voice label `ராஜாவின் குரல்`.

### `மனம்` and `நிழல்` remain dramatic roles

Scene 13 explicitly frames a `மனப் போராட்டம்`; these labels are personified internal/dramatic roles and are not silently collapsed into ordinary `ராணி` metadata.

### `தாய்` / `தர்யம்` are Thayammal

Scene 52 explicitly introduces Geetha's mother immediately before `தாய்:`. `தர்யம்` is the source-exact one-off scene-17 label resolved by correction audit. Both map downstream to Thayammal while the exact source labels remain unchanged.

### `சங்` is Sangaran

Scene 57 explicitly introduces Current, Sankaran and Kannamma before `சங்:`. The abbreviation is therefore source-secure.

### `வேலை` remains context-sensitive

The short label appears in more than one work/household setting, so the downstream entity remains a worker/servant role category rather than falsely asserting one physical individual.

### `மன்` is not merged with `மன்னர்கள்`

The plural source label is a collective; `மன்` is kept as a separate unnamed-king role.

## Embedded dramatic identities

Nested-performance identities remain distinct from outer-film characters:

- `சேரன் செங்குட்டுவன்` section: Cheran Senguttuvan, Venmal, Villavan, Kanakar, Vijayar, Kanaka-Vijaya collective, Tamil poet, kings, unnamed king, warriors and opening voice;
- `அகல்யா` rehearsal: Ahalya, Indra, sage and Rama-costume role;
- `சாக்ரடீஸ்` drama: Socrates, Melitus, Anitus, Crito, judge, prison guard and people/audience.

## T055 / T056 referential correction

Final screenplay QA removed five duplicate dialogue records from the old scene-55 derivative because they belonged exclusively to scene 56. The entity identities and 80-label coverage do not change, but all evidence pointers must refer to the current **1,071-record** corpus.

In particular, any older support pointer to deleted `raja-rani-s055-d026`–`raja-rani-s055-d030` is obsolete. Rani's relevant flashback evidence is in `raja-rani-s056-d002` / `raja-rani-s056-d004`.

Canonical Tamil pages were not changed.

## Integrity rules confirmed

1. Every one of the **80** exact labels is covered by the downstream entity mapping.
2. No dialogue `speaker_label`, delimiter, Tamil text, page provenance or valid record ID was changed by entity normalization.
3. Similar spelling alone was never sufficient to merge labels.
4. Role/collective dispositions are used where source evidence does not establish a named physical person.
5. No blocked-scene restriction remains; every evidence scene is source-verified.
6. Character normalization exists only downstream in `characters/entities.json`.
7. Supporting record IDs must exist in the corrected 1,071-record dialogue corpus.

## Disposition

**PASS — character/entity derivative complete: 80/80 labels, 44/44 verified entities / roles / collectives.**

The current production frontier is no longer character work. Preserve this layer while translating the 11 numbered front-matter songs into English.
