# பராசக்தி — scene derivatives

**Stage:** structured derivatives  
**Scene index:** complete  
**Individual scene-text files:** **complete — 46 / 46 observed scenes**

This directory is a derivative layer built only from the fully verified canonical Tamil transcription. It does **not** replace or normalize the canonical source text in `../transcription/parts/`.

## Canonical authority

- Source: `TVA_BOK_0062968_பராசக்தி.pdf`
- Canonical dialogue/song range: PDF **4–57** / printed pp. **3–56**
- Tamil fidelity status: **54 verified / 0 review**
- Canonical parts:
  - `../transcription/parts/part-01-pdf-4-35.md`
  - `../transcription/parts/part-02-pdf-36-57.md`

## Scene index

[`index.json`](index.json) records every observed scene heading with its canonical number and source-page provenance.

The booklet contains **46 visible scene headings**. Headings **23** and **34** are not observed and are therefore not invented in this derivative layer.

The documented late numbering correction is preserved:

- PDF 49 / printed p.48: booklet prints `காட்சி—48`; canonical scene number is **43**.
- PDF 57 / printed p.56: booklet prints `காட்சி—43`; canonical final scene number is **48**.

For those two records, `index.json` stores both `source_heading` and `canonical_heading`. The corresponding derivative files also record the differing source heading in their provenance headers.

## Scene-text extraction — complete

Completed batches:

- Batch 1: `scene-01.md` through `scene-10.md`
- Batch 2: `scene-11.md` through `scene-20.md`
- Batch 3: `scene-21.md`, `scene-22.md`, `scene-24.md`, `scene-25.md`, `scene-26.md`, `scene-27.md`, `scene-28.md`, `scene-29.md`, `scene-30.md`
- Batch 4: `scene-31.md`, `scene-32.md`, `scene-33.md`, `scene-35.md`, `scene-36.md`, `scene-37.md`, `scene-38.md`, `scene-39.md`, `scene-40.md`
- Batch 5: `scene-41.md` through `scene-48.md`

The derivative layer now contains **all 46 observed scene files**. No `scene-23.md` or `scene-34.md` exists because those headings are not observed in the primary source.

### Final batch boundary verification

The final Part 02 batch was checked against both [`index.json`](index.json) and the verified canonical Part 02 text:

- scene 41 — PDF 46 / printed p.45
- scene 42 — PDF 48 / printed p.47
- scene 43 — PDF 49 / printed p.48; booklet source heading **48**, canonical heading **43**
- scene 44 — PDF 51 / printed p.50
- scene 45 — PDF 51 / printed p.50
- scene 46 — PDF 55 / printed p.54
- scene 47 — PDF 55 / printed p.54
- scene 48 — PDF 57 / printed p.56; booklet source heading **43**, canonical final heading **48**

`scene-48.md` runs through `—சுபம்—` and the printer line, then stops before the PDF 58 rear advertisement / back matter.

### Cross-part scene 30

Scene 30 is a deliberate cross-part derivative. Its heading begins on PDF 35 / printed p.34 in Part 01, but the scene continues onto **PDF 36 / printed p.35**, which is stored in the canonical Part 02 file. `scene-30.md` includes that verified continuation and stops immediately before `காட்சி—31` begins on PDF 37.

### Scene 33 and absent scene 34

Scene 33 starts on **PDF 38 / printed p.37** and continues across PDF **39, 40, 41 and 42**. Because no `காட்சி—34` heading is observed, `scene-33.md` continues uninterrupted until immediately before `காட்சி—35` on PDF 42.

## Derivative rules

Each scene file:

1. copies Tamil only from the verified canonical transcription;
2. retains every canonical page anchor occurring inside the scene;
3. records the scene's starting PDF/printed page in provenance;
4. preserves songs, dialogue, stage directions and page-boundary continuity exactly as represented in the canonical layer;
5. stops at the next observed canonical scene heading, even when a scene crosses a transcription-part boundary;
6. preserves documented source/canonical scene-number differences in provenance;
7. is never used to repair or overwrite the canonical transcription.

## Scene derivative completion state

- Scene index records: **46 / 46 complete**
- Scene-text files: **46 / 46 complete**
- Canonical missing headings preserved as absent: **23, 34**
- Canonical/source numbering corrections preserved: **43 / 48**
- Scene extraction status: **complete**

## Next structured derivative

The next activity is the **dialogue index** defined by Stage 5 of `docs/ARCHIVAL_WORKFLOW.md`.

Before bulk extraction, define a small deterministic schema that records at minimum:

- canonical scene number;
- exact speaker label as represented in the verified Tamil;
- dialogue text without normalization;
- PDF / printed-page provenance;
- source scene-number provenance where scene 43 or 48 is involved.

Stage directions, songs and non-speaker narrative text must remain distinguishable from speaker-labelled dialogue rather than being silently converted into dialogue records.
