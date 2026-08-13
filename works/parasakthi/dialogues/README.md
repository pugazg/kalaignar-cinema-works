# பராசக்தி — dialogue index

**Stage:** structured derivatives  
**Canonical authority:** fully verified Tamil transcription  
**Dialogue index status:** **complete and verified — 46/46 observed scenes**

This directory is a machine-readable dialogue derivative built from the verified canonical Tamil and completed scene derivatives. It does **not** replace, normalize, or repair the canonical transcription.

## Files and storage

- `schema.json` — fixed deterministic dialogue-record schema.
- `index.json` — final compact manifest/checkpoint.
- `records/scene-XX.json` — dialogue records for each observed canonical scene.

The original scenes 1–2 pilot was migrated losslessly into scene-sharded files before bulk extraction. That was a storage-only change; the record schema remained fixed.

## Record rules

Each record represents one explicitly speaker-labelled utterance and preserves:

- stable ID `parasakthi-sNNN-dNNN`;
- canonical scene number;
- printed/source scene heading where different;
- exact `speaker_label`;
- exact Tamil `text` without normalization;
- PDF/printed-page provenance;
- source scene file.

A `page_segments` array is used only when a single utterance crosses a canonical page boundary.

Speaker-label variants are **not** expanded or merged. Character normalization belongs to the next character-index layer.

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
- provenance comments, printer marks and back matter.

Parenthetical material inside a speaker-labelled utterance remains part of that utterance. A standalone direction between portions of a continuing labelled speech is not turned into dialogue text.

### Documented source-label delimiter anomalies

The canonical source is not normalized to add missing punctuation:

- `parasakthi-s021-d040` — source form `கல் ! கிறுக்கண்ணு! கிறுக்கண்ணு!`.
- `parasakthi-s025-d011` — `சி. ஜி. டி.` line without the usual colon.
- `parasakthi-s025-d017` — second `சி. ஜி. டி.` line without the usual colon.

### Scene-number provenance

The booklet contains two documented late numbering errors, preserved in dialogue records as source provenance:

- canonical **scene 43** uses `source_scene_heading: 48` (PDF 49 / printed p.48);
- canonical **scene 48** uses `source_scene_heading: 43` (PDF 57 / printed p.56).

Scenes **23 and 34 are not observed** and have no dialogue files.

## Final verified totals

- Observed scenes represented: **46 / 46**
- Dialogue records: **642**
- Zero-record observed scenes: **26, 29, 48**
- Missing source headings: **23, 34**

Final batch, scenes 41–48: **115 records**

- scene 41 — **23**
- scene 42 — **1**
- scene 43 — **19** (`source_scene_heading: 48`)
- scene 44 — **4**
- scene 45 — **30**
- scene 46 — **4**
- scene 47 — **34**
- scene 48 — **0** (`source_scene_heading: 43`)

Scene 48 correctly contains zero dialogue records because its content is the unlabelled closing song plus `—சுபம்—` / printer line.

## Cross-page dialogue records

Verified cross-page records in the complete index:

- `parasakthi-s001-d001` — PDF 4→5
- `parasakthi-s009-d001` — PDF 12→13
- `parasakthi-s013-d023` — PDF 16→17
- `parasakthi-s028-d023` — PDF 33→34
- `parasakthi-s033-d053` — PDF 41→42
- `parasakthi-s042-d001` — PDF 48→49
- `parasakthi-s043-d003` — PDF 49→50
- `parasakthi-s043-d017` — PDF 50→51
- `parasakthi-s045-d001` — PDF 51→53
- `parasakthi-s045-d003` — PDF 53→54
- `parasakthi-s045-d018` — PDF 54→55

## Next structured derivative

The dialogue index is closed as **complete/verified**. The next structured derivative is the **character index**: map exact source speaker labels to stable character entities while retaining every original label and recording uncertain/role-based mappings explicitly rather than silently normalizing them.
