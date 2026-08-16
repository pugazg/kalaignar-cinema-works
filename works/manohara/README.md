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

## Scene derivative layer — complete-verified

The verified transition audit contains **57 principal source-visible transition dispositions** (`T001`–`T057`). These are used as the start points for **57 archival scene segments** in `scenes/index.json`.

This is a derivative navigation system only. The booklet still has **no source scene numbers**. IDs such as `manohara-s001` and filenames such as `scene-001.md` must never be presented as numbers printed by the source.

Final scene checkpoint:

- archival scene segments indexed: **57/57**;
- scene index: **complete**;
- scene-text derivatives: **57/57 complete-verified**;
- completed: `manohara-s001`–`manohara-s057`;
- five genuine source continuities across canonical storage-part boundaries were preserved rather than converted into false scene breaks: `s016`, `s030`, `s036`, `s041`, and `s051`;
- no source scene numbers, synthetic endings, or duplicate boundary separators were introduced.

The segmentation policy and safeguards are documented in `scenes/README.md`.

## Dialogue index — in progress

The dialogue layer is active under `dialogues/` and follows the repository's established scene-sharded immutable-record model, adapted for Manohara's unnumbered source structure.

Current checkpoint:

- dialogue scene shards completed: **40/57** — `manohara-s001` through `manohara-s040`;
- immutable explicitly speaker-labelled dialogue records: **676**;
- eighth batch (`s036`–`s040`) added **209** records;
- `manohara-s036` alone contributes **88** records from the long court confrontation and its aftermath;
- cross-page dialogue records are now **6** — the previous three plus `manohara-s036-d032` (PDF 51→52), `manohara-s036-d041` (PDF 52→53), and `manohara-s036-d077` (PDF 56→57);
- the unlabelled collective cries under `(சபையோர்)` on PDF 55 remain outside the dialogue index, while the later explicit `சபையோர் :` line on PDF 56 is indexed with its immediately following unlabelled continuation kept in the same record;
- `manohara-s038` intentionally leaves the empty-speaker line `: இப்ப நான் சொல்றபடி சொல்லணும்......` unindexed;
- `manohara-s039-d029` preserves the explicit printed label `வசந்தசேனை மனதிற்குள்` exactly rather than converting it to narrative or a normalized character identity;
- the separately printed Ugrasenan letter in `manohara-s040` remains outside the dialogue index because it is a letter block rather than explicitly speaker-labelled dialogue;
- source-label/delimiter anomaly records remain **4**; this batch introduces no new delimiter form;
- `manohara-s024` remains the sole zero-record scene so far;
- `speaker_label` preserves the exact source-visible label and is never expanded or normalized at this layer;
- source-unlabelled material is never assigned to an inferred speaker merely to increase dialogue coverage;
- character normalization remains deferred to the later character/entity index;
- next dialogue batch: **`manohara-s041`–`manohara-s045`**.

Dialogue policy, schema and checkpoint are recorded in `dialogues/README.md`, `dialogues/schema.json` and `dialogues/index.json`.

## Status

| Layer | Status |
|---|---|
| Source intake | complete |
| Structural mapping | verified |
| Numbered-scene disposition | not-applicable — none printed |
| Canonical Tamil | **complete-verified — 82/82 pages** |
| Visual fidelity audit | **complete — 82/82 pages** |
| Archival scene index | **complete — 57 derivative segments** |
| Scene-text derivatives | **complete-verified — 57/57** |
| Dialogue index | **in-progress — 40/57 scenes, 676 records** |
| Character index | blocked until dialogue layer |
| Song/performance authorship | blocked until earlier structured layers |
| English translation | blocked until structured source layer |
| Reader / Reading Room integration | blocked / not-started |

## Next activity

**Continue dialogue indexing with `manohara-s041` through `manohara-s045` in the next meaningful batch. Create records only for non-empty explicitly speaker-labelled utterances, preserve exact label/delimiter/text/page provenance, keep cross-page utterances whole, and never assign source-unlabelled speech to an inferred speaker.**
