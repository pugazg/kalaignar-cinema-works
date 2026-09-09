# நாம்

Source-first archival workspace for the Kalaignar cinema work **நாம்**.

## Current checkpoint

- source intake: **complete**;
- structural mapping: **verified**;
- canonical Tamil transcription: **67/67 COMPLETE-VERIFIED**;
- canonical Tamil verified pages: **67/67**;
- visual fidelity audit: **67/67 PASS / COMPLETE**;
- historical-Tamil-glyph audit: **67/67 final-verified / COMPLETE**;
- open source uncertainty markers: **0**;
- scene derivatives: **45/45 COMPLETE-VERIFIED; boundary ownership QA PASS**;
- dialogue index: **590 immutable records / COMPLETE-VERIFIED / QA PASS**;
- character/entity index: **28 entities / 45/45 labels / 590/590 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance/authorship gate: **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED / QA PASS; 1 source-attributed + 6 unresolved item-level authorships**;
- English translation: **45/45 COMPLETE-VERIFIED / 797 units / whole-work QA PASS**; reader/export: **COMPLETE-VERIFIED / QA PASS**; Reading Room payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS / site not-applied**.

Current transcription index: `transcription/index.json`  
Completed batches: `transcription/parts/pdf-005-009.md`, `transcription/parts/pdf-010-014.md`, `transcription/parts/pdf-015-019.md`, `transcription/parts/pdf-020-024.md`, `transcription/parts/pdf-025-029.md`, `transcription/parts/pdf-030-034.md`, `transcription/parts/pdf-035-039.md`, `transcription/parts/pdf-040-044.md`, `transcription/parts/pdf-045-049.md`, `transcription/parts/pdf-050-054.md`, `transcription/parts/pdf-055-059.md`, `transcription/parts/pdf-060-064.md`, `transcription/parts/pdf-065-069.md`, `transcription/parts/pdf-070-071.md`  
Current textual notes: `notes/textual-notes-pdf-070-071.md`

## Controlling source

- file: `TVA_BOK_0064201_நாம்.pdf`;
- source identifier: `TVA_BOK_0064201`;
- PDF pages: **72**;
- byte size: **115,948,588**;
- SHA-256: `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`;
- text layer: **image-only**;
- visible title: **நாம்**;
- visible author: **மு. கருணாநிதி**.

The rendered scan is the controlling textual authority. The source PDF itself is not stored in this repository.


## Scene-text derivative checkpoint

- source-numbered scenes: **45/45 COMPLETE-VERIFIED**;
- exact sequence: **காட்சி 1–45**;
- canonical PDF representation: **67/67 pages, PDF 5–71**;
- boundary ownership QA: **PASS — 0 gaps / 0 overlaps**;
- scene index: `scenes/index.json`;
- QA: `notes/scene-boundary-ownership-qa.md`;
- canonical scene-region / joined scene-span SHA-256: `787695af1e3d5c3dae28085b76558df9efae73fe239c39e802989442fa593146` / `787695af1e3d5c3dae28085b76558df9efae73fe239c39e802989442fa593146` — **MATCH**;
- canonical Tamil changed by derivative generation: **0**.

**Next:** No required repository-internal processing remains for நாம். Reader/export and the source-linked Reading Room payload are complete-verified with QA PASS. Keep Tamil, scene, dialogue, character, song-source and English records closed. Apply `works/naam/integrations/reading-room/reading-room.json` in the separate Kalaignar Digital Library / Reading Room implementation repository only when that repository is explicitly authorized for modification; before applying it, fetch that repository's live state and use a fail-closed importer pinned to this verified payload/manifest. Site application remains not-applied here. Do not create a PDF, EPUB or other publication package unless separately requested.

## Immutable dialogue checkpoint

