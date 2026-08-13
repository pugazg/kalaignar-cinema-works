# பராசக்தி — character index

**Stage:** structured derivatives  
**Authority:** completed 642-record dialogue index  
**Status:** pilot verified

This directory maps the booklet's exact dialogue `speaker_label` values to stable character/entity identifiers. It is a separate derivative layer: **no dialogue record is rewritten, normalized, or relabelled**.

## Files

- `schema.json` — entity/mapping schema.
- `labels-inventory.json` — complete inventory of the exact speaker labels present in all 642 dialogue records.
- `entities-pilot.json` — first evidence-backed character mappings.
- `index.json` — current character-index checkpoint.

## Complete source-label inventory

The completed dialogue layer contains:

- **642** dialogue records;
- **46** observed scenes;
- **69 distinct exact `speaker_label` strings**.

The inventory records each exact label and the canonical scenes in which it occurs. Labels are not silently expanded even where an abbreviation looks obvious.

## Mapping policy

1. The exact `speaker_label` inside `dialogues/records/` is immutable.
2. A stable entity may collect multiple exact source-label variants only when source context supports the identity.
3. Similar spelling alone is not enough to merge labels.
4. Generic labels (`ஒரு`, `மற்`, `மற்ற`, ordinal speakers, role descriptions, etc.) may later become role/collective entities rather than named characters.
5. Ambiguous labels stay unresolved until sufficient source-context evidence exists.
6. `supporting_records` in an entity are representative evidence anchors, not an exhaustive list of every utterance by that entity.
7. `scenes` is the union of scenes containing the mapped exact source labels.

## Verified pilot

The pilot contains **8 character entities** covering **18 of the 69 exact labels**:

- `parasakthi-char-gunasekaran` — குணசேகரன் — `குண`
- `parasakthi-char-kalyani` — கல்யாணி — `கல்யாணி`, `கல்யா`, `கல்`
- `parasakthi-char-chandrasekaran` — சந்திரசேகரன் — `சந்`, `சந்திர`, `சேகர்`
- `parasakthi-char-gnanasekaran` — ஞானசேகரன் — `ஞான`, `ஞா`
- `parasakthi-char-saraswati` — சரஸ்வதி — `சரஸ்`, `சர`
- `parasakthi-char-thangappan` — தங்கப்பன் — `தங்கப்பன்`, `தங்`
- `parasakthi-char-manickam-pillai` — மாணிக்கம் பிள்ளை — `மாணிக்கம்`, `மாணிக்`, `மாணி`, `மணி`
- `parasakthi-char-vimala` — விமலா — `விம`

All eight pilot entities are marked `verified` / `high` confidence because their mappings are supported by direct dialogue context and recurring scene continuity.

### Deliberately unresolved in the pilot

The pilot does **not** map labels merely because a likely identity can be inferred. For example, `நொண்டி` and `நொ` remain outside the ஞானசேகரன் entity pending the systematic expansion pass. Generic labels such as `ஒரு`, `மற்`, `வந்த`, `வந்`, and ordinal labels also remain unmapped.

## Checkpoint

- Distinct exact source labels: **69**
- Pilot entities: **8**
- Exact labels mapped in pilot: **18**
- Labels remaining for systematic review: **51**
- Existing dialogue records modified: **0**

## Next activity

Expand the character/entity mapping across the remaining **51 exact labels**. Resolve straightforward named and recurring role labels using source-context evidence, create role/collective entities where appropriate, and leave genuinely ambiguous abbreviations explicitly unresolved. Only after that full pass should the character index be marked complete.
