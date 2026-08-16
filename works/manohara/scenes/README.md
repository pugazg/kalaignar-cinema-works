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
- The opening global title/credit lines (`மனோகரா` / `திரைக்கதை வசனம்`) remain in the canonical transcription and are not repeated as a scene heading.

## Current checkpoint

- archival scene segments indexed: **57/57**;
- source-numbered scene count: **not applicable**;
- scene-text derivatives completed: **23/57** — `manohara-s001` through `manohara-s023`;
- completed derivative source span: opening PDF **7** through PDF **36**, ending immediately before audit transition `T024` (`வசந்தா-அரசர் படுக்கையறை`);
- `manohara-s016` legitimately crosses the Part 01 / Part 02 storage boundary because the source action continues from PDF 30 to PDF 31 before `T017`;
- `manohara-s017` preserves the Pandya public inquiry and Rajapriyan's marriage-as-sentence pronouncement;
- `manohara-s018` preserves the Pandya-palace dialogue up to, but not including, the separate song/boat transition `T019`;
- `manohara-s019` preserves the `“சிங்காரப் பைங்கிளியே... பேசு”` performance/boat occurrence and Bauthayan's failed dagger attack;
- `manohara-s020` preserves the Vasanthasena–Bauthayan war-sword conspiracy;
- `manohara-s021` preserves the false-death message to Padmavati, Bauthayan's exposure and Manoharan's oath;
- `manohara-s022` preserves Vasanthasena ordering Bauthayan's death;
- `manohara-s023` preserves the prison poisoning-by-snake sequence and ends before `T024`;
- boundary stars are not duplicated across derivative files;
- derivative source authority: verified canonical Tamil only;
- next scene-text derivative: **`manohara-s024`**, beginning with `வசந்தா-அரசர் படுக்கையறை` / `“பொழுது புலர்ந்தது” பாட்டு` on PDF 37.

`index.json` is the authoritative scene-segmentation index for this derivative layer. `notes/scene-heading-audit.md` remains the provenance record for why each start point exists.

Dialogue indexing remains blocked until the full scene-text derivative layer is complete.
