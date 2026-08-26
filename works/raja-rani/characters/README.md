# ராஜா ராணி — character / entity index

Status: **in progress — exact-label inventory complete; entity mapping next**.

This is a downstream interpretive layer built only from the completed **892-record immutable dialogue inventory**. It maps exact source-visible `speaker_label` values to named characters, context-safe roles, collectives or explicit unresolved dispositions without changing any dialogue record.

## Controlling source for this layer

- `../dialogues/index.json` — completed eligible dialogue inventory: **892 records / 50 of 50 eligible verified scenes**.
- `../dialogues/records/scene-###.json` — immutable scene-sharded dialogue records.
- `labels-inventory.json` — complete inventory of **74 distinct exact source labels** across all 892 records.
- `schema.json` — Raja Rani character/entity mapping schema.

The eight source-review-blocked archival scenes remain outside verified character evidence:

`raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013`, `raja-rani-s033`, `raja-rani-s039`, `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055`.

Their blocking source pages are PDF 27, 48, 57 and 74. No character conclusion may use text that was excluded from the verified scene/dialogue layers merely to fill a gap.

## Exact-label inventory checkpoint

The complete eligible dialogue layer was scanned before any entity normalization:

- eligible dialogue scenes scanned: **50/50**;
- immutable dialogue records scanned: **892/892**;
- non-zero dialogue scene shards: **35**;
- zero-record eligible scene shards: **15**;
- distinct exact non-empty `speaker_label` strings: **74**;
- dialogue records modified during inventory: **0**.

The inventory deliberately keeps variants separate. Examples include `ராஜா`, `ராசா`, `ராஜ`, `ரா`; `சமரசம்`, `சம`; `சாந்தம்`, `சாந்தம்மா`, `சாந்`; `ஞானக்கண்`, `ஞான`, `ஞா`; and embedded-performance labels such as `சாக்ரடீஸ்`, `சாக்`, `மெலிடஸ்`, `மெலி`. Their presence in the same inventory does not itself prove that any two labels should be merged.

## Character-layer rules

1. Exact spelling, abbreviations and source anomalies remain immutable in `labels-inventory.json` and the dialogue records.
2. Dialogue `speaker_label`, delimiter, Tamil text and provenance must never be rewritten by this layer.
3. Multiple exact labels may map to one character only when verified scene/source context supports that relationship.
4. Similar spelling alone is not enough to merge labels.
5. A source label reused for different identities or roles must remain context-sensitive rather than being forced into one physical character.
6. Generic labels may remain `role` or `collective` entities where the source does not establish a personal identity.
7. Ambiguous identity must be recorded as `review` or `unresolved`; completion means complete disposition coverage, not guessed certainty.
8. Embedded dramatic identities remain distinct from outer-film identities unless the source itself establishes a deliberate performer/role relationship relevant to the derivative.
9. Supporting dialogue IDs are evidence anchors, not replacements for the canonical/scene source.

## Source-visible identity anchors

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

These roster forms are evidence anchors only. They do not automatically authorize merging every abbreviation or similar-looking exact dialogue label.

The screenplay also contains embedded dramatic material including `சேரன் செங்குட்டுவன்`, the `அகல்யா` rehearsal and `சாக்ரடீஸ் (நாடகம்)`. Speaker labels inside those performances must be mapped as their dramatic identities rather than silently collapsed into outer-film actors/characters.

## Files / phase state

- `schema.json` — complete; governs downstream entity records.
- `labels-inventory.json` — **complete: 74/74 distinct exact labels from 892/892 records**.
- `index.json` — character-phase checkpoint.
- `entities.json` — **next; not yet created**.

No `entities-pilot.json` is required merely for symmetry with older works. A pilot should be added only if it materially helps evidence review.

## Next activity

Begin evidence-backed entity mapping for all **74 exact source labels**. Reconcile abbreviations and variants only when verified scene context supports the relationship; preserve embedded dramatic identities separately; represent generic labels as roles/collectives where appropriate; and keep any genuinely ambiguous label at `review` or `unresolved` rather than guessing.

Do not modify any file under `../dialogues/records/` during character work.
