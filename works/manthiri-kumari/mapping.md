# Structural map — மந்திரி குமாரி

Source: `TVA_BOK_0026144_மந்திரி_குமாரி.pdf`

This map is source-structural only. It does not treat the prose story summary as screenplay scenes and it does not infer lyric authorship from the printed `கதை, வசனம் : மு. கருணாநிதி` credit.

## Physical-source checkpoint

- physical PDF pages: **14**;
- byte size: **579,782**;
- SHA-256: `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`;
- image-only scan; rendered pages control canonical transcription;
- cover title: `மந்திரி குமாரி` under `மாடர்ன் தியேட்டர்ஸ்`;
- story/dialogue credit on PDF 2: `கதை, வசனம் : மு. கருணாநிதி`;
- no explicit edition statement or publication year was observed.

## Whole-source map

| PDF page(s) | Printed pagination | Structure | Disposition |
|---|---|---|---|
| 1 | none visible | illustrated cover — `மாடர்ன் தியேட்டர்ஸ்` / `மந்திரி குமாரி` | cover paratext |
| 2 | none visible | cast, dance, music/playback, writer/director and production/printer credits | canonical source metadata / credits layer |
| 3 | none visible | `"மந்திரி குமாரி"—கதைச்சுருக்கம்` begins | verified canonical prose story summary |
| 4 | `3` | story-summary continuation | verified canonical prose story summary |
| 5 | `4` | story-summary conclusion | verified canonical prose story summary |
| 6 | none visible | `மந்திரி குமாரி—பாடல்கள்` begins | verified canonical song/performance source text |
| 7 | `6` | song/performance continuation | verified canonical song/performance source text |
| 8 | `7` | song/performance continuation | verified canonical song/performance source text |
| 9 | `8` | song/performance continuation | verified canonical song/performance source text |
| 10 | `9` | song/performance continuation | verified canonical song/performance source text |
| 11 | `10` | song/performance continuation | verified canonical song/performance source text |
| 12 | `11` | song/performance continuation | verified canonical song/performance source text |
| 13 | `12` | song/performance conclusion | verified canonical song/performance source text |
| 14 | none visible | advertisement for `அமரகவி` | unrelated back-cover paratext; exclude from canonical Mandhiri Kumari text |

### Pagination note

The visible numerals establish a continuous internal sequence around the unnumbered section-opening pages, but unprinted numerals are **not** promoted to source-visible pagination. Canonical anchors therefore record only actually visible printed numbers and otherwise use the PDF page alone.

## Story-summary structure

PDF **3–5** is a continuous prose `கதைச்சுருக்கம்`. It is not printed as scene-by-scene screenplay/dialogue.

Rules:

- do not create source scene numbers from paragraph breaks;
- do not turn quoted/reported speech into a film-wide immutable dialogue index;
- preserve continuous prose and PDF-page provenance;
- derive only from verified canonical Tamil.

Source-linked Tamil derivative:

- `story-summary/full-text.md`;
- `story-summary/index.json`;
- **3/3 source PDF pages / 1 continuous record / 0 synthetic scene IDs / 0 immutable dialogue IDs**.

English derivative:

- `translations/story-summary.json`;
- **1/1 translated record / 13 logical prose units / 1 cross-page unit**;
- translation status: **complete-verified**.

## Song/performance section — exact heading sequence

The song/performance corpus runs PDF **6–13** and contains **15** separately headed source blocks. Repeated labels such as `ராஜகுமாரி` represent distinct source occurrences and must not be merged merely because their headings match.

| Block | Exact heading as printed | PDF page(s) | Structural notes |
|---:|---|---:|---|
| 1 | `தர்பார் நடனம்` | 6 | dance/performance block |
| 2 | `ராஜகுமாரி` | 6–7 | cross-page continuation |
| 3 | `குமாரி கமலா நடனம்` | 7 | dance/performance block; source includes `(இசை)` cues |
| 4 | `மந்திரிகுமாரி` | 7–8 | cross-page continuation; source includes `(பெண்)` cues |
| 5 | `மந்திரிகுமாரி—பார்த்திபன்` | 8 | character-pair exchange |
| 6 | `குமாரி வனஜா நடனம்` | 8–9 | cross-page dance/performance block with `தொகையறா` / `பாட்டு` structure |
| 7 | `தளபதி பார்ட்டி கோரஸ்` | 9–10 | cross-page chorus/performance block |
| 8 | `கற்பகம்—பூலோகம்` | 10 | labelled character exchange with `வசனம்` / song cues |
| 9 | `ராஜகுமாரி` | 10–11 | cross-page occurrence distinct from block 2 |
| 10 | `லலிதா—பத்மினி—ராகினி நடனம்` | 11 | dance/performance block |
| 11 | `மாட்டுக்கார பையன்` | 11–12 | cross-page; explicitly contains `தொகையறா` and `பாட்டு` subdivisions |
| 12 | `மந்திரிகுமாரி—ராஜகுமாரி` | 12 | character-pair exchange |
| 13 | `பார்த்திபன்—மந்திரிகுமாரி` | 12–13 | cross-page character-pair exchange; internal turn labels are `பார்த்திபன்` / `அமுதவல்லி` and remain unnormalized |
| 14 | `உழவன்—தொகையறா` | 13 | `தொகையறா` followed by `பாட்டு` material |
| 15 | `ராஜகுமாரி` | 13 | final printed performance block; distinct from blocks 2 and 9 |

