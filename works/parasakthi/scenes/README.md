# பராசக்தி — scene derivatives

**Stage:** structured derivatives  
**Scene index:** complete  
**Individual scene-text files:** in progress — **38 / 46 complete**

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
- Batch 4: `scene-31.md`, `scene-32.md`, `scene-33.md`, `scene-35.md`, `scene-36.md`, `scene-37.md`, `scene-38.md`, `scene-39.md`, `scene-40.md`

The derivative layer now contains **38 / 46 observed scene files**. Scenes 23 and 34 remain absent because no such source headings are observed.

### Batch 4 boundary verification

The Part 02 batch was checked against both [`index.json`](index.json) and `../transcription/parts/part-02-pdf-36-57.md`:

- scene 31 — PDF 37 / printed p.36
- scene 32 — PDF 37 / printed p.36
- scene 33 — PDF 38 / printed p.37
- scene 35 — PDF 42 / printed p.41
- scene 36 — PDF 43 / printed p.42
- scene 37 — PDF 43 / printed p.42
- scene 38 — PDF 43 / printed p.42
- scene 39 — PDF 44 / printed p.43
- scene 40 — PDF 45 / printed p.44

Because scene **34 is absent**, `scene-33.md` deliberately continues across PDF 38–42 and stops only immediately before `காட்சி—35`. No artificial scene break is inserted.

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

Extract the final **8 observed scenes**:

- `scene-41.md`
- `scene-42.md`
- `scene-43.md`
- `scene-44.md`
- `scene-45.md`
- `scene-46.md`
- `scene-47.md`
- `scene-48.md`

For scenes 43 and 48, preserve the documented canonical/source distinction: source PDF 49 prints 48 but canonical scene is 43; source PDF 57 prints 43 but canonical final scene is 48.

After this batch, verify every boundary against `index.json` and the verified Part 02 canonical text, then mark the 46-file scene derivative activity complete before beginning another derivative type.
