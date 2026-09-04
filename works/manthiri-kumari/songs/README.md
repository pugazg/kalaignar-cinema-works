# மந்திரி குமாரி — song / performance structured layer

Source: `TVA_BOK_0026144_மந்திரி_குமாரி.pdf`  
Canonical authority: `../transcription/full-text.md`

Status: **complete-verified — 15/15 source-linked records**.

## Files

- `schema.json` — schema for one Manthiri Kumari performance record.
- `index.json` — machine index and QA summary for all 15 records.
- `records/001.json`–`records/015.json` — the 15 separately headed PDF 6–13 source blocks, in source order.
- `performance-inventory.md` — human-readable source/cross-witness inventory.
- `cross-witness-comparison.md` — comparison against the later `கலைஞர் திரை இசைப் பாடல்கள்` corpus.
- `match-report-001-oorukku-uzhaippavandi.md` — detailed block-11 witness comparison.
- `AUTHORSHIP_GATE.md` — lyric-authorship evidence boundary.
- `../translations/index.json` — complete-verified English translation index for the story summary and all 15 performance records.

## Record model

Each record preserves:

- stable archival ID `manthiri-kumari-performance-001` through `-015`;
- exact printed heading;
- PDF-page and observed printed-page provenance;
- complete verified Tamil split into source-page segments;
- source-visible `தொகையறா` / `பாட்டு` subdivisions;
- source-visible speaker/performance cues;
- cross-witness disposition;
- item-level lyric-authorship status.

These record IDs are **archival navigation identifiers only**. The booklet itself does not number the 15 performance blocks.

## QA checkpoint

- expected records: **15**;
- completed records: **15**;
- missing/duplicate IDs: **0 / 0**;
- canonical source pages represented: **PDF 6–13, 8/8**;
- current-anthology confirmed witness: **1/15** — block 11 `மாட்டுக்கார பையன்` ↔ `kalaignar-song-001`;
- source-only against the current anthology corpus: **14/15**;
- booklet item-level lyricist credits: **0/15**;
- unresolved item-level lyric authorship at this evidence tier: **15/15**;
- synthetic screenplay scene IDs created: **0**;
- canonical Tamil modified by this derivative phase: **no**.

`source-only` means only that the current 54-song anthology has no corresponding record. It is not an authorship verdict.

## English checkpoint

The source-linked English layer is now **complete-verified**:

- performance translations: **15/15**;
- translation sections: **52**;
- Tamil source lines/cues mapped: **234**;
- English lines/cues mapped: **234**;
- line-count mapping mismatches: **0**;
- cross-page translated performance records: **7** — `002`, `004`, `006`, `007`, `009`, `011`, `013`;
- translation-induced authorship upgrades: **0**;
- canonical Tamil changed by translation: **no**.

See `../translations/README.md`, `../translations/index.json` and `../translations/FINAL_TRANSLATION_QA.md`.

## Authority boundary

The canonical Tamil remains `../transcription/full-text.md`. The JSON records are source-linked derivatives and must not be used to silently repair the canonical source layer.

The booklet's `கதை, வசனம் : மு. கருணாநிதி` credit establishes story/dialogue credit for the film, not automatic lyric authorship for these blocks. The later anthology remains a separate witness.

## Next activity

Proceed to the **deterministic bilingual reader/export layer** from the completed verified Tamil and English story-summary/performance structures.

Preserve the booklet's natural story-summary + performance navigation, page provenance, source-visible cues and unresolved lyric-authorship state. Do not convert this source into screenplay scenes.
