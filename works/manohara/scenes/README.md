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
- scene-text derivatives completed: **35/57** — `manohara-s001` through `manohara-s035`;
- completed derivative source span: opening PDF **7** through PDF **48**, ending immediately before audit transition `T036` (`அரசர் அவைக்கூடம்`);
- `manohara-s016` legitimately crosses the Part 01 / Part 02 storage boundary because the source action continues from PDF 30 to PDF 31 before `T017`;
- `manohara-s030` legitimately crosses the Part 02 / Part 03 storage boundary because the Vasantha-festival action continues onto PDF 43 before `T031`;
- `manohara-s031` preserves Manoharan's appeal to Padmavati after the Vasantha-festival clash;
- `manohara-s032` preserves the short king-room transition with Vasanthasena at the door, retaining the source's unmatched opening bracket in the stage direction;
- `manohara-s033` preserves the Padmavati/Vijaya inquiry, Vasanthasena's counter-plot and staged suicide sequence through PDF 46;
- `manohara-s034` preserves the eavesdropping/suspicion sequence and the king's order that Padmavati be imprisoned and Manoharan apologize;
- `manohara-s035` preserves the Padmavati-room response and Manoharan's departure to demand the reason for the order;
- boundary stars are not duplicated across derivative files;
- derivative source authority: verified canonical Tamil only;
- next scene-text derivative: **`manohara-s036`**, beginning with `அரசர் அவைக்கூடம்` on PDF 48.

`index.json` is the authoritative scene-segmentation index for this derivative layer. `notes/scene-heading-audit.md` remains the provenance record for why each start point exists.

Dialogue indexing remains blocked until the full scene-text derivative layer is complete.
