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
3. Historical-glyph verification — **10 pages per iteration from PDF 24 onward; commit/push every batch; repeat through PDF 90.**
4. Final visual verification — **full-work final source pass.**

Do not interleave phases.

## Historical-glyph families

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

No global replacement; inspect source pixels occurrence by occurrence.

## Durable checkpoint

- intake: **COMPLETE**;
- structural mapping / scene-heading audit: **COMPLETE-VERIFIED / 71 headings**;
- first-pass transcription: **COMPLETE — PDF 4–90 / 87 of 87**;
- visual verification: **COMPLETE — PDF 4–90 / 87 of 87 VERIFIED**;
- visually verified contiguous range: **PDF 4–90**;
- draft pages: **0**;
- dedicated historical-glyph verification: **PDF 4–33 / 30 of 87 VERIFIED / IN PROGRESS**;
- dedicated glyph pages remaining: **57**;
- cumulative canonical glyph corrections: **0**;
- unresolved glyph holds: **0**;
- final visual verification: **NOT-STARTED**;
- open uncertainty markers: **0 recorded**;
- derivatives: **BLOCKED**.

## Dedicated historical-glyph batch 5 — PDF 24–33

- first user-authorized **10-page** dedicated glyph iteration;
- all ten pages were independently re-read against the controlling scan under the dedicated gate;
- every occurrence of the mandated glyph families was checked occurrence by occurrence;
- representative source confirmations include `காலையிலே`, `பரவாயில்லை`, `மனுஷனைக்`, `வயசானவனு`, `கண்ணாயிரம்`, `கண்ணைத்`, `என்னைப்பன்`, `தலைமயிரைப்`, `என்னையா`, `அவனைத்தடுத்து`, `வயசான`, `காலை`, `குதிரைகளைப்`, `உன்னையும்`, `இன்னொரு`, `நொண்டியபடியே`, `இன்னைக்கு`, `அவனைப்பிடிச்சு`, `குடிகாரனை`, `பிள்ளை`, `தகப்பனை`, and repeated `பச்சிலை` forms;
- canonical page-text glyph corrections in this batch: **0**;
- cumulative canonical glyph corrections in the dedicated phase: **0**;
- unresolved glyph holds: **0**.

## Exact next activity

> **Run dedicated historical-glyph verification on PDF 34–43 as the next ten-page batch. Inspect every mandated historical Tamil glyph occurrence directly against enlarged source pixels; make only source-supported glyph-identity corrections; record the evidence in `notes/historical-glyph-audit.md`; update the dedicated glyph counters to 40/87 and next batch PDF 44–53; commit/push the batch to `main`; then synchronize durable status. Do not begin final full visual verification until historical-glyph verification reaches PDF 90.**
