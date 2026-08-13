# Parasakthi — handover after completed Tamil fidelity audit

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

This is the controlling continuation note for **Parasakthi after completion of the canonical Tamil visual-fidelity audit and during structured scene derivatives**.

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
4. `works/parasakthi/notes/fidelity-audit.md`
5. `works/parasakthi/metadata.yaml`
6. `works/parasakthi/mapping.md`
7. `works/parasakthi/transcription/full-text.md`
8. `works/parasakthi/transcription/parts/part-01-pdf-4-35.md`
9. `works/parasakthi/transcription/parts/part-02-pdf-36-57.md`
10. `works/parasakthi/scenes/README.md`
11. `works/parasakthi/scenes/index.json`
12. the completed scene derivative files under `works/parasakthi/scenes/`
13. `data/works.json`
14. relevant READMEs

## Canonical coverage and final audit result

The canonical Tamil transcription covers **PDF 4–57 / printed pp. 3–56** and has completed page-by-page visual fidelity audit.

- Total canonical pages: **54 verified / 0 review**
- Part 01: **32 verified / 0 review**
- Part 02: **22 verified / 0 review**
- Remaining source uncertainties: **0**
- Remaining canonical uncertainty markers: **0**

The final two Part 01 readings were resolved by reviewer-assisted direct inspection of the source scan and applied in commit `13b29064d01d606f64f2ae817b25008d21394f75`:

