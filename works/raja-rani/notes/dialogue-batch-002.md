# ராஜா ராணி — Dialogue Batch 002

## Scope

Second immutable dialogue-index production batch after completion of the verified scene-text layer.

The batch resumes after the blocked `s011`–`s013` group and processes verified scene derivatives:

- `scene-014.md` through `scene-023.md`
- archival IDs `raja-rani-s014` through `raja-rani-s023`
- source span covered by those scenes: PDF **28–40 / printed pp.27–39**

No dialogue shard was created for blocked `s011`, `s012` or `s013`.

## Extraction rule

Only source-visible utterances with an explicit non-empty speaker label and printed delimiter were emitted as immutable dialogue records.

Not promoted into dialogue records:

- source-unlabelled speech or text lacking an explicit speaker delimiter;
- narrative/stage material without a speaker label;
- decorative scene separators;
- song/performance cues;
- dialogue implied only from context.

Exact source speaker labels and printed delimiters were retained. Character-name normalization remains deferred to the later character/entity layer.

## Result

Dialogue shard files created:

- `dialogues/records/scene-014.json` — **0** records
- `dialogues/records/scene-015.json` — **36** records
- `dialogues/records/scene-016.json` — **10** records
- `dialogues/records/scene-017.json` — **48** records
- `dialogues/records/scene-018.json` — **41** records
- `dialogues/records/scene-019.json` — **0** records
- `dialogues/records/scene-020.json` — **0** records
- `dialogues/records/scene-021.json` — **50** records
- `dialogues/records/scene-022.json` — **0** records
- `dialogues/records/scene-023.json` — **36** records

Batch total: **221 immutable labelled-dialogue records across 10 processed scenes**.

Zero-record verified scenes in this batch:

- `raja-rani-s014`
- `raja-rani-s019`
- `raja-rani-s020`
- `raja-rani-s022`

These scenes contain only source transition/stage descriptions and therefore correctly remain zero-dialogue scenes.

## Cross-page dialogue records

One new explicitly labelled utterance crosses a physical source page boundary and remains one immutable record with `page_provenance` plus `page_segments`:

- `raja-rani-s021-d048` — PDF **37→38 / printed 36→37** (`சம:`), preserving the physical-page split inside `வளர்த்` / `துடுச்சே` rather than silently rewriting the source segmentation.

Cumulative cross-page dialogue records after Batch 002: **4**.

## Source-label / delimiter observations

No new non-colon speaker-label delimiter anomaly was promoted in this batch. The three Batch-001 tracked anomaly records remain the cumulative set.

Exact source-visible label variation and abbreviations such as `கர`, `வந்`, `சாந்`, `சமை`, `ராஜா` and `ராசா` remain unnormalized in the immutable dialogue layer.

## Important exclusions observed

- In `s015`, `ராணி வெளியிலே போர்டு பார்த்தேன்.` has no printed delimiter after `ராணி`; it therefore remains outside the immutable dialogue index rather than receiving an inferred colon.
- In `s015`, `[கதவு தட்டப்படுகிறது] எஸ் கமின்...` and the later unlabelled `சாப்புடு...டேய் கரண்ட்!...` are not assigned to an inferred speaker.
- `s014`, `s019`, `s020` and `s022` are transition-only verified scenes and correctly produce zero records.
- No dialogue record was created from blocked `s011`–`s013`.

## Canonical-source status

No new canonical Tamil correction was required during this dialogue batch. Dialogue extraction used the already verified scene derivatives as the immediate source layer and did not alter page transcription or scene text.

The global Tamil fidelity position remains unchanged:

- verified source pages: **75/79**
- review source pages: **4/79 — PDF 27, 48, 57, 74**
- verified screenplay pages: **66/70**
- blocked archival scenes: **8**

## Cumulative dialogue position

After Batch 002:

- eligible verified dialogue scenes: **50**
- blocked scenes: **8**
- scenes processed: **20/50**
- dialogue records: **424**
- zero-record scenes: **6** — `s008`, `s010`, `s014`, `s019`, `s020`, `s022`
- cross-page records: **4**
- tracked non-colon source-label/delimiter anomalies: **3**

## Next activity

**Dialogue Batch 003:** process verified `scene-024.md` through `scene-032.md` in source order, then stop before blocked `s033`.

Preserve the same immutable-record rules, exact source labels/delimiters, page provenance and cross-page continuity. Do not create a dialogue shard for blocked `s033`.