- source scenes represented: **45/45**;
- immutable explicit dialogue records: **590**;
- distinct exact speaker labels: **45**;
- multi-page dialogue records: **8**;
- source-unlabelled speaker inference: **0**;
- QA: `notes/dialogue-index-qa.json` — **PASS**;
- dialogue index: `dialogues/index.json`;
- canonical Tamil / scene text modified by this phase: **0 / 0**.

**Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.

## Character/entity closure checkpoint

- immutable dialogue authority: **590 records / QA PASS**;
- exact source labels mapped: **45/45**;
- dialogue records mapped exactly once: **590/590**;
- entities: **28** — 14 named / 13 role / 1 collective;
- unresolved labels / records: **0 / 0**;
- source anomaly `உன்மீனு`: preserved upstream, mapped to `மீனு` only here;
- QA: `notes/character-entity-qa.json` — **PASS**;
- upstream text/dialogue modifications: **0**.

**Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.

## Song / performance / authorship closure checkpoint

- mapped source-visible performance structures: **7/7 retained — reconciled**;
- clearly bounded Tamil performance derivatives: **7**;
- item-level authorship resolved from source: **1** — `ஆயிரம் தெய்வங்கள்` → `பாரதியார்` (PDF 4 credit; body PDF 16);
- unresolved item-level authorship: **6**;
- broad PDF 4 `கதை, வசனம், பாடல்... மு. கருணாநிதி` credit is preserved but not promoted to unsupported item-level attributions;
- QA: `notes/song-performance-qa.json` — **PASS**;
- upstream canonical / scene / dialogue / character modifications: **0 / 0 / 0 / 0**.

**Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.

## Song/performance reconciliation before English

- initial gate: 6 records;
- pre-English marker sweep: **45/45 scenes scanned**;
- omitted explicit performance restored: **காட்சி 1 / PDF 6–7 / `(பாட்டு)` → `naam-perf-007`**;
- reconciled source-visible performance coverage: **7/7**;
- authorship: **1 source-attributed / 6 unresolved item-level**;
- existing `naam-perf-001`–`006` IDs preserved unchanged;
- upstream Tamil / scene / dialogue / character modifications: **0**.

## English translation pilot checkpoint

- source scene: **1/45 VERIFIED**;
- translation units: **21**;
- immutable dialogue links: **14/14 exactly once**;
- narrative / stage-direction units: **4 / 1**;
- performance cue / full-song units: **1 / 1**;
- translated performance occurrence: **`naam-perf-007`**;
- Tamil→English song role/line mappings: **23/23**;
- cross-page English units: **1** (`naam-en-s001-u021`, PDF 6–7);
- inferred source-unlabelled speakers: **0**;
- authorship upgrades: **0**;
- upstream source-layer modifications caused by English: **0**.

**Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.

## English scenes 2–5 checkpoint

- cumulative verified source scenes: **5/45**;
- cumulative verified English units: **131**;
- cumulative immutable dialogue links: **99**;
- batch scenes 2–5: **110 units / 85/85 immutable dialogue links**;
- source-unlabelled speech: **1 unit, deliberately unassigned**;
- performance records in batch: **0**; cumulative translated performance records: **1/7**;
- song mappings remain **23/23** from scene 1;
- upstream source-layer modifications caused by this batch: **0**.

**Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.

## Source-visible publication / credit evidence

- PDF 1 prints the title, `மு. கருணாநிதி`, price `0-8-0`, and a physically damaged publication line;
- PDF 3 gives the fuller source-visible organization line **`ஆசீர்வாதபுரம் ஆதிதிராவிட நல உரிமைச் சங்கத்தார்`**;
- PDF 4 prints the broad credit **`கதை, வசனம், பாடல்... மு. கருணாநிதி`** and separately credits **`பாட்டு 'ஆயிரம் தெய்வங்கள்'—பாரதியார்.`**;
- PDF 4 also prints `தயாரிப்பாளர் ஜூபிடர் & மேகலா பிக்சர்ஸ்`;
- PDF 72 prints **`அச்சிட்டது ஆதி பிரஸ், சென்னை—12.`**;
- no explicit publication year or edition statement has been located in this scan, so none is inferred.

