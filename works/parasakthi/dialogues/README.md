# பராசக்தி — dialogue index

**Stage:** structured derivatives  
**Canonical authority:** fully verified Tamil transcription  
**Dialogue index status:** in progress — verified through scenes **1–20**

This directory is a machine-readable dialogue derivative built from the verified canonical Tamil / completed scene derivatives. It does **not** replace, normalize, or repair the canonical transcription.

## Files and storage

- `schema.json` — fixed deterministic dialogue-record schema.
- `index.json` — compact manifest and extraction checkpoint.
- `records/scene-XX.json` — all dialogue records belonging to one observed canonical scene.

The original scenes 1–2 pilot was migrated losslessly into scene-sharded files before bulk extraction. That was a storage-only change; the record schema remains fixed.

## Record rules

Each dialogue record represents exactly one explicitly speaker-labelled utterance and carries:

- stable `id` in the form `parasakthi-sNNN-dNNN`;
- `canonical_scene`;
- `source_scene_heading` from `../scenes/index.json`;
- exact `speaker_label` before the colon;
- exact `text` without normalization;
- one or more `page_provenance` entries;
- `source_scene_file`.

A `page_segments` array is added only when one utterance crosses a canonical page boundary.

### Speaker labels

Do **not** expand, merge, or standardize labels. Variants such as `சந்`, `சந்திர`, `ஞான`, `ஞா`, `மாணிக்கம்`, `மாணிக்`, `மாணி`, `மணி`, `கல்யாணி`, `கல்யா`, and `கல்` remain exactly as represented in the verified Tamil. Character normalization belongs in the later character index.

### Dialogue versus other textual material

Included: material explicitly marked by a speaker label.

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
- scene 19's unlabelled performance/verse passages following the initial labelled `குண` line are excluded until the next explicit speaker label.

### Page boundaries

A single utterance crossing a page anchor remains one record. `page_provenance` lists every involved page and `page_segments` records the exact text belonging to each page.

Verified cross-page records through scene 20:

- `parasakthi-s001-d001` — `தங்கப்பன்`, PDF 4 / printed p.3 → PDF 5 / printed p.4.
- `parasakthi-s009-d001` — `குண`, PDF 12 / printed p.11 → PDF 13 / printed p.12.
- `parasakthi-s013-d023` — `குண`, PDF 16 / printed p.15 → PDF 17 / printed p.16.

### Scene-number provenance

For ordinary scenes, `source_scene_heading` equals `canonical_scene`. Later:

- canonical scene 43 must retain `source_scene_heading: 48`;
- canonical scene 48 must retain `source_scene_heading: 43`.

Headings 23 and 34 are not observed and must not be invented.

## Verified extraction through scene 20

Per-scene record counts:

- scenes 1–10: **1, 41, 8, 8, 5, 19, 22, 5, 1, 7**
- scene 11 — **2**
- scene 12 — **7**
- scene 13 — **26**
- scene 14 — **16**
- scene 15 — **16**
- scene 16 — **10**
- scene 17 — **1**
- scene 18 — **11**
- scene 19 — **11**
- scene 20 — **36**

Scenes 11–20 add **136 records**. Cumulative state: **253 dialogue records across 20 completed scenes**.

## Next batch

Extract and verify the next observed canonical scenes in the **21–30 range**: **21, 22, 24, 25, 26, 27, 28, 29 and 30**. Scene 23 is absent and must not be created. Preserve the same fixed schema, exact labels, source page provenance, and scene-sharded storage.
