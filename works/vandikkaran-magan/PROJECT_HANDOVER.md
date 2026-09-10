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
- visual verification: **PDF 4–63 / 60 of 87 COMPLETE-VERIFIED**;
- visually verified contiguous range: **PDF 4–63**;
- pages still awaiting visual verification: **27**;
- historical-glyph verification: **0 / NOT-STARTED** under current phase order;
- legacy prospective glyph checks on PDF 4–13: **10 pages** only; these do not close the later glyph phase;
- final visual verification: **NOT-STARTED**;
- open uncertainty markers: **0 recorded**;
- derivatives: **BLOCKED**.

## Latest visual-verification batch — PDF 59–63

- all five pages were re-read directly from enlarged source pixels;
- PDF 59 restores `சேலைத் தலைப்பை` and source `மாமக் களஞ்சியத்தில்`;
- PDF 60 restores `கனவன் கட்டளையாம்மா?` and source-connected `ஆடு!—நல்ல`;
- PDF 61 restores `தூங்கி யிருந்தால்`, `சிறு நரி ஆட்டும் வாலே!`, `வேணுமோ`, `வச்சிகிட்டு`, and `நல்லாத் தின்னுட்டு`;
- PDF 62 restores `என்னமாப்பிள்ளை`, `வில்லாவளைக்கப்`, `வெற்றிபெறத் தான்`, `என்றும்போல்`, and `கடையேழு வள்ளல்களே`;
- PDF 63 restores `ஜால்ராப் புலவர்`, `மறந்துட்டீங்க?`, `மாரோடு மார்`, `பொண்ணும்மா`, and stage-direction `பலரும்`;
- scene starts in the batch are `33-எ`, `34`, `35`, `36`, `37`, and `38`;
- all five records are now `visual-verified`;
- dedicated historical-glyph verification remains NOT-STARTED.

## Exact next activity

> **Visually verify PDF 64–68 directly against the attached controlling scan as one five-page batch. Correct every source discrepancy without normalization or guesswork, mark all five page records `visual-verified`, update `transcription/index.json` to 65/87, commit/push the batch to `main`, synchronize durable status, and continue with PDF 69–73. Do not begin dedicated historical-glyph verification until the visual phase reaches PDF 90.**