The Bharathiyar item-level credit is a source-specific exception and must survive the later song/authorship gate. The broad Kalaignar `பாடல்` credit must not be used to overwrite it.

## Source structure

- front matter: **PDF 1–4**;
- screenplay/dialogue text: **PDF 5–71** — **67 pages**;
- back matter / printer imprint: **PDF 72**;
- visible printed numerals: **6–71** on PDF 6–71;
- PDF 5 opens the screenplay but no printed page numeral is visibly established there; do not manufacture one in canonical anchors;
- source-numbered scene headings: **45**, sequential **காட்சி 1–45**;
- numbering gaps / repeats / out-of-order headings observed: **0 / 0 / 0**;
- full scene-start map: `mapping.md`.

Handwritten pencil numbers and marks near upper-right margins are later annotations and are not printed pagination or canonical text.

## Canonical Tamil first-pass checkpoint

PDF **5–71 / 67 of 67 pages** is transcribed and **67/67 dual-gate COMPLETE-VERIFIED**. The three former source-obscuration holds on PDF 5, PDF 10 and PDF 24 were closed by recorded user manual controlling-scan verdicts; open source uncertainty is now **0**.

Safeguards:

- PDF 5 has no invented printed-page number;
- exact speaker labels, stage directions, source colloquial forms, punctuation and verse lineation are retained;
- PDF 6 `அவளை` is treated as a historical-`ளை` glyph-decoding case;
- PDF 6 `சூரியனால்` was checked against the historical `னா` family;
- PDF 11 `கண்ணாடிச்` is a positive `ணா`-family first-pass case;
- scan-backed reconciliation of PDF 15–19 corrected `எல்லோருக்கும்`, `உருண்டோடிடுமே`, `அவன் கை வலி`, `என்னே`, and `என் மருமகளும்`;
- PDF 21 `நீதானா...?` is a historical-`னா` decoding: the old glyph can resemble `நீதானு...?`, but the source-supported Unicode identity is `நீதானா...?`;
- PDF 25–29 final audit corrected `உங்களை`, `கடமைசபதம் எடுத்திருக்கிறேன்`, `லக்ஷ்மி`, `ஹல்லோ`, and `(ஆரஞ்சுப்பழமும் வைக்கப்படுகிறது)` from direct pixels;
- PDF 26 `அலைந்தான்` is source-backed `லை`;
- PDF 27 `சாணைக்கல்லிலே` / `சாணைக்கல்லை` are checked historical-`ணை` cases;
- PDF 28 `காதலை நான்` is checked against historical `லை` / `னா` forms;
- PDF 29 `அணா` is a positive historical-`ணா` case;
- PDF 31 `தவறான` is checked historical `றா`; PDF 31 `இவனை` and PDF 32 `அவனை` / `ஜமீனையே` are checked historical `னை`;
- PDF 34 `அவளை` is checked historical `ளை`; PDF 34 `பஞ்சணை` is checked historical `ணை`;
- PDF 35 `நானம்மா` is checked historical `னா`; PDF 37 `உன்னை` is checked historical `னை`; PDF 39 `எமனோடு` is checked historical `னோ`;
- PDF 40/41/43/44 `உன்னை` / `குமரனை` are checked historical `னை`; PDF 42 `மண்ணைவாரிப்` is checked historical `ணை`;
- PDF 45 `கொன்றாய்` is checked historical `றா`; PDF 48–49 `என்னை` is checked historical `னை`; PDF 49 `மணாளன்` is checked historical `ணா`; PDF 49 `கேளேனோ` is checked historical `னோ`;
- PDF 51 `என்னை` is checked historical `னை`; PDF 52/54 `மலையங்களா` and PDF 52–53 `அண்ணுமலை` are checked historical `லை`;
- PDF 50 completes the mapped scene-31 lyrical witness from the booklet only; PDF 52 opens `காட்சி-32`, and PDF 54 opens `காட்சி 33`;
- PDF 65–69 `மனிதனாகுகிறதும்` / `மனிதனாகுவதும்`, `காலணா`, `காலை`, `மனைவி`, `உயிலை`, and `உன்னை` were checked against occurrence-specific historical families;
- PDF 65 opens `காட்சி 40` and `காட்சி 41`; PDF 67 opens `காட்சி 42` and `காட்சி 43`; PDF 68 opens `காட்சி-44` and `காட்சி-45`; PDF 69 ends mid-Kumaran dialogue and PDF 70 must continue the same utterance;
- PDF 65–69 adds no new distinct song/lyric/performance structure and introduces **0 new explicit uncertainty markers**;
- PDF 70–71 completes `காட்சி-45`; PDF 70 continues the PDF 69 utterance without a repeated speaker label and PDF 70→71 preserves the physical `சொந்த` / `மாக்குகிறேன்!` cross-page continuation;
- PDF 70 preserves source-visible `பத்தரை மாத்துத் தங்கம்!`; PDF 71 closes with `(குமரன் உயிரை இழக்கிறான்)`, `“உலகைத்திருத்தும் உத்தமர்களுக் கெல்லாம் இது தான் முடிவா?”`, `இதை மாற்றி அமைப்பது யார்?`, and final `நாம்`;
- PDF 70–71 adds **0** new uncertainty markers and no new distinct song/lyric/performance structure; historical-glyph first-pass coverage is now **67/67**;
- PDF 49 / `காட்சி-31` opens the mapped lyrical witness beginning `பேசும் யாழே பெண் மானே`; only the booklet text is preserved and PDF 50 continues the same source block;
- PDF 40–44 retains source-period/colloquial forms including `கோவேரிக் கழுதைக்கு`, `ஆவேஷ மூச்சால்`, `விட்டானுக்கும்?`, `மண்டேகங்கள்`, `நாய்க்குட்டி`, and `மாத்திரை முன்னேற்ற ஆஸ்பத்திரியை`;
- PDF 35–36 / `காட்சி 21` preserves the booklet's complete lineated lyrical witness beginning `மணமில்லா மலர் நானம்மா!`; authorship remains not adjudicated;
- source-irregular forms such as PDF 20 `போறு ஞானம்!`, PDF 21 `மாடெல்லே`, PDF 22 `பாலிலா`, PDF 23 `தூர பந்து` / `மட்டாக`, PDF 24 `கெளரவம்`, and PDF 25–29 `மண்ணுங்கட்டியாவது`, `ஏணிப்படியாக்கிக்`, `லஷ்மி`, `ஜமீன்தாரணி யாக்க`, `காண்டிராக்ட்காரன்` remain unmodernized;
- the three former holds are now resolved by user manual controlling-scan verdicts: PDF 5 `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`, PDF 10 `நீ இங்கே வேலை பார்க்கிற வரைக்கும்`, PDF 24 `கெளரவம் தேடி`;
- **67/67** canonical pages are dual-gate VERIFIED.

