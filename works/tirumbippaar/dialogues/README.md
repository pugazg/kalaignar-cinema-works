# திரும்பிப்பார்! — dialogue index

**Stage:** structured derivatives  
**Canonical authority:** fully verified Tamil transcription and completed 93-scene derivative set  
**Dialogue index status:** **in progress — scenes 1–50 complete**

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

## Progress through scene 50

- scenes completed: **50 / 93**
- dialogue records: **593**
- zero-record scenes: **10, 11, 25, 26, 43**
- verified cross-page dialogue records: **3**
  - `tirumbippaar-s001-d006` — PDF 9→10 / printed pp.1→2
  - `tirumbippaar-s041-d034` — PDF 56→57 / printed pp.48→49
  - `tirumbippaar-s045-d015` — PDF 59→60 / printed pp.51→52

Batch 1, scenes 1–10: **96 records**.

Batch 2, scenes 11–20: **105 records**.

Batch 3, scenes 21–30: **93 records**.

Batch 4, scenes 31–40: **167 records**.

Batch 5, scenes 41–50: **132 records**:

- scene 41 — 36
- scene 42 — 5
- scene 43 — 0
- scene 44 — 1
- scene 45 — 23
- scene 46 — 7
- scene 47 — 17
- scene 48 — 17
- scene 49 — 20
- scene 50 — 6

### Scene 41 derivative repair during dialogue extraction

While preparing batch 5, direct comparison with the verified canonical Part 03 exposed a prior scene-41 derivative drift. The canonical text has PDF 53 dialogue `பாண்டியன்: கேளேன் தருகிறேன் ...`, followed by the PDF 54 exchange beginning `பரந்தாமன்: (கேலியாக சிரித்து விட்டு) சரியான திருடன்பா!...`; the stored scene derivative had previously substituted different wording and omitted the PDF 54 page anchor.

`../scenes/scene-41.md` was repaired from the already-verified canonical transcription before dialogue extraction. No canonical transcription was changed. The repair also restores the genuine cross-page Poomaal utterance spanning PDF 56→57, represented as `tirumbippaar-s041-d034` with `page_segments`.

Scene 43 correctly has zero dialogue records because its printed content is unlabelled narrative about the office boy singing `கலப்படம்` and Paranthaman reacting; neither the song text nor a speaker-labelled utterance is printed there.

Scene 44 has one dialogue record: Pandiyan's explicitly labelled opening paragraph. The following paragraph after the standalone `(கருடன் ஆத்திரம்)` direction is an unlabelled continuation and therefore remains in the scene/canonical layer rather than being silently merged into the dialogue record.

Scene 45 contributes the second new cross-page record in this batch: Pandiyan's `லஞ்சத்திலே சிக்கவடி-` line continues on the next page as `கும் பரந்தாமனல்ல நான்...`, preserved as `tirumbippaar-s045-d015` with page segments.

Scene 31 contains an unlabelled song-performance direction plus two explicitly labelled utterances; the song itself is not converted into dialogue records because no lyrics or explicit song speaker labels are printed there.

Scene 33 preserves the source's standalone direction `(ஒருவனிடம்)` and following unlabelled `ஏய்....நீ ஆமோதிடா!` in the scene derivative, but the dialogue record for Punnakodi stops before that standalone direction. The later explicitly labelled `ஒருவன்:` utterance is indexed normally. This follows the same explicit-label boundary rule used throughout the dialogue layer.

Scenes 25 and 26 correctly have zero dialogue records because both are composed of unlabelled narrative/stage material. Scene 29's standalone `கோஷம்` likewise remains in the canonical/scene layer rather than being silently assigned to a speaker.

## Next batch

Extract and verify dialogue records for **scenes 51–60** from the completed scene derivatives and canonical Tamil, keeping this schema fixed.
