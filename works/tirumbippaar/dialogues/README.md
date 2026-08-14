# திரும்பிப்பார்! — dialogue index

**Stage:** structured derivatives  
**Canonical authority:** fully verified Tamil transcription and completed 93-scene derivative set  
**Dialogue index status:** **in progress — scenes 1–30 complete**

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

## Progress through scene 30

- scenes completed: **30 / 93**
- dialogue records: **294**
- zero-record scenes: **10, 11, 25, 26**
- verified cross-page dialogue records: **1**
  - `tirumbippaar-s001-d006` — PDF 9→10 / printed pp.1→2

Batch 1, scenes 1–10: **96 records**.

Batch 2, scenes 11–20: **105 records**.

Batch 3, scenes 21–30: **93 records**:

- scene 21 — 10
- scene 22 — 6
- scene 23 — 2
- scene 24 — 4
- scene 25 — 0
- scene 26 — 0
- scene 27 — 5
- scene 28 — 29
- scene 29 — 23
- scene 30 — 14

Scenes 25 and 26 correctly have zero dialogue records: both are composed of unlabelled narrative/stage material rather than explicitly speaker-labelled utterances. Scene 29 preserves the standalone `கோஷம்` block in the scene derivative, but that unlabelled chant is not converted into dialogue records. Scene 29 also crosses the part-02 → part-03 storage boundary at PDF 36; no individual labelled utterance crosses that page boundary, so no new `page_segments` record is required.

Scene 10 correctly has zero dialogue records because it consists only of an unlabelled visual description of Bama's tears becoming a waterfall/river. Scene 11 likewise has zero dialogue records because the source gives only an unlabelled direction that Paranthaman and another woman are singing while travelling by boat; no lyrics or explicit speaker-labelled utterance are printed in that scene.

In scene 5, the unlabelled `ஏ பையா! கூடா ஒரு கப் காபி கொண்டாந்து கொடு.` following a standalone stage direction remains excluded rather than being silently assigned to Garudan. The same explicit-label discipline is retained throughout the dialogue layer.

## Next batch

Extract and verify dialogue records for **scenes 31–40** from the completed scene derivatives and canonical Tamil, keeping this schema fixed.
