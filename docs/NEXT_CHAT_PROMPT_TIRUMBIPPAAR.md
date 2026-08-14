# Next-chat prompt — Tirumbippaar

Copy the prompt below into a new chat and attach the same source PDF `TVA_BOK_0014652_திரும்பிப்பார்.pdf`.

---

Continue the Kalaignar cinema-works archival project for **`திரும்பிப்பார்!`**.

GitHub repository:
`https://github.com/pugazg/kalaignar-cinema-works`

Attached source PDF:
`TVA_BOK_0014652_திரும்பிப்பார்.pdf`

Use the GitHub connector and work directly in the existing repository on `main`.

## MANDATORY STARTUP

Before making any change, read completely:

1. `docs/ARCHIVAL_WORKFLOW.md`
2. `docs/SOURCE_POLICY.md`
3. `docs/TRANSCRIPTION_GUIDE.md`
4. `docs/HANDOVER_TIRUMBIPPAAR.md`
5. `works/tirumbippaar/README.md`
6. `works/tirumbippaar/metadata.yaml`
7. `works/tirumbippaar/notes/fidelity-audit.md`
8. `works/tirumbippaar/mapping.md`
9. `works/tirumbippaar/notes/scene-heading-audit.md`
10. `works/tirumbippaar/transcription/parts/part-04-pdf-64-91.md`
11. `works/tirumbippaar/transcription/parts/part-05-pdf-92-112.md`

Inspect current `main` first and continue existing work. Do not create duplicate Tirumbippaar files and do not redo already verified pages.

## SOURCE AUTHORITY

The attached scan is the controlling source for this edition.

Expected source checkpoint:

- identifier: `TVA_BOK_0014652`
- 112 PDF pages
- main screenplay: PDF 9–112 / printed pp.1–104
- SHA-256: `973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682`
- printed-page formula: `printed page = PDF page - 8`

Do not rely on OCR as canonical evidence. Inspect rendered scan pages directly.

Do not silently modernize, correct, normalize, reconstruct or improve the Tamil. Preserve source spelling, punctuation, wording, exact speaker labels, repetition, unusual grammar, typographical forms, English code-switching, scene-marker irregularities, stage directions and printed/performance structures.

Do not repair text from film audio, subtitles, web copies, later editions, English translation, memory or familiar quotations.

If a reading is not confidently supported by the scan, keep the uncertainty explicit instead of guessing.

## CURRENT CHECKPOINT

At handover preparation, the repository state is:

- structural mapping: **verified**
- scene heading audit: **93/93 dispositioned**
- observed scenes: **1–93**, no numbering gaps/repeats/out-of-order findings
- first-pass Tamil transcription: **104/104 pages physically present**
- fidelity audit: **in-progress**
- verified pages: **75**
- draft pages: **29**
- review/unresolved audited pages: **0**
- verified range: PDF **9–83 / printed pp.1–75**
- remaining draft range: PDF **84–112 / printed pp.76–104**

Part status:

- part 01 (PDF 9–13): verified
- part 02 (PDF 14–35): verified
- part 03 (PDF 36–63): verified
- part 04 (PDF 64–91): PDF 64–83 verified; PDF 84–91 draft
- part 05 (PDF 92–112): draft

Documented integrity repairs already completed:

- PDF 61–63 were restored after a missing stored first-pass gap was discovered, and are now verified.
- PDF 80's missing source page anchor/boundary was repaired before verification.

Structured scene/dialogue/character/song/English derivatives are still `not-started` and must remain blocked until the Tamil fidelity audit completes.

## EXACT ACTIVITY TO PERFORM

**Complete the entire remaining Tamil visual fidelity audit in this activity: PDF 84–112 / printed pp.76–104 — all 29 remaining pages.**

For each page:

1. inspect the rendered scan directly;
2. compare every visible line with the stored first-pass transcription;
3. correct only where the scan supports the correction;
4. preserve source anomalies and historical/colloquial forms;
5. retain genuine uncertainty explicitly;
6. change the page anchor to `status=verified` only after complete visual comparison.

Update both:

- `works/tirumbippaar/transcription/parts/part-04-pdf-64-91.md` for PDF 84–91;
- `works/tirumbippaar/transcription/parts/part-05-pdf-92-112.md` for PDF 92–112.

If all 29 pages pass, synchronize:

- `works/tirumbippaar/metadata.yaml`
- `works/tirumbippaar/notes/fidelity-audit.md`
- `works/tirumbippaar/transcription/README.md`
- `works/tirumbippaar/transcription/full-text.md`
- `works/tirumbippaar/transcription/parts/README.md`
- `works/tirumbippaar/README.md`
- root `README.md`
- `data/works.json`

Then record the canonical Tamil fidelity audit as complete with **104 verified / 0 draft / 0 review** only if that is actually supported by the completed audit.

Do not modify the source PDF or any Parasakthi source/transcription/derivative files.

After completing and committing the work to `main`, compare the final HEAD with the starting checkpoint and report exactly which files changed.

If the full Tamil fidelity audit is complete, set the next archival activity to **scene index / scene-text derivative construction from the now-verified canonical Tamil**, following the existing repository workflow and using Parasakthi only as a reference implementation—not as a textual source.

Report:

- pages audited and verified;
- important source-supported corrections and any unresolved readings;
- final Tamil page counts/status;
- files changed;
- final `main` commit SHA;
- exact next activity.

---
