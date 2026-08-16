# மனோகரா

Source-led archival work for the supplied screenplay/dialogue booklet `TVA_BOK_0010102_மனோகரா.pdf`.

The rendered scan is the controlling source for this edition. The PDF's OCR layer is useful only for navigation and must not be treated as canonical text.

## Verified source checkpoint

- source title: `மனோகரா`;
- printed credit: `திரைக்கதை வசனம்` / `மு. கருணாநிதி`;
- title-page publisher: `மூனா கானா பதிப்பகம்`;
- title-page address: `1/1 ஜக்கரியா காலணி 2-வது தெரு, சென்னை-24`;
- edition statement: `முதற்பதிப்பு : பிப்ரவரி 1954.`;
- rights statement: `உரிமை : ஆசிரியருக்கே.`;
- price: `விலை எட்டணா`;
- printer line: `Bharat Devi Press, 2/16, Mount Road, Madras-2.`;
- archive/source identifier from the supplied filename: `TVA_BOK_0010102`;
- PDF pages: **90**;
- file size: **30,684,695 bytes**;
- SHA-256: `87518fd8c290d7880aa2ddd9f2b5999c9d421d48fe1f02d61cf8e254393236a9`.

## Source boundaries

- PDF 1: illustrated front cover;
- PDF 2: title / screenplay-dialogue credit / publisher page;
- PDF 3: rights / first-edition date / price / printer page;
- PDF 4–5: `நாடகக் கதை` summary;
- PDF 6: `முன்னுரை`;
- PDF 7–88: screenplay/dialogue text;
- PDF 89: boxed back-matter advertisement/catalogue headed `ஒப்பிட்டுப் பாருங்கள்!`;
- PDF 90: back-cover advertisement for `முரசொலி`, with a later library/news-agent stamp over the printed advertisement.

The interior pagination supports `printed page = PDF page - 1` for the continuous book sequence. PDF 5 is visibly p.4, PDF 8 is visibly p.7, and PDF 88 is visibly p.87. Section-opening folios are suppressed on PDF 4, 6 and 7, so the main screenplay occupies logical printed pp. **6–87**.

## Structural finding

This edition does **not** print numbered scene headings. Scene boundaries therefore must not be invented or retroactively numbered during intake. The source uses decorative star separators, parenthetical/bracketed stage transitions, bare location labels and continuous dialogue/action instead. `mapping.md` and `notes/scene-heading-audit.md` record that source structure without claiming a source scene count.

The scan also contains an extended play-within-the-play sequence, several explicit song/performance references, a war-proclamation/chant-like passage, and a separately printed letter. These are structural findings only. No song authorship has been inferred from the screenplay/dialogue credit.

## Canonical Tamil checkpoint

The complete source-order first pass is stored in six archival batches:

- `transcription/parts/part-01-pdf-7-30.md` — PDF **7–30** / logical printed pp. **6–29** — **24 verified pages**;
- `transcription/parts/part-02-pdf-31-42.md` — PDF **31–42** / logical printed pp. **30–41** — **12 verified pages**;
- `transcription/parts/part-03-pdf-43-54.md` — PDF **43–54** / logical printed pp. **42–53** — **12 verified pages**;
- `transcription/parts/part-04-pdf-55-66.md` — PDF **55–66** / logical printed pp. **54–65** — **12 verified pages**;
- `transcription/parts/part-05-pdf-67-78.md` — PDF **67–78** / logical printed pp. **66–77** — **12 verified pages**;
- `transcription/parts/part-06-pdf-79-88.md` — PDF **79–88** / logical printed pp. **78–87** — **10 draft pages**;
- cumulative first-pass coverage: **82/82 canonical pages — complete**;
- current page status: **72 verified / 10 draft / 0 review**;
- aggregate first-pass status: **`draft-complete`**.

## Visual fidelity audit

The scan-led visual comparison has now covered the **entire 82-page canonical range**, but Part 06 still awaits correction application and post-application recheck, so the overall fidelity gate remains **in progress**.

Part 01, **PDF 7–30 / logical printed pp.6–29**, is **complete-verified**. Four visual-audit batches recorded **89** source-supported correction groups. All 89 were applied in a controlled rewrite, the rewritten range was checked again against the ledger and rendered scans, and all **24** Part 01 page anchors were promoted to `verified`.

Part 02, **PDF 31–42 / printed pp.30–41**, is **complete-verified**. Its two six-page visual-audit batches recorded **43** source-supported correction groups. All 43 were applied in one controlled rewrite, the corrected range passed a post-application recheck with **0 unresolved source readings**, and all **12** Part 02 page anchors were promoted to `verified`.