Block 7's verified printed heading is **`தளபதி பார்ட்டி கோரஸ்`**.

## Song/performance structured record layer

The 15 blocks have one-to-one source-linked records:

- schema: `songs/schema.json`;
- index: `songs/index.json`;
- records: `songs/records/001.json`–`songs/records/015.json`;
- record count: **15/15**;
- source PDF coverage: **6–13, 8/8 pages**;
- missing/duplicate IDs: **0 / 0**;
- canonical Tamil changed by derivative creation: **no**;
- synthetic screenplay scene IDs created: **0**.

The records preserve source-page segmentation, exact headings, `தொகையறா` / `பாட்டு` subdivisions and source-visible speaker/performance cues.

## English song/performance translation layer

English translation is **complete-verified** under `translations/`:

- performance schema: `translations/performance.schema.json`;
- translation index: `translations/index.json`;
- performance records: `translations/performances/001.json`–`015.json`;
- final QA: `translations/FINAL_TRANSLATION_QA.md`;
- translated performance records: **15/15**;
- sections: **52**;
- Tamil source lines/cues: **234**;
- English lines/cues: **234**;
- line-mapping mismatches: **0**;
- cross-page translated records: **7** — `002`, `004`, `006`, `007`, `009`, `011`, `013`;
- synthetic scene IDs: **0**;
- canonical Tamil changed by translation: **no**.

## Bilingual reader/export layer

Reader/export is **complete-verified — QA PASS** under `editions/bilingual/`.

- navigation model: `story-summary-plus-performance-blocks`;
- top-level source units: **16/16** — 1 story summary + 15 performances;
- story-summary logical units: **13/13**;
- performance sections: **52/52**;
- Tamil / English performance line-cues: **234 / 234**;
- line-pair mismatches: **0**;
- cross-page performance records retained: **7/7**;
- synthetic scene IDs: **0**;
- canonical Tamil changed: **no**;
- QA: **PASS**.

The reader composition is `editions/bilingual/reader-edition.json`; the HTML surface loads only the verified translation records named there, so the reader does not become a competing textual authority.

## Authorship boundary

PDF 2 directly verifies Kalaignar's **story/dialogue** credit: `கதை, வசனம் : மு. கருணாநிதி`.

The booklet does **not** provide a source-visible item-level lyricist line for each of the 15 performance blocks. Therefore:

- booklet item-level lyricists verified: **0/15**;
- unresolved item-level lyricists: **15/15**;
- translation/reader-induced authorship upgrades: **0**.

Unresolved authorship does not block translation, reader construction or Reading Room payload preparation; it must remain visible in downstream metadata unless separately evidenced.

## Known cross-witness relationship

The later anthology contains one current `மந்திரிகுமாரி` record corresponding to booklet block 11, `மாட்டுக்கார பையன்`, represented there as `ஊருக்கு உழைப்பவண்டி`.

- confirmed existing anthology witness: **1/15**;
- source-only in the current anthology corpus: **14/15**;
- later anthology text used to repair this booklet: **no**.

## Scan / paratext notes

- PDF 1 has visible cover surface loss/abrasion, including a white damaged region at lower right; the title remains readable.
- No missing or duplicated physical PDF page was observed in the 14-page pass.
- No text-critical crop was observed on pages 2–13.
- PDF 14 is an unrelated `அமரகவி` advertisement and remains paratext only.

## Gate status

- source intake: **complete**;
- structural mapping: **verified**;
- canonical Tamil transcription: **complete-verified — PDF 2–13**;
- visual fidelity audit: **complete-verified — 12/12 canonical PDF pages, 0 unresolved readings**;
- post-fidelity correction reconciliation: **complete**;
- credits layer: **complete-verified**;
- story-summary Tamil derivative: **complete-verified**;
- song/performance Tamil records: **complete-verified — 15/15**;
- booklet-evidence lyric-authorship gate: **complete-with-unresolved-item-authorship — 15 unresolved**;
- English translation: **complete-verified**;
- bilingual reader/export: **complete-verified — QA PASS**;
- Reading Room integration: **ready / not-started**;
- scene/dialogue full-work model: **not supported by this booklet**.

## Exact next activity

> **Prepare and QA a provenance-safe Reading Room integration payload from the complete-verified bilingual reader. Preserve the booklet's natural story-summary + 15-performance navigation, page provenance, source-visible cues, cross-witness dispositions and unresolved item-level lyric authorship. Do not invent screenplay scenes or upgrade authorship through presentation metadata.**
