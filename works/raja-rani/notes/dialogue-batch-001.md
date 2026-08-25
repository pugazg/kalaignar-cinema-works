# ராஜா ராணி — Dialogue Batch 001

## Scope

First immutable dialogue-index production batch after completion of the verified scene-text layer.

Processed verified scene derivatives:

- `scene-001.md` through `scene-010.md`
- archival IDs `raja-rani-s001` through `raja-rani-s010`
- source span covered by those scenes: PDF **10–25 / printed pp.9–24**

The batch stops before `s011`–`s013`, which remain blocked because their scene spans intersect review-source PDF 27.

## Extraction rule

Only source-visible utterances with an explicit non-empty speaker label were emitted as immutable dialogue records.

Not promoted into dialogue records:

- source-unlabelled speech;
- narrative/stage material without a speaker label;
- decorative scene separators;
- written newspaper/letter text;
- source-unlabelled ceremonial/performance speech;
- dialogue implied only from context.

Exact source speaker labels and printed delimiters were retained. Character-name normalization is deferred to the later character/entity layer.

## Result

Dialogue shard files created:

- `dialogues/records/scene-001.json` — **9** records
- `dialogues/records/scene-002.json` — **21** records
- `dialogues/records/scene-003.json` — **27** records
- `dialogues/records/scene-004.json` — **23** records
- `dialogues/records/scene-005.json` — **22** records
- `dialogues/records/scene-006.json` — **13** records
- `dialogues/records/scene-007.json` — **30** records
- `dialogues/records/scene-008.json` — **0** records
- `dialogues/records/scene-009.json` — **58** records
- `dialogues/records/scene-010.json` — **0** records

Batch total: **203 immutable labelled-dialogue records across 10 processed scenes**.

Zero-record verified scenes:

- `raja-rani-s008`
- `raja-rani-s010`

Both contain only source stage/transition material and therefore correctly remain zero-dialogue scenes.

## Cross-page dialogue records

Three explicitly labelled utterances cross physical source pages and remain single immutable records with `page_provenance` plus `page_segments`:

1. `raja-rani-s004-d006` — PDF 13→14 / printed 12→13 (`மன்:`)
2. `raja-rani-s004-d023` — PDF 14→15 / printed 13→14 (`புல:`)
3. `raja-rani-s005-d010` — PDF 15→18 / printed 14→17 (`சேரன்:`), including the complete source-continuous long recitation

No other Batch-001 labelled utterance crosses a physical page boundary.

## Source-label / delimiter anomalies retained

Three non-colon source delimiters are intentionally preserved and tracked rather than normalized:

- `raja-rani-s004-d001` — `நாடகத் துவக்கத்திற்கு முன்பு குரல்.` → delimiter `.`
- `raja-rani-s004-d007` — `தமிழ்நாட்டுப் புலவர்.` → delimiter `.`
- `raja-rani-s007-d023` — `கீதாவின் தாய் தாயம்மாள்;` → delimiter `;`

These are source-label forms in the verified scene layer, not character-normalization decisions.

## Important exclusions observed

- In `s004`, the source-unlabelled ceremonial call beneath `கனக விசயர் சபை` is not assigned an invented speaker.
- In `s007`, the unlabelled continuation around the ring-giving stage action after `சம: கொடுத்தா போச்சு...` is not assigned to Samarasam by inference.
- In `s009`, newspaper headlines, the printed letter to Leela, its continuation across PDF 22→23, and other unlabelled written/narrative material remain outside the immutable dialogue index.
- The two transition-only scenes `s008` and `s010` correctly produce zero records.

## Canonical-source status

No new canonical Tamil correction was required during this dialogue batch. Dialogue extraction used the already verified scene derivatives as the immediate source layer and did not alter page transcription or scene text.

The global Tamil fidelity position is unchanged:

- verified source pages: **75/79**
- review source pages: **4/79 — PDF 27, 48, 57, 74**
- verified screenplay pages: **66/70**
- blocked archival scenes: **8**

## Cumulative dialogue position

After Batch 001:

- eligible verified dialogue scenes: **50**
- blocked scenes: **8**
- scenes processed: **10/50**
- dialogue records: **203**
- zero-record scenes: **2**
- cross-page records: **3**
- tracked non-colon source-label/delimiter anomalies: **3**

## Next activity

Dialogue Batch 002: resume after blocked `s011`–`s013` and process verified `scene-014.md` through `scene-023.md` in source order.

Preserve the same immutable-record rules, exact source labels/delimiters and cross-page continuity. Do not create dialogue shards for blocked `s011`–`s013`.
