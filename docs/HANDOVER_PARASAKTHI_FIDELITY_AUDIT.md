# Parasakthi — handover after completed Tamil fidelity audit

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

This is the controlling continuation note for **Parasakthi after completion of the canonical Tamil visual-fidelity audit, completion of all scene-text derivatives, and verified dialogue indexing through scenes 1–10**.

## Source

- Work: `பராசக்தி`
- Source booklet: `பராசக்தி — முழு வசனம் + பாடல்கள்`
- File: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- Actual PDF pages: **58**
- PDF 4–57 = printed pp. **3–56**
- PDF 58 = rear advertisement/back matter
- Image-only scan; the scan is the controlling textual source.

Do not replace source readings from film audio, subtitles, web copies, later editions, memory, or familiar quotations. Future source corrections must remain source-led and documented.

## Files to read before continuing

Fetch current `main` versions of:

1. `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `works/parasakthi/metadata.yaml`
4. relevant verified canonical transcription / scene derivative files
5. `works/parasakthi/scenes/index.json`
6. `works/parasakthi/dialogues/README.md`
7. `works/parasakthi/dialogues/schema.json`
8. `works/parasakthi/dialogues/index.json`
9. completed files under `works/parasakthi/dialogues/records/`
10. `data/works.json`
11. relevant READMEs

## Canonical Tamil — complete

The canonical Tamil transcription covers **PDF 4–57 / printed pp.3–56** and has completed page-by-page visual fidelity audit.

- Total canonical pages: **54 verified / 0 review**
- Part 01: **32 verified / 0 review**
- Part 02: **22 verified / 0 review**
- Remaining source uncertainties: **0**
- Remaining canonical uncertainty markers: **0**

Final reviewer-assisted Part 01 readings:

- PDF 5 / printed p.4: `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?`
- PDF 16 / printed p.15: `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

Part 02 was fully consolidated and post-rewrite verified. Nine materially corrupted first-pass blocks were retranscribed directly from the scan on PDF **42, 44, 45, 46, 48, 49, 52, 53 and 54**.

## Critical scene-number correction

Do **not** revert the documented canonical correction:

- PDF 49 / printed p.48: booklet `காட்சி—48` → canonical **scene 43**; provenance keeps source heading 48.
- PDF 57 / printed p.56: booklet `காட்சி—43` → canonical final **scene 48**; provenance keeps source heading 43.

Headings **23 and 34 are not observed**. Do not invent them.

## Scene structured derivatives — complete

- Scene index: **46 / 46 observed records complete**
- Individual scene files: **46 / 46 complete**
- Completed canonical scenes: **1–22, 24–33, 35–48**

Important boundaries:

- scene 30 crosses PDF 35→36 across the canonical part-file boundary;
- scene 33 continues through PDF 42 because scene 34 is absent;
- scene 48 ends at `—சுபம்—` / printer line and excludes PDF 58 back matter.

Canonical Tamil must remain untouched by derivative extraction.

## Dialogue index — verified through scenes 1–10

Dialogue indexing is the active Stage 5 derivative.

Files:

- `works/parasakthi/dialogues/README.md`
- `works/parasakthi/dialogues/schema.json` — **fixed record schema**
- `works/parasakthi/dialogues/index.json` — compact manifest/checkpoint
- `works/parasakthi/dialogues/records/scene-XX.json` — scene-sharded dialogue records

### Storage refinement

The initial 42-record scenes 1–2 pilot was migrated losslessly from the monolithic index into `records/scene-01.json` and `records/scene-02.json` before the first bulk batch. The **record schema did not change**. Scene sharding is only a storage/layout refinement to keep each scene independently auditable and avoid repeatedly rewriting one large record array.

### Current dialogue state

- Status: **in-progress-verified**
- Completed canonical scenes: **1–10**
- Total dialogue records: **117**
- New records in scenes 3–10 batch: **75**
- Next batch: **scenes 11–20**

Per-scene record counts:

- 1: **1**
- 2: **41**
- 3: **8**
- 4: **8**
- 5: **5**
- 6: **19**
- 7: **22**
- 8: **5**
- 9: **1**
- 10: **7**

### Dialogue-record rules

Each record represents exactly one explicitly speaker-labelled utterance and carries:

- stable ID `parasakthi-sNNN-dNNN`;
- canonical scene number;
- source scene heading from `scenes/index.json`;
- exact speaker label before the colon;
- exact Tamil text without normalization;
- PDF / printed-page provenance;
- source scene file.

Do **not** expand or merge speaker labels. Exact variants such as `சந்`, `சந்திர`, `ஞான`, `ஞா`, `மாணிக்கம்`, `மாணிக்`, `மாணி`, and `மணி` remain distinct at this layer. Character normalization belongs to the later character index.

Standalone stage directions, narrative prose, scene headings, unlabelled songs/verse, provenance comments, printer marks and back matter are **not dialogue records**. Parenthetical text inside a speaker-labelled line remains part of that dialogue.

Explicitly speaker-labelled sung/verse material **is** indexed. Scene 4's `தங்` / `கல்` / `இரு` verse exchange is therefore present; scene 8's unlabelled opening song remains excluded.

### Cross-page utterances verified so far

A single utterance crossing a canonical page boundary remains one record, with every page in `page_provenance` and exact `page_segments`:

- `parasakthi-s001-d001` — `தங்கப்பன்`, PDF 4 / printed p.3 → PDF 5 / printed p.4.
- `parasakthi-s009-d001` — `குண`, PDF 12 / printed p.11 → PDF 13 / printed p.12.

## Durable current state

- Structural mapping: **verified**
- Canonical Tamil: **54 verified / 0 review**
- Scene index: **complete — 46 records**
- Scene-text derivatives: **complete — 46 / 46**
- Dialogue index: **in-progress-verified — 117 records / scenes 1–10**
- Character index: **not-started**
- Song authorship mapping: **not-started**
- English translation: **not-started**

## Translation and song gates

The Tamil source is fully verified, so English translation may begin later as a separate derivative activity. Song-specific attribution remains gated because the booklet credits multiple lyric contributors.

Do **not** alter canonical Tamil merely to make a derivative, translation or index smoother.

## Exact next work

Continue the dialogue index with canonical **scenes 11–20**.

For each scene:

1. read its verified scene derivative plus `scenes/index.json`;
2. extract only explicitly speaker-labelled utterances;
3. preserve exact speaker labels and exact Tamil text;
4. assign stable IDs starting at `d001` within that scene;
5. carry correct PDF / printed-page provenance from page anchors;
6. preserve cross-page utterances as one record with `page_segments`;
7. exclude standalone directions, unlabelled songs/verse and narrative text;
8. write the records to `dialogues/records/scene-XX.json`;
9. verify count and final record for each scene before advancing `dialogues/index.json`.

After scenes 11–20 are verified, update the manifest, dialogue README, metadata, `data/works.json`, work/root READMEs if needed, and this handover. The following batch should then begin with the next observed scenes after 20, remembering scene 23 is absent.
