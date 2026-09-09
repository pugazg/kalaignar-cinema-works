# வண்டிக்காரன் மகன்

Source-led archival workspace for the 1978 first-edition dialogue/screenplay booklet **`வண்டிக்காரன் மகன்`**.

## Source authority

Controlling source: `TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf`

- source/archive identifier: `TVA_BOK_0062961`;
- PDF pages: **90**;
- byte size: **26,391,039**;
- SHA-256: `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`;
- image-only scan; source pixels are canonical authority.

Do not silently modernize spelling, punctuation, speaker labels, scene numbering, performance structures, or historical Tamil character identity.

## Verified source boundaries

| PDF pages | Disposition |
|---|---|
| 1 | front cover |
| 2 | title / writer / publisher credits |
| 3 | edition / price / printer |
| 4–5 | `கலைஞரின் முன்னுரை` |
| 6–87 | screenplay/dialogue, printed pp.5–86 |
| 88–89 | film credits |
| 90 | back cover |

For PDF 6–87, **printed page = PDF page − 1**.

## Structural mapping checkpoint

The source has **71 observed scene-heading occurrences**. Preserve inserted suffix headings, the combined `45-46` heading, multiple scene starts on one source page, and internal location captions exactly as printed. The source-visible `53-டி` heading starts at PDF 83 / printed p.82 and corrects the earlier 70-heading inventory. See `mapping.md` and `notes/scene-heading-audit.md`.

## Historical Tamil glyph rule

The later dedicated historical-glyph phase must inspect occurrence by occurrence:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Use `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`. Never global-replace. Source pixels control.

## User-directed processing sequence

1. **First-pass transcription:** 5 PDF pages → commit/push → repeat through PDF 90.
2. **Visual verification:** 5 PDF pages → commit/push → repeat through PDF 90.
3. **Historical-glyph verification:** 5 PDF pages → commit/push → repeat through PDF 90.
4. **Final visual verification:** full-work final source check.

Do not interleave phases.

## Current status

- source intake: **COMPLETE**;
- structural mapping / scene-heading audit: **COMPLETE-VERIFIED / 71 observed headings**;
- first-pass transcription: **COMPLETE — PDF 4–90 / 87 of 87 scoped pages**;
- visual verification: **IN PROGRESS — PDF 4–18 / 15 of 87 VERIFIED**;
- remaining visual-verification pages: **72**;
- historical-glyph verification: **NOT-STARTED** under the mandatory phase order;
- legacy prospective glyph checks on PDF 4–13: **10 pages** only; these do not close the later dedicated glyph phase;
- final visual verification: **NOT-STARTED**;
- open uncertainty markers: **0 recorded**;
- structured derivatives / English / reader work: **BLOCKED**.

## Latest five-page visual batch

- PDF **14–18 / printed 13–17** visually verified against the controlling scan;
- the batch required substantial correction of OCR-like first-pass substitutions rather than status-only review;
- PDF 16 includes scene `8`; PDF 17 scene `9`; PDF 18 scene `10` and the source-visible `ஒருநாடகம்` song block;
- all five page records are now `visual-verified`.

## Exact next activity

> **Visually verify PDF 19–23 against the controlling scan as the next five-page batch; correct source discrepancies without silent normalization; mark those five records `visual-verified`; update `transcription/index.json`; commit/push the batch; then continue in five-page visual batches through PDF 90. Do not begin dedicated historical-glyph verification yet.**
