# Raja Rani — character exact-label inventory checkpoint

## Scope

This checkpoint completes the mandatory exact-speaker-label inventory before character/entity normalization.

Controlling derivative source:

- `works/raja-rani/dialogues/index.json`
- `works/raja-rani/dialogues/records/scene-###.json`

Only the **50 eligible verified dialogue scenes** are in scope. The eight archival scenes blocked by review-source pages remain excluded: `s011`, `s012`, `s013`, `s033`, `s039`, `s053`, `s054`, `s055`.

## Coverage reconciliation

- eligible scene shards examined: **50/50**
- non-zero dialogue scene shards: **35**
- zero-record eligible scene shards: **15**
- immutable dialogue records examined: **892/892**
- sum of the 35 non-zero shard `record_count` values: **892**
- distinct exact non-empty `speaker_label` strings: **74**
- output: `works/raja-rani/characters/labels-inventory.json`
- dialogue records changed: **none**

The 15 zero-record eligible scenes are `s008`, `s010`, `s014`, `s019`, `s020`, `s022`, `s027`, `s029`, `s030`, `s032`, `s037`, `s038`, `s042`, `s043`, `s048`.

## Inventory policy

The inventory is intentionally exact and non-normalizing. It preserves source-visible variants as different labels even when later evidence may map them to one entity. Examples include:

- `ராஜா`, `ராசா`, `ராஜ`, `ரா`
- `சமரசம்`, `சம`
- `சாந்தம்`, `சாந்தம்மா`, `சாந்`
- `ஞானக்கண்`, `ஞான`, `ஞா`
- `கரண்ட்`, `கரண்டு`, `கர`
- `சாக்ரடீஸ்`, `சாக்`
- `மெலிடஸ்`, `மெலி`

No merge is asserted by listing those examples together.

The inventory also preserves generic/collective labels (`மன்னர்கள்`, `வீரர்கள்`, `பல குரல்கள்`, `மக்கள்`), role labels (`வேலைக்காரன்`, `சமையல்காரன்`), and embedded-performance identities (`அகல்யா`, `இந்திரன்`, `சாக்ரடீஸ்`, etc.) without prematurely converting them into outer-film identities.

## Integrity checks

1. Every exact label in `labels-inventory.json` occurs in at least one of the 50 eligible dialogue shards.
2. Every listed scene ordinal is an eligible scene containing that exact label.
3. The inventory contains **74 unique labels**.
4. The dialogue shard record counts reconcile exactly to the completed dialogue-index total of **892**.
5. No source-review-blocked scene was used to add a label or identity claim.
6. No dialogue `speaker_label`, delimiter, text or provenance was modified.

## Next gate

Entity mapping is now unblocked.

The next activity is to create evidence-backed character/role/collective dispositions for all 74 exact labels. Similarity alone is not sufficient for a merge. Outer-film cast evidence, verified scene context and embedded-performance boundaries must control the mapping, with `review` or `unresolved` retained wherever identity is not secure.
