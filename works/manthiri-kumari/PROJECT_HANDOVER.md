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
13. `works/manthiri-kumari/songs/performance-inventory.md`
14. `works/manthiri-kumari/songs/cross-witness-comparison.md`
15. `works/manthiri-kumari/songs/AUTHORSHIP_GATE.md`

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
- later user-approved lexical/spelling campaign across PDF 6–13: **applied**;
- source subdivision wording: **`தொகையறா`** in the applicable performance subdivisions/headings;
- currently existing affected downstream song/cross-witness surfaces: **reconciled**.

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

Path: `works/manthiri-kumari/story-summary/`

Status: **initialized; structured/source-linked derivative completion pending**.

Rules:

- preserve the continuous PDF 3–5 prose structure;
- preserve PDF-page provenance;
- do not convert paragraphs into screenplay scenes;
- do not manufacture immutable dialogue records from reported/quoted synopsis speech;
- derive only from verified canonical Tamil.

### Song/performance layer

- source blocks: **15/15 inventoried and classified**;
- exact heading reconciliation: **complete**;
- source subdivision form: `தொகையறா` / `பாட்டு` where applicable;
- current later-anthology match: **1/15**, `மாட்டுக்கார பையன்` ↔ `kalaignar-song-001` / `ஊருக்கு உழைப்பவண்டி`;
- source-only blocks in the current 54-song anthology corpus: **14/15**;
- duplicate anthology parent records created: **0**;
- existing parent anthology lyrics modified: **0**;
- block-11 line-level comparison: **complete-reconciled after the latest lexical corrections**;
- item-level lyric authorship verified by this booklet: **0/15**;
- blocks requiring separate item-level evidence: **15/15**;
- source-linked structured records for the 15 blocks: **not-started**.

Relevant files:

- `songs/performance-inventory.md`
- `songs/cross-witness-comparison.md`
- `songs/match-report-001-oorukku-uzhaippavandi.md`
- `songs/AUTHORSHIP_GATE.md`

## Source-authority boundaries

- rendered scan controls canonical Tamil;
- explicit user manual scan verdicts control their reviewed occurrences unless later direct scan evidence reopens them;
- OCR, film audio, subtitles, web lyrics, memory and later anthology text must not repair this booklet silently;
- `கதை, வசனம் : மு. கருணாநிதி` is primary-source evidence for story/dialogue credit only;
- item-level lyric authorship remains a separate evidence gate;
- `source-only` against the later anthology means only “not represented in that corpus,” not positive or negative authorship.

## Current blocked/downstream layers

- screenplay scene derivatives: **not applicable**;
- film-wide immutable dialogue index: **not applicable**;
- English translation: **blocked until the source-appropriate Tamil derivative structures are complete**;
- reader/export: **blocked**;
- Reading Room integration: **blocked downstream**.

## Exact next activity

Proceed without redundant clarification:

> **Complete the source-linked continuous PDF 3–5 `கதைச்சுருக்கம்` derivative from verified canonical Tamil. Preserve source order and PDF-page provenance, and do not manufacture screenplay scenes or immutable dialogue records. Then create source-linked structured records for all 15 PDF 6–13 song/performance blocks while preserving the existing authorship and cross-witness dispositions.**

At the completion of each major derivative phase, synchronize work README/metadata/handover plus `data/works.json`, root README, master handover and `docs/STATUS_CONSISTENCY_AUDIT.md` before declaring the phase closed.
