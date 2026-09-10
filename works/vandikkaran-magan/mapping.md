# வண்டிக்காரன் மகன் — Structural Mapping

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — archive ID `TVA_BOK_0062961`, **90 pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`**, image-only first-edition scan.

## Source identity and boundaries

PDF 2 prints `வண்டிக்காரன் மகன்`, `மூலக்கதை அண்ணா`, `திரைக்கதை-வசனம் கலைஞர்`, `கனி பதிப்பகம்`, `சென்னை-34.`. PDF 3 prints `முதற் பதிப்பு : 1978`. PDF 88–89 includes film-level `பாடல்கள்: கவிஞர் வாலி`; that is metadata only and does not by itself settle item-level song authorship.

| PDF | Printed | Disposition |
|---|---:|---|
| 1–3 | — | cover/title/edition metadata |
| 4–5 | — | `கலைஞரின் முன்னுரை` |
| 6–87 | 5–86 | canonical screenplay/dialogue |
| 88–89 | — | film credits |
| 90 | — | back cover |

For PDF 6–87, **printed = PDF − 1**.

## Scene-heading system — corrected and closed

Derivative boundary QA reconciled the structural inventory with the already verified canonical pages and established **72 source-visible headings**. PDF 10 contains the previously omitted inventory item `காட்சி — 4 எ.` → source scene ID `4-எ`.

- observed headings: **72/72**;
- base numeric range: **1–56**;
- unsuffixed/combined occurrences: **55**;
- suffix insertions: **17**;
- combined printed heading: **`45-46`**;
- multiple scene starts on one page are source-supported;
- internal location captions are not automatically scene boundaries.

Observed identifying sequence:

`1, 2, 3, 4, 4-எ, 5, 6, 7, 8, 9, 10, 10-எ, 11, 12, 13, 14, 14-எ, 15, 16, 16-எ, 17, 18, 19, 20, 20-எ, 21, 22, 22-எ, 23, 24, 24-எ, 24-பி, 24-சி, 24-டி, 25, 26, 27, 28, 29, 29-எ, 30, 31, 32, 33, 33-எ, 34, 35, 36, 37, 38, 39, 40, 41, 42, 42-எ, 43, 44, 45-46, 47, 48, 49, 50, 51, 52, 53, 53-எ, 53-பி, 53-சி, 53-டி, 54, 55, 56`

Exact source typography and start pages are recorded in `notes/scene-heading-audit.md`; scene ownership is fixed by `scenes/index.json`.

## Song / performance derivative gate

- source-visible occurrences: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- full or clearly bounded Tamil bodies: **6** — source scenes `10`, `20`, `24-சி`, `36`, `48`, `53-சி`;
- cue-only / non-lyric performance records: **3** — source scenes `7`, `32`, `42-எ`;
- item-level source-attributed lyric authorship: **0**;
- unresolved item-level lyric authorship: **6**;
- PDF 88 `பாடல்கள்: கவிஞர் வாலி`: preserved as film-level metadata only, not promoted to item-level authorship;
- missing chant/lyric text reconstructed: **0**;
- canonical Tamil / scene / dialogue / character mappings changed by this layer: **0**.

## Historical-glyph / source gates

Canonical first pass, visual verification, dedicated historical-glyph verification and final full visual verification are all **87/87 COMPLETE / PASS**, with **0** open source/glyph holds and **0** final-pass corrections.

## Scene derivative gate

- derivatives: **72/72 COMPLETE-VERIFIED**;
- screenplay coverage: **82/82 — PDF 6–87**;
- gaps / overlaps / duplicate ownership: **0 / 0 / 0**;
- canonical scene-body and joined derivative SHA-256: `84227c9855f3de942c8f1c240f9e6ddeee2d13f348fdda14b7712a81c4cfc19a`;
- non-scene PDF 4–5 and PDF 88–90 excluded.

## Dialogue derivative gate

- immutable dialogue records: **773 / COMPLETE-VERIFIED-RECONCILED / QA PASS**;
- exact source speaker labels: **38**;
- zero-dialogue scenes: **15**;
- cross-page dialogue records: **3**;
- anomalous non-colon candidates promoted: **0/16**;
- source-unlabelled blocks assigned a speaker: **0**;
- canonical Tamil / scene files changed by dialogue construction: **0**.

## Character/entity derivative gate

- exact source labels mapped: **38/38**;
- immutable dialogue records mapped: **773/773**;
- entities: **32 — 15 characters / 14 roles / 3 collectives**;
- verified / review / unresolved entities: **32 / 0 / 0**;
- unmapped labels / dialogue records: **0 / 0**;
- dialogue/source labels rewritten: **0**.

## Exact next activity

English translation is now **60/72 VERIFIED / QA PASS**.

**Translate and verify the remaining archive scene ordinals 61–72 as the final 12-scene English batch. Preserve source order and exact Tamil label/provenance metadata; link reconciled immutable dialogue IDs exactly once; keep source-unlabelled speech unassigned; link only verified song/performance occurrences; preserve unresolved item-level authorship as unresolved; and do not modify closed Tamil, scene, dialogue-record, character-mapping or song-record authorities.**
