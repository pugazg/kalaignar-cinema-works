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

The interior pagination supports `printed page = PDF page - 1` for the continuous book sequence. Section-opening folios are suppressed on PDF 4, 6 and 7, so the main screenplay occupies logical printed pp. **6–87**.

## Structural finding

This edition does **not** print numbered scene headings. Scene boundaries therefore must not be retroactively presented as source scene numbers. The source uses decorative star separators, parenthetical/bracketed stage transitions, bare location labels and continuous dialogue/action instead. `mapping.md` and `notes/scene-heading-audit.md` document that source structure.

The scan also contains an extended play-within-the-play sequence, explicit song/performance references, a war-proclamation/chant-like passage, and a separately printed letter. No song authorship has been inferred from the screenplay/dialogue credit.

## Canonical Tamil — complete-verified

The complete source-order Tamil layer is stored in six verified archival batches:

- `transcription/parts/part-01-pdf-7-30.md` — PDF **7–30** / logical printed pp. **6–29** — **24 verified pages**;
- `transcription/parts/part-02-pdf-31-42.md` — PDF **31–42** / logical printed pp. **30–41** — **12 verified pages**;
- `transcription/parts/part-03-pdf-43-54.md` — PDF **43–54** / logical printed pp. **42–53** — **12 verified pages**;
- `transcription/parts/part-04-pdf-55-66.md` — PDF **55–66** / logical printed pp. **54–65** — **12 verified pages**;
- `transcription/parts/part-05-pdf-67-78.md` — PDF **67–78** / logical printed pp. **66–77** — **12 verified pages**;
- `transcription/parts/part-06-pdf-79-88.md` — PDF **79–88** / logical printed pp. **78–87** — **10 verified pages**.

Final canonical status: **82 verified / 0 draft / 0 review**.

## Visual fidelity audit — complete

Every canonical page PDF **7–88 / logical printed pp.6–87** has been compared against the rendered scan and passed its correction/recheck gate. There are **0 unresolved source readings**.

Part-level correction totals after final rechecks:

- Part 01 — **89** corrections;
- Part 02 — **43**;
- Part 03 — **48**;
- Part 04 — **63**;
- Part 05 — **69**;
- Part 06 — **68 final corrections**.

Part 06's initial full-range audit recorded **63** corrections. After those were applied, the mandatory second complete visual comparison found **5 additional scan-supported corrections**. Those were applied before verification. The final Part 06 record is `notes/fidelity-audit-part06-final.md`.

Important final-page disposition: `பத்மா! என் இதயராணி. என்னை மன்னித்துவிடு.` continues the king's speech without a printed speaker label; it is not converted into an invented/new speaker label in the canonical text.

## Scene derivative layer — in progress

The verified transition audit contains **57 principal source-visible transition dispositions** (`T001`–`T057`). These are used as the start points for **57 archival scene segments** in `scenes/index.json`.

This is a derivative navigation system only. The booklet still has **no source scene numbers**. IDs such as `manohara-s001` and filenames such as `scene-001.md` must never be presented as numbers printed by the source.

Current scene checkpoint:

- archival scene segments indexed: **57/57**;
- scene index: **complete**;
- scene-text derivatives: **23/57 complete-verified**;
- completed: `manohara-s001`–`manohara-s023`;
- `manohara-s016` preserves the genuine PDF 30→31 continuity across the Part 01 / Part 02 storage boundary;
- `manohara-s017` preserves the Pandya inquiry and Rajapriyan's public marriage judgment;
- `manohara-s018` ends before the separate song/boat transition `T019`;
- `manohara-s019` preserves the `“சிங்காரப் பைங்கிளியே... பேசு”` performance/boat occurrence and failed dagger attack;
- `manohara-s020`–`manohara-s023` preserve the Vasanthasena–Bauthayan conspiracy, the false report to Padmavati, Manoharan's oath, Vasanthasena's counter-order and Bauthayan's prison death;
- next: `manohara-s024`, beginning with `வசந்தா-அரசர் படுக்கையறை` / `“பொழுது புலர்ந்தது” பாட்டு` on PDF 37;
- dialogue indexing remains blocked until all scene-text derivatives are complete.

The segmentation policy and safeguards are documented in `scenes/README.md`.

## Status

| Layer | Status |
|---|---|
| Source intake | complete |
| Structural mapping | verified |
| Numbered-scene disposition | not-applicable — none printed |
| Canonical Tamil | **complete-verified — 82/82 pages** |
| Visual fidelity audit | **complete — 82/82 pages** |
| Archival scene index | **complete — 57 derivative segments** |
| Scene-text derivatives | **in-progress — 23/57 complete-verified** |
| Dialogue index | blocked until scene-text layer |
| Character index | blocked until dialogue layer |
| Song/performance authorship | blocked until earlier structured layers |
| English translation | blocked until structured source layer |
| Reader / Reading Room integration | blocked / not-started |

## Next activity

**Continue scene-text derivatives from `manohara-s024` / transition `T024`, beginning with `வசந்தா-அரசர் படுக்கையறை` and the `“பொழுது புலர்ந்தது” பாட்டு` reference on PDF 37. Copy only from the verified canonical Tamil, preserve page anchors and source irregularities, and do not create source scene numbers or synthetic scene-ending prose.**
