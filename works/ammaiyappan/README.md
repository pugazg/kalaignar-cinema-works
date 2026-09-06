# அம்மையப்பன்

Source-led archival work for `TVA_BOK_0064230_அம்மையப்பன்.pdf`. The rendered scan controls canonical Tamil; OCR, film audio, subtitles, web text and later editions are non-canonical.

Because this 1954 source contains frequent historical Tamil typeforms, canonical Tamil requires **two independent verification gates**:

1. complete visual source-fidelity comparison; and
2. historical-Tamil-glyph verification under `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.

A page is final Tamil verified only when both gates pass. Work-level tracking is in `notes/historical-glyph-audit.md`; the completed retrospective correction synchronization is recorded by `notes/historical-glyph-sync-manifest.json` and `notes/historical-glyph-sync-report.json`.

## Source checkpoint

- title: `அம்மையப்பன்`;
- printed credit: `கதை வசனம்` / `மு. கருணாநிதி`;
- PDF pages: **111**;
- source SHA-256: `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`;
- first edition: **செப்டம்பர், 1954**;
- publisher: `முரசொலி பதிப்பகம்`, `சென்னை-14`;
- main screenplay/dialogue: **PDF 5–109 / logical printed pp.3–107**;
- PDF 110–111: advertisement/back matter, excluded from canonical screenplay.

The booklet prints no numbered scene sequence. Current verified derivative mapping records **63 source-visible structural boundaries / 41 distinct heading forms**; archive scene ordinals are navigation derivatives only.

Locked source verdicts:

- PDF 56 / printed p.54: **`பழுதார் வீதி`**;
- PDF 107 / printed p.105: **`தூக்குமேடை`**; rejected reading `தாக்குமேடை` must not reappear.

## Canonical Tamil first pass — complete draft coverage

- expected canonical pages: **105**;
- completed first-pass range: **PDF 5–109 / printed pp.3–107**;
- progress: **105/105 pages**;
- first-pass state: **draft-complete**;
- continuous assembled transcription: `transcription/full-text.md`, through **PDF 109**;
- assembly QA: `transcription/ASSEMBLY_QA.md` — **PASS**;
- open first-pass uncertainty markers: **0**;
- final uncertainty ledger: `notes/textual-notes-pdf-105-109.md` for markers **115–116**.

The first-pass draft, assembly, visual-fidelity audit and historical-glyph audit are complete. Canonical Tamil is **105/105 dual-gate verified**.

## Retrospective historical-glyph backfill — CLOSED through PDF 74

The previously visual-passed PDF 5–74 range was re-inspected from the source for historical Tamil typeforms before forward verification resumed.

- retrospective source review: **PDF 5–74 = 70/70 pages complete**;
- pages requiring no historical-glyph correction: **32**;
- pages with source-established correction sets: **38**;
- correction synchronization: **complete**;
- synchronization commit: `880978627191a122f55b50522d112d163faa7e10`;
- synchronized logical occurrences across canonical/provenance surfaces: **97**;
- global replacement used: **no**;
- source whitespace/layout preserved by the synchronization pass: **yes**;
- genuine same-edition control readings preserved on PDF **48, 62, 64 and 69**: **PASS**.

The synchronization report is `notes/historical-glyph-sync-report.json`. Retained first-pass provenance was changed only where the matching audited occurrence existed; older unresolved placeholders were not silently filled from the newer canonical layer.

Therefore **PDF 5–74 / logical pp.3–72 are now dual-gate verified: 70/105 pages**.

Forward dual-gate verification through PDF 84 is recorded by commit `0da97f94e829bef9b387bf59be580933b97ed122` and `notes/dual-gate-sync-report-pdf-075-084.json`.

Forward dual-gate verification through PDF 94 is recorded by commit `1911df2c97d45dfe07f1b9073bdf6368378ddf44` and `notes/dual-gate-sync-report-pdf-085-094.json`.

## Historical Tamil glyph gate

The minimum known reform-sensitive families to inspect occurrence-by-occurrence are:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

This list is a minimum, not exhaustive. Old ligatures, faint vowel marks, broken/worn type and edition-specific forms must also be inspected. Character identity must be determined from enlarged source pixels and same-edition evidence where needed; no OCR authority, semantic guessing, spelling modernization or global replacement is permitted.

## First-pass assembly QA

The continuous draft was assembled from the existing PDF 5–14 `full-text.md` plus all bounded parts from PDF 15–109. Automated boundary QA records:

- **105 / 105** page anchors present;
- exact source-anchor order **PDF 5, 6, …, 109**;
- missing anchors: **0**;
- duplicate anchors: **0**;
- bounded-part boundary presence: **PASS**;
- locked `தூக்குமேடை`: **PASS**;
- rejected `தாக்குமேடை`: **absent**;
- visible unresolved first-pass spans: **116**.

Canonical Tamil, scene segmentation, dialogue indexing, character/entity indexing, and the source-only song/performance gate are now closed. English translation is active.

## Post-closure dialogue-boundary correction

The verified scene-3 source form `பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......` is a distinct **பூங்காவனம்** dialogue unit. The exact semicolon delimiter is preserved in `dialogues/source-role-resolved-records.json` and must not be normalized or swallowed into the preceding பலதேவர் utterance.

Current structured authority after that correction:

- explicit colon-labelled dialogue records: **1,009**;
- source-role-resolved dialogue supplements: **16**;
- downstream dialogue units: **1,025**;
- exact source speaker-label strings: **62**;
- unresolved source-role blocks: **0**;
- character/entity dialogue coverage: **1,025/1,025**;
- exact-label coverage: **62/62**;
- source punctuation normalizations: **0**.

The other preserved source-explicit non-colon form remains scene 5 `திரு; ...`; neither semicolon is normalized to a colon.

## Current status

| Layer | Status |
|---|---|
| Source intake | complete |
| Whole-scan inspection | complete — 111/111 |
| Structural mapping | verified |
| Canonical Tamil | **complete-verified — 105/105 dual gate** |
| Visual fidelity | **105/105 PASS** |
| Historical Tamil glyph audit | **105/105 PASS** |
| Open canonical uncertainty markers | **0** |
| Scene segmentation preflight | **PASS — 63 boundaries** |
| Scene-text derivatives | **complete-verified — 63/63** |
| Boundary-ownership QA | **PASS — 0 gaps / 0 overlaps / 105 pages represented** |
| Dialogue index | **complete-source-role-resolved — 1,025/1,025 downstream units (1,009 explicit + 16 supplements)** |
| Character/entity index | **complete-verified-reconciled — 26 entities / 62 labels / 1,025 units** |
| Song/performance authorship gate | **complete-verified-source-only — 5 source-visible occurrences / 0 standalone lyric files** |
| English translation / reader | **verified through scene 10/63 — 225/225 current units; reader blocked pending complete English** |

Late source correction before scene generation: PDF 10 heading `மடாலயம்` → **`மாடம்`**, direct-scan verified and recorded in `notes/post-fidelity-corrections.md`; no derivative regeneration was needed because scene files did not yet exist. Post-fidelity correction commit: `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`.

## English checkpoint through scene 10

- verified scenes: **10/63**;
- verified English units: **225**;
- dialogue units: **196** = **190 explicit dialogue records + 6 source-role supplements**;
- stage/action units: **28**;
- standalone song-reference units: **1**;
- cross-page English units: **2**;
- song/performance occurrence links encountered so far: **2** — `ammaiyappan-song-001`, `ammaiyappan-song-002`;
- frozen Tamil/dialogue/character/song evidence modified by English: **no**.

Batch QA is recorded in `translations/BATCH_002_005_REVIEW.md` and `translations/BATCH_006_010_REVIEW.md`. Scene 7 preserves only the printed Muthan–Muthayi performance cue; scene 10 links only the printed Kambar-attributed fragment, with no absent lyric or verse reconstruction.

## Exact next activity

**Translate and source-review archival scenes 11–15. Preserve the closed source-role supplements in scene 11, exact Tamil speaker labels and PDF/printed-page provenance, and do not modify frozen source evidence.**
