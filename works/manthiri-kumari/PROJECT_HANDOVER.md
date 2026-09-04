# Project handover — மந்திரி குமாரி

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/manthiri-kumari/`

## Live-main rule

Treat live GitHub `main` and the rendered controlling scan as authoritative over older copied checkpoints. Preserve newer durable work; do not reset or repeat completed phases because an older handover says otherwise.

## Mandatory startup

Before changing this work, read completely:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `docs/SOURCE_POLICY.md`
4. `docs/TRANSCRIPTION_GUIDE.md`
5. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
6. `docs/STATUS_CONSISTENCY_AUDIT.md`
7. `works/manthiri-kumari/README.md`
8. `works/manthiri-kumari/metadata.yaml`
9. `works/manthiri-kumari/mapping.md`
10. `works/manthiri-kumari/notes/INTAKE_AUDIT.md`
11. `works/manthiri-kumari/notes/fidelity-audit.md`
12. `works/manthiri-kumari/notes/post-fidelity-corrections.md`
13. `works/manthiri-kumari/story-summary/index.json`
14. `works/manthiri-kumari/songs/index.json`
15. `works/manthiri-kumari/songs/AUTHORSHIP_GATE.md`
16. `works/manthiri-kumari/translations/README.md`
17. `works/manthiri-kumari/translations/index.json`
18. `works/manthiri-kumari/translations/FINAL_TRANSLATION_QA.md`
19. `works/manthiri-kumari/editions/bilingual/README.md`
20. `works/manthiri-kumari/editions/bilingual/reader-edition.json`
21. `works/manthiri-kumari/editions/bilingual/PREFLIGHT_QA_REPORT.md`
22. `works/manthiri-kumari/editions/bilingual/QA_REPORT.md`
23. `works/manthiri-kumari/editions/bilingual/manifest.json`
24. `docs/SONG_TRANSLATION_GUIDE.md` when touching translated performance text.

## Controlling source

`TVA_BOK_0026144_மந்திரி_குமாரி.pdf`

- 14 physical PDF pages;
- 579,782 bytes;
- SHA-256 `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`;
- image-only scan;
- rendered pages control canonical Tamil.

## Source classification

This is a **film story-and-song booklet**, not a full screenplay/dialogue transcript.

- PDF 1: cover;
- PDF 2: cast/production credits with direct `கதை, வசனம் : மு. கருணாநிதி` credit;
- PDF 3–5: continuous prose `கதைச்சுருக்கம்`;
- PDF 6–13: 15 separately headed song/performance blocks;
- PDF 14: unrelated `அமரகவி` advertisement / paratext.

Do not create screenplay scenes or a film-wide dialogue index from this booklet.

## Completed source/Tamil gates

- source intake / whole-scan inspection: **complete, 14/14**;
- structural map: **verified**;
- canonical Tamil PDF 2–13: **complete-verified, 12/12 pages**;
- unresolved canonical readings: **0**;
- post-fidelity user scan corrections: **recorded, applied and reconciled**;
- source subdivision wording: **`தொகையறா`** where applicable;
- credits layer: **complete-verified**;
- story-summary Tamil derivative: **complete-verified — 1 continuous record / PDF 3–5**;
- song/performance Tamil records: **complete-verified — 15/15 / PDF 6–13**;
- synthetic screenplay scene IDs in source-derived layers: **0**.

Canonical authority: `works/manthiri-kumari/transcription/full-text.md`.

## Authorship / cross-witness state

- printed film-wide credit: `கதை, வசனம் : மு. கருணாநிதி` — story/dialogue only;
- booklet item-level lyricists verified: **0/15**;
- item-level lyricists unresolved: **15/15**;
- confirmed current-anthology witness: **1/15**, `மாட்டுக்கார பையன்` ↔ `kalaignar-song-001`;
- source-only relative to the current anthology corpus: **14/15**;
- later anthology used to repair this booklet's Tamil: **no**.

Unresolved lyric authorship does not block translation, reader/export, or Reading Room preparation. It must remain unresolved downstream unless separately evidenced.

## English translation — complete-verified

- story-summary English: **1/1**, **13** logical prose units, **1** cross-page unit;
- performance English: **15/15**, **52** sections;
- Tamil / English performance lines-cues: **234 / 234**;
- line-mapping mismatches: **0**;
- cross-page translated performance records: **7** — `002`, `004`, `006`, `007`, `009`, `011`, `013`;
- missing / duplicate translation records: **0 / 0**;
- authorship upgrades introduced by translation: **0**;
- canonical Tamil changed by translation: **no**;
- synthetic screenplay scene IDs created: **0**;
- final translation QA: **PASS**.

Performance 13 permanently retains the evidence distinction between its printed heading `பார்த்திபன்—மந்திரிகுமாரி` and internal turn labels `பார்த்திபன்` / `அமுதவல்லி`; do not normalize that mismatch.

## Bilingual reader/export — complete-verified

Directory: `works/manthiri-kumari/editions/bilingual/`

Files:

- `README.md`;
- `build.py`;
- `reader-edition.json`;
- `reader-edition.md`;
- `reader-edition.html`;
- `PREFLIGHT_QA_REPORT.md`;
- `QA_REPORT.md`;
- `manifest.json`.

Checkpoint:

- navigation model: **story summary + 15 performance blocks**;
- top-level source structures: **16/16**;
- story-summary logical units: **13/13**;
- performance records: **15/15**;
- performance sections: **52/52**;
- Tamil / English performance line-cues: **234 / 234**;
- line-pair mismatches: **0**;
- cross-page performance records retained: **7/7**;
- current-anthology disposition retained: **1 confirmed witness / 14 source-only**;
- item-level lyric authorship retained: **0 verified / 15 unresolved**;
- synthetic screenplay scene IDs introduced: **0**;
- canonical Tamil changed by reader/export: **no**;
- preflight QA: **PASS**;
- whole-reader QA: **PASS**.

The reader is deliberately source-linked: `reader-edition.json` names the verified translation records and the HTML renderer loads those records. It does not create a second independent bilingual text corpus.

## Source-authority boundaries

- rendered scan controls canonical Tamil;
- explicit user manual scan verdicts control their reviewed occurrences unless later direct scan evidence reopens them;
- OCR, film audio, subtitles, web lyrics, memory and later anthology text must not repair this booklet silently;
- translation and reader layers are downstream and must never repair canonical Tamil;
- item-level lyric authorship remains independently evidence-based;
- archival record IDs are navigation only and are not source numbering.

## Current downstream state

- English translation: **complete-verified**;
- deterministic bilingual reader/export: **complete-verified — QA PASS**;
- Reading Room integration: **ready / not-started**;
- screenplay scene derivatives / film-wide immutable dialogue index: **not applicable**.

## Exact next activity

Proceed without redundant clarification:

> **Prepare and QA a provenance-safe Reading Room integration payload from the complete-verified bilingual reader. Preserve the booklet's natural `கதைச்சுருக்கம்` + 15-performance navigation, Tamil/English source pairing, PDF-page provenance, source-visible cues, the 1/15 cross-witness relationship, and 15/15 unresolved item-level lyricists. Do not invent screenplay scenes or upgrade authorship through presentation metadata.**

At Reading Room payload completion, synchronize the integration QA/status plus `metadata.yaml`, work README/handover, `data/works.json`, root README, master handover and `docs/STATUS_CONSISTENCY_AUDIT.md` before declaring the phase closed.
