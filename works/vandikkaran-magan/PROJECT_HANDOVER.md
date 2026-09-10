# வண்டிக்காரன் மகன் — Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/vandikkaran-magan/`

**LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf`

- 90 PDF pages;
- 26,391,039 bytes;
- SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`;
- image-only; source pixels are authority.

Use only the attached controlling PDF for source verification unless the user explicitly requests an external comparison.

## Verified source structure

- PDF 1 — front cover;
- PDF 2 — title/credits;
- PDF 3 — edition/price/printer;
- PDF 4–5 — `கலைஞரின் முன்னுரை`;
- PDF 6–87 — screenplay/dialogue, printed pp.5–86;
- PDF 88–89 — film credits;
- PDF 90 — back cover.

Main screenplay pagination: **printed = PDF − 1**.

`notes/scene-heading-audit.md` records **71 observed scene-heading occurrences**. Preserve suffix insertions, source-specific heading punctuation/spacing, the combined `45-46` heading, multiple scene starts on one page, and internal location captions without normalization.

## Mandatory user-directed phase order

1. First-pass transcription — **5 pages per iteration; commit/push every batch; repeat through PDF 90.**
2. Visual verification — **5 pages per iteration; commit/push every batch; repeat through PDF 90.**
3. Historical-glyph verification — **5 pages per iteration; commit/push every batch; repeat through PDF 90.**
4. Final visual verification — **full-work final source pass.**

Do not interleave phases.

## Historical-glyph families for the later dedicated phase

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

No global replacement; inspect source pixels occurrence by occurrence.

## Durable checkpoint

- intake: **COMPLETE**;
- structural mapping / scene-heading audit: **COMPLETE-VERIFIED / 71 headings**;
- first-pass transcription: **COMPLETE — PDF 4–90 / 87 of 87**;
- visual verification: **PDF 4–83 / 80 of 87 COMPLETE-VERIFIED**;
- visually verified contiguous range: **PDF 4–83**;
- pages still awaiting visual verification: **7**;
- historical-glyph verification: **0 / NOT-STARTED** under current phase order;
- legacy prospective glyph checks on PDF 4–13: **10 pages** only; these do not close the later glyph phase;
- final visual verification: **NOT-STARTED**;
- open uncertainty markers: **0 recorded**;
- derivatives: **BLOCKED**.

## Latest visual-verification batch — PDF 79–83

- all five pages were re-read directly from enlarged source pixels;
- PDF 79 restores `ஏண்டா`, `கண்ணைத் திறக்கிறது ரொம்பகஷ்டம்`, `ஆனா ஒரு நாளுக்குத் திறக்கத்தான் போகிறேன்`, `இவ்வளவுநாளா`, and `ஜம்புலிங்க`;
- PDF 80 restores `ஊரே வளர்ந்துச்சு`, `உங்களைப் போல`, and `உங்களைச்`;
- PDF 81 restores `யாருக்கென்று`, `ஓட்டைக் குடிசைப்`, source heading dash forms for `53 / 53 எ / 53 பி / 53 சி`, `கட்டளைப்படி`, and `அழகி ஒன்று`;
- PDF 82 preserves the source-visible song/performance and fire-sequence text;
- PDF 83 restores `அரிவாள் மனைக்கட்டையாலடிக்கப்போக`, `ஆனபிறகு`, and `ஏற்பட்டதில்லே`, with source `53 டி` preserved;
- all five records are now `visual-verified`;
- dedicated historical-glyph verification remains NOT-STARTED.

## Exact next activity

> **Visually verify PDF 84–88 directly against the attached controlling scan as one five-page batch. Correct every source discrepancy without normalization or guesswork, mark all five page records `visual-verified`, update `transcription/index.json` to 85/87, commit/push the batch to `main`, synchronize durable status, and continue with PDF 89–90. Do not begin dedicated historical-glyph verification until the visual phase reaches PDF 90.**
