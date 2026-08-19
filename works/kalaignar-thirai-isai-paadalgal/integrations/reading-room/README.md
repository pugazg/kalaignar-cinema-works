# Reading Room integration — கலைஞர் திரை இசைப் பாடல்கள்

This directory is the downstream integration boundary between the verified archive in `pugazg/kalaignar-cinema-works` and the Kalaignar Digital Library / Reading Room presentation layer.

Preferred public surface: `https://nenjukkuneethi.org/read`

## Authority

The public UI is downstream. It must not become a new textual authority.

Authority remains:

1. rendered anthology scan for Tamil;
2. 54/54 verified Tamil song files;
3. 54/54 complete-verified source-linked English translation records;
4. deterministic English reader/export package;
5. this Reading Room payload;
6. website presentation.

Do not use the website to silently repair Tamil or English.

## Payload

`reading-room.json` is generated deterministically by `build.py` from:

- `editions/en/reader-edition.json`;
- `editions/en/manifest.json`;
- `songs/index.json`;
- `songs/page-map.json`;
- `translations/index.json`.

The payload is designed for direct structured-data consumption rather than scraping generated HTML.

It provides:

- **23 film groups** in first-appearance order;
- **54 songs** in anthology order `001–054`;
- **1,105 paired Tamil/English lines-cues**;
- Tamil and English song titles;
- film title and anthology-printed year;
- music and voice credits where printed;
- exact PDF page arrays;
- immutable Tamil/English source paths;
- `pilot-verified` / `verified` item status history;
- `anthology-attributed` attribution state;
- source and English section/turn labels;
- presentation-only navigation/search guidance.

## Navigation contract

For this film-song anthology, the natural navigation is:

1. **film** — first appearance in the anthology;
2. **song** — anthology song number within the film grouping.

This is deliberately different from screenplay works, whose natural navigation is scene-based.

A suggested presentation slug is included as UI metadata only. The consuming Reading Room implementation remains free to map it to its own route system without changing archival IDs.

## Language contract

Supported presentation modes may be:

- Tamil;
- English;
- parallel Tamil/English.

Language switching is presentation only. Stored Tamil and English strings must remain exactly as supplied by the verified payload.

The English remains `semantic-poetic-source-faithful`: do not smooth Kalaignar's repetition, rhetoric, political/social force, concrete images, colloquial energy, Tamil cultural vocabulary, performance terms or documented source pressure points for UI fluency.

## Search contract

A public search index may include:

- Tamil song title;
- English title;
- film title;
- Tamil lyric text;
- English lyric text.

Search normalization/tokenization may be performed in a separate index, but normalized text must never replace stored source/translation text.

## Attribution contract

All 54 items remain `anthology-attributed`.

A website card, search hit, reader page or translated display must not promote that status into original-film `primary-source-verified` authorship without separate item-level evidence being added upstream.

## Provenance contract

Keep the source PDF page array available behind the reader interface. All eight cross-page songs must retain both pages:

- `009` — 38–39;
- `019` — 53–54;
- `023` — 58–59;
- `024` — 62–63;
- `036` — 86–87;
- `037` — 90–91;
- `051` — 121–122;
- `052` — 123–124.

## QA and manifest

`QA_REPORT.md` must be **PASS** before downstream consumption.

`manifest.json` records hashes for the structured reader inputs, song/page indexes, translation index, payload builder and generated payload/QA output.

Never hand-edit `reading-room.json`. Update authoritative upstream data and rerun `build.py` instead.

## Repository boundary

This directory prepares the verified integration payload only. It does **not** claim that the public Reading Room implementation repository has been modified.

Applying the payload to a separate implementation repository requires that repository to be explicitly in scope. Until then, site application status remains `not-applied`.
