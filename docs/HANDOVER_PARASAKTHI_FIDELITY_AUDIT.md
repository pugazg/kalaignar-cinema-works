# Parasakthi — handover after completed Tamil fidelity audit

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

This is the controlling continuation note for **Parasakthi after completion of the canonical Tamil visual-fidelity audit and completion of all scene-text derivatives**.

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
12. completed scene files under `works/parasakthi/scenes/`
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
- Canonical derivative: `works/parasakthi/scenes/scene-43.md`
- Scene derivative provenance records `source_heading=48`.

### PDF 57 / printed p.56

- Booklet prints: `காட்சி—43`
- Canonical visible heading: **`காட்சி—48`**
- Canonical final derivative: `works/parasakthi/scenes/scene-48.md`
- Scene derivative provenance records `source_heading=43`.

Headings **23 and 34 are not observed** in the source. Do not invent them.

## Structured derivatives — scene activity complete

The repository is in Stage 5 of `docs/ARCHIVAL_WORKFLOW.md`: **Structured Derivatives**.

### Scene index — complete

- `works/parasakthi/scenes/index.json`
- Records: **46**, one for each observed scene heading
- Missing/unobserved headings retained as absent: **23, 34**
- Canonical/source numbering distinction retained for scenes **43 and 48**

### Scene-text derivatives — complete

All **46 observed scene files** now exist.

Completed batches:

1. scenes **1–10**
2. scenes **11–20**
3. observed scenes **21–30**, with scene 23 absent
4. observed scenes **31–40**, with scene 34 absent
5. final scenes **41–48**

Current scene derivative state:

- Completed scene files: **46 / 46**
- Completed canonical scenes: **1–22, 24–33, 35–48**
- Scene-text derivative status: **complete**
- Canonical Tamil remains untouched by derivative extraction.

### Important cross-part boundary: scene 30

Scene 30 starts on **PDF 35 / printed p.34** in canonical Part 01, continues onto **PDF 36 / printed p.35** stored in Part 02, and stops immediately before `காட்சி—31` on PDF 37. Do not truncate it to the Part 01 file boundary.

### Important missing-heading boundary: scene 33

Scene 33 starts on **PDF 38 / printed p.37** and continues across PDF **39, 40, 41 and 42**. Because no `காட்சி—34` heading is observed, `scene-33.md` continues uninterrupted until immediately before `காட்சி—35` on PDF 42. Do not create `scene-34.md` or split scene 33 artificially.

### Final batch start-page verification

- scene 41 — PDF 46 / printed p.45
- scene 42 — PDF 48 / printed p.47
- scene 43 — PDF 49 / printed p.48; source heading 48 → canonical 43
- scene 44 — PDF 51 / printed p.50
- scene 45 — PDF 51 / printed p.50
- scene 46 — PDF 55 / printed p.54
- scene 47 — PDF 55 / printed p.54
- scene 48 — PDF 57 / printed p.56; source heading 43 → canonical 48

`scene-48.md` runs through `—சுபம்—` and `கோபி பிரிண்டர்ஸ், சென்னை -1.` and stops before the PDF 58 rear advertisement / back matter.

### Scene derivative rules remain binding

Individual scene files are derivatives, not replacements for canonical text. They:

1. copy Tamil only from verified canonical part files;
2. retain canonical page anchors occurring within the scene;
3. stop immediately before the next observed canonical scene heading;
4. preserve dialogue, directions, verse/song lineation and punctuation as represented in the canonical layer;
5. record scene start-page provenance;
6. preserve the source/canonical numbering distinction for scenes 43 and 48;
7. do not repair or overwrite canonical Tamil.

## Durable current state

- Structural mapping: **verified**
- Canonical Tamil coverage: **complete — PDF 4–57 / printed pp. 3–56**
- Full visual fidelity audit: **complete**
- Total canonical page status: **54 verified / 0 review**
- Scene-number correction: **source PDF49 48 → canonical 43; source PDF57 43 → canonical 48**
- Structured derivative scene index: **complete — 46 records**
- Individual scene-text derivatives: **complete — 46 / 46**
- Dialogue index: **not-started — next structured derivative**
- Character index: **not-started**
- PDF 58: rear advertisement/back matter, recorded as `paratext`
- Per-song authorship mapping: **not-started**
- English translation: **not-started**

## Translation and song gates

The Tamil source is fully verified, so English translation may begin later as a separate derivative activity.

Song-specific extraction or attribution must still pass the separate authorship gate because the booklet credits multiple lyric contributors.

Do **not** alter canonical Tamil merely to make a derivative, translation or index smoother.

## Exact next work

Begin the **dialogue index** as the next structured derivative in the Stage 5 ordering.

First define a deterministic, reviewable dialogue-record schema. At minimum each dialogue record should carry:

- a stable dialogue-record ID;
- canonical scene number;
- exact speaker label as represented in the verified canonical Tamil;
- dialogue text copied without normalization;
- PDF page and printed-page provenance;
- source-heading provenance where canonical scene 43 or 48 is involved.

Important rules:

- do not normalize or expand speaker labels during extraction;
- do not treat stage directions or narrative prose as dialogue;
- songs/verse blocks must remain distinguishable from speaker-labelled dialogue;
- if a dialogue utterance crosses a page boundary, preserve both page provenances rather than silently assigning it to one page;
- use the verified canonical text / completed scene derivatives as the extraction source, never film subtitles or outside copies.

Recommended first implementation step: create a dialogue-index README/schema plus a machine-readable index file, then populate a small verified batch before bulk extraction.
