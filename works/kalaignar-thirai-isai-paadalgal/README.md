# கலைஞர் திரை இசைப் பாடல்கள்

Source-led archival work for the supplied anthology **`கலைஞர் திரை இசைப் பாடல்கள்`**, compiled by **நெல்லை ஜெயந்தா**.

## PDF-specific operating rule

For this PDF only: inspect the rendered page; if it contains an actual numbered lyric body or directly continues one, create/process that song file; otherwise ignore the page for lyric-file work. Do not import absent lyrics from outside this PDF.

The complete **194-page PDF has been visually scanned**:

- song-bearing pages: **62**;
- ignored pages: **132**;
- songs located: **54/54**;
- final song-bearing page: **130**.

See `notes/FULL_PDF_SONG_PAGE_SCAN.md` and `songs/page-map.json`.

## Tamil status

- verified: **54/54** (`001–054`);
- draft/review/not-started: **0/0/0**;
- Tamil song transcription: **complete-verified**;
- Tamil fidelity audit: **complete**;
- unresolved Tamil readings: **0**.

Cross-page verified Tamil song records are `009`, `019`, `023`, `024`, `036`, `037`, `051`, and `052`.

## English translation status

The English layer is **54/54 complete-verified** under `semantic-poetic-source-faithful` mode.

- pilot-verified: **3** (`001–003`);
- verified: **51** (`004–054`);
- draft/review/not-started: **0/0/0**;
- guide: `docs/SONG_TRANSLATION_GUIDE.md`;
- final translation review: `translations/BATCH_047_054_REVIEW.md`.

The English is deliberately **not** a singable rewrite or generic paraphrase. Across all 54 songs it retains repetition, social/political force, concrete images, rhetorical questions, colloquial energy, culture-bearing vocabulary, performance terms and verified source-specific constructions. No verified Tamil file was changed by the English translation layer.

## English reader/export preflight

**PASS — complete.**

Report: `editions/en/PREFLIGHT_QA_REPORT.md`  
Probe: `editions/en/audit_probe.py`  
Workflow: `.github/workflows/kalaignar-song-anthology-english-preflight.yml`

The automated whole-corpus gate verified:

- **54/54** translation records and **54/54** verified Tamil source links;
- anthology order **001–054**, with no gaps or duplicate IDs/paths;
- the status distinction **3 pilot-verified + 51 verified**;
- **54/54 `anthology-attributed`** records with no attribution promotion;
- **1,105 Tamil lines/cues ↔ 1,105 English lines/cues**, with zero line-count mismatches;
- zero source-page, Tamil-title, film-title or translation-mode mismatches;
- exactly eight complete cross-page records: `009`, `019`, `023`, `024`, `036`, `037`, `051`, `052`;
- **0 warnings / 0 errors**.

Reader/export generation must treat the complete-verified English records as immutable input. The preflight does not authorize stylistic smoothing of Kalaignar-language decisions.

## Attribution

The 2024 anthology is authoritative for what this edition prints and attributes. Default item status remains `anthology-attributed`; a verified English translation or reader/export derivative does not automatically upgrade that to original-film `primary-source-verified` authorship.

The anthology's `மந்திரிகுமாரி` editorial note mentions the censored/prohibited `ஆளப்பிறந்தவன் தமிழன் அவன்தானே`. Because its lyric is not printed as a numbered item, it remains an editorial note and is not inserted into the `001–054` corpus.

## Next activity

Generate deterministic publication-facing English reader/export outputs from the 54 verified translation records: Markdown, standalone HTML and machine-readable JSON, followed by generated-output QA and an integrity manifest. Preserve anthology order, source/page provenance, item status history, attribution state and the approved Kalaignar-language English exactly.
