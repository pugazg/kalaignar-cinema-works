# திரும்பிப்பார்! — character index

**Stage:** structured derivatives  
**Canonical authority:** corrected/scan-closed Tamil transcription, completed 93-scene derivatives, and completed **1,042-record** dialogue index  
**Character index status:** **complete-verified-reconciled — 45/45 exact speaker labels dispositioned**

This directory maps the dialogue layer's exact `speaker_label` values to stable named characters, unnamed roles, or collective entities. It is a derivative only: **no dialogue record is rewritten, relabelled, normalized, or corrected here**.

## Files

- `schema.json` — deterministic character/entity schema.
- `labels-inventory.json` — complete inventory of the **45** distinct exact speaker labels observed across all 93 dialogue shards after corrected-source reconciliation.
- `entities-pilot.json` — reconciled pilot mapping for the eight central recurring characters.
- `entities.json` — complete reconciled mapping of all exact labels.
- `index.json` — compact completion manifest/checkpoint.

## Reconciled completion summary

- dialogue records scanned: **1,042**
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
- dialogue records modified by this layer: **no**
- stable entity IDs preserved from the historical mapping wherever identity continuity was unchanged: **yes**

A `verified` role or collective means the exact source label has a verified disposition; it does **not** imply that every generic occurrence is one physical person.

## Corrections reflected from the stable dialogue corpus

The historical character layer was built against 1,040 dialogue records and therefore became stale when the Tamil correction pass repaired exact labels and recovered two omitted scene-41 utterances. The regenerated layer now reflects the stable 1,042-record corpus.

Important exact-label changes include:

- `பூமால்` → `பூமாலை`;
- `புண்ணகோடி` → `புண்யகோடி`;
- historical OCR variant `குணமணி` resolved to `குண்டுமணி` throughout the corrected dialogue records;
- `ஊஷா` → `உஷா`;
- `சமையல்காரி` → `சமையல்காரன்`;
- `அம்மாள்` → `அம்மாமி`;
- the old normalized `சப்-இன்ஸ்பெக்டர்` inventory entry is replaced by the two exact printed spacing variants `சப்- இன்ஸ்பெக்டர்` and `சப் - இன்ஸ்பெக்டர்`.

These are evidence-layer updates, not silent normalization. The entity layer may group exact spelling/spacing variants when source context proves one role, while the immutable dialogue records continue to preserve the exact printed labels.

## Mapping discipline

Named characters are merged only where the source context establishes continuity. Generic or reused labels remain roles/collectives instead of being forced into named-character identities.

Important cases:

- `குண்டுமணி` maps to the stable household-helper character **குண்டுமணி**. The former `குணமணி` inventory variant was an earlier transcription error and is no longer treated as a valid exact source label.
- `அவன் குரல்` in scene 79 maps to **பாண்டியன்** because the scene itself places Pandiyan at Kumudha's locked house immediately before that voice-over.
- `குரல்` is **not** globally mapped to Pandiyan, Bama, or Punyakodi. The exact label is reused for different contextual voices in scenes 38, 67 and 72, so it remains a `role` category.
- `பையன்` is a generic role category. It appears in materially different contexts and is not treated as one continuing boy.
- `ஒரு தொழிலாளி`, `தொழிலாளி`, `தொழிலாளி ஒருவன்`, and `மற்றொரு தொழிலாளி` are grouped under an unnamed **தொழிலாளி** role category. This groups equivalent role labels without asserting one individual worker.
- `தொழிலாளர்கள்`, `கூட்டம்`, and `மற்றவர்கள்` remain collective entities.
- `போலீஸ்` and `II போலீஸ்` form a police-role category and do not imply one officer.
- `சப்- இன்ஸ்பெக்டர்` and `சப் - இன்ஸ்பெக்டர்` map to one unnamed sub-inspector role while retaining both exact source labels.
- `Echo` in scene 81 remains a source-visible performance/echo device rather than being assigned to a human character.
- `முதலாளி` is mapped to the stable unnamed **மில் முதலாளி** because the same Sivashakti Mill owner / Usha's father recurs across the labour and household sequences.
- `வாட்ச்மேன்` remains an unnamed recurring role; the source supports his continuity around Kumudha but never supplies a personal name.

## Source policy

The character layer may resolve aliases or role equivalence, but it may not alter the canonical transcription or dialogue records. Exact source labels remain the evidence trail. Similar spelling alone is not enough to merge identities, and contextual ambiguity is never repaired from film memory, subtitles, web copies, or later editions.

## Next structured derivative

The character/entity layer is now synchronized with the corrected Tamil source. The next activity is to reconcile the **English translation and reader/export/EPUB layers** wherever the corrected Tamil changes wording, meaning, exact speaker linkage, or source structure. Historical verification of those downstream outputs remains provisional until that pass is complete.
