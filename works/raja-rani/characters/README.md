# ராஜா ராணி — character / entity index

Status: **initialized — exact-label inventory next**.

This is a downstream interpretive layer built only from the completed **892-record immutable dialogue inventory**. It will map exact source-visible `speaker_label` values to named characters, context-safe roles, collectives or explicit unresolved dispositions without changing any dialogue record.

## Controlling source for this layer

- `../dialogues/index.json` — completed eligible dialogue inventory: **892 records / 50 of 50 eligible verified scenes**.
- `../dialogues/records/scene-###.json` — immutable scene-sharded dialogue records.
- `schema.json` — Raja Rani character/entity mapping schema.

The eight source-review-blocked archival scenes remain outside verified character evidence:

`raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013`, `raja-rani-s033`, `raja-rani-s039`, `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055`.

Their blocking source pages are PDF 27, 48, 57 and 74. No character conclusion may use text that was excluded from the verified scene/dialogue layers merely to fill a gap.

## Character-layer rules

1. **Inventory every exact source label before normalization.** `labels-inventory.json` must be produced from all 892 immutable dialogue records before entity mapping begins.
2. Exact spelling, abbreviations and source anomalies remain separate inventory labels.
3. Dialogue `speaker_label`, delimiter, Tamil text and provenance are immutable and must never be rewritten by this layer.
4. Multiple exact labels may map to one character only when verified scene/source context supports that relationship.
5. Similar spelling alone is not enough to merge labels.
6. A source label reused for different identities or roles must remain context-sensitive rather than being forced into one physical character.
7. Generic labels may remain `role` or `collective` entities where the source does not establish a personal identity.
8. Ambiguous identity must be recorded as `review` or `unresolved`; completion means complete disposition coverage, not guessed certainty.
9. Embedded dramatic identities remain distinct from outer-film identities unless the source itself establishes a deliberate performer/role relationship relevant to the derivative.
10. Supporting dialogue IDs are evidence anchors, not replacements for the canonical/scene source.

## Source-visible identity anchors already available

The verified PDF-9 cast roster provides direct outer-film identity evidence for these principal roles:

- `ராஜா`
- `பாபு`
- `சமரசம்`
- `ஞானக்கண்ணு`
- `கரண்ட்`
- `ராணி`
- `கீதா`
- `சாந்தம்`
- `கீதாவின் தாய்`

These roster forms are **evidence anchors only** at this initialization checkpoint. They do not authorize merging every abbreviation or similar-looking dialogue label before the complete exact-label inventory and scene-context review.

The screenplay also contains embedded dramatic material such as `சேரன் செங்குட்டுவன்` and `சாக்ரடீஸ் (நாடகம்)`. Speaker labels inside those performances must be mapped as their dramatic identities rather than silently collapsed into the outer-film actors/characters.

## Files / phase state

- `schema.json` — created; governs downstream entity records.
- `index.json` — initialization checkpoint.
- `labels-inventory.json` — **next; not yet created**.
- `entities.json` — blocked until exact-label inventory is complete.

No `entities-pilot.json` is created merely for symmetry with older works. A pilot may be added only if it materially helps evidence review after the complete label inventory exists.

## Next activity

Scan all **892** immutable dialogue records and create `labels-inventory.json` containing every distinct exact non-empty `speaker_label` and the verified scene ordinals in which it occurs.

Only after that inventory is complete should entity mapping begin. Do not modify any file under `../dialogues/records/` during character work.
