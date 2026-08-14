# திரும்பிப்பார்! — dialogue index

**Stage:** structured derivatives  
**Canonical authority:** fully verified Tamil transcription and completed 93-scene derivative set  
**Dialogue index status:** **in progress — scenes 1–20 complete**

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

## Progress through scene 20

- scenes completed: **20 / 93**
- dialogue records: **201**
- zero-record scenes: **10, 11**
- verified cross-page dialogue records: **1**
  - `tirumbippaar-s001-d006` — PDF 9→10 / printed pp.1→2

Batch 1, scenes 1–10: **96 records**.

Batch 2, scenes 11–20: **105 records**:

- scene 11 — 0
- scene 12 — 21
- scene 13 — 8
- scene 14 — 1
- scene 15 — 19
- scene 16 — 5
- scene 17 — 21
- scene 18 — 3
- scene 19 — 8
- scene 20 — 19

Scene 10 correctly has zero dialogue records because it consists only of an unlabelled visual description of Bama's tears becoming a waterfall/river. Scene 11 likewise has zero dialogue records because the source gives only an unlabelled direction that Paranthaman and another woman are singing while travelling by boat; no lyrics or explicit speaker-labelled utterance are printed in that scene.

In scene 5, the unlabelled `ஏ பையா! கூடா ஒரு கப் காபி கொண்டாந்து கொடு.` following a standalone stage direction remains excluded rather than being silently assigned to Garudan. The same explicit-label discipline is retained in scenes 11–20: unlabelled song/stage material is preserved in the scene derivative but not converted into dialogue records.

## Next batch

Extract and verify dialogue records for **scenes 21–30** from the completed scene derivatives and canonical Tamil, keeping this schema fixed.
