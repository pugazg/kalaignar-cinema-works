# Raja Rani — Correction 005 downstream reconciliation

Status: **PASS — Correction 005 closed; later direct-scan source resolutions also propagated**

This note preserves the durable downstream result of the late manual Correction 005 campaign. Canonical Tamil page files remain authoritative. Subsequent source-review resolutions are recorded separately in `final-source-review-resolution.md` but their current census is reflected here so this mandatory startup note does not regress the repository state.

## Permanent invariants

- controlling screenplay: PDF 10–79; PDF 80 is back cover;
- exact source labels propagate without normalization;
- source-unlabelled speech remains unlabelled;
- English fluency is never evidence for changing Tamil;
- song authorship is not promoted without item-level evidence;
- existing stable IDs and provenance remain stable unless source structure itself changes.

## Correction 005 — complete

The user-led old-glyph comparison campaign was reconciled through canonical Tamil, scene derivatives, dialogue records, character metadata, affected song derivatives/metadata and all English records that existed during the gate.

Important durable outcomes include:

- scene 17 exact source label `தர்யம்`;
- scene 24 `அகல்யா` material corrected without normalization;
- scene 34 corrected `raja-rani-s034-d060` speaker ownership to exact `ராணி`;
- PDF 72 `சாக்ரடீசின்`;
- final user-adjudicated PDF 76–79 forms;
- English scene 15 `கிரஷ்` preserved as `Crush`;
- English scene 17 source metadata preserves `தர்யம்`;
- affected numbered-song wording reconciled without upgrading authorship.

The Correction 005 content and count QA passed. Do not reopen this campaign merely because a copied historical checkpoint predates later source resolutions.

## Later final source resolutions

After Correction 005, the user's direct scan review subsequently resolved every remaining source limitation:

- PDF 27: `இரவெல்லாம்`;
- PDF 48: `வந்தனா`, `திடீர்னு`;
- PDF 57: `முன்னுக்கு பின் முரணாயிகிட்டே போவது?`;
- PDF 74: `K. N. சங்கரன் ...` is a non-canonical ownership/library stamp; the screenplay continues directly from `ராஜா: விதவை.` to `சாந்: வித்தாரக்கள்ளி! விநாசகாரி`.

Durable detail: `works/raja-rani/notes/final-source-review-resolution.md`.

These later resolutions unblocked `s011`–`s013`, `s033`, `s039`, and `s053`–`s055` and were propagated through canonical pages, scene/dialogue derivatives, character mapping and production metadata.

## Current source / derivative census

The live Raja Rani-local layers now reconcile as:

- canonical source pages: **79/79 verified / 0 review**;
- screenplay pages: **70/70 verified**;
- archival scenes: **58/58 verified / 0 blocked**;
- immutable dialogue records: **1,076 / 58 scenes**;
- zero-dialogue scenes: **16**;
- genuine cross-page dialogue records: **12**;
- tracked source-label/delimiter anomalies: **3**;
- exact source speaker labels: **80/80**;
- verified entities / roles / collectives: **44**.

Five exact labels entered the full census from formerly blocked scenes: `மனம்`, `நிழல்`, `ஞானக்கண் குரல்`, `ராஜாவின் குரல்`, `சமரசம் குரல்`. `மனம்` and `நிழல்` remain separate source-personified dramatic roles; the three explicit voice labels map to established characters downstream without rewriting the immutable labels.

## Song/performance state

Correction 005 affected numbered-song wording on songs 1, 3, 4, 7, 8 and 11. Tamil derivatives and embedded source excerpts were reconciled without changing authorship disposition.

Current census:

- numbered songs / verified Tamil derivatives: **11/11**;
- screenplay singing references: **4**;
- total occurrences: **15**;
- later anthology Kalaignar-attributed numbered songs: **5** — 3, 5, 6, 7, 8;
- unresolved lyricist: **6** — 1, 2, 4, 9, 10, 11;
- original-booklet item-level lyricist credits: **0**.

## English translation state

The later source-resolution pass added no English content. Current checkpoint remains:

- translated scenes: **30/58** — scenes 1–10, 14–32, 34;
- verified English units: **715**;
- immutable dialogue links in translated scenes: **622/622**;
- source-unlabelled spoken units: **11**;
- cross-page English units: **6**;
- translated screenplay performance occurrences: **2**;
- unit mix: **633 dialogue / 78 stage direction / 2 performance cue / 2 written text**.

The historical `BATCH_024_034_REVIEW.md` correctly records that s033 was unavailable when that batch ran. Historical batch files should not be rewritten to pretend later source resolutions existed earlier.

## Next production activity

Per user instruction, process **10 verified untranslated scenes per iteration**, in source order.

Next batch:

`raja-rani-s011`, `s012`, `s013`, `s033`, `s035`, `s036`, `s037`, `s038`, `s039`, `s040`.

There are now **no source-review skips**.

## Shared mirrors

`data/works.json` and root README may lag the work-local state. Do not let stale shared mirrors override the Raja Rani-local indexes, metadata, README, handover and translation index.
