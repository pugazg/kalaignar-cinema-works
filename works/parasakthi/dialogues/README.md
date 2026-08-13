# பராசக்தி — dialogue index

**Stage:** structured derivatives  
**Canonical authority:** fully verified Tamil transcription  
**Dialogue index status:** pilot

This directory is a machine-readable dialogue derivative built from the verified canonical Tamil / completed scene derivatives. It does **not** replace, normalize, or repair the canonical transcription.

## Files

- `schema.json` — deterministic record schema.
- `index.json` — dialogue records and extraction checkpoint.

## Record rules

Each dialogue record represents exactly one speaker-labelled utterance from a canonical scene.

Required provenance:

- stable `id` in the form `parasakthi-sNNN-dNNN`;
- `canonical_scene`;
- `source_scene_heading` from `scenes/index.json`;
- exact `speaker_label` as represented before the colon in the verified Tamil;
- `text` copied without normalization;
- one or more `page_segments`, each carrying `pdf_page`, `printed_page`, and the text belonging to that page;
- `source_scene_file`.

### Speaker labels

Do **not** expand or standardize labels. For example, `சந்`, `ஞான`, `குண`, `சரஸ்`, and `பேசு` remain exactly those labels. Character-name normalization belongs in a later character-index layer, not here.

### Page boundaries

If an utterance crosses a page anchor, it remains **one dialogue record**. Its `page_segments` array records each source page separately, and `text` joins those verified segments with a newline. Do not split a single utterance merely because the scan page changes.

### Material excluded from dialogue records

The dialogue index contains only speaker-labelled utterances. The following remain outside the dialogue records:

- scene headings;
- stage directions / parenthetical narrative blocks that are not attached to a speaker line;
- songs and verse blocks without a speaker label;
- editorial/provenance comments;
- printer marks and back matter.

Parenthetical text occurring **inside a speaker-labelled utterance** remains part of that utterance exactly as transcribed.

### Scene-number provenance

For ordinary scenes, `source_scene_heading` equals `canonical_scene`. For the documented booklet misprints:

- canonical scene 43 uses `source_scene_heading: 48`;
- canonical scene 48 uses `source_scene_heading: 43`.

Do not revert these canonical scene numbers.

## Pilot batch

The initial verified pilot covers canonical **scenes 1–2**.

This deliberately tests:

1. scene 1's unlabelled opening song, which is excluded from dialogue records;
2. scene 1's `தங்கப்பன்` utterance spanning PDF 4 / printed p.3 and PDF 5 / printed p.4 as one record with two page segments;
3. scene 2's abbreviated speaker labels, which are preserved exactly rather than expanded.

After the pilot is checked against `scenes/scene-01.md`, `scenes/scene-02.md`, and `scenes/index.json`, bulk extraction can proceed in scene batches without changing the schema unless a genuinely new source structure requires it.
