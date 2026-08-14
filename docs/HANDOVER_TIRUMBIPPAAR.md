# Tirumbippaar — controlling project handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover prepared: 2026-08-14  
Status checkpoint before this handover: `7836b4c6b645ef90abc5753d185d9cc5b04c3533`

Current stage: **canonical Tamil visual fidelity audit in progress**.

## Source authority

- Source PDF: `TVA_BOK_0014652_திரும்பிப்பார்.pdf`
- Source identifier: `TVA_BOK_0014652`
- SHA-256: `973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682`
- 112 PDF pages.
- Explicit edition statement on PDF 2: `முதல் பதிப்பு: 1953`.
- Main screenplay: PDF **9–112** / printed pp. **1–104**.
- Printed-page formula for the main text: `printed page = PDF page - 8`.
- Cover credit as printed: `கதை - வசனம் — கலைஞர் மு. கருணாநிதி`.
- PDF 3–6: `கலைஞர் பேசுகிறார்!`.
- PDF 7: `முக்கிய அறிவிப்பு`.
- PDF 8: catalogue advertisement.
- PDF 2 lower printer/imprint line is physically cropped; the archive supports only `சிட்டி பிரஸ், மதுரை ரோ…`. Do not reconstruct the missing continuation.

The supplied rendered scan is the controlling source. Embedded OCR is navigation-only.

## Source discipline — mandatory

Do not silently modernize, normalize, correct, reconstruct, paraphrase or improve the Tamil.

Preserve source-supported:

- spelling and historical/colloquial forms;
- punctuation and ellipses;
- exact speaker labels, including anomalous labels;
- scene-marker irregularities;
- English code-switching such as `Reading Room`, `News Paper Sheet`, `Carriage`, `wife`, `Phone`, `yes`, etc.;
- stage directions and printed/performance structures;
- repetition, unusual grammar and typographical forms.

Do not repair the source from film audio, subtitles, web quotations, later editions, memory, familiar dialogue, or English translation.

If a scan reading cannot be supported confidently, keep the uncertainty explicit rather than guessing.

## Structural state

Structural work is complete and verified:

- observed scene headings: **93**;
- scene range: **1–93**;
- numbering gaps: none observed;
- repeats: none observed;
- out-of-order scene numbers: none observed;
- canonical scene-number corrections: none;
- 93/93 scene starts and exact location headings dispositioned;
- main-text missing/duplicate/crop findings: none observed.

Authoritative structural files:

- `works/tirumbippaar/mapping.md`
- `works/tirumbippaar/notes/scene-heading-audit.md`

Performance/song candidates are only source-linked candidates at this stage. Do not infer authorship.

## Canonical Tamil transcription state

The first-pass transcription is physically complete for the full main-text range PDF **9–112 / printed pp.1–104**: **104/104 pages**.

Current page status:

- **75 verified**;
- **29 draft**;
- **0 review**;
- **0 unresolved audited pages**.

Continuous verified range: PDF **9–83 / printed pp.1–75**.

Remaining draft range: PDF **84–112 / printed pp.76–104** — exactly **29 pages**.

Part status:

1. `transcription/parts/part-01-pdf-9-13.md` — PDF 9–13 / pp.1–5 — **verified**.
2. `transcription/parts/part-02-pdf-14-35.md` — PDF 14–35 / pp.6–27 — **verified**.
3. `transcription/parts/part-03-pdf-36-63.md` — PDF 36–63 / pp.28–55 — **verified**.
4. `transcription/parts/part-04-pdf-64-91.md` — **mixed**: PDF 64–83 / pp.56–75 verified; PDF 84–91 / pp.76–83 draft.
5. `transcription/parts/part-05-pdf-92-112.md` — PDF 92–112 / pp.84–104 — **draft**.

Authoritative progress files:

- `works/tirumbippaar/metadata.yaml`
- `works/tirumbippaar/notes/fidelity-audit.md`
- `works/tirumbippaar/transcription/README.md`
- `works/tirumbippaar/transcription/full-text.md`
- `works/tirumbippaar/transcription/parts/README.md`
- `works/tirumbippaar/README.md`
- `data/works.json`

## Completed fidelity batches

- PDF 9–13 / printed pp.1–5: 5/5 verified.
- PDF 14–18 / printed pp.6–10: 5/5 verified.
- PDF 19–23 / printed pp.11–15: 5/5 verified.
- PDF 24–53 / printed pp.16–45: 30/30 verified.
- PDF 54–83 / printed pp.46–75: 30/30 verified.

The last completed batch is PDF **54–83 / printed pp.46–75**.

## Integrity repairs already made

Two first-pass storage problems were discovered during fidelity work and were documented rather than hidden:

1. `part-03-pdf-36-63.md` previously stopped at PDF 60 even though project status claimed PDF 36–63 coverage. PDF **61–63 / printed pp.53–55** were restored from the scan, then later fidelity-verified.
2. During the PDF 54–83 audit, PDF **80 / printed p.72** text was found to lack an explicit page anchor. The PDF 79/80 source boundary was restored from the scan before verification.

The first-pass coverage claim is now physically true for PDF 9–112.

## Structured derivatives — intentionally blocked

All remain `not-started`:

- scene index;
- scene text derivatives;
- dialogue index;
- character index;
- song authorship mapping;
- Tamil song derivatives;
- English translation.

Do not start these until the full canonical Tamil fidelity audit is complete, unless the repository workflow is explicitly changed and documented.

## Exact next activity

**Audit all remaining 29 pages in one activity: PDF 84–112 / printed pp.76–104.**

For every page:

1. inspect the rendered source image directly;
2. compare every visible line against the stored first-pass transcription;
3. apply only scan-supported corrections;
4. preserve source anomalies rather than normalizing them;
5. keep any genuinely uncertain reading explicit;
6. promote a page from `draft` to `verified` only after the entire page passes visual comparison.

This remaining activity spans:

- PDF 84–91 in `part-04-pdf-64-91.md`;
- PDF 92–112 in `part-05-pdf-92-112.md`.

After the last page passes:

- set canonical Tamil fidelity audit to **complete**;
- record **104 verified / 0 draft / 0 review** if and only if all pages pass;
- set audited-through PDF 112 / printed p.104;
- synchronize `metadata.yaml`, `notes/fidelity-audit.md`, transcription READMEs/indexes, work README, root README and `data/works.json`;
- confirm no source PDF or Parasakthi source/derivative files were modified;
- then make the **scene index / scene-text derivative layer** the next archival activity.

## Startup order for the next chat

Before changing anything, read:

1. `docs/ARCHIVAL_WORKFLOW.md`
2. `docs/SOURCE_POLICY.md`
3. `docs/TRANSCRIPTION_GUIDE.md`
4. this handover: `docs/HANDOVER_TIRUMBIPPAAR.md`
5. `works/tirumbippaar/README.md`
6. `works/tirumbippaar/metadata.yaml`
7. `works/tirumbippaar/notes/fidelity-audit.md`
8. `works/tirumbippaar/mapping.md`
9. `works/tirumbippaar/notes/scene-heading-audit.md`
10. the relevant transcription parts (`part-04` and `part-05`).

Then inspect current `main` and continue existing work. Do not create duplicate Tirumbippaar files or restart earlier completed batches.
