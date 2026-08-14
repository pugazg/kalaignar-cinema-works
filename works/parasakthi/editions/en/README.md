# Parasakthi — English reader edition

This directory is the publication-facing export layer built from the **verified source-linked English translation records** under `../../translations/records/`.

It is deliberately downstream of the canonical Tamil/source layers. Nothing in this directory may be used to repair, normalize, or overwrite canonical Tamil, scene derivatives, dialogue records, character mappings, song inventory, Tamil song derivatives, or transcription files.

## Build and QA

Run from the repository root:

```bash
python works/parasakthi/editions/en/build.py
```

The builder performs whole-work structural/source-link QA before writing outputs. Any failed invariant exits non-zero and prevents a release build.

The QA gate checks, among other things:

- all **46 observed canonical scenes** are present in canonical order;
- canonical scenes **23 and 34** remain absent rather than being invented;
- all **769 English units** are unique, sequential and `verified`;
- kind totals remain **641 dialogue / 114 stage direction / 13 song / 1 quoted verse**;
- all **16 cross-page units** exactly match the translation index;
- every source path exists;
- every linked dialogue record is checked against the immutable record for scene, exact Tamil `speaker_label`, and page provenance;
- every song/verse occurrence ID exists in the verified song inventory;
- direct source-linked material without a dialogue record remains explicitly source-located rather than being assigned an invented ID;
- PDF/printed-page provenance remains inside the verified canonical range;
- reader outputs contain every verified English unit exactly once;
- no editorial placeholder tokens survive in reader text.

## Generated outputs

The build creates:

- `reader-edition.md` — continuous Markdown edition with scene navigation and invisible unit/page provenance comments;
- `reader-edition.html` — standalone responsive and print-friendly HTML edition;
- `reader-edition.json` — concatenated machine-readable edition retaining full source-linked unit metadata;
- `QA_REPORT.md` — generated whole-work QA result;
- `manifest.json` — deterministic integrity manifest containing aggregate input and output SHA-256 values.

## Reader policy

The reader outputs do **not** rewrite verified English translation text. Exact Tamil source `speaker_label` values remain visible for dialogue so that a publication layer does not silently resolve or rename source labels. Songs and quoted verse keep their verified English line order; stage directions remain distinct units.

Canonical scene **43** retains the documented provenance that the booklet prints heading **48** on PDF 49. Canonical final scene **48** retains the provenance that the booklet prints heading **43** on PDF 57.

This is a provenance-safe reader/export derivative, not a new translation authority.
