# கலைஞர் திரை இசைப் பாடல்கள் — English Reader/Export Generated-Output QA

Status: **PASS**

This report validates the deterministic reader/export package generated from the 54 complete-verified source-linked English translation records. The build does not edit the Tamil or English source-linked layers.

## Generated package

- `reader-edition.md`
- `reader-edition.html`
- `reader-edition.json`
- `QA_REPORT.md`
- `manifest.json`

## PASS results

| Check | Result |
|---|---:|
| Songs in anthology order | **54 / 54** |
| English lyric lines/cues | **1105 / 1105** |
| Pilot-verified items | **3** (`001–003`) |
| Verified items | **51** (`004–054`) |
| Cross-page records | **8 / 8** |
| Markdown song anchors | **54 / 54** |
| Markdown line markers | **1105 / 1,105** |
| HTML song markers | **54 / 54** |
| HTML line markers | **1105 / 1,105** |
| JSON song records | **54 / 54** |
| JSON line records | **1105 / 1,105** |
| Attribution drift | **0** |
| Status drift | **0** |
| Source-page drift | **0** |
| Missing/extra/duplicate song IDs | **0** |
| Missing/extra/duplicate translation IDs | **0** |
| Missing/extra/duplicate line IDs | **0** |
| English-line text drift in JSON/HTML | **0** |
| Warnings | **0** |
| Errors | **0** |

## Provenance safeguards

All 54 generated song entries retain Tamil title, English title, film title, source PDF page array, immutable Tamil source path, item status and `anthology-attributed` state. All eight cross-page records retain their full arrays: `009` 38–39, `019` 53–54, `023` 58–59, `024` 62–63, `036` 86–87, `037` 90–91, `051` 121–122 and `052` 123–124.

## Kalaignar-language safeguard

The build concatenates the stored English lines/cues exactly. It does not smooth, paraphrase, modernize or replace source-shaped English during publication generation. The 1,105 stored English lines/cues are represented exactly once in each machine-addressable output layer.

## Gate disposition

**Generated-output QA: PASS.**

The deterministic English reader/export package is complete-verified and may proceed to downstream Reading Room integration without reopening the verified Tamil or English source-linked layers.
