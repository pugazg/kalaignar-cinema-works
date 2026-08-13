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

- `scene-21.md`
- `scene-22.md`
- `scene-24.md`
- `scene-25.md`
- `scene-26.md`
- `scene-27.md`
- `scene-28.md`
- `scene-29.md`
- `scene-30.md`

Scene 23 is absent and was not invented.

Batch 3 start-page verification:

- scene 21 — PDF 26 / printed p.25
- scene 22 — PDF 28 / printed p.27
- scene 24 — PDF 29 / printed p.28
- scene 25 — PDF 29 / printed p.28
- scene 26 — PDF 31 / printed p.30
- scene 27 — PDF 32 / printed p.31
- scene 28 — PDF 32 / printed p.31
- scene 29 — PDF 35 / printed p.34
- scene 30 — PDF 35 / printed p.34

Current scene derivative state:

- Completed scene files: **29 / 46**
- Completed canonical scenes: **1–22, 24–30**
- All observed scene headings beginning in Part 01 are now extracted.
- Canonical Tamil remains untouched by derivative extraction.

### Important cross-part boundary: scene 30

Scene 30 starts on **PDF 35 / printed p.34** in canonical Part 01, but it continues onto **PDF 36 / printed p.35**, which is stored in the Part 02 canonical file. The next scene heading, `காட்சி—31`, begins only on PDF 37.

Therefore `works/parasakthi/scenes/scene-30.md` deliberately contains:

- the scene-30 material from PDF 35 in Part 01;
- the continuing verified material from PDF 36 in Part 02;
- no PDF 37 anchor and no scene-31 material.

Do not truncate scene 30 back to the Part 01 file boundary. The derivative boundary is the next observed scene heading, not the canonical-part split.

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
- Individual scene-text derivatives: **29 / 46 complete**
- Part 01-starting scene derivatives: **complete**
- Cross-part derivative: **scene 30 spans PDF 35–36**
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

Begin the Part 02 scene-text derivative batch for observed scenes in the **31–40 numbering range**.

Because **scene 34 is absent**, create exactly these **9 files**:

`scene-31.md`, `scene-32.md`, `scene-33.md`, `scene-35.md`, `scene-36.md`, `scene-37.md`, `scene-38.md`, `scene-39.md`, `scene-40.md`.

For each file:

- extract only from the verified Part 02 canonical text;
- begin at its canonical heading;
- retain page anchors occurring inside the scene;
- stop immediately before the next observed scene heading;
- preserve the canonical Tamil exactly;
- verify the start page and boundary against `scenes/index.json`.

After that batch, update `scenes/README.md`, `metadata.yaml`, `data/works.json`, work README and this handover, then advance to the final observed scenes **41–48**.
