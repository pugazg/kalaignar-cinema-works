# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Scope

This audit covers the complete PDF-specific song-presence scan, line-level Tamil lyric verification for all **54 numbered songs**, the complete source-linked English translation corpus, and the whole-corpus English reader/export preflight.

The rendered scan controls Tamil. Verified Tamil song files control the English derivative. The complete-verified English translation records then control reader/export generation. No external recording, lyric website, subtitle, alternate edition, campaign text, commentary, or soundtrack-memory reconstruction is used to repair any layer.

## Full-PDF page classification

**PASS — 194/194 pages scanned.**

- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs located: **54/54**;
- final song-bearing page: **130**.

Authoritative ledger: `notes/FULL_PDF_SONG_PAGE_SCAN.md`  
Machine map: `songs/page-map.json`

## Final Tamil lyric fidelity status

- draft: **0**;
- verified: **54** (`001–054`);
- review: **0**;
- not started: **0**;
- unresolved Tamil song readings: **0**.

The Tamil song corpus is **complete-verified** and immutable derivative input.

## English translation gate

The source-linked English translation corpus is **54/54 complete-verified** under `semantic-poetic-source-faithful` mode.

- `001–003`: **3 pilot-verified**;
- `004–054`: **51 verified**;
- draft/review/not-started: **0/0/0**;
- all 54 records remain `anthology-attributed`.

The approved English retains Kalaignar's language, rhetoric, repetition, political/social force, concrete imagery, colloquial energy, culture-bearing vocabulary and source-specific constructions. It is not a singable adaptation.

## Cross-page source records

The following eight songs span more than one song-bearing page and remain one record each across the Tamil, translation and reader-preflight layers:

- `009` — PDF 38–39;
- `019` — PDF 53–54;
- `023` — PDF 58–59;
- `024` — PDF 62–63;
- `036` — PDF 86–87;
- `037` — PDF 90–91;
- `051` — PDF 121–122;
- `052` — PDF 123–124.

## English reader/export preflight

**PASS.**

Authoritative report: `editions/en/PREFLIGHT_QA_REPORT.md`  
Probe: `editions/en/audit_probe.py`  
Workflow: `.github/workflows/kalaignar-song-anthology-english-preflight.yml`

The automated run checks the translation records independently against `translations/index.json`, `songs/page-map.json`, and all 54 verified Tamil song files.

PASS results:

- translation record files: **54/54**;
- source-linked Tamil song files: **54/54**;
- anthology order: **001–054, no gaps**;
- item status distribution: **3 pilot-verified / 51 verified**;
- `anthology-attributed`: **54/54**;
- mapped Tamil lyric lines/cues: **1,105**;
- mapped English lines/cues: **1,105**;
- Tamil/English line-count mismatches: **0**;
- duplicate anthology song numbers: **0**;
- duplicate translation IDs: **0**;
- duplicate song IDs: **0**;
- duplicate translation record paths: **0**;
- source-page mismatches against the verified page map: **0**;
- Tamil-title mismatches: **0**;
- film-title mismatches: **0**;
- attribution drift: **0**;
- translation-mode drift: **0**;
- cross-page provenance mismatches: **0**;
- warnings/errors: **0/0**.

The preflight explicitly preserves the distinction between `pilot-verified` and `verified`, and it does not promote anthology attribution into original-film primary-source verification.

## Final gate result

- Tamil transcription: **complete-verified — 54/54**;
- Tamil fidelity audit: **complete**;
- English translation: **complete-verified — 54/54**;
- English reader/export preflight: **complete-pass**;
- deterministic reader/export package: **complete-verified**;
- generated-output QA: **PASS**;
- generated songs: **54/54**;
- generated English lines/cues: **1,105/1,105**;
- cross-page records: **8/8**;
- generated-output warnings/errors: **0/0**.

**PASS — the source-linked Tamil and English layers and the deterministic English reader/export derivative are all closed at their verified checkpoints.**

## Generated-output integrity

`editions/en/QA_REPORT.md` confirms that Markdown, standalone HTML and machine-readable JSON each retain the complete 54-song anthology order and all 1,105 English lines/cues. There are zero missing/extra/duplicate song IDs, translation IDs or line IDs, zero source-page/status/attribution drift and zero English text drift in the machine-addressable outputs.

`editions/en/manifest.json` hashes **110 authoritative inputs** and the generated Markdown, HTML, JSON and QA report. Output SHA-256 values are recorded in `metadata.yaml`.

## Next activity

No required repository-internal archival or publication-generation gate remains for this anthology. Downstream Reading Room integration may proceed without reopening or smoothing the verified Tamil or Kalaignar-language English.


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
- source-side adjudications: **5** metadata discrepancies — one film label
  (`001`) and four canonical song titles (`004`, `007`, `008`, `015`);
- project-created English-title derivatives refreshed: **3** (`007`, `008`,
  `015`), re-derived from their corrected canonical Tamil titles after
  independent review found they still carried the superseded wording.
  `007` dropped a qualifier taken from the voice credit and now matches `005`,
  which carries the identical Tamil title; `008` dropped a continuation taken
  from the following lyric line; `015` renders the title's own `(சோகம்)` as a
  parenthetical qualifier rather than restating the page context label
  `சோக கீதம்`, which remains in the section layer;
- corpus census unchanged: **23** films, **54** songs, **1,105** line-cues,
  **8** cross-page records, **3** pilot-verified / **51** verified,
  **54** `anthology-attributed`;
- `editions/en/` regenerated through its own builder — **PASS**, 0 warnings,
  0 errors;
- `integrations/reading-room/build.py` — **PASS**, 23 film groups, 54 songs,
  1,105 line-cues, 0 warnings, 0 errors.

No attribution state was promoted, and no generated output was hand-edited.
