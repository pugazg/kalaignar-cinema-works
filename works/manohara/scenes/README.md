# மனோகரா — archival scene derivatives

Status: **complete-verified**.

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

## Final checkpoint

- archival scene segments indexed: **57/57**;
- source-numbered scene count: **not applicable**;
- scene-text derivatives completed: **57/57** — `manohara-s001` through `manohara-s057`;
- derivative source span: canonical screenplay PDF **7–88 / logical printed pp.6–87**;
- genuine cross-storage continuities preserved: **5** — `manohara-s016`, `manohara-s030`, `manohara-s036`, `manohara-s041`, and `manohara-s051`;
- `manohara-s052` preserves the final prison capture and Padmavati's realization that Purushothaman has understood the truth;
- `manohara-s053` preserves Manoharan bound to the pillar and Vasanthan's refusal to accept the throne obtained through violence;
- `manohara-s054` preserves the attempt to seize Vijaya's newborn child from prison;
- `manohara-s055` preserves the climactic confrontation from the child-sacrifice threat through Padmavati's command, the breaking of Manoharan's bonds, Ugrasenan's death, Vasanthan's death and the king's release;
- `manohara-s056` preserves Kesari Varma's final confrontation with Vasanthasena in the cave;
- `manohara-s057` preserves the closing palace reconciliation and final `கடமை, கண்ணியம், கட்டுப்பாடு` line;
- boundary stars are not duplicated across derivative files;
- derivative source authority: verified canonical Tamil only.

`index.json` is the authoritative scene-segmentation index for this derivative layer. `notes/scene-heading-audit.md` remains the provenance record for why each start point exists.

With all **57/57** scene texts complete-verified, the scene-text gate is closed successfully and **dialogue indexing may begin as the next structured derivative layer**. Dialogue extraction must continue to use the verified canonical/scene text without normalizing source speaker labels or silently resolving irregular labels.
