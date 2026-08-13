# பராசக்தி — dialogue index

**Stage:** structured derivatives  
**Canonical authority:** fully verified Tamil transcription  
**Dialogue index status:** in progress — verified through observed scenes in the **1–30 range**

This directory is a machine-readable dialogue derivative built from the verified canonical Tamil / completed scene derivatives. It does **not** replace, normalize, or repair the canonical transcription.

## Files and storage

- `schema.json` — fixed deterministic dialogue-record schema.
- `index.json` — compact manifest and extraction checkpoint.
- `records/scene-XX.json` — all dialogue records belonging to one observed canonical scene.

The original scenes 1–2 pilot was migrated losslessly into scene-sharded files before bulk extraction. That was a storage-only change; the record schema remains fixed.

## Record rules

Each dialogue record represents exactly one explicitly speaker-labelled utterance and carries a stable ID, canonical/source scene numbers, exact speaker label, exact Tamil text, PDF/printed-page provenance, and source scene file. A `page_segments` array is added only when one utterance crosses a canonical page boundary.

### Speaker labels

Do **not** expand, merge, or standardize labels. Variants such as `சந்`, `சந்திர`, `ஞான`, `ஞா`, `மாணிக்கம்`, `மாணிக்`, `மாணி`, `மணி`, `கல்யாணி`, `கல்யா`, and `கல்` remain exactly as represented in the verified Tamil. Character normalization belongs in the later character index.

### Explicit label punctuation anomalies

The record schema itself is unchanged, but this batch encountered a genuine source-layout variation: an utterance can be explicitly speaker-labelled even when the booklet/transcription does not use the usual colon delimiter.

Documented cases:

- scene 21 final line: `கல் ! கிறுக்கண்ணு! கிறுக்கண்ணு!` → indexed as `parasakthi-s021-d040`; no colon is inserted into the canonical source.
- scene 25: two `சி. ஜி. டி.` utterances omit the usual colon → indexed as `parasakthi-s025-d011` and `parasakthi-s025-d017`.

These are retained because the speaker prefix is explicit in the source. The corresponding scene-record wrappers preserve the anomalous source forms in `source_label_anomalies`.

### Dialogue versus other textual material

Included: material explicitly marked by a speaker label, including the documented punctuation-anomaly cases above.

Excluded:

- scene headings;
- standalone stage directions / narrative prose;
- unlabelled songs and verse blocks;
- unlabelled monologue/prose even when context strongly identifies the speaker;
- editorial/provenance comments;
- printer marks and back matter.

Parenthetical text inside a speaker-labelled utterance remains part of that utterance exactly as transcribed. Explicitly speaker-labelled sung/verse material is indexed; unlabelled songs are not.

Examples already verified:

- scene 4's labelled `தங்` / `கல்` / `இரு` verse exchange is indexed;
- scene 8's unlabelled opening song is excluded;
- scene 17's unlabelled lullaby and unlabelled `மனசாட்சி` prose are excluded, while its explicitly labelled `குண` utterance is indexed;
- scenes 26 and 29 contain no explicitly speaker-labelled utterances, so their record files correctly contain **0 records**.

### Page boundaries

A single utterance crossing a page anchor remains one record. `page_provenance` lists every involved page and `page_segments` records the exact text belonging to each page.

Verified cross-page records through this checkpoint:

- `parasakthi-s001-d001` — PDF 4→5.
- `parasakthi-s009-d001` — PDF 12→13.
- `parasakthi-s013-d023` — PDF 16→17.
- `parasakthi-s028-d023` — PDF 33→34.

### Scene-number provenance

For ordinary scenes, `source_scene_heading` equals `canonical_scene`. Later:

- canonical scene 43 must retain `source_scene_heading: 48`;
- canonical scene 48 must retain `source_scene_heading: 43`.

Headings 23 and 34 are not observed and must not be invented.

## Verified extraction checkpoint

Dialogue indexing is now verified for **29 observed scenes**: canonical scenes **1–22 and 24–30**. Scene 23 remains absent.

- Previous cumulative total through scene 20: **253**
- Observed scenes 21–30 batch: **160**
- Cumulative dialogue records: **413**

This batch's per-scene counts:

- scene 21 — **40**
- scene 22 — **11**
- scene 24 — **6**
- scene 25 — **26**
- scene 26 — **0**
- scene 27 — **3**
- scene 28 — **48**
- scene 29 — **0**
- scene 30 — **26**

Scene 30 is a cross-part scene: it starts on PDF 35 in Part 01 and continues on PDF 36 in Part 02. `records/scene-30.json` is built from the complete scene derivative and is not truncated at the transcription-file boundary.

## Next batch

Extract and verify the next observed canonical scenes in the **31–40 range**: **31, 32, 33, 35, 36, 37, 38, 39 and 40**. Scene 34 is absent and must not be created. Preserve the fixed record schema, exact Tamil, source-label anomalies when explicitly present, page provenance and scene-sharded storage.
