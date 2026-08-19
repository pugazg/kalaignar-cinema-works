# English translations — கலைஞர் திரை இசைப் பாடல்கள்

This directory contains source-linked English translations of the **54/54 complete-verified Tamil song files** under `../songs/`.

## Translation authority

- verified Tamil song files are the controlling textual source;
- the anthology's page provenance remains attached to every translation record;
- English never overwrites or repairs Tamil;
- external recordings, subtitles, web lyrics and alternate editions are not translation authorities for this layer;
- authorship status remains independent: the default remains `anthology-attributed` unless stronger item-level evidence is separately established.

## Kalaignar-language rule

English must retain Kalaignar's language rather than flattening it into generic lyric prose.

Follow `docs/SONG_TRANSLATION_GUIDE.md`:

- preserve repetition and refrain architecture;
- preserve political/social satire without euphemism;
- preserve concrete images and rhetorical questions;
- preserve colloquial energy and culture-bearing vocabulary;
- do not invent rhyme or smooth away awkward/source-specific constructions merely to make the English prettier;
- when a verified Tamil form is unusual, translate conservatively and document the pressure point instead of silently correcting the Tamil.

The default translation mode is `semantic-poetic-source-faithful`. This is **not** a singable adaptation.

## Record layout

- `schema.json` — translation-record schema;
- `index.json` — whole-corpus English translation status;
- `records/song-001.json` through `records/song-054.json` — source-linked English records;
- `PILOT_REVIEW.md` — approved pilot voice and structural decisions;
- seven scaled reviews through `BATCH_047_054_REVIEW.md` — all PASS.

Each record preserves anthology song number, exact source-song path, source PDF page(s), film title, attribution status, Tamil section/turn labels, Tamil lines alongside English lines, and translator notes for source-specific wording.

## Final translation checkpoint

- source Tamil songs: **54/54 complete-verified**;
- English translated: **54/54 complete-verified**;
- pilot-verified: **3** (`001–003`);
- verified: **51** (`004–054`);
- draft/review/not-started: **0/0/0**.

All translation gates pass. No verified Tamil song file was changed by the English layer.

## Reader/export preflight

**PASS — the completed translation layer is cleared for deterministic reader/export generation.**

Report: `../editions/en/PREFLIGHT_QA_REPORT.md`  
Probe: `../editions/en/audit_probe.py`

The preflight independently reconciles the records against the translation index, verified Tamil song files and verified page map. It confirms **54/54 records**, **54/54 source links**, **3 pilot-verified + 51 verified**, **54/54 anthology-attributed**, **1,105 Tamil mapped lines/cues ↔ 1,105 English lines/cues**, all eight cross-page arrays, and **0 warnings / 0 errors**.

The preflight treats every translation record as immutable reader input. It does not authorize publication-facing smoothing of Kalaignar-language wording or documented pressure points.

## Next activity

Build deterministic publication-facing derivatives under `../editions/en/`: `reader-edition.md`, standalone `reader-edition.html`, machine-readable `reader-edition.json`, generated-output `QA_REPORT.md`, and `manifest.json`. Generated QA must prove that all 54 songs and all 1,105 English mapped lines/cues survive exactly once with source provenance, item status and attribution state intact.
