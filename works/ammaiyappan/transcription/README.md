# அம்மையப்பன் — canonical Tamil transcription

Controlling source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

The rendered scan controls. OCR, parsed text, film audio, subtitles, web quotations and later editions are non-canonical.

## Current first-pass progress

- canonical screenplay range: **PDF 5–109 / logical printed pp.3–107**;
- canonical pages expected: **105**;
- first-pass pages completed: **100 / 105**;
- completed range: **PDF 5–104 / logical pp.3–102**;
- current state of completed pages: **draft**;
- verified pages: **0**;
- review pages: **0**;
- open first-pass uncertain readings: **114**;
- next source page: **PDF 105 / printed p.103**;
- full visual fidelity audit: **not-started**.

PDF 5 has no visible printed folio. Its anchor therefore records `logical_printed=3` with `printed_folio=suppressed`; PDF 6 onward uses the visible printed page where present.

## First-pass storage / assembly

`index.json` is the active progress/assembly authority while the first pass is growing.

- `full-text.md` currently contains the assembled continuous draft through **PDF 14**;
- bounded parts contain **PDF 15–104** in consecutive source-order batches;
- the newest part is `parts/pdf-095-104.md`;
- `parts/pdf-065-074.md` remains explicitly `draft-high-uncertainty` in the index;
- before the full PDF 5–109 first pass is declared complete, every bounded part must be assembled into `full-text.md` in exact source order and checked for boundary loss/duplication.

This temporary part-file workflow avoids repeatedly rewriting an increasingly large canonical draft while preserving stable page provenance.

## First-pass policy

- source order only;
- exact visible headings/speaker labels/stage directions where secure;
- no modernization or silent repair;
- uncertain old-typeface tokens remain visibly marked with `⟦reading?⟧` or an explicitly unresolved scan-backed span;
- user-reviewed scan verdicts remain locked occurrence-by-occurrence;
- no scene/dialogue/character derivative work until the whole canonical range has subsequently passed the separate fidelity audit.

## Batch status

- Batch 1 — PDF 5–9: draft complete.
- Batch 2 — PDF 10–14: draft complete.
- Batch 3 — PDF 15–24: draft complete; stored in `parts/pdf-015-024.md`.
- Batch 4 — PDF 25–34: draft complete; stored in `parts/pdf-025-034.md`.
- Batch 5 — PDF 35–44: draft complete after direct scan reconciliation; `தனபதி` restored where initially misread as `தளபதி`.
- Batch 6 — PDF 45–54: draft complete.
- Batch 7 — PDF 55–64: draft complete; preserves locked `பழுதார் வீதி` and the PDF 64→65 quoted-poetry boundary.
- Batch 8 — PDF 65–74: coverage complete, **high uncertainty**; 39 batch markers.
- Batch 9 — PDF 75–84: draft complete; 10 batch markers.
- Batch 10 — PDF 85–94: draft complete; 10 batch markers; preserves source-visible transition sequence beyond the narrower intake inventory.
- Batch 11 — PDF 95–104: draft complete; stored in `parts/pdf-095-104.md`; 7 batch markers numbered **108–114** in `../notes/textual-notes-pdf-095-104.md`.

Batch 11 includes the source transitions `பாழ் மண்டபம்`, `வேங்கை நாட்டு அவைக்கூடம்`, `பூங்காவனம் அறை`, `முத்தனின் தோழர்கள் பேசிக் கொண்டிருத்தல்`, `சுமதி வீடு`, and `சிறைச்சாலை`. It preserves the long source-visible political/social denunciation passages without silent normalization. **PDF 104 ends inside Muthan's speech and PDF 105 visibly continues that same speech.**

Open first-pass readings do not block continuation of the first pass, but they do block any claim of verified Tamil until the separate full rendered-scan fidelity audit.

## Exact next activity

Complete the **final first-pass batch PDF 105–109 / printed pp.103–107**, beginning with the PDF 104→105 continuation and preserving the locked PDF 107 / printed p.105 heading `தூக்குமேடை`. Then assemble all bounded parts into `full-text.md` in exact source order and run boundary loss/duplication QA before declaring the canonical first pass closed. Do not start scene/dialogue derivatives or the fidelity audit before that assembly checkpoint.