Part 03, **PDF 43–54 / printed pp.42–53**, is **complete-verified**. The final source-led set contains **48 actual correction groups**: 30 from PDF 43–48 and 18 from a direct re-audit of PDF 49–54. All 48 were applied in commit `f084ff91647ec1d76d2a113351e1a769fc8bad53`; the corrected range passed a post-application visual comparison with **0 unresolved source readings**, and all 12 anchors were promoted in `7f1413a451b7ac4ee769c0f20766f9c08939d753`. The definitive record is `notes/fidelity-audit-part03-final.md`.

Part 04, **PDF 55–66 / printed pp.54–65**, is **complete-verified**. Batch 9 recorded **33** source-supported corrections for PDF 55–60, and Batch 10 recorded **30** for PDF 61–66. All **63** reviewed corrections were applied in commit `fd9e993a21deae53a9b4310fd2022384e8ccb7c1` while all twelve anchors remained `draft`. The corrected file's Git blob matched the independently calculated expected blob `d0936ed84f4809d637b8d88e80a9309f13072d61`. The full PDF 55–66 range was then visually rechecked against the rendered scan with **0 unresolved source readings** and no additional correction required. All 12 anchors were promoted to `verified` in commit `0795ea5d668cecda8a258563d7b93d0c27f7dc29`; the verified blob is `42253eb2489e875f7b729a8aab2f084394463e85`. The definitive record is `notes/fidelity-audit-part04-final.md`.

Part 05, **PDF 67–78 / printed pp.66–77**, is **complete-verified**. Batch 11 recorded **33** source-supported corrections for PDF 67–72, and Batch 12 recorded **36** for PDF 73–78. All **69** reviewed corrections were applied in commit `9bfd56174a9d3fbb309ba52b1bca22204c234bb8` while all twelve anchors remained `draft`. The corrected file's Git blob matched the independently calculated expected blob `ae7a0b97c8aea592f3af2b7f40fe3917ecbda2ee`. The full PDF 67–78 range was then visually rechecked against the rendered scan with **0 unresolved source readings** and no additional correction required. All 12 anchors were promoted to `verified` in commit `bd2b26b558671eacd7819969bc9136ea11b3018d`; the verified blob is `86a75bdf3254b08e9551f14378f35ae58238efc0`. The definitive record is `notes/fidelity-audit-part05-final.md`.

Part 06, **PDF 79–88 / printed pp.78–87**, has completed its **10/10-page visual comparison**. Batch 13 recorded **63 clear scan-supported correction groups** with **0 unresolved source readings**. The detailed ledger is `notes/fidelity-audit-part06-batch13.md`. The 63 corrections remain deliberately unapplied, and all ten Part 06 anchors remain `draft`, until they can be written in one controlled rewrite and the corrected range can be visually rechecked.

Representative Part 06 restorations include the omitted `அதற்கும் நாள் குறித்திருக்கிறேன் மனோகரா!`, `பரலோகத்திற்கே`, source `இளந்தென்றல்`, `உன் பிள்ளைக் கனியமுதை!`, `மரண தேவதையின்`, `நீ கண்குளிரப் பார்க்க வேண்டும்`, `அநீதியை அழித்துவிடு`, `குதித்தாடும் குரங்குகளே!`, `சந்து புனை சிந்து பாடும்`, `என் வெற்றியின் உருவத்தை`, unusual source `கொல்லம் முயலும்போது`, and the final-page correction that `பத்மா! என் இதயராணி. என்னை மன்னித்துவிடு.` continues the king's speech rather than introducing a new `பத்மாவதி` speaker label.

Cumulative fidelity state:

- visually audited pages: **82/82 — complete visual comparison through PDF 88 / printed p.87**;
- verified pages: **72** — PDF **7–78**;
- draft pages: **10** — PDF **79–88**;
- review pages: **0**;
- Parts 01–05: **complete-verified**;
- Part 06: **10/10 visually audited; 63 corrections pending consolidated application**;
- unresolved source readings: **0**.

## Status

| Layer | Status |
|---|---|
| Source intake | complete |
| Structural mapping | verified |
| Numbered-scene disposition | not-applicable — none printed |
| Canonical Tamil first pass | **complete — 82/82 pages, PDF 7–88** |
| Visual fidelity audit | **in-progress — 82/82 visually compared; 72/82 verified; Part 06 rewrite/recheck pending** |
| Scene/dialogue/character derivatives | blocked / not-started |
| Song authorship / Tamil song derivatives | blocked / not-started |
| English translation | blocked / not-started |
| Reader / Reading Room integration | blocked / not-started |

## Next activity

**Apply all 63 reviewed Part 06 corrections to `transcription/parts/part-06-pdf-79-88.md` in one controlled source-led rewrite while all ten anchors remain `draft`. Mechanically verify the rewrite, then visually recheck PDF 79–88 against the rendered scan. Only after that passes with no unresolved source reading should Part 06—and therefore the entire 82-page canonical Tamil layer—be promoted to `verified`.**
