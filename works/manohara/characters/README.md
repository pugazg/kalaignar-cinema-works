# மனோகரா — character / entity index

Status: **pilot-verified / in progress**.

This is a downstream interpretive layer built from the **983 complete-verified immutable dialogue records**. It maps exact source-visible speaker labels to characters, roles or collectives without changing `speaker_label` or dialogue text in any source record.

## Source discipline

- `../dialogues/index.json` and `../dialogues/records/scene-###.json` are the structured source for this layer.
- `labels-inventory.json` inventories every exact non-empty speaker label before normalization.
- spelling, abbreviation and punctuation variants remain visible as separate source labels;
- a label is mapped to a named character only when verified scene context supports that identity;
- reused labels are **not** forced into one character merely because one occurrence is obvious;
- play-within-the-play identities remain distinct from the outer story unless the source explicitly supports a cross-layer identity;
- the 983 dialogue records remain immutable.

## Exact-label inventory checkpoint

The complete dialogue inventory contains **111 distinct non-empty source speaker labels** across **57 archival scene shards / 983 records**. `manohara-s024` has zero labelled dialogue and therefore contributes no speaker label.

The inventory intentionally preserves forms such as `வ. சே`, `வ. சே.`, `கே. வ`, `கே. வ.`, `சத். சீல`, `சிப்பாய் 2`, and the longer contextual forms `வசந்தசேனை மனதிற்குள்`, `நாடகம் பார்க்கும் ராஜப்பிரியன்` and `நாடகம் பார்க்கும் வசந்தசேனா` exactly as stored in the verified dialogue records.

## Pilot checkpoint

The first verified pilot establishes **10 named characters** and maps **51/111 exact labels**. **60 labels remain undisposed** for the next character-index pass.

Pilot entities:

- `மனோகரன்`
- `பத்மாவதி`
- `புருஷோத்தமன்`
- `வசந்தசேனை`
- `வசந்தன்`
- `விஜயா`
- `ராஜப்பிரியன்`
- `சத்யசீலர்`
- `கேசரிவர்மன்`
- `உக்ரசேனன்`

All ten pilot entities are `verified` / `high` confidence. Representative immutable dialogue IDs are stored with each entity in `entities-pilot.json`.

## Deliberately unresolved/reused labels

Several exact labels cannot safely be collapsed globally and are therefore **not** assigned in the pilot:

- `வச` is used for **வசந்தசேனை** in some scenes and **வசந்தன்** in others; scene 41 itself demonstrates both uses within one archival scene.
- `வசந்` likewise alternates between வசந்தசேனை and வசந்தன் depending on source context.
- `சேனா` is used for the play-within-the-play **தேவசேனா** in scene 8 and for வசந்தசேனை in later outer-story scenes.
- `அட்` is used for the real அக்ஷயன் and, elsewhere, for மனோகரன் while he is in the false-Akshayan disguise.
- `வர்` is used in the nested play's வர்மன் material and later for கேசரிவர்மன்.
- `தோழி` / `தோ` are generic attendant/friend labels used in more than one context and are not automatically equated with a single named woman.

These are not transcription defects. They are source-level label reuse and must be handled as explicit role/context dispositions rather than silently normalized.

## Nested play safeguard

Scene 8 contains a play-within-the-play with labels including `உத்தம புருஷன்`, `ஈஸ்வரி வர்மன்`, `கமலாவதி`, `தேவசேனா`, `ராஜா`, `வர்மன்`, `வர்மா`, `கம`, `உத்`, `அஜயன்`, `அஜ`, and `நாடக தேவசேனா`. Those performance identities are not automatically merged with similarly patterned outer-story characters. The main-story observer labels `நாடகம் பார்க்கும் ராஜப்பிரியன்` and `நாடகம் பார்க்கும் வசந்தசேனா`, however, are explicitly source-labelled as the outer characters and are safely mapped in the pilot.

## Files

- `schema.json` — Manohara entity-derivative schema.
- `labels-inventory.json` — complete exact-label inventory, **111 labels**.
- `entities-pilot.json` — first **10 verified entities / 51 mapped labels**.
- `index.json` — current character-layer checkpoint.

## Next activity

Dispose the remaining **60 exact labels** into verified named characters, stable roles/collectives, or explicit review/unresolved entities. Reused shorthand labels must remain context-safe; do not rewrite the dialogue layer to make normalization easier.
