# மனோகரா — character / entity index

Status: **complete-verified**.

This is a downstream interpretive layer built from the **983 complete-verified immutable dialogue records**. It maps exact source-visible speaker labels to named characters, context-safe roles, collectives, or explicit unresolved dispositions without changing `speaker_label`, delimiter, dialogue text, or provenance in any dialogue record.

## Source discipline

- `../dialogues/index.json` and `../dialogues/records/scene-###.json` are the structured source for this layer.
- `labels-inventory.json` inventories every exact non-empty speaker label before normalization.
- spelling, abbreviation and punctuation variants remain visible as separate source labels;
- a label is mapped to a named character only when verified scene context supports that identity;
- reused labels are not forced into one character merely because one occurrence is obvious;
- play-within-the-play identities remain distinct from the outer story;
- the **983 dialogue records remain immutable**.

## Completion checkpoint

The complete dialogue inventory contains **111 distinct non-empty source speaker labels** across **57 archival scene shards / 983 records**. `manohara-s024` has zero labelled dialogue and contributes no speaker label.

Final character/entity disposition:

- exact source labels inventoried: **111/111**;
- exact labels dispositioned: **111/111**;
- remaining unmapped labels: **0**;
- stable character/role/collective/unresolved entities: **37**;
- verified entities: **36**;
- review entities: **0**;
- unresolved entities: **1**;
- verified source labels: **110**;
- review source labels: **0**;
- unresolved source labels: **1** — `வர்மா`;
- dialogue records modified: **no**.

`entities.json` is the complete disposition file. `entities-pilot.json` remains as the earlier pilot checkpoint and is not the final mapping authority.

## Named-character mappings added after the pilot

The completion pass safely establishes additional named characters from source context, including:

- nested-play `அஜயன்` / `அஜ` → **அஜயன்**;
- `அட்சயன்` → the real **அக்ஷயன்**, while `அட்` remains context-sensitive because that shorthand is also used for மனோகரன் in disguise;
- nested-play `ஈஸ்வரி வர்மன்` / `வர்மன்` → **ஈஸ்வரி வர்மன்**;
- nested-play `உத்தம புருஷன்` / `உத்` / `ராஜா` → **உத்தம புருஷன்**;
- nested-play `கமலாவதி` / `கமலா` / `கம` → **கமலாவதி**;
- nested-play `தேவசேனா` / `நாடக தேவசேனா` → **தேவசேனா**;
- `பெளத்தாயன்` / `பெளத்தாயன` / `பெளத்` / disguise label `துறவி` → **பெளத்தாயனன்**;
- `முத்து விஜயன்` / `மு. வி` / `முத்து` → **முத்து விஜயன்**;
- `விகடன்` / `விகட` / `விக` → **விகடன்**;
- scene-42 `வீர` → **வீரசிம்ஹன்**, because உக்ரசேனன் explicitly addresses him as `வீரசிம்ஹா!` immediately before the response.

The completion pass also adds `அரூபம்` / `அரூ` to **கேசரிவர்மன்**. Scene 1 establishes Kesari's guru-created invisibility medicine; scene 39's invisible speaker describes the same guru-derived medicine, providing source-internal continuity rather than an external inference.

## Context-reused labels

The following exact labels are deliberately represented as context-role entities rather than forced into one physical character:

- `அட்` — real அக்ஷயன் in scenes 40 and 51, but மனோகரன் in the false-Akshayan disguise in scene 41;
- `வச` — used for both வசந்தசேனை and வசந்தன்; scene 41 alone contains both uses;
- `வசந்` — likewise alternates between வசந்தசேனை and வசந்தன் across scenes;
- `சேனா` — nested-play தேவசேனா in scene 8, later outer-story வசந்தசேனை;
- `வர்` — nested-play ஈஸ்வரி வர்மன் in scene 8, outer-story கேசரிவர்மன் in scene 40;
- `தோ` / `தோழி` / `தோழி 1` / `தோழி 2` — generic friend/attendant labels used for more than one woman and narrative context.

These are source-level label reuse, not transcription errors. The role dispositions preserve that fact without rewriting the dialogue layer.

## Generic role / collective dispositions

The final index also keeps unnamed source roles categorical where personal identity is not established: `காவலர்`, `சிப்பாய்`, `பிரதானி`, `வைத்தியர்`, `வீரன்`, `முரசறைவோன்`, the recurring `பெரியவர் / குருதேவர்`, `மனக்குரல்`, and the collective `சபையோர்`. Grouping equivalent role labels does not assert that every occurrence is one physical person.

## Remaining unresolved source label

`வர்மா` in `manohara-s008-d003` remains **unresolved**. It occurs inside the nested play immediately before an `ஈஸ்வரி வர்மன்` response, but the printed sequence does not support assigning that label confidently to ஈஸ்வரி வர்மன், உத்தம புருஷன், or another specific character without inference. The exact source label is therefore preserved with an explicit unresolved disposition rather than silently repaired.

## Files

- `schema.json` — Manohara entity-derivative schema.
- `labels-inventory.json` — complete exact-label inventory, **111 labels**.
- `entities-pilot.json` — historical pilot checkpoint: **10 entities / 51 mapped labels**.
- `entities.json` — final complete disposition: **37 entities / 111 labels**.
- `index.json` — compact completion manifest/checkpoint.

## Next structured derivative

Begin the **source-visible song/performance inventory and per-song authorship mapping gate**. Use the booklet's own evidence first. Do **not** infer lyric authorship from `திரைக்கதை வசனம் / மு. கருணாநிதி`, performer identity, proximity to dialogue, or soundtrack memory. Missing lyrics remain absent unless they are printed in the source.
