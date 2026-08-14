# திரும்பிப்பார்! — dialogue index

**Stage:** structured derivatives  
**Canonical authority:** fully verified Tamil transcription and completed 93-scene derivative set  
**Dialogue index status:** **in progress — scenes 1–10 complete**

This directory is a machine-readable dialogue derivative built only from the verified canonical Tamil and completed Tirumbippaar scene derivatives. It does **not** replace, normalize, correct, modernize, reconstruct, or repair the canonical transcription.

## Files and storage

- `schema.json` — fixed deterministic dialogue-record schema.
- `index.json` — compact manifest/checkpoint.
- `records/scene-XX.json` — dialogue records for each canonical scene.

## Record rules

Each record represents one explicitly speaker-labelled utterance and preserves:

- stable ID `tirumbippaar-sNNN-dNNN`;
- canonical scene number;
- source scene heading;
- exact `speaker_label`;
- exact verified Tamil `text` without normalization;
- PDF/printed-page provenance;
- source scene file.

A `page_segments` array is used only when a single utterance crosses a canonical page boundary.

Speaker-label variants are **not** expanded or merged. Character normalization belongs to the later character-index layer.

### Included / excluded material

Included:

- explicitly speaker-labelled prose;
- explicitly speaker-labelled sung/verse material;
- explicit speaker labels whose source delimiter is anomalous but unambiguous.

Excluded:

- scene headings;
- standalone stage directions and narrative prose;
- unlabelled songs/verse;
- unlabelled monologue/prose even when context identifies the speaker;
- provenance comments and printer/back-matter material.

Parenthetical material inside a speaker-labelled utterance remains part of that utterance. A standalone direction between portions of a continuing labelled speech is not silently merged into dialogue text.

## Batch 1 — scenes 1–10

- scenes completed: **10 / 93**
- dialogue records: **96**
- zero-record scenes: **10**
- cross-page dialogue records: **1**
  - `tirumbippaar-s001-d006` — PDF 9→10 / printed pp.1→2

Per-scene record counts:

- scene 1 — 8
- scene 2 — 13
- scene 3 — 2
- scene 4 — 15
- scene 5 — 25
- scene 6 — 14
- scene 7 — 12
- scene 8 — 4
- scene 9 — 3
- scene 10 — 0

Scene 10 correctly has zero dialogue records because the scene consists only of the unlabelled visual description of Bama's tears becoming a waterfall/river. The description remains preserved in the scene derivative and canonical transcription, but is not converted into a dialogue record.

In scene 5, the unlabelled `ஏ பையா! கூடா ஒரு கப் காபி கொண்டாந்து கொடு.` that follows a standalone stage direction is not silently assigned to Garudan; the dialogue layer follows the explicit-label rule used by the reference implementation.

## Next batch

Extract and verify dialogue records for **scenes 11–20** from the completed scene derivatives and canonical Tamil, keeping this schema fixed.
