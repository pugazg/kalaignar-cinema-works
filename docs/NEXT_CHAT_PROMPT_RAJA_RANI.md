# Next Chat Prompt — Raja Rani — Whole-Work Bilingual Reader / Export

Continue directly in:

`pugazg/kalaignar-cinema-works`

Branch: `main`

Active work: `works/raja-rani/` — **ராஜா ராணி**

Controlling full source: `TVA_BOK_0017188_ராஜா_ராணி.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve any newer durable state. Do not reset, repeat or overwrite later work because this prompt contains an older checkpoint.

Source identity:

- PDF pages: **80**
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`
- numbered front-matter songs: PDF **4–9**
- screenplay/dialogue: PDF **10–79**, printed pp. **9–78**
- PDF 80: back cover

## Mandatory startup

Before any write, read completely:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `docs/SOURCE_POLICY.md`
4. `docs/TRANSCRIPTION_GUIDE.md`
5. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
6. `docs/HANDOVER_RAJA_RANI.md`
7. this `docs/NEXT_CHAT_PROMPT_RAJA_RANI.md`
8. `works/raja-rani/README.md`
9. `works/raja-rani/metadata.yaml`
10. `works/raja-rani/translations/README.md`
11. `works/raja-rani/translations/index.json`
12. `works/raja-rani/translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`
13. `works/raja-rani/translations/songs/index.json`
14. `works/raja-rani/translations/songs/FINAL_NUMBERED_SONG_TRANSLATION_QA.md`
15. `works/raja-rani/songs/index.json`
16. `works/raja-rani/songs/inventory.json`
17. root `README.md`
18. `data/works.json`
19. `docs/STATUS_CONSISTENCY_AUDIT.md`
20. inspect one or more completed reader/export implementations in this repository for architecture/QA patterns only; never reuse another work's text.

## Source and structured layers — COMPLETE

There are **no blocked/review source pages or screenplay scenes**.

- source pages: **79/79 verified**;
- screenplay pages: **70/70 verified**;
- scene derivatives: **58/58 verified / 0 blocked**;
- unique dialogue corpus: **1,071 immutable records / 58 scenes / 12 cross-page records**;
- character mapping: **80/80 exact labels / 44 verified entities/roles/collectives**;
- Tamil numbered songs: **11/11 verified**;
- screenplay singing references: **4**;
- song authorship: **5 later-anthology Kalaignar-attributed / 6 unresolved**.

Permanent direct-scan verdicts include PDF 27 `இரவெல்லாம்`, PDF 48 `வந்தனா` / `திடீர்னு`, PDF 57 `முன்னுக்கு பின் முரணாயிகிட்டே போவது?`, and the PDF-74 non-canonical `K. N. சங்கரன் ...` stamp disposition.

`r1.md`–`r4.md`, OCR and parsed PDF text are candidate/navigation aids only.

## English screenplay — COMPLETE

Do not reopen normal screenplay translation production.

- scenes: **58/58**;
- verified units: **1,236**;
- immutable dialogue links: **1,071/1,071**;
- dialogue-kind units: **1,090**;
- stage-direction units: **137**;
- performance-cue units: **4**;
- written-text units: **5**;
- source-unlabelled spoken units: **19**;
- genuine cross-page English units: **15**;
- draft/review units: **0/0**.

Final QA: `works/raja-rani/translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`.

### T055/T056 permanent correction

Do not restore the deleted duplicate scene-55 records `s055-d026`–`s055-d030`. Scene 55 has **25** source dialogue records; scene 56 owns the `(முன்)` flashback and has **5**. Corpus total is **1,071**. Canonical pages were unchanged.

## English numbered songs — COMPLETE

Do not repeat song translation.

- numbered song bodies: **11/11 complete-verified**;
- translation sections / turn groups: **67**;
- Tamil source line/cue entries represented: **181**;
- English line/cue entries represented: **181**;
- multi-page song records: **4** — songs 2, 3, 8 and 10;
- draft/review/not-started song records: **0/0/0**.

Final QA: `works/raja-rani/translations/songs/FINAL_NUMBERED_SONG_TRANSLATION_QA.md`.

Authorship remains exactly:

- later-anthology Kalaignar-attributed: songs **3, 5, 6, 7, 8**;
- unresolved: songs **1, 2, 4, 9, 10, 11**;
- original-booklet item-level lyricist credits: **0**.

Performance links remain exactly: songs 3/5/8 verified to scenes 4/16/40; song 11 → scene 58 **review-level** only.

## EXACT NEXT ACTIVITY — deterministic whole-work reader/export

Build the Raja Rani bilingual reader/export from verified structured records.

Requirements:

1. preserve two source structures rather than flattening them:
   - the 11 actually numbered front-matter songs;
   - the 58 archive-only screenplay scene segments, which are **not** source scene numbers;
2. use verified structured English/Tamil records as inputs, not OCR or generated HTML;
3. include all **58** screenplay scene translation records exactly once and all **11** numbered-song translation records exactly once;
4. include all **1,236** screenplay unit IDs exactly once;
5. verify all **1,071/1,071** immutable dialogue links exactly once;
6. retain **19** source-unlabelled spoken units without assigning speakers;
7. retain **15** genuine cross-page screenplay translation units;
8. retain **4** screenplay performance cues without importing missing lyric bodies;
9. retain the **4** multi-page numbered-song records and their page provenance;
10. preserve song authorship tiers and the review-level song-11/scene-58 link;
11. reject synthetic scene-end prose, duplicate stage action, placeholder text, page-order regressions, duplicate IDs, missing links or provenance drift;
12. generate reproducible reader outputs consistent with mature repository policy, normally Markdown + standalone HTML + machine-readable JSON + QA report + integrity manifest;
13. after reader QA PASS, prepare source-linked Reading Room integration data for `https://nenjukkuneethi.org/read`;
14. do not create a new standalone PDF or EPUB by default.

## Repository-wide anti-staleness requirement

A phase is **not complete** until current status has been synchronized beyond `works/raja-rani/`.

After the reader/export gate, inspect and update all relevant current repository documents, including at minimum:

- work-local metadata/README/index/QA/handover/next prompt;
- `data/works.json`;
- root `README.md`;
- `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md` when project-level status changes;
- `docs/STATUS_CONSISTENCY_AUDIT.md`;
- any current shared guide/status document affected by the new phase.

Run a repository-wide stale-reference sweep before declaring completion. Historical batch checkpoints may retain historical counts if clearly labeled historical; current production/status mirrors may not remain stale.