## Canonical Tamil closure — user manual source verdicts

- PDF 5: **`அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`**;
- PDF 10: **`நீ இங்கே வேலை பார்க்கிற வரைக்கும்`**;
- PDF 24: **`கெளரவம் தேடி`**;
- authority basis: explicit user manual inspection of the controlling scan, permitted by the binding cinema-work processing guide;
- canonical Tamil: **67/67 COMPLETE-VERIFIED**;
- visual / historical-glyph / dual-gate: **67/67 / 67/67 / 67/67**;
- open source uncertainties: **0**;
- final audit: `notes/canonical-closure-user-manual.md`;
- no downstream derivative reconciliation required because derivatives had not yet started.

**Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.

## Song / verse / performance structures mapped or confirmed so far

High-confidence source-visible structures now include:

1. PDF 16 / காட்சி 7 — explicit `[பாட்டு]`, the source-credited Bharathiyar item **ஆயிரம் தெய்வங்கள்**;
2. PDF 18 / காட்சி 8 — source-visible lyrical duet beginning **`பேசும் யாழே பெண் மானே`**, labelled `குமரன்`, `மீனு`, `இருவர்`; authorship **not adjudicated**;
3. PDF 35–36 / காட்சி 21 — multi-line lyrical block beginning `மணமில்லா மலர் நானம்மா!`;
4. PDF 49–50 / காட்சி 31 — multi-page lyrical block with repeated `(பேதம்)` cues;
5. PDF 59–60 — two poetic/song-like blocks between காட்சி 36 and காட்சி 37;
6. PDF 64 / காட்சி 39 — explicit **`பின்னணிப் பாடல்`** block.

