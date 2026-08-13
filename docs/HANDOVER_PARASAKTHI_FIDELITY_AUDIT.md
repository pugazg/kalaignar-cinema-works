# Parasakthi — handover after completed Tamil fidelity audit

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

This is the controlling continuation note for **Parasakthi after completed canonical Tamil fidelity work, completed scene derivatives, and verified dialogue indexing through canonical scene 20**.

## Source

- Work: `பராசக்தி`
- Source booklet: `பராசக்தி — முழு வசனம் + பாடல்கள்`
- File: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- Actual PDF pages: **58**
- Canonical dialogue/song range: PDF **4–57** / printed pp. **3–56**
- PDF 58: rear advertisement/back matter
- Image-only scan; the scan controls the source text.

Never repair Tamil from film audio, subtitles, web copies, later editions or memory.

## Canonical Tamil — complete

- Total canonical pages: **54 verified / 0 review**
- Part 01: **32 verified / 0 review**
- Part 02: **22 verified / 0 review**
- Remaining uncertainties: **0**
- Remaining uncertainty markers: **0**

Final reviewer-assisted Part 01 readings:

- PDF 5: `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?`
- PDF 16: `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

Nine materially corrupted Part 02 first-pass blocks were retranscribed directly from the scan on PDF 42, 44, 45, 46, 48, 49, 52, 53 and 54.

## Scene numbering and derivatives

There are **46 observed scene headings**. Headings **23 and 34 are absent** and must never be invented.

Documented source/canonical correction:

- PDF 49 / printed p.48: booklet heading 48 → canonical **scene 43**.
- PDF 57 / printed p.56: booklet heading 43 → canonical final **scene 48**.

The scene index and all **46/46 observed scene files** are complete.

Important boundaries:

- scene 30 crosses PDF 35→36 across canonical part files;
- scene 33 continues through PDF 42 because scene 34 is absent;
- scene 48 ends before PDF 58 back matter.

## Dialogue index — active Stage 5 derivative

Read before continuing:

1. `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `works/parasakthi/metadata.yaml`
4. `works/parasakthi/scenes/index.json`
5. relevant verified `works/parasakthi/scenes/scene-XX.md` files
6. `works/parasakthi/dialogues/README.md`
7. `works/parasakthi/dialogues/schema.json`
8. `works/parasakthi/dialogues/index.json`
9. existing `works/parasakthi/dialogues/records/scene-XX.json`
10. `data/works.json`

### Storage

- `dialogues/schema.json` — fixed record schema.
- `dialogues/index.json` — compact manifest/checkpoint.
- `dialogues/records/scene-XX.json` — scene-sharded records.

The original scenes 1–2 pilot was migrated losslessly into scene-sharded storage. This did **not** change the record schema.

### Dialogue rules

Each record is one **explicitly speaker-labelled** utterance and preserves:

- stable ID `parasakthi-sNNN-dNNN`;
- canonical scene number;
- source scene heading;
- exact speaker label before the colon;
- exact Tamil text without normalization;
- PDF / printed-page provenance;
- source scene file.

Do not normalize speaker labels. Variants such as `சந்`/`சந்திர`, `ஞான`/`ஞா`, `மாணிக்கம்`/`மாணிக்`/`மாணி`/`மணி`, and `கல்யாணி`/`கல்யா`/`கல்` remain distinct here.

Standalone stage directions, unlabelled songs/verse, and unlabelled prose are excluded even when context strongly identifies a speaker. Parenthetical text inside a labelled utterance remains part of that record. Explicitly labelled sung/verse material is included.

Examples:

- scene 4 labelled verse is indexed;
- scene 8 unlabelled opening song is excluded;
- scene 17 unlabelled lullaby and unlabelled `மனசாட்சி` prose are excluded; only the labelled `குண` line is indexed;
- scene 19 unlabelled performance/verse after the first `குண` record is excluded until the next explicit speaker label.

### Cross-page rule

A labelled utterance crossing a page anchor remains one record with multiple `page_provenance` entries and exact `page_segments`.

Verified cross-page records:

- `parasakthi-s001-d001` — PDF 4→5
- `parasakthi-s009-d001` — PDF 12→13
- `parasakthi-s013-d023` — PDF 16→17

## Dialogue checkpoint

Dialogue indexing is verified through canonical **scenes 1–20**.

- Records before this batch (scenes 1–10): **117**
- Scenes 11–20 batch: **136**
- Cumulative records: **253**
- Completed scenes: **1–20**

Scene counts for 11–20:

- 11: 2
- 12: 7
- 13: 26
- 14: 16
- 15: 16
- 16: 10
- 17: 1
- 18: 11
- 19: 11
- 20: 36

## Exact next work

Extract the next observed canonical scenes in the **21–30 range**:

**21, 22, 24, 25, 26, 27, 28, 29 and 30**.

Scene 23 is absent — do not create `scene-23.json`.

For each scene:

1. read the verified scene derivative and `scenes/index.json`;
2. extract only explicitly speaker-labelled utterances;
3. preserve exact labels and Tamil text;
4. start IDs at `d001` within each scene;
5. carry page provenance from canonical anchors;
6. preserve cross-page utterances as one record with `page_segments`;
7. write `dialogues/records/scene-XX.json`;
8. verify record count and final record before advancing the manifest.

Special upcoming case: **scene 30 crosses the Part 01/Part 02 transcription-file boundary**, but its completed scene derivative already contains the full verified scene. Use the scene derivative as the extraction source and do not truncate it at PDF 35.

After the 21–30 observed-scene batch, update the dialogue manifest, README, metadata, `data/works.json`, relevant READMEs and this handover. The following dialogue batch should begin with observed scenes in the 31–40 range, remembering scene 34 is absent.

## Other gates

- Character index: not started.
- Song authorship mapping: not started; mixed lyric credits require item-level verification.
- English translation: not started; Tamil is fully verified and eligible for later translation derivative work.
