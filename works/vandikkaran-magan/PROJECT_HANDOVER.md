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

Main screenplay pagination: **printed = PDF − 1**. `notes/scene-heading-audit.md` records **71 observed scene-heading occurrences**; preserve source heading punctuation/spacing, suffix insertions, the combined `45-46` heading, multiple scene starts on one page, and internal location captions without normalization.

## Mandatory user-directed phase order

1. First-pass transcription — **5 pages per iteration; commit/push every batch; repeat through PDF 90.**
2. Visual verification — **5 pages per iteration; commit/push every batch; repeat through PDF 90.**
3. Historical-glyph verification — **15 pages per iteration from PDF 34 onward; final remainder may be shorter; commit/push every batch; repeat through PDF 90.**
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
- dedicated historical-glyph verification: **PDF 4–78 / 75 of 87 VERIFIED / IN PROGRESS**;
- dedicated glyph pages remaining: **12**;
- active dedicated glyph batch size: **15 source pages**;
- cumulative canonical glyph corrections: **0**;
- unresolved glyph holds: **0**;
- final visual verification: **NOT-STARTED**;
- open uncertainty markers: **0 recorded**;
- derivatives: **BLOCKED**.

## Dedicated historical-glyph batch 8 — PDF 64–78

- all fifteen pages were independently re-read against the controlling scan under the dedicated gate;
- every occurrence of the mandated glyph families was checked occurrence by occurrence;
- representative source confirmations include `மாப்பிள்ளை`, `கிளிஞ்சலைக்`, `உன்னை`, `ஆணையிட்டுச்`, `கலைச்சுக்`, `கண்ணாயிரம்`, `பெண்ணைத்`, `பின்னையிட்ட`, `அன்னையிட்ட`, `சொன்னால்`, `கல்யாணம்`, `காவலனைத்`, `திருவிளையாடலைப்`, `கருணை`, `மணலைக்`, `சாய்கிறார்`, `மாப்பிள்ளே`, `வயிற்றுப்பிள்ளையா`, `வேலை`, `கண்ணைக்`, `அவளைப்`, `காளை`, `சொன்னா`, `கண்ணைத்`, `அத்தனைக்கும்`, `ஆலையில்`, `யானைத்`, `பேரப்பிள்ளே`, `காளையைப்`, `நாளைக்கு`, `உங்களையா`, `இல்லையே`, `உன்னையும்`, and `மனைவிக்கு`;
- canonical page-text glyph corrections in this batch: **0**;
- cumulative canonical glyph corrections in the dedicated phase: **0**;
- unresolved glyph holds: **0**.

## Exact next activity

> **Run dedicated historical-glyph verification on PDF 79–90 as the final twelve-page remainder. Inspect every mandated historical Tamil glyph occurrence directly against enlarged source pixels; make only source-supported glyph-identity corrections; record the evidence in `notes/historical-glyph-audit.md`; update the dedicated glyph counters to 87/87 and close the historical-glyph phase; commit/push the remainder to `main`; then synchronize durable status and transition to final full visual verification.**
