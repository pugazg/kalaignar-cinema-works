# பராசக்தி — scene derivatives

**Stage:** structured derivatives  
**Scene index:** complete  
**Individual scene-text files:** in progress — **29 / 46 complete**

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
- Batch 3: `scene-21.md`, `scene-22.md`, `scene-24.md`, `scene-25.md`, `scene-26.md`, `scene-27.md`, `scene-28.md`, `scene-29.md`, `scene-30.md`

The completed scene derivatives now cover **all observed scene headings that begin in Part 01**: **29 files total**. Scene 23 is absent in the source and is not created.

Batch 3 start-page verification against [`index.json`](index.json):

- scene 21 — PDF 26 / printed p.25
- scene 22 — PDF 28 / printed p.27
- scene 24 — PDF 29 / printed p.28
- scene 25 — PDF 29 / printed p.28
- scene 26 — PDF 31 / printed p.30
- scene 27 — PDF 32 / printed p.31
- scene 28 — PDF 32 / printed p.31
- scene 29 — PDF 35 / printed p.34
- scene 30 — PDF 35 / printed p.34

### Cross-part scene 30

Scene 30 is a deliberate cross-part derivative. Its heading begins on PDF 35 / printed p.34 in Part 01, but the scene continues onto **PDF 36 / printed p.35**, which is stored in the canonical Part 02 file. `scene-30.md` therefore includes that verified PDF 36 continuation and stops immediately before `காட்சி—31` begins on PDF 37. This preserves the actual scene boundary rather than the transcription-file boundary.

No `scene-23.md` or `scene-34.md` will be created unless new primary-source evidence establishes those headings.

## Derivative rules

Each scene file must:

1. copy Tamil only from the verified canonical transcription;
2. retain every page anchor that occurs within the scene;
3. record the scene's starting PDF/printed page;
4. preserve songs, dialogue, stage directions and page-boundary continuity exactly as represented in the canonical layer;
5. point back to the canonical part file through its provenance metadata;
6. stop at the next observed canonical scene heading even when a scene crosses a transcription-part boundary;
7. never be used to repair or overwrite the canonical transcription.

## Next batch

Begin Part 02 scene derivatives for the observed scenes in the **31–40 numbering range**. Because scene **34 is absent in the source**, create exactly these **9 files**:

- `scene-31.md`
- `scene-32.md`
- `scene-33.md`
- `scene-35.md`
- `scene-36.md`
- `scene-37.md`
- `scene-38.md`
- `scene-39.md`
- `scene-40.md`

Verify each boundary against `index.json` and the verified Part 02 canonical text before advancing to scenes 41–48.
