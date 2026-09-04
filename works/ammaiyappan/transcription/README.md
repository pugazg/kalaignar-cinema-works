# அம்மையப்பன் — canonical Tamil transcription

Controlling source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

The rendered scan controls. OCR, parsed text, film audio, subtitles, web quotations and later editions are non-canonical.

## Current first-pass progress

- canonical screenplay range: **PDF 5–109 / logical printed pp.3–107**;
- canonical pages expected: **105**;
- first-pass pages completed: **60 / 105**;
- completed range: **PDF 5–64 / logical pp.3–62**;
- current state of completed pages: **draft**;
- verified pages: **0**;
- review pages: **0**;
- open first-pass uncertain readings: **48**;
- next source page: **PDF 65 / printed p.63**;
- full visual fidelity audit: **not-started**.

PDF 5 has no visible printed folio. Its anchor therefore records `logical_printed=3` with `printed_folio=suppressed`; PDF 6 onward uses the visible printed page where present.

## First-pass storage / assembly

`index.json` is the active progress/assembly authority while the first pass is growing.

- `full-text.md` currently contains the assembled continuous draft through **PDF 14**;
- `parts/pdf-015-024.md` contains **PDF 15–24**;
- `parts/pdf-025-034.md` contains **PDF 25–34**;
- `parts/pdf-035-044.md` contains **PDF 35–44**;
- `parts/pdf-045-054.md` contains **PDF 45–54**;
- `parts/pdf-055-064.md` contains **PDF 55–64**;
- before the full PDF 5–109 first pass is declared complete, all bounded part files must be assembled into `full-text.md` in exact source order and checked for boundary loss/duplication.

This temporary part-file workflow avoids repeatedly rewriting an increasingly large canonical draft while preserving stable page provenance.

## First-pass policy

- source order only;
- exact visible headings/speaker labels/stage directions;
- no modernization or silent repair;
- uncertain old-typeface tokens remain visibly marked with `⟦reading?⟧`;
- user-reviewed scan verdicts remain locked occurrence-by-occurrence;
- no scene/dialogue/character derivative work until the whole canonical range has subsequently passed the separate fidelity audit.

## Batch 1 — PDF 5–9

Status: **draft complete for this batch**.

## Batch 2 — PDF 10–14

Status: **draft complete for this batch**.

This batch preserves the source headings `மாடம்`, `குதிரைக் கொட்டடி` and `வாள் பயிற்சிக் கூடம்`, plus page-boundary continuation of Maykainathar's speech from PDF 10 into PDF 11.

## Batch 3 — PDF 15–24

Status: **draft complete for this batch**.

Stored in `parts/pdf-015-024.md`. The batch preserves the source transitions `சுகதேவன் அறை`, `திரிசங்கு வீட்டின் கொல்லைப்புறம்`, `பலதேவர் மாளிகை` and `ஆற்றங்கரை`, plus the source-visible cross-page split in Sukhadev's line from PDF 19 (`...அதா`) to PDF 20 (`வது காதல்...`).

## Batch 4 — PDF 25–34

Status: **draft complete for this batch**.

Stored in `parts/pdf-025-034.md`. The batch preserves the source transitions `தென்றல் மாளிகை`, `பலதேவர் மாளிகை`, `குதிரைக் கொட்டடி`, `பூங்காவனம் அறை`, `திரிசங்கு வீடு` and `அஞ்சல் மனை`. Eight new glyph-sensitive/phrase readings remain visibly marked rather than guessed.

## Batch 5 — PDF 35–44

Status: **draft complete for this batch after scan reconciliation**.

Stored in `parts/pdf-035-044.md`. The batch preserves the transitions `மடாலயம்`, `அஞ்சல் மனை`, `தென்றல் மாளிகை` and `ஆற்றங்கரை சோலையோரம்`. Direct scan reconciliation restored the source-visible `தனபதி` label where the initial draft had incorrectly read `தளபதி`; five new uncertain spans remain explicitly marked.

## Batch 6 — PDF 45–54

Status: **draft complete for this batch**.

Stored in `parts/pdf-045-054.md`. The batch preserves the source transitions `தென்றல் மாளிகை`, `தோட்டம்`, `அஞ்சல் மனை` and the return to `தென்றல் மாளிகை`. Fifteen new glyph-sensitive spans remain visibly marked rather than being reconstructed from semantic expectation.

## Batch 7 — PDF 55–64

Status: **draft complete for this batch**.

Stored in `parts/pdf-055-064.md`. The batch preserves the source transitions `பழுதார் வீதி`, `திரிசங்கு வீடு`, `சுகதேவன் மாளிகை` and `பாசறை சமையல் கூடம்`. The locked intake reading `பழுதார் வீதி` is retained exactly. Nine new glyph-sensitive spans remain explicitly marked, including the quoted poetic material on PDF 64; its final marked fragment continues across the boundary into PDF 65 and must remain joined by provenance during later review.

Open first-pass readings needing later glyph-level adjudication are recorded in `../notes/textual-notes.md`. They do not block continuation of the first pass.

## Exact next activity

Continue canonical Tamil first-pass transcription at **PDF 65 / printed p.63**, in a meaningful source-order batch with the same stable anchor and uncertainty policy. Do not start scene/dialogue derivatives.
