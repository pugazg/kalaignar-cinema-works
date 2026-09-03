# ராஜா ராணி — Post-Fidelity Source Corrections

## Purpose

Record source-backed corrections discovered after the full rendered-scan fidelity phase had already been closed-with-source-limitations.

The controlling source remains `TVA_BOK_0017188_ராஜா_ராணி.pdf`. Corrections in this file are accepted only from direct reinspection of the rendered scan or an explicit user verdict based on direct inspection of that controlling scan. OCR, film audio, subtitles, web text, later editions and contextual reconstruction are not canonical authority.

## Correction 001 — PDF 49–50 / printed pp.48–49

During preparation of scene-text Batch 005, PDF 49 and PDF 50 were reopened against fresh high-resolution renders because their local page headers still carried stale bookkeeping.

The recheck found source-label normalization errors:

- **PDF 49:** source-visible dialogue label **`ராசா:`** was restored where the first pass had normalized it to `ராஜா:`.
- **PDF 50:** the same source-visible **`ராசா:`** dialogue form was restored.
- PDF 50 separately prints the stage-direction name as **`ராஜா`**; that distinct source form was preserved.

No unrelated wording was changed.

## Correction 002 — PDF 53 / printed p.52

The scan confirms:

- dialogue labels print **`ராசா:`**, not normalized `ராஜா:`;
- the T036 stage direction prints **`(ராசா, ராணியைக் கொண்டு வந்து விடுகிறான்...)`**.

The canonical page and downstream derivatives were reconciled accordingly.

## Correction 003 — PDF 58–59 / printed pp.57–58

Fresh high-resolution review confirmed that the source deliberately alternates `ராஜா:` and `ராசா:` on these pages. Only the normalized occurrences were restored; genuinely printed `ராஜா:` labels and stage-direction forms were left unchanged.

## Correction 004 — PDF 66 / printed p.65

The first dialogue label at the top of PDF 66 is visibly **`ராசா:`**. The canonical page had normalized it to `ராஜா:`. The dialogue label was restored while distinct running-text `ராஜா` forms on the same page were preserved.

## Correction 005 — user-led old-glyph comparison campaign

A later comparison campaign reopened canonical wording after derivative layers had already been built. The user compared repository pages against `r1.md`, `r2.md`, `r3.md` and later comparison material, then manually inspected disputed words in the scan because the old Tamil typeface caused repeated OCR and visual-reading errors.

Permanent policy established by this campaign:

- repository text and OCR/comparison text are candidate readings only;
- rendered scan evidence controls disputed old-typeface glyphs;
- the user's explicit manual scan verdict controls that reviewed occurrence unless later stronger direct source evidence reopens it;
- occurrence-specific variation must remain occurrence-specific;
- no global modernization or normalization.

The campaign was completed through the final PDF 075–080 comparison and its downstream reconciliation. The dedicated durable reconciliation record is:

`works/raja-rani/notes/correction-005-reconciliation.md`

Important retained source forms include:

- PDF 59: **`நினைக்கிறேன்`** for the explicitly adjudicated Neither case;
- PDF 69: **`வீசும்`** for the explicitly adjudicated Neither case;
- PDF 71: **`மாறினான்`**;
- PDF 72: **`சாக்ரடீசின்`**;
- scene 17 exact source label: **`தர்யம்`**;
- scene 34 corrected ownership occurrence: **`ராணி`**;
- final manually adjudicated PDF 76–79 forms recorded in the reconciliation note.

Correction 005 downstream reconciliation has **passed**. English translation production is no longer paused by that campaign.

## Correction 006 — PDF 48 / printed p.47 direct-scan resolution

PDF 48 remained a bounded review page after the earlier fidelity gate because two short spans in Raja's recollection immediately before `சமரசம் வீடு` were visually insecure.

A comparison extract suggested candidate readings, after which the user directly inspected the controlling PDF and authoritatively resolved the two spans as:

- **`வந்தனா`**
- **`திடீர்னு`**

The canonical passage now reads:

`...நான் எடுத்துகிட்டு...ஒன்கிட்ட கொடுக்கிறதுக்கு வந்தனா? வந்தா திடீர்னு சமரசம் வீடு...`

This is a direct source-backed resolution, not an OCR substitution.

### Downstream propagation of Correction 006

The resolution has been propagated through:

- `pages/048.md` — status promoted to `verified`;
- `scenes/scene-033.md` — created as complete-verified;
- `dialogues/records/scene-033.json` — **57 immutable labelled records**;
- `scenes/index.json` and `dialogues/index.json`;
- character label inventory and entity mapping;
- `metadata.yaml` and work README;
- translation eligibility/index/README;
- Tamil fidelity disposition;
- Raja Rani handover and next-chat prompt;
- Correction 005 reconciliation state note.

Scene 33 has one genuine PDF 48→49 cross-page dialogue record (`raja-rani-s033-d049`). The scene introduces no new exact speaker-label string and no new character entity.

## Current source-fidelity census

After Correction 006:

- audited source pages: **79/79**;
- verified source pages: **76/79**;
- review source pages: **3/79 — PDF 27, 57, 74**;
- audited screenplay pages: **70/70**;
- verified screenplay pages: **67/70**;
- review screenplay pages: **3/70**.

Current blocked scenes are therefore only:

- `s011`–`s013` — PDF 27;
- `s039` — PDF 57;
- `s053`–`s055` — PDF 74.

`raja-rani-s033` is no longer blocked.

## Current structured-derivative census

- archival scene segments: **58**;
- eligible verified scene derivatives: **51**;
- blocked scene derivatives: **7**;
- immutable dialogue records: **949**;
- dialogue cross-page records: **12**;
- exact source speaker labels: **75/75**;
- character entities / roles / collectives: **42**;
- English translation eligibility: **51 scenes**.

## Current translation frontier

The completed translation checkpoint remains **30/51 eligible scenes / 715 verified English units / 622/622 immutable dialogue links in translated scenes**.

Per the user's 10-scene iteration rule, the next eligible translation batch is:

`raja-rani-s033`, `s035`, `s036`, `s037`, `s038`, skip blocked `s039`, then `s040`, `s041`, `s042`, `s043`, `s044`.

## Rule for future source corrections

If new direct scan evidence changes a canonical reading:

1. update the canonical page first;
2. record the source-backed verdict here or in the appropriate dedicated audit note;
3. reconcile only the affected scene/dialogue/character/song/translation derivatives;
4. preserve stable IDs and page provenance wherever structure itself has not changed;
5. update the current work-local census before resuming downstream production.
