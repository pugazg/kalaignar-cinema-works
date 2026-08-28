# திரும்பிப்பார்! — English reader edition

This directory is the publication-facing export and packaging layer built from the **complete-verified corrected-source English records** under `../../translations/records/`.

It remains downstream of the canonical Tamil/source layers. Nothing here may be used to normalize or overwrite canonical Tamil, scene derivatives, dialogue records, character mappings, song inventory or transcription files.

## Status

**Complete-verified — whole-work reader QA PASS and deterministic EPUB 3 package QA PASS.**

Current reader checkpoint:

- canonical scenes: **93/93**;
- verified English units: **1,330/1,330**;
- unit kinds: **1,049 dialogue / 262 stage direction / 7 song-reference / 2 chant / 10 written-text / 0 full-song**;
- immutable labelled dialogue records linked exactly once: **1,042/1,042**;
- source-visible unlabelled spoken units: **7**;
- genuine cross-page English units: **12**;
- synthetic `(Scene ends.)` units from structural `★`: **0**;
- page-order regressions: **0**;
- missing/extra immutable dialogue links: **0 / 0**.

Current EPUB checkpoint:

- format: **EPUB 3**;
- packaged scenes: **93/93**;
- packaged verified units: **1,330/1,330**, each unit ID exactly once;
- scene XHTML documents: **93**;
- ZIP members: **99**;
- package size: **370,218 bytes**;
- EPUB SHA-256: `88bf02ac345926d02a3b6e25ea262c3f6aafe59383a620b2bb160cdd3fabbb31`;
- deterministic fixed ZIP timestamps and uncompressed members: **verified**;
- `mimetype` first, exact and uncompressed: **verified**;
- TOC, OPF manifest and spine coverage: **verified**.

The deterministic release was generated and committed by GitHub Actions in **`55bb983eb2959190f025250099793ab5efce2b9f`**.

## Generated outputs

- `reader-edition.md` — continuous Markdown edition with scene navigation and invisible unit/page provenance comments
- `reader-edition.html` — standalone responsive HTML edition
- `reader-edition.json` — machine-readable edition retaining source-linked metadata
- `QA_REPORT.md` — generated whole-work reader QA result
- `manifest.json` — reader integrity manifest
- `tirumbippaar-en.epub` — deterministic EPUB 3 package
- `EPUB_QA_REPORT.md` — generated EPUB package QA result
- `package-manifest.json` — EPUB integrity/package manifest

`manifest.json` records the 94 translation inputs, the 188-file validation set, output hashes and the **1,330 / 1,042** release checkpoint. `package-manifest.json` records the final EPUB hash, size, scene count, unit count and deterministic packaging metadata.

## Build and QA

From the repository root, the publication sequence is:

```bash
python works/tirumbippaar/editions/en/sync_status.py --prepare-index
python works/tirumbippaar/editions/en/normalize_source_order.py
python works/tirumbippaar/editions/en/audit_probe.py
python works/tirumbippaar/editions/en/build.py
python works/tirumbippaar/editions/en/package.py
python works/tirumbippaar/editions/en/sync_status.py --metadata
```

The active GitHub workflow is `.github/workflows/tirumbippaar-english-edition.yml`.

`normalize_source_order.py` does not renumber English unit IDs or rewrite translations. It synchronizes exact speaker-label metadata to immutable dialogue records and restores the two source-proven carry-over units in scenes 37 and 39 to their printed order. Any dialogue-linked page-provenance mismatch causes the workflow to stop for manual source review instead of silently rewriting provenance.

`audit_probe.py` verifies the complete 93-scene corpus before generation. `build.py` performs the reader release gate and writes Markdown/HTML/JSON outputs. `package.py` creates and validates the deterministic EPUB. `sync_status.py --metadata` updates `../../metadata.yaml` only after the package QA checkpoint passes.

## Reader policy

The reader and EPUB outputs do **not** rewrite verified English translation text. Exact Tamil `speaker_label` values remain attached to labelled dialogue. Source-unlabelled speech remains unlabelled. Stage directions, chants, song references and written text remain distinct structures.

Stable historical English IDs are preserved even where corrected source order places a later-numbered recovered unit earlier in a scene. Unit identity and source order are separate concerns.

Source-sensitive structures retained in the final package include scene 31 `பாண்டியன் என் சொல்லை`, scene 41's recovered dialogue links, scene 63's stable split/cross-page structure, scene 72's source wording/order, scene 90's death transition, scene 92's newspaper/Court opening, and scene 93's Jail opening, final departure direction and `வணக்கம்.`. The closing `★` remains structural and is not rendered as invented prose.

## Public reading target

The intended downstream public reading surface is the Kalaignar Digital Library / Reading Room at `https://nenjukkuneethi.org/read`. Web integration should prefer the structured verified repository data or `reader-edition.json`, not OCR or reparsed generated HTML.

Recommended navigation remains by the source's **93 scenes**, with Tamil/English access and provenance kept behind the reading presentation. Search indexes, collection cards and filters are presentation derivatives and must not alter canonical text, stable IDs or source metadata.

This directory is a provenance-safe publication derivative, not a new textual authority.
