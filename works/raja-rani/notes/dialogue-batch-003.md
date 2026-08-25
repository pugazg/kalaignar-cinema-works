# ராஜா ராணி — Dialogue Batch 003

## Scope

Third immutable dialogue-index production batch after completion of the verified scene-text layer.

Processed verified scene derivatives:

- `scene-024.md` through `scene-032.md`
- archival IDs `raja-rani-s024` through `raja-rani-s032`
- source span covered by those scenes: PDF **40–46 / printed pp.39–45**

The batch stops before blocked `s033`, whose scene span intersects review-source PDF 48. No dialogue shard was created for `s033`.

## Extraction rule

Only source-visible utterances with an explicit non-empty speaker label and printed delimiter were emitted as immutable dialogue records.

Not promoted into dialogue records:

- source-unlabelled speech or text lacking an explicit speaker delimiter;
- narrative/stage material without a speaker label;
- decorative scene separators;
- dialogue implied only from context.

Exact source speaker labels and printed delimiters were retained. Character-name normalization remains deferred to the later character/entity layer.

## Result

Dialogue shard files created:

- `dialogues/records/scene-024.json` — **32** records
- `dialogues/records/scene-025.json` — **33** records
- `dialogues/records/scene-026.json` — **1** record
- `dialogues/records/scene-027.json` — **0** records
- `dialogues/records/scene-028.json` — **64** records
- `dialogues/records/scene-029.json` — **0** records
- `dialogues/records/scene-030.json` — **0** records
- `dialogues/records/scene-031.json` — **3** records
- `dialogues/records/scene-032.json` — **0** records

Batch total: **133 immutable labelled-dialogue records across 9 processed scenes**.

Zero-record verified scenes in this batch:

- `raja-rani-s027`
- `raja-rani-s029`
- `raja-rani-s030`
- `raja-rani-s032`

These scenes contain only source transition/stage descriptions and therefore correctly remain zero-dialogue scenes.

## Cross-page dialogue records

No new labelled utterance in Batch 003 crosses a physical source page boundary.

Cumulative cross-page dialogue records therefore remain **4**:

- `raja-rani-s004-d006`
- `raja-rani-s004-d023`
- `raja-rani-s005-d010`
- `raja-rani-s021-d048`

## Source-label / delimiter observations

No new non-colon speaker-label delimiter anomaly was observed in this batch. The three Batch-001 anomaly records remain the cumulative set.

Exact source-visible variants and abbreviations remain immutable, including forms such as `இந்தி`, `அகல்`, `முனி`, `ராஜ`, `ராசா`, `சாந்`, `சம`, and `வேலை`.

## Important exclusions observed

- In `s028`, the PDF-46 continuation `இந்தா! அது வச்சு இருந்தேனே. அது எங்கே?` has no printed speaker label/delimiter in the verified scene derivative, so it remains outside the immutable dialogue index rather than being assigned by context.
- `s027`, `s029`, `s030` and `s032` are transition-only verified scenes and correctly produce zero records.
- No dialogue record was created from blocked `s033`.

## Canonical-source status

No new canonical Tamil correction was required during this dialogue batch. Dialogue extraction used the already verified scene derivatives as the immediate source layer and did not alter page transcription or scene text.

The global Tamil fidelity position remains unchanged:

- verified source pages: **75/79**
- review source pages: **4/79 — PDF 27, 48, 57, 74**
- verified screenplay pages: **66/70**
- blocked archival scenes: **8**

## Cumulative dialogue position

After Batch 003:

- eligible verified dialogue scenes: **50**
- blocked scenes: **8**
- scenes processed: **29/50**
- dialogue records: **557**
- zero-record scenes: **10** — `s008`, `s010`, `s014`, `s019`, `s020`, `s022`, `s027`, `s029`, `s030`, `s032`
- cross-page records: **4**
- tracked non-colon source-label/delimiter anomalies: **3**

## Next activity

**Dialogue Batch 004:** skip blocked `s033`, then process verified `scene-034.md` through `scene-038.md` in source order and stop before blocked `s039`.

Preserve the same immutable-record rules, exact source labels/delimiters, page provenance and cross-page continuity. Do not create dialogue shards for blocked `s033` or `s039`.
