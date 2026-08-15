# திரும்பிப்பார்! — English reader edition

This directory is the publication-facing export layer built from the **complete-verified source-linked English translation records** under `../../translations/records/`.

It is deliberately downstream of the canonical Tamil/source layers. Nothing in this directory may be used to repair, normalize or overwrite canonical Tamil, scene derivatives, dialogue records, character mappings, song inventory or transcription files.

## Status

**Complete-verified — whole-work reader QA PASS.**

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

## Build and QA

Run from the repository root:

```bash
python works/tirumbippaar/editions/en/audit_probe.py
python works/tirumbippaar/editions/en/build.py
```

`audit_probe.py` provides a diagnostic preflight across all scene shards. `build.py` performs the release gate and exits non-zero if a required invariant fails.

The QA gate checks, among other things:

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

## Generated outputs

The passing build generates and the workflow commits:

- `reader-edition.md` — continuous Markdown edition with scene navigation and invisible unit/page provenance comments;
- `reader-edition.html` — standalone responsive and print-friendly HTML edition;
- `reader-edition.json` — concatenated machine-readable edition retaining source-linked metadata;
- `QA_REPORT.md` — generated whole-work QA result;
- `manifest.json` — deterministic integrity manifest containing aggregate input and output SHA-256 values.

The first complete reader build was produced by GitHub Actions in commit `e7b427f` after a passing whole-work QA run.

## Reader policy

The reader outputs do **not** rewrite verified English translation text. Exact Tamil source `speaker_label` values remain visible for labelled dialogue. Source-unlabelled speech remains unlabelled. Stage directions, chants, song references and written text remain distinct structures.

The source-sensitive readings already verified in the archival layers remain controlling, including scene 31 **`பாண்டியன் என் சொல்லை`**, scene 72 `[தாசி வீடு`, scene 90 `[மரணமூச்சுவிடும் பரந்தாமன்]`, scene 91 `பத்திரிகை News`, and scene 93 final `வணக்கம்.`. The final `★` remains structural and is not rendered as invented prose.

This is a provenance-safe reader/export derivative, not a new translation authority.
