# Raja Rani — Bilingual Archive Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Active work: `works/raja-rani/` — **ராஜா ராணி**

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first in every fresh chat. Preserve any newer durable state. Do not reset, repeat or reopen completed work merely because this handover records an older checkpoint.

## Controlling source

- filename: `TVA_BOK_0017188_ராஜா_ராணி.pdf`
- PDF pages: **80**
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`
- numbered front-matter songs: PDF **4–9**
- canonical screenplay/dialogue range: PDF **10–79**, printed pp. **9–78**
- PDF 80: unnumbered back cover

Comparison files `r1.md`–`r4.md`, OCR and parsed PDF text are candidate/navigation aids only. The rendered source scan and recorded direct user scan verdicts control canonical Tamil.

## Mandatory startup

Read completely before changing anything:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `docs/SOURCE_POLICY.md`
4. `docs/TRANSCRIPTION_GUIDE.md`
5. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
6. this handover
7. `docs/NEXT_CHAT_PROMPT_RAJA_RANI.md`
8. `works/raja-rani/README.md`
9. `works/raja-rani/metadata.yaml`
10. `works/raja-rani/notes/final-source-review-resolution.md`
11. `works/raja-rani/notes/post-fidelity-corrections.md`
12. `works/raja-rani/notes/correction-005-reconciliation.md`
13. `works/raja-rani/translations/README.md`
14. `works/raja-rani/translations/index.json`
15. `works/raja-rani/translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`
16. `works/raja-rani/translations/songs/index.json`
17. `works/raja-rani/translations/songs/FINAL_NUMBERED_SONG_TRANSLATION_QA.md`
18. `works/raja-rani/songs/index.json`
19. `works/raja-rani/songs/inventory.json`
20. repository-wide current mirrors: root `README.md`, `data/works.json`, `docs/STATUS_CONSISTENCY_AUDIT.md`.

## Permanent source rules

- rendered scan evidence controls disputed characters;
- OCR/parsed PDF/comparison text are candidate readings only;
- preserve user-reviewed occurrence-specific source verdicts and exact source speaker labels;
- source-unlabelled speech remains unlabelled;
- non-canonical ownership/library stamps are not screenplay text;
- no global normalization or silent reconstruction;
- translation never repairs Tamil or upgrades song authorship;
- a major phase is not durably closed until both work-local and repository-wide current-status mirrors are synchronized.

## Final source-review state — fully closed

There are **no review/source-blocked pages or scenes**.

Durable direct-scan verdicts include:

- PDF 27: `இரவெல்லாம்`;
- PDF 48: `வந்தனா`, `திடீர்னு`;
- PDF 57: `முன்னுக்கு பின் முரணாயிகிட்டே போவது?`;
- PDF 74: `K. N. சங்கரன் ...` is a non-canonical ownership/library stamp; canonical screenplay continues directly `ஞான: நீ விதவை.` → `ராஜா: விதவை.` → `சாந்: வித்தாரக்கள்ளி! விநாசகாரி`.

Current source census:

- verified source pages: **79/79**;
- verified screenplay pages: **70/70**;
- archival scenes: **58/58 verified**, blocked **0**;
- unique immutable dialogue records: **1,071** across all 58 scenes;
- zero-dialogue scenes: **16**;
- genuine cross-page dialogue records: **12**;
- exact speaker labels: **80/80**;
- entities / roles / collectives: **44**, all verified;
- numbered songs: **11/11 Tamil derivatives**;
- screenplay singing refs: **4**;
- total song/singing occurrences: **15**;
- song authorship: **5 later-anthology Kalaignar attributions / 6 unresolved**.

## T055 / T056 boundary correction — closed

Final English QA caught a derivative segmentation error: the older scene-55 derivative duplicated the complete `(முன்)` flashback that belongs to scene 56. This is corrected without changing canonical page transcription.

Final disposition:

- scene 55 dialogue shard: **25 records**;
- scene 56 dialogue shard: **5 records**;
- corrected corpus dialogue census: **1,071**;
- deleted duplicate IDs `s055-d026`–`s055-d030` must not be restored.

Durable QA: `works/raja-rani/translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`.

## Correction 005 — closed

The late old-glyph/source correction campaign is reconciled through canonical Tamil, scenes, dialogue records, character labels/entities, affected song derivatives/metadata and English. Durable record: `works/raja-rani/notes/correction-005-reconciliation.md`.

Do not revert permanent forms such as PDF 72 `சாக்ரடீசின்`, scene-17 exact label `தர்யம்`, scene-34 corrected `ராணி` ownership, final PDF 76–79 manual adjudications, or any final source-review verdict above.

## English screenplay translation — COMPLETE

- translated scenes: **58/58**;
- verified English units: **1,236**;
- immutable dialogue links: **1,071/1,071**;
- source-unlabelled spoken units: **19**;
- genuine cross-page English units: **15**;
- screenplay performance/singing occurrences represented: **4/4**;
- unit mix: **1,090 dialogue / 137 stage direction / 4 performance cue / 5 written text**;
- draft/review screenplay units: **0/0**.

Final QA: `works/raja-rani/translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`.

## Numbered-song English translation — COMPLETE

Dedicated layer: `works/raja-rani/translations/songs/`.

- numbered song bodies: **11/11 complete-verified**;
- translation sections / source-turn groups: **67**;
- Tamil source line/cue entries represented: **181**;
- English line/cue entries represented: **181**;
- multi-page song records: **4** — songs 2, 3, 8 and 10;
- draft/review/not-started song records: **0/0/0**.

Final QA: `works/raja-rani/translations/songs/FINAL_NUMBERED_SONG_TRANSLATION_QA.md`.

Authorship is unchanged:

- **later-anthology Kalaignar-attributed:** songs **3, 5, 6, 7, 8**;
- **unresolved lyricist:** songs **1, 2, 4, 9, 10, 11**;
- original-booklet item-level lyricist credits: **0**.

Performance links are unchanged: songs 3/5/8 have verified screenplay links; song 11/scene 58 remains **review-level**.

## EXACT NEXT ACTIVITY — whole-work bilingual reader/export

The source-linked bilingual textual content is complete. Do **not** reopen normal transcription or translation production.

Build a deterministic Raja Rani bilingual reader/export from the verified structured records, following the mature repository reader pattern.

Required gate:

1. inspect current reader/export patterns from completed works such as Manohara/Parasakthi/Tirumbippaar without reusing their text;
2. define the Raja Rani reader source set from verified scene translation records plus the 11 verified numbered-song translation records;
3. preserve the source distinction between numbered front-matter songs and archive-only screenplay scene segmentation;
4. verify all 58 scene records and 11 song records are represented exactly once;
5. verify all 1,236 screenplay unit IDs exactly once and all 11 numbered-song English records exactly once;
6. preserve 1,071/1,071 immutable dialogue linkage, 19 source-unlabelled spoken units, 15 cross-page screenplay units, 4 screenplay performance cues, and 4 multi-page numbered-song records;
7. preserve source/page provenance and song authorship/performance-link tiers;
8. generate only reproducible reader outputs supported by repository policy, normally Markdown/HTML/JSON + QA/manifest;
9. after reader QA PASS, prepare source-linked Reading Room integration data for `https://nenjukkuneethi.org/read`;
10. do not create a new standalone PDF/EPUB by default.

## Repository-wide anti-staleness rule

At every major Raja Rani checkpoint, synchronize all current production surfaces, not only `works/raja-rani/`:

- work metadata/readmes/indexes/QA/handover;
- `data/works.json`;
- root `README.md`;
- `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md` when the project-level checkpoint changes;
- `docs/STATUS_CONSISTENCY_AUDIT.md`;
- any other current shared guide/status document whose instructions or counts are affected.

Historical batch reviews may retain historical counts when they are explicitly presented as historical checkpoints. Current status mirrors must not remain stale.
