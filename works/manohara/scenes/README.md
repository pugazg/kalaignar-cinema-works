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
- scene-text derivatives completed: **51/57** — `manohara-s001` through `manohara-s051`;
- completed derivative source span: opening PDF **7** through the opening lines of PDF **79**, ending immediately before audit transition `T052` (`சிறைச்சாலை`);
- `manohara-s016` legitimately crosses the Part 01 / Part 02 storage boundary because the source action continues from PDF 30 to PDF 31 before `T017`;
- `manohara-s030` legitimately crosses the Part 02 / Part 03 storage boundary because the Vasantha-festival action continues onto PDF 43 before `T031`;
- `manohara-s036` legitimately crosses the Part 03 / Part 04 storage boundary; the long royal-court sequence continues through PDF 57 and ends immediately before `T037` on PDF 58;
- `manohara-s041` legitimately crosses the Part 04 / Part 05 storage boundary, preserving Manoharan's entry in the false-Atchayan/physician disguise through the opening of PDF 67 before `T042`;
- `manohara-s042` preserves Ugrasenan's camp, his disguised entry with the ascetic force, and the palace takeover preparations through PDF 69;
- `manohara-s043` preserves the cave response in which Manoharan is sent back into the palace while Rajapriyan is sent for Pandya support;
- `manohara-s044`–`manohara-s048` preserve the Ugrasenan–Vasanthasena chamber sequence, Vijaya's childbirth/prison sequence, Vasanthan's warning to Purushothaman, the exposure of Vasanthasena and Ugrasenan, and Purushothaman's imprisonment;
- `manohara-s049` preserves Vasanthasena's order that the disguised Manoharan kill Vijaya's newborn child and his internal refusal;
- `manohara-s050` preserves the real Atchayan's escape, the palace conspiracy discussion, and Manoharan's failed attempt to remove Padmavati, Vijaya and the child from prison;
- `manohara-s051` legitimately crosses the Part 05 / Part 06 storage boundary: the real Atchayan exposes the false Atchayan on PDF 78 and the recognition continues onto the opening of PDF 79 before `T052`;
- boundary stars are not duplicated across derivative files;
- derivative source authority: verified canonical Tamil only;
- next scene-text derivative: **`manohara-s052`**, beginning with `சிறைச்சாலை` on PDF 79.

`index.json` is the authoritative scene-segmentation index for this derivative layer. `notes/scene-heading-audit.md` remains the provenance record for why each start point exists.

Dialogue indexing remains blocked until the full scene-text derivative layer is complete.