PDF 15 also contains the quoted fragment `ஓரிடந்தனிலே...`; it remains dialogue-owned and is not promoted to a reconstructed standalone song. PDF 20–34 introduces no newly distinct standalone lyric/song block; PDF 35–36 contains the already mapped scene-21 lyrical block; PDF 40–44 adds no new standalone lyric/song block; PDF 49 opens the mapped scene-31 lyrical block; PDF 50 completes it without outside reconstruction.

These structures remain source candidates until verified canonical transcription and the later song/performance gate. No missing lyrics or authorship will be reconstructed from outside sources.

## Historical Tamil glyph policy

This source uses older Tamil type and must follow `../../docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` from the first canonical page onward.

Every canonical page must be inspected at enlarged/native resolution for at least the known families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Rules:

- identify historical character identity before encoding modern Unicode;
- preserve source spelling, grammar, vocabulary and punctuation;
- use same-edition glyph comparison when needed;
- OCR is navigation/discovery aid only;
- never global-replace a historical glyph family;
- unresolved clusters remain `needs-review`;
- a page will not be called verified until both ordinary visual fidelity and its historical-glyph check pass.

Work audit: `notes/historical-glyph-audit.md`.

## User-supplied contextual note

The user describes the film as making the rationalist movement its central protagonist, foregrounding the working-class voice, and introducing rationalist thought throughout. This is retained as **user-supplied context**, not silently promoted to source-visible bibliographic/textual evidence.

## Exact next activity

**Begin Phase 5 scene-text derivatives from the fully verified canonical Tamil. Create one derivative for each source-numbered காட்சி 1–45 in source order, preserve exact source headings, page provenance and cross-page/cross-part continuity, and run scene-boundary ownership QA before proceeding to the dialogue index. Do not alter canonical Tamil except for later source-supported corrections.**


## English scenes 6–15 checkpoint

- English scenes verified: **15/45 cumulative**;
- cumulative units: **363**;
- immutable dialogue links: **279**;
- source-unlabelled speech retained without inferred labels: **4**;
- translated performance records: **3/7 — `naam-perf-007`, `naam-perf-001`, `naam-perf-002`**;
- performance line/cue mappings: **57**;
- closed upstream-layer changes: **0**.

**Iteration rule:** 10 source scenes per iteration; final remainder may be smaller.

**Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.


## English scenes 16–25 checkpoint

- English scenes verified: **25/45 cumulative**;
- cumulative units: **501**;
- immutable dialogue links: **380**;
- source-unlabelled speech retained without inferred labels: **10**;
- translated performance records: **4/7 — `naam-perf-007`, `naam-perf-001`, `naam-perf-002`, `naam-perf-003`**;
- performance line/cue mappings: **74**;
- closed upstream-layer changes: **0**.

**Iteration rule:** 10 source scenes per iteration; final remainder may be smaller.

**Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.


## English scenes 26–35 checkpoint

- English scenes verified: **35/45 cumulative**;
- cumulative units: **680**;
- immutable dialogue links: **506**;
- source-unlabelled speech retained without inferred labels: **19**;
- translated performance records: **5/7**;
- performance line/cue mappings: **84**;
- source-local chants: **1 / 16 mappings**;
- closed upstream-layer changes: **0**.

