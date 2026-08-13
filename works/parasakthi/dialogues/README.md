# பராசக்தி — dialogue index

**Stage:** structured derivatives  
**Canonical authority:** fully verified Tamil transcription  
**Dialogue index status:** in progress — verified through scenes **1–10**

This directory is a machine-readable dialogue derivative built from the verified canonical Tamil / completed scene derivatives. It does **not** replace, normalize, or repair the canonical transcription.

## Files and storage

- `schema.json` — fixed deterministic dialogue-record schema.
- `index.json` — compact manifest and extraction checkpoint.
- `records/scene-XX.json` — all dialogue records belonging to one observed canonical scene.

The pilot originally stored scenes 1–2 directly in `index.json`. Before the first bulk batch, those 42 records were migrated losslessly into scene-sharded files. This changes only storage layout; **the dialogue-record schema is unchanged**. Scene sharding keeps later extraction auditable without repeatedly rewriting one large JSON record array.

## Record rules

Each dialogue record represents exactly one speaker-labelled utterance from a canonical scene and carries:

- stable `id` in the form `parasakthi-sNNN-dNNN`;
- `canonical_scene`;
- `source_scene_heading` from `../scenes/index.json`;
- exact `speaker_label` as represented before the colon in the verified Tamil;
- `text` copied without normalization;
- one or more `page_provenance` entries carrying `pdf_page` and `printed_page`;
- `source_scene_file`.

A `page_segments` array is added only when one utterance crosses a page boundary, so the exact source-page break remains recoverable.

### Speaker labels

Do **not** expand, merge, or standardize labels. Forms such as `சந்`, `சந்திர`, `ஞான`, `ஞா`, `மாணிக்கம்`, `மாணிக்`, `மாணி`, and `மணி` remain exactly as represented in the verified Tamil. Character-name normalization belongs in a later character-index layer.

### Page boundaries

If an utterance crosses a page anchor, it remains **one dialogue record**. `page_provenance` lists every involved page and `page_segments` records the exact text belonging to each page.

Verified cross-page records through scene 10:

- `parasakthi-s001-d001` — `தங்கப்பன்`, PDF 4 / printed p.3 → PDF 5 / printed p.4.
- `parasakthi-s009-d001` — `குண`, PDF 12 / printed p.11 → PDF 13 / printed p.12.

### Dialogue versus other textual material

The index contains only material that is explicitly speaker-labelled in the canonical text.

Excluded:

- scene headings;
- standalone stage directions / narrative prose;
- unlabelled songs and verse blocks;
- editorial/provenance comments;
- printer marks and back matter.

Parenthetical text occurring **inside a speaker-labelled utterance** remains part of that utterance exactly as transcribed.

Explicitly labelled sung/verse utterances are dialogue records because the booklet assigns them speaker labels. Therefore scene 4's labelled exchange (`தங்`, `கல்`, `இரு`) is indexed, while scene 8's unlabelled opening song is not.

### Scene-number provenance

For ordinary scenes, `source_scene_heading` equals `canonical_scene`. For the documented booklet misprints later in the work:

- canonical scene 43 must use `source_scene_heading: 48`;
- canonical scene 48 must use `source_scene_heading: 43`.

Do not revert those canonical scene numbers.

## Verified extraction through scene 10

Per-scene record counts:

- scene 1 — **1**
- scene 2 — **41**
- scene 3 — **8**
- scene 4 — **8**
- scene 5 — **5**
- scene 6 — **19**
- scene 7 — **22**
- scene 8 — **5**
- scene 9 — **1**
- scene 10 — **7**

Cumulative state: **117 dialogue records across 10 completed scenes**.

All scene files were checked against the corresponding verified scene derivative and canonical page anchors before this checkpoint was advanced.

## Next batch

Extract and verify dialogue records for canonical **scenes 11–20** using the same fixed schema and scene-sharded storage. Do not alter the canonical Tamil, normalize speaker labels, or infer character identities during dialogue extraction.