- PDF 5 / printed p.4: `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?`
- PDF 16 / printed p.15: `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

Do not reintroduce uncertainty markers at either location unless new primary-source evidence demonstrates a problem.

Part 02 was fully consolidated and post-rewrite verified. Nine materially corrupted first-pass blocks were retranscribed directly from the scan on PDF **42, 44, 45, 46, 48, 49, 52, 53 and 54**. The final Part 02 corrective commit is `ac4828c60f9a69590f1fc6b2da17114f62c16d22`.

## Critical scene-number correction

The booklet itself contains a two-heading scene-number misprint/transposition near the end. **Do not revert the canonical correction.**

### PDF 49 / printed p.48

- Booklet prints: `காட்சி—48`
- Canonical visible heading: **`காட்சி—43`**
- Reason: this scene follows `காட்சி—42` and precedes `காட்சி—44`.

### PDF 57 / printed p.56

- Booklet prints: `காட்சி—43`
- Canonical visible heading: **`காட்சி—48`**
- Reason: this is the final scene after `காட்சி—46` and `காட்சி—47`.

The source readings are preserved in provenance comments and in `mapping.md`, `metadata.yaml`, and `scenes/index.json`.

Headings **23 and 34 are not observed** in the source. Do not invent them.

## Structured derivatives — in progress

The repository is in Stage 5 of `docs/ARCHIVAL_WORKFLOW.md`: **Structured Derivatives**.

### Scene index — complete

- `works/parasakthi/scenes/index.json`
- Records: **46**, one for each observed scene heading
- Missing/unobserved headings retained as absent: **23, 34**
- Canonical/source numbering distinction retained for scenes **43 and 48**

### Scene derivative batch 1 — complete

Canonical scenes **1–10** were extracted from verified Part 01.

### Scene derivative batch 2 — complete

Canonical scenes **11–20** were extracted from verified Part 01 and checked against both `scenes/index.json` and canonical Part 01 boundaries.

### Scene derivative batch 3 — complete

All remaining observed scene headings beginning in Part 01 were extracted:

`scene-21.md`, `scene-22.md`, `scene-24.md`, `scene-25.md`, `scene-26.md`, `scene-27.md`, `scene-28.md`, `scene-29.md`, `scene-30.md`.

Scene 23 is absent and was not invented.

### Scene derivative batch 4 — complete

The first Part 02 batch was extracted:

`scene-31.md`, `scene-32.md`, `scene-33.md`, `scene-35.md`, `scene-36.md`, `scene-37.md`, `scene-38.md`, `scene-39.md`, `scene-40.md`.

Scene 34 is absent and was not invented.

Batch 4 start-page verification:

- scene 31 — PDF 37 / printed p.36
- scene 32 — PDF 37 / printed p.36
- scene 33 — PDF 38 / printed p.37
- scene 35 — PDF 42 / printed p.41
- scene 36 — PDF 43 / printed p.42
- scene 37 — PDF 43 / printed p.42
- scene 38 — PDF 43 / printed p.42
- scene 39 — PDF 44 / printed p.43
- scene 40 — PDF 45 / printed p.44

Current scene derivative state:

- Completed scene files: **38 / 46**
- Completed canonical scenes: **1–22, 24–33, 35–40**
- Remaining scene files: **41–48**
- Canonical Tamil remains untouched by derivative extraction.

### Important cross-part boundary: scene 30

Scene 30 starts on **PDF 35 / printed p.34** in canonical Part 01, but it continues onto **PDF 36 / printed p.35**, which is stored in the Part 02 canonical file. The next scene heading, `காட்சி—31`, begins only on PDF 37.

Therefore `works/parasakthi/scenes/scene-30.md` deliberately contains the scene-30 material from PDF 35 and PDF 36, and stops before the PDF 37 anchor / scene 31 material. Do not truncate it to the Part 01 file boundary.

### Important missing-heading boundary: scene 33

Scene 33 starts on **PDF 38 / printed p.37** and continues across PDF **39, 40, 41 and 42**. Because no `காட்சி—34` heading is observed, `scene-33.md` continues uninterrupted until immediately before `காட்சி—35` on PDF 42. Do not create `scene-34.md` or split scene 33 artificially.

### Scene derivative rules

Individual scene files are derivatives, not replacements for canonical text. When extracting a scene:

1. copy Tamil only from the verified canonical part files;
2. retain every canonical page anchor occurring inside the scene;
3. stop immediately before the next observed canonical scene heading;
4. preserve dialogue, directions, verse/song lineation and punctuation as represented in the canonical layer;
5. add a derivative provenance header with canonical scene number, starting PDF/printed page and canonical part;
6. if a scene crosses a transcription-part boundary, continue across the part boundary until the next observed scene heading;
7. do not use a scene file to make new textual corrections to the canonical Tamil.

## Durable current state

- Structural mapping: **verified**
- Canonical Tamil coverage: **complete — PDF 4–57 / printed pp. 3–56**
- Full visual fidelity audit: **complete**
- Total canonical page status: **54 verified / 0 review**
- Scene-number correction: **source PDF49 48 → canonical 43; source PDF57 43 → canonical 48**
- Structured derivative scene index: **complete — 46 records**
- Individual scene-text derivatives: **38 / 46 complete**
- Part 01-starting scene derivatives: **complete**
- Part 02 derivative extraction: **complete through canonical scene 40**
- Cross-part derivative: **scene 30 spans PDF 35–36**
- Missing-heading continuation: **scene 33 spans PDF 38–42 because scene 34 is absent**
- Dialogue index: **not-started**
- Character index: **not-started**
- PDF 58: rear advertisement/back matter, recorded as `paratext`
- Per-song authorship mapping: **not-started**
- English translation: **not-started**

## Translation and song gates

The Tamil source is fully verified, so English translation may begin later as a separate derivative activity.

Song-specific extraction or attribution must still pass the separate authorship gate because the booklet credits multiple lyric contributors.

Do **not** alter canonical Tamil merely to make a derivative, translation or index smoother.

## Exact next work

Extract the final **8 observed scene derivatives** from verified Part 02:

`scene-41.md`, `scene-42.md`, `scene-43.md`, `scene-44.md`, `scene-45.md`, `scene-46.md`, `scene-47.md`, `scene-48.md`.

For each file:

- begin at its canonical heading;
- retain every page anchor occurring within the scene;
- stop immediately before the next observed canonical scene heading (scene 48 runs to the end of canonical dialogue/song content);
- preserve the canonical Tamil exactly;
- verify the start page and boundary against `scenes/index.json`.

Critical numbering rules for this final batch:

- canonical `scene-43.md` starts on PDF 49 / printed p.48 where the booklet itself prints `காட்சி—48`; preserve the source/canonical distinction in provenance and do **not** change the canonical heading back to 48;
- canonical `scene-48.md` starts on PDF 57 / printed p.56 where the booklet itself prints `காட்சி—43`; canonical final heading remains 48.

After the eight files are created and verified:

- scene-text derivatives will be **46 / 46 complete**;
- update `scenes/README.md`, `metadata.yaml`, `data/works.json`, work README and this handover;
- mark scene-text derivative extraction complete;
- only then choose the next separate structured derivative activity (dialogue index, character index, song-authorship mapping, or English translation).
