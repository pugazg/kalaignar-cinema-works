# வண்டிக்காரன் மகன் — Reading Room integration payload QA

**Status:** PASS  
**Site application:** not-applied  
**Source scan SHA-256:** `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`  
**Reader authority:** `works/vandikkaran-magan/editions/en/reader-edition.json`

## Verified payload checks

- source-numbered screenplay navigation: **72/72 scenes** in verified printed-heading order;
- Tamil scene texts: **72/72**, generated from verified scene derivatives without provenance comments;
- verified English units: **1,181/1,181 exactly once**;
- unit kinds: **800 dialogue / 316 stage-direction / 10 performance-cue / 53 song / 2 written-text**;
- immutable labelled dialogue links: **773/773 exactly once**;
- source-unlabelled spoken units: **27/27**, retained with no invented speaker/dialogue ID;
- cross-page English units: **58/58**, preserving all PDF/printed page provenance;
- verified song/performance identities: **9/9**, represented across **66** linked English units;
- performance source forms: **6 bounded Tamil bodies + 3 cue-only/non-lyric records**;
- item-level lyric authorship: **0 source-attributed / 6 unresolved / 3 not-applicable**;
- PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only and is not promoted item-by-item;
- source page provenance remains within screenplay PDF **6–87** / printed **5–86**, with `printed = PDF - 1`;
- exact source scene IDs, including suffixes and combined `45-46`, are preserved;
- structural `★` separators are not manufactured into English prose;
- editorial placeholder tokens in payload source/translation text: **0**;
- closed Tamil/dialogue/character/song/translation/reader evidence modified by payload generation: **0**.

## Output

- `reading-room.json` — SHA-256 `1d1b611c1261eac75577c8c0499123c260406005f26448bb9aac5f6df22339ba` — **1,610,402 bytes**.

This payload is a deterministic data derivative for the separate Kalaignar Digital Library / Reading Room implementation. The public-site repository has **not** been modified or deployed by this step.
