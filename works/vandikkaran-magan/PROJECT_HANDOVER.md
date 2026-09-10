# வண்டிக்காரன் மகன் — Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/vandikkaran-magan/`

**LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253` / first edition 1978 / image-only**. Source pixels control canonical Tamil; do not substitute web text, film audio, OCR, later editions or memory.

## Closed source authority

- PDF 4–5 — `கலைஞரின் முன்னுரை`;
- PDF 6–87 — screenplay/dialogue, printed pp.5–86;
- PDF 88–89 — film credits;
- PDF 90 — back cover;
- canonical source pages: **87/87 — PDF 4–90**;
- visual verification: **87/87 COMPLETE**;
- historical-glyph verification: **87/87 COMPLETE / 0 holds**;
- final full visual verification: **87/87 PASS / 0 final corrections**;
- open uncertainty markers: **0**.

## Structural / scene authority

The corrected source-visible scene inventory is **72/72**, after derivative QA exposed the previously omitted but already canonical PDF 10 heading `காட்சி — 4 எ.` (`4-எ`). The sequence spans base numbers 1–56, **17 suffix insertions**, and the source-combined `45-46` heading. `notes/scene-heading-audit.md` is the current mapping record.

Scene-text derivatives are **72/72 COMPLETE-VERIFIED** in `scenes/`. Boundary ownership QA is **PASS**:

- screenplay coverage: **82/82 pages — PDF 6–87**;
- gaps: **0**;
- overlaps: **0**;
- duplicate source ownership: **0**;
- joined scene-span SHA-256 equals canonical scene-body SHA-256: `84227c9855f3de942c8f1c240f9e6ddeee2d13f348fdda14b7712a81c4cfc19a`.

PDF 4–5 and PDF 88–90 are deliberately outside the scene layer. No canonical Tamil was rewritten by scene construction.

## Derivative gate state

- scene-text derivatives: **COMPLETE-VERIFIED — 72/72 / QA PASS**;
- immutable dialogue index: **COMPLETE-VERIFIED — 744 records / 38 exact labels / QA PASS**;
- delimiter distribution: **`:—` 736 / `:` 8**;
- zero-dialogue scenes: **15**;
- cross-page dialogue records: **3** — each remains one logical record with multi-page provenance;
- reviewed anomalous non-colon candidates: **16/16 excluded from dialogue starts**;
- unlabelled source blocks assigned a speaker: **0**;
- duplicate dialogue IDs / speaker-label normalizations: **0 / 0**;
- dialogue build checkpoint: `a7b80ccac2473b998b40bb05577a439fd970136b`;
- character/entity index: **COMPLETE-VERIFIED — 32 entities / 38/38 labels / 744/744 dialogue records / QA PASS**;
- character/entity types: **15 named characters / 14 roles / 3 collectives**;
- character/entity review / unresolved: **0 / 0**;
- source label variants remain immutable upstream; interpretive merges exist only in `characters/`;
- song/performance authorship gate: **READY-NEXT**;
- English translation: **BLOCKED**;
- reader/export / Reading Room: **BLOCKED**.

The three verified cross-page records are `vandikkaran-magan-s035-d006` (source scene `25`, PDF 48→49), `vandikkaran-magan-s055-d004` (source scene `42-எ`, PDF 68→69), and `vandikkaran-magan-s070-d005` (source scene `54`, PDF 85→86). The 16 non-colon preflight candidates are source-visible punctuation/verse fragments and were not promoted to dialogue. No canonical Tamil or scene file was changed by dialogue construction.

Character/entity mapping closed with **0** unmapped labels and **0** unmapped dialogue records. Source-supported mappings include `காளிங்` + `காளிங்க` → காளிங்கராயன், `சொக்` + `சொக்க` → சொக்கலிங்கம், and `ஜமீன்` + `ஜமீன்தார்` → ஜம்புலிங்க பூபதி. Possessive voice labels `கண்ணாயிரத்தின் குரல்`, `சடையன் குரல்`, and `விங்கன் குரல்` link to their named characters only in the interpretive layer. Generic roles/collectives remain categorical; `லிங்கன்` remains distinct from `விங்கன்`, and `ஜம்பு` remains distinct from `ஜம்புலிங்க பூபதி`.

## Exact next activity

> **Begin the song/performance authorship gate from the closed source, scene, dialogue and character/entity layers. Inventory source-visible song, verse and performance occurrences first; preserve exact source wording, lineation, cues and provenance; do not infer item-level lyric authorship from the film-level `பாடல்கள்: கவிஞர் வாலி` credit alone; assign authorship only where item-level evidence supports it; run whole-work occurrence/authorship coverage QA before English translation. Do not rewrite canonical Tamil, scenes, immutable dialogue records or character/entity mappings.**

