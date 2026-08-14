# திரும்பிப்பார்! — dialogue index

**Stage:** structured derivatives  
**Canonical authority:** fully verified Tamil transcription and completed 93-scene derivative set  
**Dialogue index status:** **complete — scenes 1–93 complete**

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

## Final progress

- scenes completed: **93 / 93**
- dialogue records: **1,040**
- zero-record scenes: **10, 11, 25, 26, 43, 54**
- verified cross-page dialogue records: **8**
  - `tirumbippaar-s001-d006` — PDF 9→10 / printed pp.1→2
  - `tirumbippaar-s041-d034` — PDF 56→57 / printed pp.48→49
  - `tirumbippaar-s045-d015` — PDF 59→60 / printed pp.51→52
  - `tirumbippaar-s063-d003` — PDF 79→80 / printed pp.71→72
  - `tirumbippaar-s072-d001` — PDF 87→88 / printed pp.79→80
  - `tirumbippaar-s076-d012` — PDF 91→92 / printed pp.83→84
  - `tirumbippaar-s080-d022` — PDF 96→97 / printed pp.88→89
  - `tirumbippaar-s080-d028` — PDF 97→98 / printed pp.89→90

Batch totals:

- scenes 1–10 — **96 records**
- scenes 11–20 — **105 records**
- scenes 21–30 — **93 records**
- scenes 31–40 — **167 records**
- scenes 41–50 — **132 records**
- scenes 51–60 — **124 records**
- scenes 61–70 — **89 records**
- scenes 71–80 — **106 records**
- scenes 81–93 — **128 records**

The final scenes 51–93 were completed in one archival activity. They add **447 records**, taking the dialogue layer from 593 to 1,040 records.

### Explicit-label decisions in the completed layer

Scene 54 correctly has zero dialogue records. Its Reading Room material is a printed newspaper report without an explicit speaker label, so the text remains in the scene/canonical layer.

Scene 63 adds `tirumbippaar-s063-d003`, where Punnakodi's labelled utterance crosses PDF 79→80. Scene 72 adds `tirumbippaar-s072-d001`, preserving Paranthaman's PDF 87→88 utterance and the source distinction between `அழித்தெழுதாச் சித்திரமே!` and the following explicitly labelled `குரல்:` line. Scene 76 adds `tirumbippaar-s076-d012` across the Part 04→Part 05 storage boundary. Scene 80 adds two cross-page Poomaal records, `tirumbippaar-s080-d022` and `tirumbippaar-s080-d028`.

Several source-visible blocks remain intentionally outside the dialogue index. Scene 83's `அவசர வேண்டுகோள்` letter is unlabelled. Scene 84's initial newspaper/advertisement reading is unlabelled even though the staging identifies the watchman. Scene 85's address-card block is unlabelled. Scene 88's line after the standalone `(பையன் போக)` direction is unlabelled. Scene 91's mill-handover stage direction and `பத்திரிகை News` block are unlabelled. Scene 93's `வணக்கம்.` is an ending structure, not dialogue.

### Earlier derivative repair during dialogue extraction

While preparing scenes 41–50, direct comparison with verified canonical Part 03 exposed a prior scene-41 derivative drift. `../scenes/scene-41.md` was repaired from the already-verified canonical transcription to restore the canonical opening Pandiyan/Paranthaman exchange and the missing PDF 54 page anchor. No canonical transcription was changed.

## Next structured derivative

Build the **character index** from the completed 93-scene dialogue index, completed scene derivatives and verified canonical Tamil. Character normalization or alias resolution belongs there; the dialogue layer itself continues to preserve exact source speaker labels.
