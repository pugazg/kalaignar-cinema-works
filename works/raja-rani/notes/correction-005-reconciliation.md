# Raja Rani — Correction 005 downstream reconciliation

Status: **content reconciliation and QA passed; subsequent PDF-48 source resolution propagated; shared repository mirrors may lag**

This note preserves the durable downstream state after the late manual source-correction campaign recorded as Correction 005 and later source-backed resolutions. Canonical Tamil page files remain authoritative.

## Permanent invariants

- Controlling screenplay span: PDF 10–79; PDF 80 is the blank back cover.
- Existing dialogue IDs, scene IDs, translation unit IDs and page provenance remain stable unless the source unit itself changes structurally.
- Corrected exact speaker labels propagate without normalization.
- Source-unlabelled speech remains unlabelled.
- English fluency is never evidence for changing Tamil.
- Song authorship is not promoted without item-level evidence.
- Current review/source-limited pages are only PDF **27, 57 and 74**.

## Correction 005 canonical / scene / dialogue propagation — complete

The Correction 005 source-order propagation pass was completed through the end of the screenplay for all scenes eligible at the time. Existing scene and dialogue IDs/provenance were retained.

Important durable corrections include:

- scene 017 exact source label `தர்யம்`, retained without normalization;
- scene 024 `அகல்யா நாடக ஒத்திகை` corrections across PDFs 40–42;
- scene 034 corrected PDF-52 ownership label, with stable `raja-rani-s034-d060` now `ராணி`;
- scene 040/041 corrections across PDFs 58–61;
- scene 044/046/050/051/052 cross-page and source-text reconciliations;
- PDF 72 `சாக்ரடீசின்`;
- final user-adjudicated PDF 76–79 forms.

Scene/dialogue files not text-affected were checked without unnecessary rewrites. Review-source scenes were never reconstructed from context or OCR.

## Subsequent PDF 48 resolution — scene 33 unblocked

At the time Correction 005 originally closed, PDF 48 / printed p.47 still carried two explicit uncertain spans immediately before `சமரசம் வீடு`, so scene 33 was correctly excluded from verified derivatives.

The user later inspected the controlling PDF directly and resolved those two occurrences as:

- **`வந்தனா`**
- **`திடீர்னு`**

The canonical passage is now:

`...நான் எடுத்துகிட்டு...ஒன்கிட்ட கொடுக்கிறதுக்கு வந்தனா? வந்தா திடீர்னு சமரசம் வீடு...`

This later source-backed resolution has now been propagated through:

- `pages/048.md` — promoted from review to verified;
- `scenes/scene-033.md` — newly created as complete-verified;
- `dialogues/records/scene-033.json` — **57 immutable labelled records**;
- scene/dialogue indexes;
- character label inventory and entity mapping;
- work metadata / README;
- translation eligibility/index/README;
- Raja Rani handover and next-chat prompt;
- Tamil fidelity disposition note.

Scene 33 includes one genuine PDF 48→49 cross-page dialogue record, `raja-rani-s033-d049`. It introduces no new exact speaker-label string and no new character entity.

## Current blocked scenes

Only the following remain blocked by currently unresolved source pages:

- scenes `s011`–`s013` — PDF 27;
- scene `s039` — PDF 57;
- scenes `s053`–`s055` — PDF 74.

Scene `s033` is **not blocked** anymore.

## English translation reconciliation and production state

All English records that existed during the Correction 005 reconciliation were audited against their corrected Tamil source. Notable durable repairs include:

- scene 15 `raja-rani-en-s015-u020`: source `கிரஷ்` preserved as `Crush`;
- scene 17 `raja-rani-en-s017-u017`: exact source metadata label `தர்யம்` preserved;
- scene 6 source-visible `வீசினாய்` correction reflected in English;
- corrected anomalous/source-exact readings in scenes 2–5 retained without silently repairing Tamil.

