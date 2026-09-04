# Structural map — மந்திரி குமாரி

Source: `TVA_BOK_0026144_மந்திரி_குமாரி.pdf`

This map is source-structural only. It does not treat the prose story summary as screenplay scenes and it does not infer lyric authorship from the printed `கதை, வசனம் : மு. கருணாநிதி` credit.

## Physical-source checkpoint

- physical PDF pages: **14**;
- byte size: **579,782**;
- SHA-256: `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`;
- image-only scan; rendered pages control canonical transcription;
- story/dialogue credit on PDF 2: `கதை, வசனம் : மு. கருணாநிதி`;
- no explicit edition statement or publication year observed.

## Whole-source map

| PDF page(s) | Printed pagination | Structure | Disposition |
|---|---|---|---|
| 1 | none visible | illustrated cover | cover paratext |
| 2 | none visible | cast/music/production/writer credits | canonical source metadata / credits |
| 3 | none visible | `"மந்திரி குமாரி"—கதைச்சுருக்கம்` begins | canonical story-summary prose |
| 4 | `3` | story-summary continuation | canonical story-summary prose |
| 5 | `4` | story-summary conclusion | canonical story-summary prose |
| 6 | none visible | `மந்திரி குமாரி—பாடல்கள்` begins | canonical song/performance text |
| 7 | `6` | song/performance continuation | canonical song/performance text |
| 8 | `7` | song/performance continuation | canonical song/performance text |
| 9 | `8` | song/performance continuation | canonical song/performance text |
| 10 | `9` | song/performance continuation | canonical song/performance text |
| 11 | `10` | song/performance continuation | canonical song/performance text |
| 12 | `11` | song/performance continuation | canonical song/performance text |
| 13 | `12` | song/performance conclusion | canonical song/performance text |
| 14 | none visible | `அமரகவி` advertisement | unrelated paratext |

Unprinted page numbers are not promoted to source-visible pagination.

## Story-summary structure

PDF **3–5** is continuous prose, not scene-by-scene screenplay/dialogue.

- Tamil derivative: `story-summary/full-text.md` + `story-summary/index.json`;
- source pages: **3/3**;
- continuous records: **1**;
- synthetic scene IDs: **0**;
- immutable dialogue IDs: **0**;
- English derivative: `translations/story-summary.json` — **1/1 / 13 logical units / 1 cross-page unit**, complete-verified.

## Song/performance source order

| Block | Exact heading as printed | PDF page(s) |
|---:|---|---:|
| 1 | `தர்பார் நடனம்` | 6 |
| 2 | `ராஜகுமாரி` | 6–7 |
| 3 | `குமாரி கமலா நடனம்` | 7 |
| 4 | `மந்திரிகுமாரி` | 7–8 |
| 5 | `மந்திரிகுமாரி—பார்த்திபன்` | 8 |
| 6 | `குமாரி வனஜா நடனம்` | 8–9 |
| 7 | `தளபதி பார்ட்டி கோரஸ்` | 9–10 |
| 8 | `கற்பகம்—பூலோகம்` | 10 |
| 9 | `ராஜகுமாரி` | 10–11 |
| 10 | `லலிதா—பத்மினி—ராகினி நடனம்` | 11 |
| 11 | `மாட்டுக்கார பையன்` | 11–12 |
| 12 | `மந்திரிகுமாரி—ராஜகுமாரி` | 12 |
| 13 | `பார்த்திபன்—மந்திரிகுமாரி` | 12–13 |
| 14 | `உழவன்—தொகையறா` | 13 |
| 15 | `ராஜகுமாரி` | 13 |

Block 13's internal turn labels remain `பார்த்திபன்` / `அமுதவல்லி`; they are not normalized to the heading.

## Structured Tamil / English layers

- Tamil performance records: **15/15 complete-verified**, `songs/records/001.json`–`015.json`;
- source PDF coverage: **6–13 / 8/8 pages**;
- missing/duplicate IDs: **0 / 0**;
- English performances: **15/15 complete-verified**;
- English sections: **52**;
- Tamil / English line-cues: **234 / 234**;
- mapping mismatches: **0**;
- cross-page records: **002, 004, 006, 007, 009, 011, 013**;
- canonical Tamil changed by downstream layers: **no**;
- synthetic screenplay scene IDs: **0**.

## Bilingual reader/export

`editions/bilingual/` is **complete-verified — QA PASS**.

- navigation model: **1 story summary + 15 performances**;
- top-level source units: **16/16**;
- performance sections: **52/52**;
- Tamil / English performance line-cues: **234 / 234**;
- mapping mismatches: **0**;
- synthetic scenes: **0**.

## Reading Room integration payload

`integrations/reading-room/` is **payload-complete-verified — QA PASS**.

- payload mode: `source-linked-composition`;
- payload: `integrations/reading-room/reading-room.json`;
- expected linked Tamil/English source records: **32**;
- story-summary units: **13**;
- performance records / sections / line-cues: **15 / 52 / 234**;
- payload bytes: **15,704**;
- payload SHA-256: `20a0db293b936757e7d01def336252f28543337f319dfae6ad7bf5ae886bab43`;
- validator: `integrations/reading-room/build.py`;
- QA: `integrations/reading-room/QA_REPORT.md` — **PASS**;
- site application: **not-applied**;
- synthetic screenplay scene IDs: **0**;
- canonical Tamil changes: **0**;
- authorship upgrades: **0**.

The payload is a composition/provenance contract for the separate Reading Room implementation. It does not create a second text authority and it does not deploy the site.

## Authorship / cross-witness boundary

- booklet item-level lyricists verified: **0/15**;
- unresolved item-level lyricists: **15/15**;
- confirmed current-anthology witness: **1/15**, block 11 ↔ `kalaignar-song-001`;
- source-only in the current anthology: **14/15**;
- later anthology text used to repair this booklet: **no**;
- translation/reader/payload authorship upgrades: **0**.

## Gate status

- source intake / structural mapping: **complete / verified**;
- canonical Tamil: **complete-verified — PDF 2–13, 12/12 pages, 0 unresolved**;
- credits/story-summary/performance Tamil layers: **complete-verified**;
- English translation: **complete-verified**;
- bilingual reader/export: **complete-verified — QA PASS**;
- Reading Room payload: **payload-complete-verified — QA PASS**;
- Reading Room site application: **not-applied**;
- scene/dialogue full-work model: **not supported by this booklet**.

## Next activity / disposition

> **No required repository-internal Manthiri Kumari work remains. Apply the verified source-linked Reading Room payload in the separate implementation repository only when explicitly authorized, preserving natural story-summary + 15-performance navigation, provenance and unresolved item-level lyric-authorship status.**
