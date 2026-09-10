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
- dedicated historical-glyph verification: **0 / 87 / NOT-STARTED**;
- legacy prospective drafting checks do not close the dedicated glyph gate;
- final visual verification: **NOT-STARTED**;
- open uncertainty markers: **0 recorded**;
- derivatives: **BLOCKED**.

## Final visual-verification closure — PDF 84–90

- PDF 84–88 was completed as the final required five-page batch before the remainder;
- PDF 89–90 was completed as the final two-page remainder batch;
- PDF 84 restores `மர்மங்களே`, `உத்தமர்னு`, `எத்தனையோ`, and `இறுக மூடிக்கிடந்த`;
- PDF 85 restores source `காட்சி - 54` and `பேயுருவில்`;
- PDF 86 restores `தணியுமட்டும்`, `சூழ்கிறார்கள்`, source `காட்சி - 55`, `முறைதவறி`, and `கள்ளக் கடத்தல்`;
- PDF 87 restores `புனிதர்-புண்ணியர்-உத்தமர்-யோகியர்னு`, `ஏன் தயக்கம்`, `காளையைக் கட்டவிழ்த்து விடவே`, and source `காட்சி - 56`;
- PDF 88–89 film-credit matter was verified directly from the scan, including `இயக்குநர்` and the source-visible technical/background-singer credits;
- PDF 90 visible back-cover text was verified without reconstructing text hidden by the physical label/scan obstruction;
- all 87 scoped page records are now `visual-verified`.

## Exact next activity

> **Begin the dedicated historical-glyph phase with PDF 4–8 as one five-page batch. Inspect every mandated historical Tamil glyph occurrence directly against enlarged source pixels; make only source-supported glyph-identity corrections; record evidence in `notes/historical-glyph-audit.md`; update the dedicated glyph counters to 5/87 and next batch PDF 9–13; commit/push to `main`; then synchronize durable status. Do not begin final full visual verification until historical-glyph verification reaches PDF 90.**
