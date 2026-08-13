# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

Current stage: **Structured Derivatives — dialogue index**.

## Canonical source state

- Source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- 58 PDF pages; PDF 4–57 / printed pp.3–56 are canonical dialogue/song pages; PDF 58 is back matter.
- Tamil canonical text: **54 verified / 0 review / 0 unresolved markers**.
- Do not repair Tamil from film audio, subtitles, web copies, later editions or memory.

Final reviewer-assisted Part 01 readings remain:

- PDF 5: `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?`
- PDF 16: `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

## Scene structure

- 46 observed canonical scenes.
- Scene 23 absent.
- Scene 34 absent.
- PDF 49 source heading 48 → canonical scene 43.
- PDF 57 source heading 43 → canonical final scene 48.
- Scene 30 crosses PDF 35→36 across the Part 01 / Part 02 transcription-file boundary.
- Scene 33 continues through PDF 42 because scene 34 is absent.
- All 46 observed scene derivatives are complete.

## Dialogue-index rules

Files:

- `works/parasakthi/dialogues/schema.json` — fixed record schema.
- `works/parasakthi/dialogues/index.json` — compact checkpoint.
- `works/parasakthi/dialogues/records/scene-XX.json` — scene-sharded records.

Each record represents one explicitly speaker-labelled utterance. Preserve exact Tamil, exact speaker label, canonical/source scene provenance, PDF/printed-page provenance and source scene file. Parenthetical text inside a labelled utterance remains part of it.

Exclude standalone directions, unlabelled prose, unlabelled songs/verse, printer marks and back matter. Explicitly labelled sung/verse material remains eligible.

A labelled utterance crossing a page boundary remains one record with `page_segments`.

### Explicit-label delimiter anomalies

The record schema remains unchanged, but the source sometimes marks a speaker without the normal colon. These are still indexed when the speaker prefix is explicit; never alter the canonical Tamil to insert punctuation.

Verified anomaly records:

- `parasakthi-s021-d040` — source form `கல் ! கிறுக்கண்ணு! கிறுக்கண்ணு!`.
- `parasakthi-s025-d011` — `சி. ஜி. டி.` line without colon.
- `parasakthi-s025-d017` — second `சி. ஜி. டி.` line without colon.

Their scene-record wrappers preserve `source_label_anomalies` notes.

## Dialogue checkpoint

Dialogue extraction is verified for **29 observed scenes**:

`1–22, 24–30`

Scene 23 is absent and has no record file.

- Previous total through scene 20: **253 records**.
- Observed scenes 21–30 batch: **160 records**.
- Cumulative total: **413 records**.

Batch counts:

- scene 21: 40
- scene 22: 11
- scene 24: 6
- scene 25: 26
- scene 26: 0
- scene 27: 3
- scene 28: 48
- scene 29: 0
- scene 30: 26

Scenes 26 and 29 correctly have zero-record files because their contents are narrative/unlabelled song material only.

Verified cross-page dialogue records:

- `parasakthi-s001-d001` — PDF 4→5
- `parasakthi-s009-d001` — PDF 12→13
- `parasakthi-s013-d023` — PDF 16→17
- `parasakthi-s028-d023` — PDF 33→34

Scene 30's record file must retain its cross-part structure: first utterance on PDF 35, remaining dialogue on PDF 36.

## Exact next work

Extract dialogue records for the next observed scenes in the **31–40 range**:

**31, 32, 33, 35, 36, 37, 38, 39, 40**

Scene 34 is absent — do not create `dialogues/records/scene-34.json`.

For each scene:

1. read the verified scene derivative and `scenes/index.json`;
2. extract explicitly speaker-labelled utterances only;
3. preserve exact labels and Tamil text;
4. assign IDs from `d001` within the scene;
5. preserve PDF/printed provenance and cross-page `page_segments`;
6. document any genuine source label-delimiter anomaly rather than normalizing it;
7. verify record count and final record before advancing the manifest.

After the 31–40 observed-scene batch, update the dialogue manifest, README, metadata, `data/works.json`, work/root README as needed, and this handover. The following batch should be the final observed scenes 41–48, preserving source-heading provenance for canonical 43 and 48.

Other stages remain: character index not started; song authorship mapping not started; English translation not started.
