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
10. `works/manthiri-kumari/notes/fidelity-audit.md`
11. `works/manthiri-kumari/notes/post-fidelity-corrections.md`
12. `works/manthiri-kumari/story-summary/index.json`
13. `works/manthiri-kumari/songs/index.json`
14. `works/manthiri-kumari/songs/AUTHORSHIP_GATE.md`
15. `works/manthiri-kumari/translations/index.json`
16. `works/manthiri-kumari/translations/FINAL_TRANSLATION_QA.md`
17. `works/manthiri-kumari/editions/bilingual/README.md`
18. `works/manthiri-kumari/editions/bilingual/reader-edition.json`
19. `works/manthiri-kumari/editions/bilingual/QA_REPORT.md`
20. `works/manthiri-kumari/editions/bilingual/manifest.json`
21. `works/manthiri-kumari/integrations/reading-room/README.md`
22. `works/manthiri-kumari/integrations/reading-room/reading-room.json`
23. `works/manthiri-kumari/integrations/reading-room/QA_REPORT.md`
24. `works/manthiri-kumari/integrations/reading-room/manifest.json`
25. `docs/SONG_TRANSLATION_GUIDE.md` when touching translated performance text.

## Controlling source

`TVA_BOK_0026144_மந்திரி_குமாரி.pdf`

- physical PDF pages: **14**;
- bytes: **579,782**;
- SHA-256: `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`;
- image-only scan; rendered pages control canonical Tamil.

## Source classification

This is a **film story-and-song booklet**, not a full screenplay/dialogue transcript.

- PDF 1 cover;
- PDF 2 credits with `கதை, வசனம் : மு. கருணாநிதி`;
- PDF 3–5 continuous prose `கதைச்சுருக்கம்`;
- PDF 6–13 fifteen song/performance blocks;
- PDF 14 unrelated `அமரகவி` advertisement.

Do not create screenplay scenes or a film-wide dialogue index from this booklet.

## Completed source / Tamil gates

- source intake / whole-scan inspection: **complete, 14/14**;
- structural map: **verified**;
- canonical Tamil PDF 2–13: **complete-verified, 12/12 pages**;
- unresolved canonical readings: **0**;
- user post-fidelity scan corrections: **recorded, applied and reconciled**;
- source subdivision form: **`தொகையறா`** where applicable;
- credits: **complete-verified**;
- story-summary Tamil: **1/1 complete-verified**;
- performance Tamil records: **15/15 complete-verified**;
- synthetic screenplay scene IDs: **0**.

Canonical authority: `works/manthiri-kumari/transcription/full-text.md`.

## Authorship / cross-witness state

- printed story/dialogue credit: `கதை, வசனம் : மு. கருணாநிதி`;
- booklet item-level lyricists verified: **0/15**;
- unresolved item-level lyricists: **15/15**;
- confirmed current-anthology witness: **1/15**, block 11 `மாட்டுக்கார பையன்` ↔ `kalaignar-song-001`;
- source-only against current anthology: **14/15**;
- later anthology used to repair booklet Tamil: **no**.

## English translation — complete-verified

- story summary: **1/1 / 13 prose units / 1 cross-page unit**;
- performances: **15/15 / 52 sections**;
- Tamil / English line-cues: **234 / 234**;
- mismatches: **0**;
- cross-page performances: **002, 004, 006, 007, 009, 011, 013**;
- authorship upgrades: **0**;
- canonical Tamil changes: **0**;
- final QA: **PASS**.

Performance 13 must retain printed heading `பார்த்திபன்—மந்திரிகுமாரி` while its internal source turn labels remain `பார்த்திபன்` / `அமுதவல்லி`.

## Bilingual reader/export — complete-verified

Directory: `works/manthiri-kumari/editions/bilingual/`

- navigation: **1 story summary + 15 performances**;
- top-level structures: **16/16**;
- story-summary units: **13/13**;
- performance sections: **52/52**;
- Tamil / English performance line-cues: **234 / 234**;
- line-pair mismatches: **0**;
- cross-page performance records: **7/7**;
- item-level lyricists: **0 verified / 15 unresolved**;
- synthetic scenes: **0**;
- canonical Tamil changes: **0**;
- preflight / final QA: **PASS / PASS**.

The reader is source-linked and is not a new textual authority.

## Reading Room integration payload — complete-verified

Directory: `works/manthiri-kumari/integrations/reading-room/`

Files:

- `reading-room.json` — source-linked composition payload;
- `build.py` — deterministic validator;
- `QA_REPORT.md` — QA PASS checkpoint;
- `manifest.json` — integrity metadata;
- `README.md` — integration contract.

Checkpoint:

- payload mode: **`source-linked-composition`**;
- expected source-link targets: **32**;
- story-summary units: **13**;
- performance records / sections / line-cues: **15 / 52 / 234**;
- confirmed anthology witness / source-only: **1 / 14**;
- item-level lyricists: **0 verified / 15 unresolved**;
- payload bytes: **15,704**;
- payload SHA-256: `20a0db293b936757e7d01def336252f28543337f319dfae6ad7bf5ae886bab43`;
- synthetic scenes: **0**;
- canonical Tamil changes: **0**;
- authorship upgrades: **0**;
- QA: **PASS**;
- site application: **not-applied**.

The payload does not deploy the separate public-site repository. It supplies the source-linked composition/provenance contract that the Reading Room implementation must resolve.

## Source-authority boundaries

- rendered scan controls canonical Tamil;
- explicit user scan verdicts control their reviewed occurrences unless later direct scan evidence reopens them;
- OCR, audio, subtitles, web lyrics, memory and later anthology text must not silently repair this booklet;
- translation, reader and payload layers must never repair canonical Tamil;
- item-level lyric authorship remains independently evidence-based;
- performance ordinals are archival source-order navigation, not printed numbering.

## Current downstream state

- Tamil / structured derivatives: **complete-verified**;
- English translation: **complete-verified**;
- bilingual reader/export: **complete-verified — QA PASS**;
- Reading Room payload: **payload-complete-verified — QA PASS**;
- Reading Room site application: **not-applied**;
- screenplay scene/dialogue full-work model: **not applicable**.

## Exact next activity / disposition

> **No required repository-internal Manthiri Kumari work remains. Apply the verified source-linked Reading Room payload in the separate Reading Room implementation repository only when that repository is explicitly authorized for modification. Preserve story-summary + 15-performance navigation, page provenance, exact source labels/cues, the 1/15 witness relationship, and 15/15 unresolved item-level lyricists.**
