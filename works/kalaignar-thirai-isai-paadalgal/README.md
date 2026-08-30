# கலைஞர் திரை இசைப் பாடல்கள்

Source-led archival work for **`கலைஞர் திரை இசைப் பாடல்கள்`**.

## Source witnesses

Two distinct source witnesses are tracked under the same work ID and remain source-separated.

1. **2024 anthology — `TVA_BOK_0065867`** — compiled by **நெல்லை ஜெயந்தா**. This is the completed 194-page source-linked corpus with 54 verified Tamil songs, 54 verified English translations and completed reader/export outputs.
2. **Earlier first-edition witness — `TVA_BOK_0065773`** — compiled by **சிலோன் விஜயேந்திரன்**, with the printed first-edition date `வைகாசி 21, திருவள்ளுவர் 2020 (03.06.89)`. Its 62-page scan has completed source intake, structural mapping and song-presence deduplication against the existing parent `songs/` folder.

The 1989 witness contains **40 numbered source sections**. Under the current rule — use the existing `songs/` folder and do not add a song that is already present — all **40/40** sections were found to be already represented by **39 distinct existing song records**. Therefore **0 new song files** and **0 new index rows** were added. Detailed mapping: `songs/SOURCE_WITNESS_0065773_DEDUP.md`.

The second witness remains preserved at `sources/tva-bok-0065773/` for provenance and possible future textual-variant study. It does not overwrite, renumber or silently correct the completed 2024 corpus.

## 2024 PDF-specific operating rule

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

## English reader/export

**Complete-verified — preflight PASS and generated-output QA PASS.**

Preflight: `editions/en/PREFLIGHT_QA_REPORT.md`  
Generated-output QA: `editions/en/QA_REPORT.md`  
Integrity manifest: `editions/en/manifest.json`  
Builder: `editions/en/build.py`

The deterministic package contains:

- `editions/en/reader-edition.md`;
- `editions/en/reader-edition.html`;
- `editions/en/reader-edition.json`.

QA confirms **54/54 songs** and **1,105/1,105 English lines/cues** exactly once in each machine-addressable output layer, with all **8 cross-page records**, **3 pilot-verified + 51 verified** statuses and **54 anthology-attributed** states intact. There are **0 warnings / 0 errors** and no English-line text drift.

The build treats the source-faithful English as immutable input. It does not smooth Kalaignar's language for publication.

## Attribution

The 2024 anthology is authoritative for what that edition prints and attributes. Default item status remains `anthology-attributed`; a verified English translation or reader/export derivative does not automatically upgrade that to original-film `primary-source-verified` authorship.

The 1989 witness likewise supports anthology-level evidence for what it prints; its presence does not by itself upgrade original-film item authorship.

The 2024 anthology's `மந்திரிகுமாரி` editorial note mentions the censored/prohibited `ஆளப்பிறந்தவன் தமிழன் அவன்தானே`. Because its lyric is not printed as a numbered item, it remains an editorial note and is not inserted into the `001–054` corpus.

<!-- BEGIN GENERATED: reading-room-status -->

## Reading Room integration payload

A verified structured payload is now available at `integrations/reading-room/reading-room.json`, with QA in `integrations/reading-room/QA_REPORT.md` and deterministic hashes in `integrations/reading-room/manifest.json`.

It contains **23 film groups / 54 songs / 1,105 paired Tamil-English lines-cues / 8 cross-page songs**, retaining exact archive IDs, source pages, item status history, printed credits where available and `anthology-attributed` state. QA reports **0 warnings / 0 errors / 0 Tamil or English text drift**.

The payload is intended for structured-data consumption by the Kalaignar Digital Library / Reading Room. Search/navigation/language-switching are presentation concerns and must not rewrite stored Tamil or the source-faithful Kalaignar-language English.

## Next activity

The public Reading Room implementation itself remains `not-applied`. Apply this payload in the separate implementation repository only when that repository is explicitly authorized for modification.

<!-- END GENERATED: reading-room-status -->

