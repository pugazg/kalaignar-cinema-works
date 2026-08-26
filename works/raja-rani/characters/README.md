# ராஜா ராணி — character / entity index

Status: **complete-verified — 74/74 exact labels dispositioned into 42 entities / role categories / collectives**.

This is a downstream interpretive layer built only from the completed **892-record immutable dialogue inventory**. Exact source-visible `speaker_label` values remain unchanged in dialogue records; normalization exists only in `entities.json` where verified scene/source context supports it.

## Controlling source for this layer

- `../dialogues/index.json` — completed eligible dialogue inventory: **892 records / 50 of 50 eligible verified scenes**.
- `../dialogues/records/scene-###.json` — immutable scene-sharded dialogue records.
- `labels-inventory.json` — complete inventory of **74 distinct exact source labels**.
- `entities.json` — complete verified character / role / collective dispositions.
- `schema.json` — Raja Rani character/entity mapping schema.
- `../notes/character-label-inventory.md` — exact-label inventory checkpoint.
- `../notes/character-entity-mapping.md` — final entity-mapping evidence and integrity checkpoint.

The eight source-review-blocked archival scenes remain outside verified character evidence:

`raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013`, `raja-rani-s033`, `raja-rani-s039`, `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055`.

Their blocking source pages are PDF 27, 48, 57 and 74. No character conclusion uses text excluded from the verified scene/dialogue layers merely to fill a gap.

## Completion totals

- eligible dialogue scenes scanned: **50/50**;
- immutable dialogue records scanned: **892/892**;
- distinct exact non-empty source labels: **74**;
- exact labels dispositioned: **74/74**;
- entities / role categories / collectives: **42**;
- verified entities: **42**;
- review entities: **0**;
- unresolved entities: **0**;
- verified labels: **74**;
- review labels: **0**;
- unresolved labels: **0**;
- dialogue records modified: **0**.

## Character-layer rules

1. Exact spelling, abbreviations and source anomalies remain immutable in `labels-inventory.json` and the dialogue records.
2. Dialogue `speaker_label`, delimiter, Tamil text and provenance are never rewritten by this layer.
3. Multiple exact labels map to one character only when verified scene/source context proves the relationship.
4. Similar spelling alone is not enough to merge labels.
5. A source label reused across contexts may be dispositioned as a context-sensitive role category rather than falsely treated as one physical person.
6. Generic labels remain `role` or `collective` entities where the source does not establish a personal identity.
7. Embedded dramatic identities remain distinct from outer-film characters.
8. Supporting dialogue IDs are evidence anchors, not replacements for the canonical/scene source.

## Important source-backed decisions

### Raja / Rani short labels

The source forms `ராஜா`, `ராசா`, and `ராஜ` map to outer-film **Raja**. The visually similar `ரா` does **not**: in scene 45 it belongs to **Rani**, established by the surrounding exchange and feminine stage-direction evidence such as `[அழுகிறாள்.]`.

### Geetha's mother

`கீதாவின் தாய் தாயம்மாள்`, `தா`, `தாயம்`, `தாயம்மாள்`, and `தாய்` map to **தாயம்மாள்**. Scene 52 explicitly says `(பாபு தயங்க. கீதாவின் தாய் உள்ளே இருந்து ஓடிவந்து)` immediately before `தாய்:`, making that short form source-secure.

### Sangaran

Scene 57 explicitly introduces `(கரண்ட், சங்கரன், கண்ணம்மா மூவரும் வருதல்.)`; the subsequent `சங்:` label therefore maps to **சங்கரன்**.

### Context-sensitive worker label

`வேலை` appears in more than one household/work setting. Together with `வேலைக்காரன்`, it is represented as a verified worker/servant **role category**, not as one asserted physical character across all occurrences.

### Embedded dramatic identities

The nested performance layers remain separate:

- `சேரன் செங்குட்டுவன்`: Cheran Senguttuvan, Venmal, Villavan, Kanakar, Vijayar, the Kanaka-Vijaya collective, Tamil poet, kings, unnamed king, warriors and opening voice;
- `அகல்யா` rehearsal: Ahalya, Indra, the sage and `ராமர் வேஷ ராமன்`;
- `சாக்ரடீஸ்`: Socrates, Melitus, Anitus, Crito, judge, prison guard and audience/people.

No embedded role is silently collapsed into the outer-film actor/character who performs it.

## Source-visible outer-film identity anchors

The verified PDF-9 cast roster directly anchors principal outer-film identities including:

- `ராஜா`
- `பாபு`
- `சமரசம்`
- `ஞானக்கண்ணு`
- `கரண்ட்`
- `ராணி`
- `கீதா`
- `சாந்தம்`
- `கீதாவின் தாய்`

Those roster forms were used as evidence anchors, not as permission to normalize unrelated labels by spelling.

## Files / phase state

- `schema.json` — complete.
- `labels-inventory.json` — **complete: 74/74**.
- `entities.json` — **complete-verified: 42 entities / role categories / collectives; 74/74 labels covered**.
- `index.json` — final character-phase status.

No `entities-pilot.json` was needed.

## Next activity

Begin the **song/performance inventory and item-level authorship gate**.

The source prints **11 numbered `பாட்டு` blocks** across PDF 4–9 and a film-wide PDF-9 `பாடல்கள்:` roster. Inventory each source-visible song/performance occurrence first. The film-wide roster must **not** be promoted to item-level authorship without item-specific evidence.

Do not modify any file under `../dialogues/records/` during song/authorship work.
