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
- dedicated historical-glyph verification: **PDF 4–13 / 10 of 87 VERIFIED / IN PROGRESS**;
- dedicated glyph pages remaining: **77**;
- legacy prospective drafting checks do not close the dedicated glyph gate;
- final visual verification: **NOT-STARTED**;
- open uncertainty markers: **0 recorded**;
- derivatives: **BLOCKED**.

## Dedicated historical-glyph batch 1 — PDF 4–8

- all five pages were independently re-read against the controlling scan under the dedicated gate;
- every occurrence of the mandated glyph families on those pages was checked occurrence by occurrence;
- PDF 4 confirms `ளை` and `றா` families in source words including `எதிர்ப்புகளை`, `பிள்ளைதான்`, and `நூற்றாண்டு`;
- PDF 5 confirms `ணா / ளை / லை / னை`, including multiple `அண்ணா` occurrences, `எதிரிகளைப்`, `தலையெழுத்தை`, `மகனை`, and `இல்லையேல்`;
- PDF 6 required no target-family glyph correction;
- PDF 7 confirms `லை / ளை / னா / னை`, including `காலைத்தொட்டுக்`, `என்னால்`, `கட்டளை`, `குமணனாய்`, `கர்ணனாய்க்`, and `புருஷனைத்`;
- PDF 8 confirms `னை / லை / ளை`, including `மனைவி`, `கவலை`, and `விளையாடு`;
- canonical page-text glyph corrections in this batch: **0**;
- unresolved glyph holds: **0**;
- audit-only correction: the old prospective `நாணயத்தின்` → `ணா` example was withdrawn because that word does not contain the `ணா` family.

## Dedicated historical-glyph batch 2 — PDF 9–13

- all five pages were independently re-read from enlarged controlling-source pixels;
- every occurrence of the mandated glyph families was checked occurrence by occurrence;
- PDF 9 confirms `னா / ளை / லை / றா`, including `முன்னால்`, `வளைத்து`, `சிலையை`, `வேலைகளைப்`, and `வெளியேறுகிறான்`;
- PDF 10 confirms `லை / ணை / னை / றா`, including `கட்டிலை`, `கருணை`, `இன்னைக்கு`, and `தருகிறாள்`;
- PDF 11 confirms `ணை / ணா / றோ / ளை / னை`, including `இணைந்து`, `கண்ணாளா`, `மூணாவது`, `இருக்கிறோம்`, `அவளைத்`, `தலையணைக்குக்`, and `உன்னை`;
- PDF 12 confirms `னை / றோ / லை / றா / னா`, including `என்னை`, `போகிறோம்`, `நிலைதடுமாறி`, `சுக்குநூறாப்`, and `அனாதை`;
- PDF 13 confirms `னை / ளை / னா / றொ / ணா / றா`, including `பானை`, `நாளைக்கு`, `சொன்னா`, `மற்றொரு`, `கண்ணாமூச்சி`, and `விளையாடுகிறார்கள்`;
- canonical page-text glyph corrections in this batch: **0**;
- cumulative dedicated-phase canonical glyph corrections: **0**;
- unresolved glyph holds: **0**.

## Exact next activity

> **Run dedicated historical-glyph verification on PDF 14–18 as the next five-page batch. Inspect every mandated historical Tamil glyph occurrence directly against enlarged source pixels; make only source-supported glyph-identity corrections; record the evidence in `notes/historical-glyph-audit.md`; update the dedicated glyph counters to 15/87 and next batch PDF 19–23; commit/push the batch to `main`; then synchronize durable status. Do not begin final full visual verification until historical-glyph verification reaches PDF 90.**