**Historical next recorded at this earlier English checkpoint:** Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch.


## English scenes 36–45 final-batch checkpoint

- English scene layer: **45/45 VERIFIED**;
- cumulative units: **797**;
- immutable dialogue links: **590/590**;
- source-unlabelled speech retained without inferred labels: **20**;
- translated performance records: **7/7**;
- performance line/cue mappings: **138**;
- source-local chant: **1 / 16 mappings**;
- whole-work reconciliation: **READY-NEXT**;
- closed upstream-layer changes: **0**.

**Next:** Run whole-work English translation reconciliation and closure QA across source scenes 1–45 before building the reader/export layer. Verify every translated unit is source-ordered and unique; all 590 immutable dialogue records are linked exactly once; source-unlabelled speech remains unassigned; all seven retained song/performance records are translated without authorship upgrades; the scene-34 chant remains a distinct chant; cross-page provenance and written-text/stage ownership are exact; no duplicate source-span ownership, synthetic scene-end prose, placeholder text, or upstream Tamil/scene/dialogue/character/song-source mutation exists. If and only if that whole-work gate passes, mark English translation complete-verified and begin Phase 10 whole-work reader/export generation.


## English whole-work reconciliation closure

- English **COMPLETE-VERIFIED**; whole-work QA **PASS**; **45/45 scenes / 797 units / 590/590 dialogue links / 20 unlabelled / 7/7 performances / 138 mappings / 1 chant (16 mappings) / 12 cross-page units**;
- duplicate source owners / placeholders / synthetic scene ends / upstream changes: **0 / 0 / 0 / 0**;
- reader/export: **READY-NEXT**.

**Next:** No required repository-internal processing remains for நாம். Reader/export and the source-linked Reading Room payload are complete-verified with QA PASS. Keep Tamil, scene, dialogue, character, song-source and English records closed. Apply `works/naam/integrations/reading-room/reading-room.json` in the separate Kalaignar Digital Library / Reading Room implementation repository only when that repository is explicitly authorized for modification; before applying it, fetch that repository's live state and use a fail-closed importer pinned to this verified payload/manifest. Site application remains not-applied here. Do not create a PDF, EPUB or other publication package unless separately requested.


<!-- Naam Phase 10 reader and payload closure -->
## Phase 10 reader/export + Reading Room closure

- reader/export: **COMPLETE-VERIFIED / QA PASS**;
- reader forms: **Markdown / standalone HTML / machine-readable JSON**;
- source scenes rendered: **45/45 source-numbered scenes exactly once**;
- English units rendered: **797/797 exactly once**;
- immutable dialogue links: **590/590**;
- source-unlabelled speech: **20 / inferred speakers 0**;
- retained performance records: **7/7 / 138 mappings**;
- scene-34 chant: **1 / 16 mappings / not promoted to the performance inventory**;
- written-text / cross-page units: **2 / 12**;
- reader JSON: `3043e1cd515d4e1bb8298ffb99709db5e3d9cc1a46bccdcaad9972692363e656` / **952,751 bytes**;
- Reading Room payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS**;
- payload: `9b97493b820ebd42c822b5fbdc53beda8dbe1d61103a1c9d2abb06a552bcf825` / **965,215 bytes**;
- site application: **not-applied**;
- upstream Tamil / scene / dialogue / character / song-source / English-record changes: **0**.

**Next:** No required repository-internal processing remains for நாம். Reader/export and the source-linked Reading Room payload are complete-verified with QA PASS. Keep Tamil, scene, dialogue, character, song-source and English records closed. Apply `works/naam/integrations/reading-room/reading-room.json` in the separate Kalaignar Digital Library / Reading Room implementation repository only when that repository is explicitly authorized for modification; before applying it, fetch that repository's live state and use a fail-closed importer pinned to this verified payload/manifest. Site application remains not-applied here. Do not create a PDF, EPUB or other publication package unless separately requested.
