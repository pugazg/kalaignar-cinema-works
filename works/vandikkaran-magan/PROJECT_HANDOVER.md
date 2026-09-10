# வண்டிக்காரன் மகன் — Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/vandikkaran-magan/`

**LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf`

- PDF pages: **90**;
- bytes: **26,391,039**;
- SHA-256: `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`;
- image-only first-edition scan; rendered source pixels control canonical Tamil.

Use only the controlling scan for source-text adjudication unless the user explicitly asks for external comparison.

## Verified source structure

- PDF 1 — front cover;
- PDF 2 — title / writer / publisher credits;
- PDF 3 — edition / price / printer;
- PDF 4–5 — `கலைஞரின் முன்னுரை`;
- PDF 6–87 — screenplay/dialogue, printed pp.5–86;
- PDF 88–89 — film credits;
- PDF 90 — back cover.

For the screenplay range, **printed page = PDF page − 1**.

`notes/scene-heading-audit.md` records **71 observed source scene-heading occurrences**. Preserve all printed irregularities, suffix insertions, the combined `45-46` heading, multiple scene starts on a page, location captions and exact heading punctuation/spacing.

Observed identifying sequence:

`1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10-எ, 11, 12, 13, 14, 14-எ, 15, 16, 16-எ, 17, 18, 19, 20, 20-எ, 21, 22, 22-எ, 23, 24, 24-எ, 24-பி, 24-சி, 24-டி, 25, 26, 27, 28, 29, 29-எ, 30, 31, 32, 33, 33-எ, 34, 35, 36, 37, 38, 39, 40, 41, 42, 42-எ, 43, 44, 45-46, 47, 48, 49, 50, 51, 52, 53, 53-எ, 53-பி, 53-சி, 53-டி, 54, 55, 56`.

## Source gates — CLOSED

- source intake: **COMPLETE**;
- structural mapping / scene-heading audit: **COMPLETE-VERIFIED / 71 headings**;
- canonical first pass: **COMPLETE — PDF 4–90 / 87 of 87**;
- visual verification: **COMPLETE — PDF 4–90 / 87 of 87**;
- dedicated historical-glyph verification: **COMPLETE — PDF 4–90 / 87 of 87**;
- cumulative canonical glyph corrections: **0**;
- unresolved glyph holds: **0**;
- final full visual verification: **COMPLETE / PASS — PDF 4–90 / 87 of 87**;
- final-pass canonical corrections: **0**;
- draft pages / open uncertainty markers: **0 / 0**.

Final source-pass evidence is recorded in `notes/final-visual-audit.md`. Canonical Tamil is now a closed upstream authority for derivative construction.

## Historical Tamil glyph rule

The dedicated gate is closed, but its rule survives any later source correction:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Never global-replace. A closed glyph verdict can be reopened only by direct contradictory evidence from the controlling scan.

## Derivative gate state

- scene-text derivatives: **READY-NEXT / NOT-STARTED**;
- dialogue index: **BLOCKED until scene layer + boundary QA close**;
- character/entity index: **BLOCKED**;
- song/performance authorship gate: **BLOCKED**;
- English translation: **BLOCKED**;
- reader/export / Reading Room: **BLOCKED**.

## Exact next activity

> **Build the scene-text derivative layer for the complete verified screenplay PDF 6–87 using all 71 observed/canonical source scene dispositions. Create `scenes/index.json` plus one scene file per observed scene disposition; preserve exact source headings, location captions, source order and page anchors; assemble cross-page scenes without duplicate ownership; keep `★` separators structural; do not create scenes from PDF 4–5 or PDF 88–90; and run whole-work boundary-ownership QA proving 0 gaps / 0 overlaps before closing the scene gate. Commit/push the scene layer, then synchronize work-local and repository-wide mirrors.**
