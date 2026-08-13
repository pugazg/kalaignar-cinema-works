# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

Current stage: **Structured Derivatives — dialogue index complete; character index next**.

## Canonical source state

- Source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- 58 PDF pages; PDF 4–57 / printed pp.3–56 are canonical dialogue/song pages; PDF 58 is back matter.
- Tamil canonical text: **54 verified / 0 review / 0 unresolved markers**.
- Never repair Tamil from film audio, subtitles, web copies, later editions or memory.

Final reviewer-assisted Part 01 readings remain:

- PDF 5: `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?`
- PDF 16: `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

## Scene structure

- **46 observed canonical scenes**.
- Scene **23 absent**.
- Scene **34 absent**.
- PDF 49 source heading **48** → canonical scene **43**.
- PDF 57 source heading **43** → canonical final scene **48**.
- Scene 30 crosses PDF 35→36 across the Part 01 / Part 02 transcription-file boundary.
- Scene 33 spans PDF 38→42 because scene 34 is absent.
- All **46/46 observed scene derivatives are complete**.

## Dialogue index — complete

Files:

- `works/parasakthi/dialogues/schema.json` — fixed record schema.
- `works/parasakthi/dialogues/index.json` — final manifest.
- `works/parasakthi/dialogues/records/scene-XX.json` — scene-sharded records.

Final state:

- Status: **complete-verified**
- Observed scenes represented: **46 / 46**
- Dialogue records: **642**
- Zero-record observed scenes: **26, 29, 48**
- Missing headings: **23, 34**

Final batch counts:

- scene 41: 23
- scene 42: 1
- scene 43: 19 (`source_scene_heading: 48`)
- scene 44: 4
- scene 45: 30
- scene 46: 4
- scene 47: 34
- scene 48: 0 (`source_scene_heading: 43`)

Scene 48 correctly has zero dialogue records because its content is the unlabelled closing song plus `—சுபம்—` / printer line.

### Dialogue extraction rules that remain controlling

Each record represents one explicitly speaker-labelled utterance. Preserve exact Tamil, exact source speaker label, canonical/source scene provenance, PDF/printed-page provenance and source scene file.

Do not expand, merge or normalize speaker labels in dialogue records. Character identity normalization belongs only in the character-index layer.

Exclude standalone stage directions, unlabelled prose, unlabelled songs/verse, printer marks and back matter. Explicitly labelled sung/verse material remains eligible. Parenthetical text inside a labelled utterance remains part of that utterance.

When a labelled utterance crosses a page boundary, keep one record and preserve `page_segments`.

### Explicit source-label punctuation anomalies

Do not insert missing punctuation into canonical text:

- `parasakthi-s021-d040` — `கல் ! கிறுக்கண்ணு! கிறுக்கண்ணு!`
- `parasakthi-s025-d011` — `சி. ஜி. டி.` line without usual colon
- `parasakthi-s025-d017` — second `சி. ஜி. டி.` line without usual colon

### Cross-page dialogue records

The complete index has **11** verified cross-page records:

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

## Exact next work — character index

Start a **character-index pilot** without changing any existing dialogue record.

Recommended first activity:

1. Read `dialogues/schema.json`, `dialogues/index.json`, and representative record files across the work.
2. Inventory every distinct exact `speaker_label` used in the 642 records.
3. Define a character/entity schema that separates:
   - stable character/entity ID;
   - preferred display name;
   - exact source-label variants;
   - role/generic labels (`ஒரு`, `மற்`, etc.);
   - confidence/status for mappings;
   - supporting dialogue record IDs / scenes.
4. Create a small verified pilot for the central family/recurring characters only.
5. **Do not infer ambiguous abbreviations solely from similarity.** If an abbreviation cannot be tied safely to one entity from source context, retain it as unresolved or role-based.
6. Do not modify the 642 dialogue records; the character index is a separate derivative layer.

After the pilot is verified, expand the mapping across all distinct speaker labels and then update metadata/checkpoints.

Other stages remain: per-song authorship mapping not started; English translation not started.
