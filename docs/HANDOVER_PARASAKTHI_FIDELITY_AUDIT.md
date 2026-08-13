# Parasakthi — handover after completed Tamil fidelity audit

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

This is the controlling continuation note for **Parasakthi after completion of the canonical Tamil visual-fidelity audit, completion of all scene-text derivatives, and completion of the dialogue-index pilot**.

## Source

- Work: `பராசக்தி`
- Source booklet: `பராசக்தி — முழு வசனம் + பாடல்கள்`
- File: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- Actual PDF pages: **58**
- PDF 4–57 = printed pp. **3–56**
- PDF 58 = rear advertisement/back matter
- Image-only scan; the scan is the controlling textual source.

Do not replace source readings from film audio, subtitles, web copies, later editions, memory, or familiar quotations. Any future correction must remain source-led and documented.

## Files to read before continuing

Fetch current `main` versions of:

1. `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `docs/TRANSCRIPTION_GUIDE.md`
4. `works/parasakthi/metadata.yaml`
5. `works/parasakthi/transcription/parts/part-01-pdf-4-35.md`
6. `works/parasakthi/transcription/parts/part-02-pdf-36-57.md`
7. `works/parasakthi/scenes/README.md`
8. `works/parasakthi/scenes/index.json`
9. relevant completed scene files under `works/parasakthi/scenes/`
10. `works/parasakthi/dialogues/README.md`
11. `works/parasakthi/dialogues/schema.json`
12. `works/parasakthi/dialogues/index.json`
13. `data/works.json`
14. relevant READMEs

## Canonical Tamil — complete

The canonical Tamil transcription covers **PDF 4–57 / printed pp. 3–56** and has completed page-by-page visual fidelity audit.

- Total canonical pages: **54 verified / 0 review**
- Part 01: **32 verified / 0 review**
- Part 02: **22 verified / 0 review**
- Remaining source uncertainties: **0**
- Remaining canonical uncertainty markers: **0**

The final two Part 01 readings were resolved by reviewer-assisted direct inspection of the source scan and applied in commit `13b29064d01d606f64f2ae817b25008d21394f75`:

- PDF 5 / printed p.4: `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?`
- PDF 16 / printed p.15: `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

Part 02 was fully consolidated and post-rewrite verified. Nine materially corrupted first-pass blocks were retranscribed directly from the scan on PDF **42, 44, 45, 46, 48, 49, 52, 53 and 54**. The final Part 02 corrective commit is `ac4828c60f9a69590f1fc6b2da17114f62c16d22`.

## Critical scene-number correction

Do **not** revert the documented canonical correction.

### PDF 49 / printed p.48

- Booklet prints: `காட்சி—48`
- Canonical heading / derivative: **scene 43**
- `scenes/scene-43.md` records `source_heading=48`.

### PDF 57 / printed p.56

- Booklet prints: `காட்சி—43`
- Canonical final heading / derivative: **scene 48**
- `scenes/scene-48.md` records `source_heading=43`.

Headings **23 and 34 are not observed** in the source. Do not invent them.

## Scene structured derivatives — complete

- `works/parasakthi/scenes/index.json`: **46 / 46 observed scene records complete**
- Individual scene files: **46 / 46 complete**
- Completed canonical scenes: **1–22, 24–33, 35–48**
- Scene 23: absent
- Scene 34: absent

Important boundaries remain documented:

- scene 30 starts on PDF 35 and continues through PDF 36 across the canonical part-file boundary;
- scene 33 continues across PDF 38–42 because scene 34 is absent;
- scene 48 ends at `—சுபம்—` / printer line and excludes PDF 58 back matter.

Canonical Tamil must remain untouched by derivative extraction.

## Dialogue index — pilot verified

Dialogue indexing is now the active Stage 5 derivative.

Files:

- `works/parasakthi/dialogues/README.md`
- `works/parasakthi/dialogues/schema.json`
- `works/parasakthi/dialogues/index.json`

Current state:

- Status: **pilot-verified**
- Scenes completed: **1–2**
- Dialogue records: **42**
- Next batch: **scenes 3–10**

### Dialogue-record rules

Each record represents exactly one speaker-labelled utterance and carries:

- stable ID `parasakthi-sNNN-dNNN`;
- canonical scene number;
- source scene heading from `scenes/index.json`;
- exact speaker label as printed/transcribed before the colon;
- exact Tamil dialogue text without normalization;
- PDF / printed-page provenance;
- source scene file.

Do **not** expand speaker abbreviations. Labels such as `சந்`, `ஞான`, `குண`, `சரஸ்`, and `பேசு` remain exact. Character-name normalization belongs only in a later character index.

Standalone stage directions, narrative prose, scene headings, unlabelled songs/verse, provenance comments, printer marks and back matter are **not dialogue records**. Parenthetical text occurring inside a speaker-labelled line remains part of that dialogue text.

### Cross-page utterance rule

A single utterance crossing a canonical page boundary remains one record. It lists every page in `page_provenance` and adds `page_segments` showing the exact text belonging to each page.

Pilot edge case already verified:

- `parasakthi-s001-d001` — speaker `தங்கப்பன்`; spans PDF 4 / printed p.3 and PDF 5 / printed p.4 as one dialogue record with two page segments.

### Pilot scene counts

- scene 1: **1 dialogue record**; the unlabelled opening song and standalone stage directions are excluded.
- scene 2: **41 dialogue records**; exact abbreviated speaker labels are preserved.
- pilot total: **42 records**.

The schema should now be treated as fixed. Change it only if a later source structure genuinely cannot be represented, and document the reason before bulk rewriting.

## Durable current state

- Structural mapping: **verified**
- Canonical Tamil coverage: **complete — PDF 4–57 / printed pp. 3–56**
- Full visual fidelity audit: **complete**
- Total canonical page status: **54 verified / 0 review**
- Scene-number correction: **source PDF49 48 → canonical 43; source PDF57 43 → canonical 48**
- Scene index: **complete — 46 records**
- Scene-text derivatives: **complete — 46 / 46**
- Dialogue index: **pilot-verified — 42 records / scenes 1–2**
- Character index: **not-started**
- Song authorship mapping: **not-started**
- English translation: **not-started**

## Translation and song gates

The Tamil source is fully verified, so English translation may begin later as a separate derivative activity.

Song-specific extraction or attribution must still pass the separate authorship gate because the booklet credits multiple lyric contributors.

Do **not** alter canonical Tamil merely to make a derivative, translation or index smoother.

## Exact next work

Continue the dialogue index with the first bulk batch: **canonical scenes 3–10**.

For each scene:

1. read the completed verified scene derivative and `scenes/index.json`;
2. extract only speaker-labelled utterances;
3. preserve exact speaker labels and exact Tamil text;
4. assign stable IDs beginning at `d001` within each scene;
5. carry correct PDF / printed-page provenance from page anchors;
6. if any one utterance crosses a page boundary, use one record with multiple `page_provenance` entries plus `page_segments`;
7. exclude standalone stage directions, unlabelled songs/verse and narrative text;
8. verify the extracted count and final record for each scene before updating `dialogues/index.json`.

After scenes 3–10 are verified, update `dialogues/README.md`, `metadata.yaml`, `data/works.json`, work README, root README if needed, and this handover. The next dialogue batch after that should begin at scene 11.
