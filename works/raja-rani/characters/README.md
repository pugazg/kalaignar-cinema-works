# ராஜா ராணி — character / entity index

Status: **complete-verified — 80/80 exact labels dispositioned into 44 entities / role categories / collectives**.

This is a downstream interpretive layer built from the completed **1,071-record immutable dialogue inventory** across all **58/58 verified scenes**. Exact source-visible `speaker_label` values remain unchanged in dialogue records; normalization exists only in `entities.json` where verified scene/source context supports it.

## Controlling source for this layer

- `../dialogues/index.json` — completed dialogue inventory: **1,071 records / 58 scenes / 0 blocked**.
- `../dialogues/records/scene-###.json` — immutable scene-sharded dialogue records.
- `labels-inventory.json` — complete inventory of **80 distinct exact source labels**.
- `entities.json` — complete verified character / role / collective dispositions.
- `schema.json` — Raja Rani character/entity mapping schema.
- `../notes/character-label-inventory.md` — exact-label inventory checkpoint, later synchronized after final source unblocking.
- `../notes/character-entity-mapping.md` — entity-mapping evidence and final reconciliation checkpoint.

## Completion totals

- verified dialogue scenes scanned: **58/58**;
- immutable dialogue records scanned: **1,071/1,071**;
- distinct exact non-empty source labels: **80**;
- exact labels dispositioned: **80/80**;
- entities / role categories / collectives: **44**;
- verified entities: **44**;
- review entities: **0**;
- unresolved entities: **0**;
- verified labels: **80**;
- review labels: **0**;
- unresolved labels: **0**.

The final unblocked material added the exact labels `மனம்`, `நிழல்`, `ஞானக்கண் குரல்`, `ராஜாவின் குரல்`, and `சமரசம் குரல்`; the preceding correction campaign had already added source-exact `தர்யம்`. `மனம்` and `நிழல்` remain verified dramatic/personification roles; the three explicit `… குரல்` forms map to their source-secure existing people.

## T055 / T056 referential correction

Final screenplay QA removed five duplicate dialogue records that had incorrectly repeated scene 56 inside scene 55. The character census remains **80 labels / 44 entities** because no label identity changed, but character evidence must use the corrected **1,071-record** dialogue corpus.

Any evidence pointer to deleted `s055-d026`–`s055-d030` is invalid. Rani's scene-56 evidence is anchored to the real `raja-rani-s056-d002` / `raja-rani-s056-d004` records instead.

Canonical page transcription was not changed by this derivative-boundary correction.

## Character-layer rules

1. Exact spelling, abbreviations and source anomalies remain immutable in `labels-inventory.json` and dialogue records.
2. Dialogue `speaker_label`, delimiter, Tamil text and provenance are never rewritten by this layer.
3. Multiple exact labels map to one character only when verified scene/source context proves the relationship.
4. Similar spelling alone is not enough to merge labels.
5. A source label reused across contexts may remain a context-sensitive role category rather than falsely becoming one physical person.
6. Generic labels remain `role` or `collective` entities where the source does not establish a personal identity.
7. Embedded dramatic identities remain distinct from outer-film characters.
8. Supporting dialogue IDs are evidence anchors only and must exist in the current corrected dialogue corpus.

## Important source-backed decisions

### Raja / Rani short labels

`ராஜா`, `ராசா`, `ராஜ`, and remembered-voice `ராஜாவின் குரல்` map to outer-film **Raja**. The visually similar `ரா` does not: in scene 45 it belongs to **Rani**, established by the surrounding exchange and source stage-direction evidence.

### Rani's internal roles

Scene 13's exact labels `மனம்` and `நிழல்` are preserved as source-personified internal/dramatic roles rather than silently normalized to ordinary `ராணி` dialogue metadata.

### Geetha's mother

`கீதாவின் தாய் தாயம்மாள்`, `தா`, `தர்யம்`, `தாயம்`, `தாயம்மாள்`, and `தாய்` map to **தாயம்மாள்**. Source-exact `தர்யம்` is deliberately retained rather than normalized.

### Sangaran

Scene 57 explicitly introduces `(கரண்ட், சங்கரன், கண்ணம்மா மூவரும் வருதல்.)`; the subsequent `சங்:` label therefore maps to **சங்கரன்**.

### Context-sensitive worker label

`வேலை` appears in more than one household/work setting. Together with `வேலைக்காரன்`, it is represented as a verified worker/servant **role category**, not as one asserted individual across every occurrence.

### Embedded dramatic identities

The nested performance layers remain separate:

- `சேரன் செங்குட்டுவன்`: Cheran Senguttuvan, Venmal, Villavan, Kanakar, Vijayar, Kanaka-Vijaya collective, Tamil poet, kings, unnamed king, warriors and opening voice;
- `அகல்யா`: Ahalya, Indra, sage and `ராமர் வேஷ ராமன்`;
- `சாக்ரடீஸ்`: Socrates, Melitus, Anitus, Crito, judge, prison guard and audience/people.

No embedded role is silently collapsed into the outer-film performer.

## Current phase

The character/entity layer is closed and should remain stable during the remaining English song work.

Next production activity: translate the **11 verified numbered front-matter song bodies**. Song translation must not modify dialogue labels, character mappings, or authorship dispositions.