Normal source-linked English production subsequently resumed. Current verified translation checkpoint is:

- translated eligible scenes: **30 / 51**;
- translated scenes: **1–10, 14–32, 34**;
- verified English units: **715**;
- immutable dialogue links in translated scenes: **622 / 622**;
- source-unlabelled spoken units: **11**;
- cross-page English units: **6**;
- translated screenplay performance occurrences: **2**;
- unit mix: **633 dialogue / 78 stage direction / 2 performance cue / 2 written text**.

The historical `BATCH_024_034_REVIEW.md` correctly records that scene 33 was skipped when that batch ran because PDF 48 was unresolved at that time. That historical batch record should not be rewritten to pretend scene 33 was eligible then. Scene 33 is instead the first scene in the next production batch.

## Character/entity reconciliation — current

The source-exact `தர்யம்` occurrence remains a distinct exact label mapped to the existing Thayammal entity. Scene 33 adds only occurrences of already-known `ராஜா`, `ராசா` and `ராணி` labels.

Current character census:

- dialogue records considered: **949**;
- eligible dialogue scenes: **51**;
- distinct exact source labels: **75**;
- labels dispositioned: **75/75**;
- entities / roles / collectives: **42**;
- verified entities: **42**;
- unresolved/review labels or entities: **0**.

## Song/performance reconciliation — complete

Correction 005 affected numbered-song source wording on songs **1, 3, 4, 7, 8 and 11**. Those Tamil derivatives and embedded source excerpts were reconciled without changing authorship dispositions.

Current song census:

- numbered song blocks / verified Tamil derivatives: **11/11**;
- screenplay singing references: **4**;
- total song/performance occurrences: **15**;
- numbered songs later anthology-attributed to Kalaignar: **5** — 3, 5, 6, 7, 8;
- numbered songs with unresolved lyricist: **6** — 1, 2, 4, 9, 10, 11;
- original-booklet item-level lyricist credits: **0**.

Performance links remain:

- scene 4 → song 3: verified;
- scene 16 → song 5: verified;
- scene 40 → song 8: verified;
- scene 58 → song 11: review.

## Current QA / count-consistency result — PASS

The Raja Rani-local authoritative layers now reconcile numerically:

- canonical source: **76 verified pages / 3 review pages**;
- screenplay: **67 verified / 3 review**;
- scene index: **58 archival / 51 eligible verified / 7 blocked**;
- dialogue index: **949 records / 51 eligible scenes / 7 blocked / 12 cross-page records / 3 tracked source-label anomalies**;
- character index: **75/75 exact labels / 42 entities**;
- song index: **11 numbered + 4 screenplay references = 15 occurrences**;
- translation index: **30/51 scenes / 715 units / 622/622 dialogue links in translated scenes**.

No Correction-005 content inconsistency remains, and the later PDF-48 resolution has been propagated through every source/structural layer needed to make scene 33 eligible for translation.

## Current translation production policy

Per user instruction, process **10 eligible verified scenes per iteration**. A blocked scene does not count toward the 10.

The exact next 10 eligible scenes are:

1. `raja-rani-s033`
2. `raja-rani-s035`
3. `raja-rani-s036`
4. `raja-rani-s037`
5. `raja-rani-s038`
6. skip blocked `raja-rani-s039`
7. `raja-rani-s040`
8. `raja-rani-s041`
9. `raja-rani-s042`
10. `raja-rani-s043`
11. `raja-rani-s044`

This is exactly 10 eligible translated scenes because s039 is excluded.

## Shared repository mirrors

`data/works.json` and the root README are shared repository mirrors and may still lag the Raja Rani-local checkpoint. Do not treat a stale shared mirror as authority over the live Raja Rani indexes, metadata, README, handover and translation index. Update shared registry files only when they can be rewritten safely without risking unrelated works.

## Current checkpoint rule

Fetch live `main` before every subsequent write. This note is a durable state description, not a substitute for the live branch.
