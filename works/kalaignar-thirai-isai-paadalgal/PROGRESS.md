# Progress — கலைஞர் திரை இசைப் பாடல்கள்

## Current phase

**English reader/export — complete-verified; generated-output QA PASS.**

Both immutable source-linked content layers remain closed:

- Tamil songs: **54/54 complete-verified**;
- English translations: **54/54 complete-verified**.

The whole-corpus preflight passed, and deterministic Markdown, standalone HTML and machine-readable JSON reader derivatives have now been generated and reconciled without rewriting the verified English.

## Source/Tamil checkpoint

- physical PDF pages scanned: **194/194**;
- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs mapped: **54/54**;
- Tamil song files verified: **54/54**;
- Tamil draft/review/not-started: **0/0/0**;
- unresolved Tamil song readings: **0**.

## English translation checkpoint

- translated: **54/54**;
- pilot-verified: **3** (`001–003`);
- verified: **51** (`004–054`);
- draft/review/not-started: **0/0/0**;
- mode: **`semantic-poetic-source-faithful`**.

## Reader/export preflight

Automated preflight: **PASS**.

Report: `editions/en/PREFLIGHT_QA_REPORT.md`  
Probe: `editions/en/audit_probe.py`  
Workflow: `.github/workflows/kalaignar-song-anthology-english-preflight.yml`

Passing checks include:

- **54/54** translation record files and **54/54** verified Tamil source links;
- anthology order **001–054** with no gaps;
- **3** `pilot-verified` + **51** `verified` statuses preserved;
- **54/54** records remain `anthology-attributed`;
- **1,105** mapped Tamil lyric lines/cues and **1,105** mapped English lines/cues;
- **0** line-count mismatches;
- **0** duplicate song numbers, translation IDs, song IDs or record paths;
- **0** source-page, Tamil-title or film-title mismatches;
- **0** translation-mode or attribution drift;
- exactly **8** cross-page records, matching the verified page map: `009`, `019`, `023`, `024`, `036`, `037`, `051`, `052`;
- **0 warnings / 0 errors**.

The preflight does not rewrite Tamil or English. Kalaignar-language decisions already fixed in the translation reviews remain immutable reader input.

## Deterministic reader/export package

Generated under `editions/en/`:

- `reader-edition.md` — **123,993 bytes**, SHA-256 `e522f7cc1508667af511cff62c8c50520618c53a43b299ca5a63739d6eaa500a`;
- `reader-edition.html` — **187,817 bytes**, SHA-256 `a330168a561cd80eb569d8d58a0f853d8fafa5d750f1cb23677bee8fc3f0da2d`;
- `reader-edition.json` — **354,357 bytes**, SHA-256 `e293d9df35930ba60bbb8987e7afeaea95befd124be182cb6ffa9db1f68bc90d`;
- `QA_REPORT.md` — generated-output QA **PASS**;
- `manifest.json` — deterministic checkpoint across **110 authoritative inputs** and all publication outputs.

Generated-output QA confirms **54/54 songs**, **1,105/1,105 English lines/cues**, **8/8 cross-page records**, the **3 pilot-verified / 51 verified** distinction, and **54/54 anthology-attributed** states with zero missing/extra/duplicate IDs, zero text drift, and **0 warnings / 0 errors**.

Kalaignar-language English is copied exactly from the verified records; the reader build performs no stylistic smoothing.

## Next activity

No required repository-internal transcription, translation, preflight, or reader/export work remains. The work is ready for **downstream Kalaignar Digital Library / Reading Room integration**, preserving anthology order, provenance, item-status history, attribution discipline and the source-faithful English.


## Reading Room integration cross-layer reconciliation

The downstream Reading Room payload builder
(`integrations/reading-room/build.py`) introduced an additional invariant that
no earlier gate covered: song-level metadata in `songs/index.json` must equal
the corresponding metadata in the generated `editions/en/reader-edition.json`.

The English reader/export preflight compared translation records against their
verified Tamil song files, and within that surface its zero-mismatch results
were correct. It never compared either against the song inventory, so five
metadata divergences sat outside every existing check until the new builder
halted on the first of them.

This reconciliation is therefore an **extension of QA coverage**, not a
correction of a previously false audit.

### Adjudication against the controlling 2024 scan

| Item | Divergence | Adjudicated from the scan |
|---|---|---|
| `001` film label | inventory `மந்திரிகுமாரி` vs lyric-page `மந்திரி குமாரி` | Both are printed. The film section heading (PDF 24) prints `மந்திரிகுமாரி` and controls film grouping; the numbered lyric page (PDF 26) prints `மந்திரி குமாரி`, now preserved as an explicit source variant in the `001` inventory `notes` and on the song page. The 1989 witness `TVA_BOK_0065773` also prints the spaced form and remains secondary evidence only. |
| `004` title | `மாரி மகமாயி மாரி` | The film song list (PDF 32) prints `மாரி மகமாயி மாரி மகமாயி`. The shortened form is not a printed title. |
| `007` title | `பேசும் யாழே பெண் மானே (சோகம்)` | The film song list (PDF 32) prints `பேசும் யாழே பெண் மானே`. The `(சோகம்)` belongs to the voice credit `ஜிக்கி (சோகம்)` on PDF 36 and is not part of the title. The credit itself is unchanged. |
| `008` title | `வருவாய் வருவாய் வைபோக` | The film song list (PDF 32) prints `வருவாய் வருவாய்...`. The previous value combined the first lyric line with the opening word of the second and was never a printed title. |
| `015` title | `காதல் துறையே புதுமைக் கனவே — சோக கீதம்` | The film song list (PDF 43) prints `காதல் துறையே புதுமைக் கனவே (சோகம்)`, which is how the list distinguishes this item from `014`, whose base title is identical. `முத்தாயி சோக கீதம்` is the performance/context label printed above the lyric on PDF 47 and remains in the song body, not in the title. `014` is unchanged. |

### Title authority for this work

- the film-specific `இப்படத்தில் இடம் பெற்ற பாடல்கள்` list controls canonical
  song-title metadata where present;
- numbered lyric pages control lyric body, role/performance/context labels and
  page-local wording;
- the film section heading controls the corpus film-grouping label;
- page-specific variants are preserved explicitly rather than normalised away;
- a title is never synthesised from a lyric first line plus another label.

### Reconciliation result

- Tamil lyric-body changes: **0** — the aggregate SHA-256 over the lyric bodies
  of all 54 song files is unchanged;
- English lyric-line changes: **0** — the aggregate SHA-256 over all 1,105
  stored English lines is unchanged, as is the aggregate over their paired
  Tamil, and every line ID is identical;
- changed fields: **5**, all song-title or film-label metadata;
- corpus census unchanged: **23** films, **54** songs, **1,105** line-cues,
  **8** cross-page records, **3** pilot-verified / **51** verified,
  **54** `anthology-attributed`;
- `editions/en/` regenerated through its own builder — **PASS**, 0 warnings,
  0 errors;
- `integrations/reading-room/build.py` — **PASS**, 23 film groups, 54 songs,
  1,105 line-cues, 0 warnings, 0 errors.

No attribution state was promoted, and no generated output was hand-edited.
