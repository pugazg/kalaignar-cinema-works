# ராஜா ராணி — Character / Entity Layer Initialization

## Purpose

This checkpoint opens the character/entity derivative phase after completion of the immutable dialogue layer.

The character layer is interpretive metadata only. It must not modify canonical Tamil, verified scene derivatives or any field in the 892 immutable dialogue records.

## Input gate

Authoritative structured input:

- `dialogues/index.json`
- `dialogues/records/scene-###.json`

Dialogue completion state at initialization:

- eligible verified scenes: **50**
- processed eligible scenes: **50/50**
- immutable labelled-dialogue records: **892**
- blocked scenes: **8**
- zero-record eligible scenes: **15**
- cross-page dialogue records: **11**
- tracked non-colon source-label/delimiter anomalies: **3**

Blocked scene IDs remain outside verified character evidence:

`raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013`, `raja-rani-s033`, `raja-rani-s039`, `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055`.

## Required order

The processing guide requires **exact-label inventory first**.

Therefore this checkpoint creates the character-layer schema and control files but deliberately does **not** create entity mappings yet.

Required next steps:

1. scan all 892 immutable dialogue records;
2. inventory every distinct exact non-empty `speaker_label`;
3. record all eligible scene ordinals in which each label occurs;
4. verify inventory coverage against the 892-record dialogue layer;
5. only then create evidence-backed entity mappings.

## Mapping discipline after inventory

- Preserve source label variants exactly in the inventory.
- Do not merge abbreviations merely because they resemble a longer name.
- Reused labels may require context-role or unresolved dispositions.
- Generic labels may remain roles or collectives.
- Embedded `சேரன் செங்குட்டுவன்`, `அகல்யா நாடக ஒத்திகை`, and `சாக்ரடீஸ் (நாடகம்)` identities must remain source-context aware.
- The verified PDF-9 cast roster may support principal outer-film identities, but it does not by itself authorize abbreviation merging.
- `verified`, `review`, and `unresolved` dispositions remain available; uncertainty is not a completion failure.

## Files created at this checkpoint

- `characters/schema.json`
- `characters/README.md`
- `characters/index.json`

`characters/labels-inventory.json` and `characters/entities.json` are intentionally absent until their respective gates are completed.

## Canonical/source effect

None. No dialogue record, scene derivative, canonical page or fidelity disposition was changed.

## Next activity

Complete the **892-record exact speaker-label inventory** and create `characters/labels-inventory.json` before any character/entity normalization is attempted.
