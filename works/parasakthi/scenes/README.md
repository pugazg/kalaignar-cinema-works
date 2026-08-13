# பராசக்தி — scene derivatives

**Stage:** structured derivatives  
**Scene index:** complete  
**Individual scene-text files:** in progress — **10 / 46 complete**

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

Completed first batch:

- `scene-01.md`
- `scene-02.md`
- `scene-03.md`
- `scene-04.md`
- `scene-05.md`
- `scene-06.md`
- `scene-07.md`
- `scene-08.md`
- `scene-09.md`
- `scene-10.md`

Each scene file was extracted from the verified canonical Part 01 text, starts at its canonical heading, stops immediately before the next scene heading, and retains canonical page anchors that occur within the scene. A derivative provenance comment records the scene number, start PDF/printed page, and canonical part.

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

Extract **canonical scenes 11–20** from verified Part 01 using the same deterministic boundary rule, then verify the ten scene boundaries against `index.json` and the canonical part.
