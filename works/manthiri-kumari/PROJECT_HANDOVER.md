# Project handover — மந்திரி குமாரி

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/manthiri-kumari/`

## Live-main rule

Treat live GitHub `main` and the rendered controlling scan as authoritative over any older checkpoint copied elsewhere. Preserve newer durable work; do not reset or repeat completed phases because an older handover says otherwise.

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
13. `works/manthiri-kumari/story-summary/README.md`
14. `works/manthiri-kumari/story-summary/index.json`
15. `works/manthiri-kumari/songs/README.md`
16. `works/manthiri-kumari/songs/schema.json`
17. `works/manthiri-kumari/songs/index.json`
18. `works/manthiri-kumari/songs/performance-inventory.md`
19. `works/manthiri-kumari/songs/cross-witness-comparison.md`
20. `works/manthiri-kumari/songs/AUTHORSHIP_GATE.md`
21. `works/manthiri-kumari/songs/match-report-001-oorukku-uzhaippavandi.md`

For translation work, also read the repository's applicable English/song translation guidance before creating translation records.

## Controlling source

`TVA_BOK_0026144_மந்திரி_குமாரி.pdf`

- 14 physical PDF pages;
- 579,782 bytes;
- SHA-256 `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`;
- image-only scan;
- rendered pages control canonical Tamil readings.

## Source classification

This is a **film story-and-song booklet**, not a full screenplay/dialogue transcript.

Source structure:

- PDF 1 cover;
- PDF 2 cast/production credits with direct `கதை, வசனம் : மு. கருணாநிதி` credit;
- PDF 3–5 continuous prose `கதைச்சுருக்கம்`;
- PDF 6–13 song/performance section with 15 separately headed blocks;
- PDF 14 unrelated `அமரகவி` advertisement / back-cover paratext.

Do not create screenplay scenes or a film-wide dialogue index from the prose synopsis.

## Completed source gates

- duplicate-work search: **complete**;
- source intake: **complete**;
- whole-scan inspection: **14/14 complete**;
- structural map: **verified**;
- canonical Tamil first pass: **complete — PDF 2–13**;
- visual fidelity audit: **complete-verified — 12/12 canonical PDF pages**;
- canonical page anchors: **12/12 verified**;
- unresolved canonical readings: **0**;
- post-fidelity user scan corrections: **recorded and applied**;
- later user-approved lexical/spelling campaign across PDF 6–13: **applied and reconciled**;
- source subdivision wording: **`தொகையறா`** in the applicable performance subdivisions/headings.

Authoritative canonical file:

`works/manthiri-kumari/transcription/full-text.md`

Correction history:

- `works/manthiri-kumari/notes/fidelity-audit.md` — initial whole-canonical-range visual audit;
- `works/manthiri-kumari/notes/post-fidelity-corrections.md` — later direct user scan verdicts and lexical corrections.

## Current derivative state

### Credits

`works/manthiri-kumari/credits/credits.yaml`

Status: **complete-verified from source**.

The booklet directly verifies:

`கதை, வசனம் : மு. கருணாநிதி`

This is evidence for story/dialogue authorship only. It does **not** automatically establish lyric authorship for any of the 15 performance blocks.

### Story summary

Status: **complete-verified**.

Files:

- `works/manthiri-kumari/story-summary/full-text.md`;
- `works/manthiri-kumari/story-summary/index.json`;
- `works/manthiri-kumari/story-summary/README.md`.

Checkpoint:

- source PDF pages represented: **3/3 — PDF 3–5**;
- source-linked records: **1**, `manthiri-kumari-story-summary-001`;
- structure: **continuous prose**;
- synthetic screenplay scene IDs: **0**;
- immutable dialogue IDs from reported/quoted synopsis speech: **0**;
- canonical Tamil changed by derivative creation: **no**.

### Song/performance structured layer

Status: **complete-verified — 15/15 source-linked records**.

Files:

- `songs/README.md`;
- `songs/schema.json`;
- `songs/index.json`;
- `songs/records/001.json`–`songs/records/015.json`;
- `songs/performance-inventory.md`;
- `songs/cross-witness-comparison.md`;
- `songs/match-report-001-oorukku-uzhaippavandi.md`;
- `songs/AUTHORSHIP_GATE.md`.

Checkpoint:

- source blocks: **15/15 inventoried and classified**;
- source-linked records: **15/15 complete-verified**;
- record IDs: `manthiri-kumari-performance-001`–`015`;
- source PDF coverage: **6–13, 8/8 pages**;
- missing / duplicate record IDs: **0 / 0**;
- exact source headings: **preserved**;
- source-page segmentation: **preserved**;
- `தொகையறா` / `பாட்டு` subdivisions: **preserved**;
- speaker/performance cues: **preserved**;
- synthetic screenplay scene IDs: **0**;
- canonical Tamil changed by record creation: **no**;
- current later-anthology match: **1/15**, record 011 `மாட்டுக்கார பையன்` ↔ `kalaignar-song-001` / `ஊருக்கு உழைப்பவண்டி`;
- source-only blocks in the current 54-song anthology corpus: **14/15**;
- duplicate anthology parent records created: **0**;
- existing parent anthology lyrics modified: **0**;
- block-11 line-level comparison: **complete-reconciled**.

### Song authorship gate

The booklet-evidence gate is complete at the evidence currently available:

- item-level lyric authorship verified by this booklet: **0/15**;
- unresolved item-level lyric authorship: **15/15**;
- film-wide `கதை, வசனம்` credit promoted to lyric credit: **no**.

Unresolved lyric authorship does **not** block source-linked English translation. Future evidence may upgrade individual records without changing canonical Tamil.

## Source-authority boundaries

- rendered scan controls canonical Tamil;
- explicit user manual scan verdicts control their reviewed occurrences unless later direct scan evidence reopens them;
- OCR, film audio, subtitles, web lyrics, memory and later anthology text must not repair this booklet silently;
- `கதை, வசனம் : மு. கருணாநிதி` is primary-source evidence for story/dialogue credit only;
- item-level lyric authorship remains independently evidence-based;
- `source-only` against the later anthology means only “not represented in that corpus,” not positive or negative authorship;
- translation is downstream and must never repair canonical Tamil.

## Current downstream state

- screenplay scene derivatives: **not applicable**;
- film-wide immutable dialogue index: **not applicable**;
- English translation: **ready / not-started**;
- reader/export: **blocked pending English translation**;
- Reading Room integration: **blocked downstream**.

## Exact next activity

Proceed without redundant clarification:

> **Begin source-linked English translation from the completed verified source structures: the continuous PDF 3–5 story-summary record and the 15 PDF 6–13 song/performance records. Preserve source order, page provenance, source-visible speaker/performance cues, `தொகையறா` / `பாட்டு` distinctions and unresolved item-level lyric authorship. Do not convert this booklet into screenplay scenes, and never use translation to repair canonical Tamil.**

At the completion of each translation phase, synchronize work-local translation indexes/status plus `metadata.yaml`, work README/handover and the repository-wide mirrors before declaring completion.
