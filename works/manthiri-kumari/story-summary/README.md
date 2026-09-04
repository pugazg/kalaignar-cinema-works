# மந்திரி குமாரி — கதைச்சுருக்கம்

Source-derived continuous prose layer for PDF **3–5** of `TVA_BOK_0026144_மந்திரி_குமாரி.pdf`.

Status: **complete-verified**.

## Authoritative inputs

- canonical Tamil: `../transcription/full-text.md`;
- controlling source: `TVA_BOK_0026144_மந்திரி_குமாரி.pdf`;
- source SHA-256: `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`.

## Derivative files

- `full-text.md` — verified PDF 3–5 synopsis text extracted from canonical Tamil with page anchors preserved;
- `index.json` — one source-linked continuous-prose record covering PDF 3–5;
- `../translations/story-summary.json` — complete-verified source-linked English translation.

## Rules / QA

- Preserve the booklet's continuous prose structure.
- Preserve PDF page provenance and observed printed pages.
- Do not convert paragraphs into screenplay scenes.
- Do not create immutable dialogue records from reported or quoted synopsis speech.
- Do not normalize or repair wording in this derivative independently of canonical Tamil.

Tamil QA result:

- source PDF pages represented: **3/3**;
- continuous story-summary records: **1**;
- synthetic scene IDs created: **0**;
- immutable dialogue IDs created: **0**;
- canonical authority changed by derivative creation: **no**.

English checkpoint:

- story-summary translations: **1/1 complete-verified**;
- logical prose translation units: **13**;
- cross-page translation units: **1**, preserving the PDF 3→4 continuation;
- synthetic scene IDs created by translation: **0**;
- canonical Tamil changed by translation: **no**.

See `../translations/index.json` and `../translations/FINAL_TRANSLATION_QA.md`.

## Next activity

Build and QA the **deterministic bilingual reader/export layer** from the complete-verified story-summary and 15 performance translations, preserving continuous-prose identity, natural booklet navigation and source/page provenance.
