# பராசக்தி — scene derivatives

**Stage:** structured derivatives  
**Scene index:** complete  
**Individual scene-text files:** in progress — **20 / 46 complete**

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

For those two records, `index.json` stores both `source_heading` and `canonical_heading` so the derivative remains traceable to the printed booklet.

## Scene-text extraction

Completed batches:

- Batch 1: `scene-01.md` through `scene-10.md`
- Batch 2: `scene-11.md` through `scene-20.md`

All **20 completed scene files** were extracted from the verified canonical Part 01 text. Each starts at its canonical heading, stops immediately before the next observed scene heading, and retains every canonical page anchor occurring within the scene. A derivative provenance comment records the canonical scene number, start PDF/printed page, and canonical part.

Batch 2 boundary verification was checked against both [`index.json`](index.json) and `../transcription/parts/part-01-pdf-4-35.md`:

- scene 11 starts PDF 14 / printed p.13;
- scene 12 starts PDF 14 / printed p.13;
- scene 13 starts PDF 15 / printed p.14;
- scene 14 starts PDF 17 / printed p.16;
- scene 15 starts PDF 18 / printed p.17;
- scene 16 starts PDF 20 / printed p.19;
- scene 17 starts PDF 21 / printed p.20;
- scene 18 starts PDF 22 / printed p.21;
- scene 19 starts PDF 23 / printed p.22;
- scene 20 starts PDF 24 / printed p.23.

No `scene-23.md` or `scene-34.md` will be created unless new primary-source evidence establishes those headings.

## Derivative rules

Each scene file must:

1. copy Tamil only from the verified canonical transcription;
2. retain every page anchor that occurs within the scene;
3. record the scene's starting PDF/printed page;
4. preserve songs, dialogue, stage directions and page-boundary continuity exactly as represented in the canonical layer;
5. point back to the canonical part file through its provenance metadata;
6. never be used to repair or overwrite the canonical transcription.

## Next batch

Extract the observed canonical scenes in the **21–30 numbering range** from verified Part 01. Because scene **23 is absent in the source**, this batch contains **9 files**: scenes **21, 22, 24, 25, 26, 27, 28, 29 and 30**.

After extraction, verify every boundary against `index.json` and the canonical Part 01 text before advancing to Part 02 scene derivatives.
