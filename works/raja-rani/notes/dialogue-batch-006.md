# ராஜா ராணி — Dialogue Batch 006

## Scope

Sixth and final immutable dialogue-index production batch for the currently verified scene-text layer. The batch skips blocked `s053`–`s055` and processes verified `scene-056.md` through `scene-058.md` in source order.

Source span represented by these verified scene derivatives: PDF **77–79 / printed pp.76–78**.

No dialogue shard was created for blocked `s053`, `s054` or `s055`.

## Extraction rule

Only source-visible utterances with an explicit non-empty speaker label and printed delimiter were emitted as immutable dialogue records. Source-unlabelled speech, narrative/stage material, decorative separators, song/performance cues, printer matter and other unlabelled structures remain outside the immutable dialogue index. Exact source-visible speaker-label forms and delimiters are preserved without normalization.

## Result

- `dialogues/records/scene-056.json` — **5** records
- `dialogues/records/scene-057.json` — **21** records
- `dialogues/records/scene-058.json` — **4** records

Batch total: **30 immutable labelled-dialogue records across 3 processed scenes**.

No new zero-record scene was introduced.

## Cross-page dialogue

No new labelled utterance crosses a physical page boundary in this batch. The cumulative cross-page record count therefore remains **11**.

## Source-label / no-inference observations

No new non-colon source-label delimiter anomaly was found; the cumulative anomaly count remains **3**.

Exact source-visible labels remain unnormalized, including `சம`, `ராணி`, `ஞான`, `ராஜா`, `சாந்தம்மா`, `கரண்ட்` and `சங்`.

Important exclusions in `s057`:

- after `சம: ...குறள் எல்லாருக்கும் பொது...விடு.`, the standalone `(சத்தம் கேட்கவே) யாரது...என்னு?` is not promoted into the preceding immutable dialogue record;
- the standalone `சமரசம்...ஏய்...ஏய்...என்னப்பா என்ன தகராறு...?` has no printed speaker delimiter and remains outside the immutable dialogue index;
- after `சம: இந்தா பொண்ணு இங்கவா! இவனா?...`, the standalone stage direction `(ஆமாம் என்று தலையசைக்க)` and following unlabelled `ஏய்! கொடு இப்படி. ஆளைப்பாரு...போடுங்க...` remain outside the immutable dialogue record rather than receiving inferred speaker metadata.

Important exclusions in `s058`:

- `(இருவரும் பாடுகிறார்கள்)` is a performance cue, not a labelled dialogue utterance;
- `நலம் வாழ்க!`, the final ornament and `அன்பு அச்சகம், மதுரை:-- 56` remain outside dialogue indexing.

The multi-paragraph `ராஜா:` utterance in `s058` remains one immutable record because it stays on the same verified source page and no new speaker label intervenes.

## Canonical-source status

No canonical Tamil correction was required during Dialogue Batch 006. The fidelity position remains unchanged:

- verified source pages: **75/79**
- review source pages: **4/79 — PDF 27, 48, 57, 74**
- verified screenplay pages: **66/70**
- blocked archival scenes: **8**

## Final eligible dialogue position

After Batch 006:

- eligible verified dialogue scenes: **50**
- blocked scenes: **8**
- scenes processed: **50/50 eligible**
- dialogue records: **892**
- zero-record scenes: **15** — `s008`, `s010`, `s014`, `s019`, `s020`, `s022`, `s027`, `s029`, `s030`, `s032`, `s037`, `s038`, `s042`, `s043`, `s048`
- cross-page records: **11**
- tracked non-colon source-label/delimiter anomalies: **3**

The immutable dialogue layer is therefore **complete for every scene currently eligible from verified Tamil**, while the eight source-review-blocked archival segments remain intentionally outside dialogue production.

## Next activity

Proceed to the **character/entity derivative gate** from the completed immutable dialogue inventory.

Character work may normalize or reconcile source-label variants only in its own downstream mapping. It must not rewrite the exact `speaker_label` values preserved in the 892 immutable dialogue records. The eight blocked scenes remain outside character evidence unless and until their Tamil source spans become fully verified.
