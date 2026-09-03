# Raja Rani — Correction 005 downstream reconciliation

Status: **PASS — Correction 005 closed; later direct-scan source resolutions and final screenplay QA also propagated**

This mandatory startup note preserves the durable result of the late manual Correction 005 campaign while reflecting later source-review and derivative-boundary corrections. Canonical Tamil page files remain authoritative. Historical batch checkpoints must not override the current live indexes.

## Permanent invariants

- controlling screenplay: PDF 10–79; PDF 80 is back cover;
- exact source labels propagate without normalization;
- source-unlabelled speech remains unlabelled;
- English fluency is never evidence for changing Tamil;
- song authorship is not promoted without item-level evidence;
- stable IDs/provenance remain stable unless a verified derivative-boundary error requires removal of duplicate derivative IDs.

## Correction 005 — complete

The user-led old-glyph comparison campaign was reconciled through canonical Tamil, scene derivatives, dialogue records, character metadata, affected song derivatives/metadata and the English records that existed during that gate.

Important durable outcomes include:

- scene 17 exact source label `தர்யம்`;
- scene 24 `அகல்யா` material corrected without normalization;
- scene 34 `raja-rani-s034-d060` speaker ownership corrected to exact `ராணி`;
- PDF 72 `சாக்ரடீசின்`;
- final user-adjudicated PDF 76–79 forms;
- English scene 15 `கிரஷ்` represented as `Crush`;
- English scene 17 source metadata preserves `தர்யம்`;
- affected numbered-song wording reconciled without upgrading authorship.

Do not reopen Correction 005 merely because an old copied checkpoint predates later source resolutions.

## Later final source resolutions

After Correction 005, the user's direct scan review resolved every remaining source limitation:

- PDF 27: `இரவெல்லாம்`;
- PDF 48: `வந்தனா`, `திடீர்னு`;
- PDF 57: `முன்னுக்கு பின் முரணாயிகிட்டே போவது?`;
- PDF 74: `K. N. சங்கரன் ...` is a non-canonical ownership/library stamp; screenplay continues directly `ஞான: நீ விதவை.` → `ராஜா: விதவை.` → `சாந்: வித்தாரக்கள்ளி! விநாசகாரி`.

Durable detail: `works/raja-rani/notes/final-source-review-resolution.md`.

These resolutions unblocked `s011`–`s013`, `s033`, `s039`, and `s053`–`s055`. There are now **0 blocked scenes**.

## T055 / T056 derivative-boundary correction

Final English QA later found that old `scene-055.md` crossed its declared `end_before=T056` boundary and duplicated the entire `(முன்)` flashback already owned by scene 56. Its dialogue shard duplicated the five scene-56 records as `s055-d026`–`s055-d030`.

Final correction:

- scene 55 dialogue shard: **25** records;
- scene 56 dialogue shard: **5** records;
- deleted duplicate IDs: `s055-d026`–`s055-d030`;
- unique immutable dialogue corpus: **1,071**;
- canonical page transcription: **unchanged**;
- character evidence pointer formerly using `s055-d027` replaced by live scene-56 evidence.

Durable QA: `works/raja-rani/translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`.

## Current source / derivative census

The live Raja Rani-local layers reconcile as:

- canonical source pages: **79/79 verified / 0 review**;
- screenplay pages: **70/70 verified**;
- archival scenes: **58/58 verified / 0 blocked**;
- immutable dialogue records: **1,071 / 58 scenes**;
- zero-dialogue scenes: **16**;
- genuine cross-page dialogue records: **12**;
- tracked source-label/delimiter anomalies: **3**;
- exact source speaker labels: **80/80**;
- verified entities / roles / collectives: **44**.

Five exact labels entered the full census from formerly blocked scenes: `மனம்`, `நிழல்`, `ஞானக்கண் குரல்`, `ராஜாவின் குரல்`, `சமரசம் குரல்`. `மனம்` and `நிழல்` remain source-personified dramatic roles; explicit voice labels map downstream without rewriting immutable labels.

## Song/performance state

Correction 005 affected numbered-song wording on songs 1, 3, 4, 7, 8 and 11. Tamil derivatives/source excerpts were reconciled without changing authorship.

Current census:

- numbered songs / verified Tamil derivatives: **11/11**;
- screenplay singing references: **4**;
- total inventoried occurrences: **15**;
- later-anthology Kalaignar-attributed numbered songs: **5** — 3, 5, 6, 7, 8;
- unresolved lyricist: **6** — 1, 2, 4, 9, 10, 11;
- original-booklet item-level lyricist credits: **0**.

## English screenplay translation — complete

The English screenplay layer subsequently advanced through every source-verified scene and is now closed:

- translated scenes: **58/58**;
- verified English units: **1,236**;
- immutable dialogue links: **1,071/1,071**;
- source-unlabelled spoken units: **19**;
- genuine cross-page English units: **15**;
- screenplay performance occurrences represented: **4/4**;
- unit mix: **1,090 dialogue / 137 stage direction / 4 performance cue / 5 written text**;
- draft/review screenplay units: **0**.

Final reviews:

- `works/raja-rani/translations/BATCH_011_040_REVIEW.md`
- `works/raja-rani/translations/BATCH_041_058_REVIEW.md`
- `works/raja-rani/translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`

Historical batch files should remain historically accurate; they need not be rewritten to pretend later source resolutions were known earlier.

## Current production activity

Screenplay translation is complete. The remaining English work is the separate **11 numbered front-matter song bodies**.

Translate songs 1–11 in source order through a dedicated source-linked song layer while preserving verified Tamil text, page provenance, existing performance relationships and current authorship tiers. Do not infer unresolved lyricists or upgrade scene 58's review-level song-11 relationship.

## Shared mirrors

`data/works.json` and the repository root README may lag this work-local state. Do not let stale shared mirrors override Raja Rani-local indexes, metadata, README, handover or final QA.
