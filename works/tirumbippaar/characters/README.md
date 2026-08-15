# திரும்பிப்பார்! — character index

**Stage:** structured derivatives  
**Canonical authority:** verified Tamil transcription, completed 93-scene derivatives, and completed 1,040-record dialogue index  
**Character index status:** **complete-verified — 45/45 exact speaker labels dispositioned**

This directory maps the dialogue layer's exact `speaker_label` values to stable named characters, unnamed roles, or collective entities. It is a derivative only: **no dialogue record is rewritten, relabelled, normalized, or corrected here**.

## Files

- `schema.json` — deterministic character/entity schema.
- `labels-inventory.json` — complete inventory of the **45** distinct exact speaker labels observed across all 93 dialogue shards.
- `entities-pilot.json` — verified pilot mapping for the eight central recurring characters.
- `entities.json` — complete verified mapping of all exact labels.
- `index.json` — compact completion manifest/checkpoint.

## Completion summary

- dialogue records scanned: **1,040**
- scenes scanned: **93 / 93**
- distinct exact source labels: **45**
- stable entities / role categories: **39**
- verified entities: **39**
- review entities: **0**
- unresolved entities: **0**
- verified source labels: **45**
- review source labels: **0**
- unresolved source labels: **0**
- label coverage: **45 / 45**
- dialogue records modified: **no**

A `verified` role or collective means the exact source label has a verified disposition; it does **not** imply that every generic occurrence is one physical person.

## Mapping discipline

Named characters are merged only where the source context establishes continuity. Generic or reused labels remain roles/collectives instead of being forced into named-character identities.

Important cases:

- `குணமணி` and `குண்டுமணி` map to the stable character **குண்டுமணி**. Both exact forms occur in the same Poomaal/Kumudha household-helper continuity; both source spellings remain untouched in dialogue records.
- `அவன் குரல்` in scene 79 maps to **பாண்டியன்** because the scene itself places Pandiyan at Kumudha's locked house immediately before that voice-over.
- `குரல்` is **not** globally mapped to Pandiyan, Bama, or Punnakodi. The exact label is reused for different contextual voices in scenes 38, 67 and 72, so it remains a `role` category.
- `பையன்` is a generic role category. It appears in materially different contexts — including the publishing office and Poomaal's teaching scene — and is not treated as one continuing boy.
- `ஒரு தொழிலாளி`, `தொழிலாளி`, `தொழிலாளி ஒருவன்`, and `மற்றொரு தொழிலாளி` are grouped under an unnamed **தொழிலாளி** role category. This groups equivalent role labels without asserting one individual worker.
- `தொழிலாளர்கள்`, `கூட்டம்`, and `மற்றவர்கள்` remain collective entities.
- `போலீஸ்` and `II போலீஸ்` form a police-role category and do not imply one officer.
- `Echo` in scene 81 remains a source-visible performance/echo device rather than being assigned to a human character.
- `முதலாளி` is mapped to the stable unnamed **மில் முதலாளி** because the same Sivashakti Mill owner / Usha's father recurs across the labour and household sequences.
- `வாட்ச்மேன்` remains an unnamed recurring role; the source supports his continuity around Kumudha but never supplies a personal name.

## Source policy

The character layer may resolve aliases or role equivalence, but it may not alter the canonical transcription or dialogue records. Exact source labels remain the evidence trail. Similar spelling alone is not enough to merge identities, and contextual ambiguity is never repaired from film memory, subtitles, web copies, or later editions.

## Next structured derivative

Begin the **per-song authorship mapping gate**. Use only source-supported booklet credits and the verified song/performance blocks before creating song-specific Tamil derivatives or any English song translations. Do not infer lyric authorship merely from proximity to dialogue or a character performance.
