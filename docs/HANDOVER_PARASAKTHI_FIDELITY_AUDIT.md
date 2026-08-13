# Parasakthi — handover after completed Tamil fidelity audit

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

This is the controlling continuation note for **Parasakthi after completion of the canonical Tamil visual-fidelity audit and entry into structured derivatives**.

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
12. `data/works.json`
13. relevant READMEs

## Canonical coverage and final audit result

The canonical Tamil transcription covers **PDF 4–57 / printed pp. 3–56**.

Two canonical parts:

- Part 01: PDF 4–35 / printed pp. 3–34
- Part 02: PDF 36–57 / printed pp. 35–56

The full canonical range has completed page-by-page visual fidelity audit and has **54 verified pages / 0 review pages**.

### Part 01 — final state

- **32 verified pages**
- **0 review pages**
- **0 remaining uncertainty markers**

The final two readings that had remained under review were resolved by direct reviewer-assisted inspection of the attached source scan and applied in commit:

`13b29064d01d606f64f2ae817b25008d21394f75`

Resolved readings:

- PDF 5 / printed p.4: `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?`
- PDF 16 / printed p.15: `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

Do not reintroduce uncertainty markers at either location unless new primary-source evidence demonstrates a problem.

### Part 02 — final state

Part 02 has been fully audited, consolidated, and post-rewrite verified:

- **22 verified pages**
- **0 review pages**
- **0 remaining uncertainty markers**

Six first-pass uncertainty markers were resolved directly from the scan:

- PDF 36: `சேர்மையா`
- PDF 37: `ஒரு அரையணா`
- PDF 40: `பாலைவனத்தை பூஞ்சோலையாக்க`
- PDF 41: `சுட்டுக் கொல்லப்பட்டிருப்போம்`
- PDF 50: `சூறையாட`
- PDF 50: `அணைப்பிலே`

Nine materially corrupted first-pass blocks were retranscribed directly from the scan:

- PDF **42, 44, 45, 46, 48, 49, 52, 53, 54**

After the first consolidated rewrite, an enlarged post-rewrite visual check identified additional source-form inaccuracies, especially on PDF 44–46 and PDF 52–54. Those were corrected in the final Part 02 corrective commit:

`ac4828c60f9a69590f1fc6b2da17114f62c16d22`

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

The source readings are preserved as hidden HTML comments immediately before the two corrected headings in `part-02-pdf-36-57.md`, and both source and canonical values are recorded in `mapping.md`, `metadata.yaml`, and the scene derivative index.

Therefore the canonical sequence near the end is:

`காட்சி—42` → **`காட்சி—43`** → `காட்சி—44` → `காட்சி—45` → `காட்சி—46` → `காட்சி—47` → **`காட்சி—48`**.

Headings 23 and 34 remain unobserved in the source; do not invent them.

## Structured derivatives — started

The repository has now entered Stage 5 of `docs/ARCHIVAL_WORKFLOW.md`: **Structured Derivatives**.

Completed first derivative artifacts:

- `works/parasakthi/scenes/README.md`
- `works/parasakthi/scenes/index.json`

The scene index contains **46 records**, one for every observed scene heading. Each record stores:

- canonical scene number;
- printed source heading;
- starting PDF page;
- starting printed page;
- canonical part;
- intended scene-file name;
- explicit correction flag for canonical scenes 43 and 48.

No scene 23 or scene 34 record/file is to be invented because those headings are absent from the scan.

### Scene derivative rule

Individual scene files are derivatives, not replacements for canonical text. When extracting a scene:

1. copy Tamil only from the verified canonical part files;
2. retain every canonical page anchor occurring inside the scene;
3. stop immediately before the next canonical scene heading;
4. preserve dialogue, directions, verse/song lineation and punctuation as represented in the canonical layer;
5. add a short derivative provenance header pointing to the canonical part and scene start page;
6. do not use a scene file to make new textual corrections to the canonical Tamil.

## Durable current state

- Structural mapping: **verified**
- Canonical Tamil coverage: **complete — PDF 4–57 / printed pp. 3–56**
- Full visual fidelity audit: **complete**
- Total canonical page status: **54 verified / 0 review**
- Remaining source uncertainties: **0**
- Remaining canonical uncertainty markers: **0**
- Scene-number correction: **source PDF49 48 → canonical 43; source PDF57 43 → canonical 48**
- Structured derivative scene index: **complete — 46 records**
- Individual scene-text derivatives: **not-started**
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

Create the first batch of individual scene-text derivative files for **canonical scenes 1–10** under `works/parasakthi/scenes/`.

For each file, extract from the verified canonical Tamil from its heading through immediately before the next scene heading, retain page anchors, and include provenance back to the canonical part. After the batch:

- verify all ten scene boundaries against `scenes/index.json` and the canonical part;
- update `scenes/README.md`, `metadata.yaml`, `data/works.json`, and this handover;
- do not begin English translation or song authorship work in the same batch.
