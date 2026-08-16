# மனோகரா — archival scene derivatives

Status: **in-progress**.

The source booklet does **not** print numbered scenes. The verified canonical Tamil therefore remains authoritative in `../transcription/parts/`; this directory is a downstream reader/navigation layer only.

## Segmentation policy

`notes/scene-heading-audit.md` verified **57 principal source-visible transition dispositions**, identified there as audit rows `T001`–`T057`. After the complete Tamil layer reached `complete-verified`, those 57 accepted transitions were adopted as the start points for **57 archival scene segments**.

Important:

- `manohara-s001` … `manohara-s057`, the numeric `ordinal`, and filenames such as `scene-001.md` are **archive-only navigation identifiers**.
- They are **not** scene numbers printed by the booklet.
- `source_scene_number` is therefore always `null`.
- Short `reader_label_ta` values in `index.json` are navigation labels derived from source-visible transition evidence; they are not silently promoted to source headings.
- Each derivative segment begins at one accepted transition and ends immediately before the next accepted transition.
- Decorative star separators are never expanded into prose such as `(Scene ends.)`.
- Boundary separators are not duplicated between adjacent derivative files.
- Page anchors are repeated inside derivatives for traceability; repeating an anchor does not create new canonical text.
- Canonical storage-part boundaries do not force scene boundaries when the verified source action continues across them.
- The opening global title/credit lines (`மனோகரா` / `திரைக்கதை வசனம்`) remain in the canonical transcription and are not repeated as a scene heading.

## Current checkpoint

- archival scene segments indexed: **57/57**;
- source-numbered scene count: **not applicable**;
- scene-text derivatives completed: **41/57** — `manohara-s001` through `manohara-s041`;
- completed derivative source span: opening PDF **7** through the opening portion of PDF **67**, ending immediately before audit transition `T042` (`[உக்ரசேனன் கூடாரம்]`);
- `manohara-s016` legitimately crosses the Part 01 / Part 02 storage boundary because the source action continues from PDF 30 to PDF 31 before `T017`;
- `manohara-s030` legitimately crosses the Part 02 / Part 03 storage boundary because the Vasantha-festival action continues onto PDF 43 before `T031`;
- `manohara-s036` legitimately crosses the Part 03 / Part 04 storage boundary; the long royal-court sequence continues through PDF 57 and ends immediately before `T037` on PDF 58;
- `manohara-s037` preserves the PDF 58 palace report and cave continuation in which Manoharan learns that Padmavati and Vijaya are imprisoned;
- `manohara-s038` preserves the prison, Vasanthasena, and Vasanthan mock-darbar material through the point immediately before `T039`;
- `manohara-s039` preserves the garden conversation, Vasanthasena's decision to turn to Ugrasenan, and the invisible Kesari Varma/Vasanthan intervention through PDF 64;
- `manohara-s040` preserves the cave interception of Atchayan, Ugrasenan's letter, and the decision to expose Vasanthasena's conspiracy rather than simply kill her;
- `manohara-s041` legitimately crosses the Part 04 / Part 05 storage boundary, preserving Manoharan's entry in the false-Atchayan/physician disguise through the opening of PDF 67 before `T042`;
- boundary stars are not duplicated across derivative files;
- derivative source authority: verified canonical Tamil only;
- next scene-text derivative: **`manohara-s042`**, beginning with `[உக்ரசேனன் கூடாரம்]` on PDF 67.

`index.json` is the authoritative scene-segmentation index for this derivative layer. `notes/scene-heading-audit.md` remains the provenance record for why each start point exists.

Dialogue indexing remains blocked until the full scene-text derivative layer is complete.
