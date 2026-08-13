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
- Scene 33 spans PDF 38→42 because scene 34 is absent.
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

The schema remains unchanged. When the source explicitly marks a speaker without the normal colon, index the utterance but do not insert punctuation into the canonical Tamil.

Verified anomaly records:

- `parasakthi-s021-d040` — source form `கல் ! கிறுக்கண்ணு! கிறுக்கண்ணு!`.
- `parasakthi-s025-d011` — `சி. ஜி. டி.` line without colon.
- `parasakthi-s025-d017` — second `சி. ஜி. டி.` line without colon.

## Dialogue checkpoint

Dialogue extraction is verified for **38 observed scenes**:

`1–22, 24–33, 35–40`

- Previous total after observed scenes 21–30: **413 records**.
- Observed scenes 31–40 batch: **114 records**.
- Cumulative total: **527 records**.

Batch counts:

- scene 31: 13
- scene 32: 4
- scene 33: 56
- scene 35: 10
- scene 36: 4
- scene 37: 8
- scene 38: 8
- scene 39: 9
- scene 40: 2

Scene 34 remains absent and has no record file.

Special cases from this batch:

- `parasakthi-s033-d053` is one utterance crossing PDF 41→42.
- Scene 33's unlabelled dream song is excluded.
- Scene 39's opening unlabelled song is excluded; its labelled dialogue begins on PDF 45.
- Scenes 26 and 29 remain legitimate zero-record files.

Verified cross-page dialogue records now are:

- `parasakthi-s001-d001` — PDF 4→5
- `parasakthi-s009-d001` — PDF 12→13
- `parasakthi-s013-d023` — PDF 16→17
- `parasakthi-s028-d023` — PDF 33→34
- `parasakthi-s033-d053` — PDF 41→42

## Exact next work

Extract the **final observed canonical scenes 41–48**.

For each scene:

1. read the verified scene derivative and `scenes/index.json`;
2. extract explicitly speaker-labelled utterances only;
3. preserve exact labels and Tamil text;
4. assign IDs from `d001` within each scene;
5. preserve PDF/printed provenance and cross-page `page_segments`;
6. document any genuine source label-delimiter anomaly rather than normalizing it;
7. verify record count and final record before advancing the manifest.

Critical final-batch provenance:

- canonical scene **43** must use `source_scene_heading: 48` because PDF 49 / printed p.48 is misprinted as scene 48;
- canonical scene **48** must use `source_scene_heading: 43` because PDF 57 / printed p.56 is misprinted as scene 43.

After scenes 41–48 are verified, mark the dialogue index **46/46 observed scenes complete**, record the final dialogue-record total, and then advance to the next structured derivative (character index unless the repository workflow is deliberately changed).

Other stages remain: character index not started; song authorship mapping not started; English translation not started.
