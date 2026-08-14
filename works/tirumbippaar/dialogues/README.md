# திரும்பிப்பார்! — dialogue index

**Stage:** structured derivatives  
**Canonical authority:** fully verified Tamil transcription and completed 93-scene derivative set  
**Dialogue index status:** **in progress — scenes 1–40 complete**

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

## Progress through scene 40

- scenes completed: **40 / 93**
- dialogue records: **461**
- zero-record scenes: **10, 11, 25, 26**
- verified cross-page dialogue records: **1**
  - `tirumbippaar-s001-d006` — PDF 9→10 / printed pp.1→2

Batch 1, scenes 1–10: **96 records**.

Batch 2, scenes 11–20: **105 records**.

Batch 3, scenes 21–30: **93 records**.

Batch 4, scenes 31–40: **167 records**:

- scene 31 — 2
- scene 32 — 28
- scene 33 — 6
- scene 34 — 6
- scene 35 — 20
- scene 36 — 23
- scene 37 — 47
- scene 38 — 13
- scene 39 — 18
- scene 40 — 4

Scene 31 contains an unlabelled song-performance direction plus two explicitly labelled utterances; the song itself is not converted into dialogue records because no lyrics or explicit song speaker labels are printed there.

Scene 33 preserves the source's standalone direction `(ஒருவனிடம்)` and following unlabelled `ஏய்....நீ ஆமோதிடா!` in the scene derivative, but the dialogue record for Punnakodi stops before that standalone direction. The later explicitly labelled `ஒருவன்:` utterance is indexed normally. This follows the same explicit-label boundary rule used throughout the dialogue layer.

No new cross-page dialogue record occurs in scenes 31–40. Several scenes span multiple printed pages, but their explicitly labelled utterances end before each page anchor; the existing `page_segments` inventory therefore remains unchanged.

Scenes 25 and 26 correctly have zero dialogue records because both are composed of unlabelled narrative/stage material. Scene 29's standalone `கோஷம்` likewise remains in the canonical/scene layer rather than being silently assigned to a speaker.

## Next batch

Extract and verify dialogue records for **scenes 41–50** from the completed scene derivatives and canonical Tamil, keeping this schema fixed.
