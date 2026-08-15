# திரும்பிப்பார்! — English reader edition

This directory is the publication-facing export and packaging layer built from the **complete-verified source-linked English translation records** under `../../translations/records/`.

It is deliberately downstream of the canonical Tamil/source layers. Nothing in this directory may be used to repair, normalize or overwrite canonical Tamil, scene derivatives, dialogue records, character mappings, song inventory or transcription files.

## Status

**Complete-verified — whole-work reader QA PASS and deterministic EPUB 3 package QA PASS.**

Final reader checkpoint:

- canonical scenes: **93/93**;
- verified English units: **1,321/1,321**;
- unit kinds: **1,047 dialogue / 254 stage direction / 7 song-reference / 2 chant / 11 written-text / 0 full-song**;
- immutable labelled dialogue records linked exactly once: **1,040/1,040**;
- source-visible unlabelled spoken units: **7**;
- genuine cross-page English units: **12**;
- synthetic `(Scene ends.)` units from structural `★`: **0**;
- page-order regressions: **0**;
- missing/extra immutable dialogue links: **0 / 0**.

Final EPUB checkpoint:

- format: **EPUB 3**;
- packaged scenes: **93/93**;
- packaged verified units: **1,321/1,321**, each unit ID exactly once;
- scene XHTML documents: **93**;
- ZIP members: **99**;
- package size: **370,615 bytes**;
- EPUB SHA-256: `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`;
- deterministic fixed ZIP timestamps and uncompressed members: **verified**;
- `mimetype` first, exact and uncompressed: **verified**;
- TOC, OPF manifest and spine coverage: **verified**.

## Primary public reading target

The intended public destination for **திரும்பிப்பார்!** is the **Kalaignar Digital Library / Reading Room at `https://nenjukkuneethi.org/read`**.

The Reading Room, rather than a new print-ready PDF, should be treated as the primary publication surface for this work. Future downstream activity should therefore prioritize preparing these verified records for web integration.

Recommended Reading Room presentation:

- collection title: **`திரும்பிப்பார்!`**;
- description: screenplay / story-dialogue booklet;
- verified scope: **93 scenes · 104 printed pages**;
- navigation: by **scene**, not by artificial chapters;
- language access: Tamil source text and verified English derivative where available;
- search: scene text, dialogue and full-text content;
- source-linked metadata should remain available behind the presentation so reader text stays traceable to the archive.

The preferred web data source is the structured verified repository data (`translations/`, `scenes/`, `dialogues/` and reader JSON as appropriate), not OCR or scraped generated HTML. Search indexes, collection cards, filters and language controls are presentation derivatives and must not modify canonical Tamil, exact speaker labels, dialogue IDs, page provenance, scene order or verified translation text.

Do **not** create an additional print-ready PDF or another standalone publication package unless it is explicitly requested for a separate purpose. The existing EPUB may remain as a reproducible archival/publication artifact, but it is not the primary public reading destination.

## Build and QA

Run from the repository root:

```bash
python works/tirumbippaar/editions/en/audit_probe.py
python works/tirumbippaar/editions/en/build.py
python works/tirumbippaar/editions/en/package.py
python works/tirumbippaar/editions/en/sync_status.py
```

`audit_probe.py` provides a diagnostic preflight across all scene shards. `build.py` performs the reader release gate and generates the Markdown/HTML/JSON derivatives. `package.py` creates and validates the deterministic EPUB 3 file. `sync_status.py` writes the verified derivative/package checkpoint back to `works/tirumbippaar/metadata.yaml`.

The reader QA gate checks, among other things:

- all **93 canonical scenes** are present in canonical order;
- all **1,321 English units** are unique, sequential and `verified`;
- all **1,040 immutable labelled dialogue records** are linked exactly once;
- the seven source-visible unlabelled spoken units remain unlabelled rather than receiving invented speaker/dialogue IDs;
- all **12 cross-page English units** exactly match `translations/index.json`;
- every linked dialogue record agrees with its immutable record for canonical scene, exact Tamil `speaker_label` and page provenance;
- every song occurrence ID used by translation exists in the song inventory;
- PDF/printed-page provenance remains inside PDF **9–112** / printed **1–104**, with `printed = PDF - 8`;
- source-only `★` separators do not reappear as synthetic `(Scene ends.)` units;
- reader Markdown and HTML contain every verified English unit exactly once;
- no editorial placeholder token survives in reader text.

The EPUB package gate additionally checks the ZIP member set, first/uncompressed `mimetype`, OPF manifest, title + 93-scene spine, 93-scene table of contents, exact per-unit XHTML coverage, and deterministic package construction.

## Generated outputs

The passing workflow generates and commits:

- `reader-edition.md` — continuous Markdown edition with scene navigation and invisible unit/page provenance comments;
- `reader-edition.html` — standalone responsive and print-friendly HTML edition;
- `reader-edition.json` — concatenated machine-readable edition retaining source-linked metadata;
- `QA_REPORT.md` — generated whole-work reader QA result;
- `manifest.json` — deterministic reader integrity manifest;
- `tirumbippaar-en.epub` — deterministic EPUB 3 publication package;
- `EPUB_QA_REPORT.md` — generated EPUB package QA result;
- `package-manifest.json` — EPUB integrity/package manifest including package SHA-256.

The first complete reader build was produced by GitHub Actions in commit `e7b427f`. The deterministic EPUB package subsequently passed the same whole-work reader gate plus its package-specific gate and is now maintained by the active workflow.

## Reader policy

The reader and EPUB outputs do **not** rewrite verified English translation text. Exact Tamil source `speaker_label` values remain visible for labelled dialogue. Source-unlabelled speech remains unlabelled. Stage directions, chants, song references and written text remain distinct structures.

The source-sensitive readings already verified in the archival layers remain controlling, including scene 31 **`பாண்டியன் என் சொல்லை`**, scene 72 `[தாசி வீடு`, scene 90 `[மரணமூச்சுவிடும் பரந்தாமன்]`, scene 91 `பத்திரிகை News`, and scene 93 final `வணக்கம்.`. The final `★` remains structural and is not rendered as invented prose.

This is a provenance-safe reader/export/package derivative, not a new translation authority.
