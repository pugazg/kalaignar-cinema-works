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

PDF **3–5** is a continuous prose `கதைச்சுருக்கம்`. It contains narrative references to film characters and events but is not printed as scene-by-scene screenplay/dialogue. Therefore:

- do not create source scene numbers from paragraph breaks;
- do not turn quoted/reported speech inside the synopsis into a film-wide immutable dialogue index;
- preserve it as continuous canonical prose with page anchors;
- any story-summary derivative must derive from the verified canonical Tamil.

The source-linked derivative is now complete at:

- `story-summary/full-text.md` — verified continuous PDF 3–5 text with page anchors;
- `story-summary/index.json` — one continuous-prose record, `manthiri-kumari-story-summary-001`.

Story-summary QA: **3/3 source PDF pages represented, 1 record, 0 synthetic scene IDs, 0 immutable dialogue IDs**.

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
| 13 | `பார்த்திபன்—மந்திரிகுமாரி` | 12–13 | cross-page character-pair exchange |
| 14 | `உழவன்—தொகையறா` | 13 | `தொகையறா` followed by `பாட்டு` material |
| 15 | `ராஜகுமாரி` | 13 | final printed performance block; distinct from blocks 2 and 9 |

Block 7 was initially stored with a normalized/misread heading. The full visual fidelity audit confirmed the printed form **`தளபதி பார்ட்டி கோரஸ்`**; this map now follows the controlling scan.

## Authorship boundary

PDF 2 directly verifies Kalaignar's **story/dialogue** credit: `கதை, வசனம் : மு. கருணாநிதி`.

The booklet does **not** provide a source-visible item-level lyricist line for each of the 15 song/performance blocks. Therefore:

- do not assign all printed songs to Kalaignar from the film-wide story/dialogue credit;
- retain honest item-level authorship states;
- compare blocks against the existing `works/kalaignar-thirai-isai-paadalgal/songs/` corpus without creating duplicates;
- external evidence, if later used for item-level lyric authorship, must be recorded separately and must never supply missing canonical text.

## Known cross-witness relationship

The existing later anthology contains one current `மந்திரிகுமாரி` record corresponding to booklet block 11, `மாட்டுக்கார பையன்`, represented there as `ஊருக்கு உழைப்பவண்டி`. The booklet remains an **independent film-specific witness**. No later-anthology text was used to repair the canonical booklet transcription.

## Scan / paratext notes

- PDF 1 has visible cover surface loss/abrasion, including a white damaged region at lower right; the title remains readable.
- No missing or duplicated physical PDF page was observed in the 14-page pass.
- No text-critical crop was observed on pages 2–13.
- PDF 14 is clearly an advertisement for another film (`அமரகவி`) and remains source paratext only.

## Gate status

- source intake: **complete**;
- structural mapping: **verified**;
- canonical Tamil transcription: **complete-verified — PDF 2–13**;
- visual fidelity audit: **complete-verified — 12/12 canonical PDF pages, 0 unresolved readings**;
- post-fidelity correction reconciliation: **complete for currently existing affected derivatives**;
- credits layer: **complete-verified**;
- story-summary derivative: **complete-verified — 1 continuous record / PDF 3–5 / 0 synthetic scene IDs / 0 immutable dialogue IDs**;
- song/performance inventory and cross-witness classification: **15/15 complete; exact-heading reconciliation complete**;
- source-linked structured song/performance records: **not-started — 0/15**;
- scene/dialogue derivative model: **not supported by this booklet as a full screenplay**;
- English translation: **blocked until source-linked performance records are complete**.

See `notes/fidelity-audit.md` and `notes/post-fidelity-corrections.md` for the correction record, including user-reviewed lexical source verdicts.

## Exact next activity

> **Create source-linked structured records for all 15 PDF 6–13 song/performance blocks from the verified canonical Tamil. Preserve the exact source headings, PDF-page provenance, `தொகையறா` / `பாட்டு` subdivisions, performance/speaker cues, the existing 1/15 cross-witness match and 14/15 source-only dispositions, and unresolved item-level lyric authorship unless separately evidenced. Then proceed to English translation only from the completed verified source-linked structures.**
