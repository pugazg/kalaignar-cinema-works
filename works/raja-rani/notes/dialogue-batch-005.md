# ராஜா ராணி — Dialogue Batch 005

## Scope

Fifth immutable dialogue-index production batch. The batch skips blocked `s039`, processes verified `scene-040.md` through `scene-052.md` in source order, and stops before blocked `s053`–`s055`.

Source span represented by these verified scene derivatives: PDF **58–73 / printed pp.57–72**.

No dialogue shard was created for blocked `s039`, `s053`, `s054` or `s055`.

## Extraction rule

Only source-visible utterances with an explicit non-empty speaker label and printed delimiter were emitted as immutable dialogue records. Source-unlabelled speech, narrative/stage material, decorative separators and written material remain outside the immutable dialogue index. Exact source-visible speaker-label forms and delimiters are preserved without normalization.

## Result

- `dialogues/records/scene-040.json` — **17** records
- `dialogues/records/scene-041.json` — **41** records
- `dialogues/records/scene-042.json` — **0** records
- `dialogues/records/scene-043.json` — **0** records
- `dialogues/records/scene-044.json` — **11** records
- `dialogues/records/scene-045.json` — **28** records
- `dialogues/records/scene-046.json` — **5** records
- `dialogues/records/scene-047.json` — **10** records
- `dialogues/records/scene-048.json` — **0** records
- `dialogues/records/scene-049.json` — **3** records
- `dialogues/records/scene-050.json` — **4** records
- `dialogues/records/scene-051.json` — **25** records
- `dialogues/records/scene-052.json` — **21** records

Batch total: **165 immutable labelled-dialogue records across 13 processed scenes**.

Zero-record verified scenes in this batch: `s042`, `s043`, `s048`.

## Cross-page dialogue

Six new genuine cross-page utterances remain single immutable records with explicit `page_segments`:

- `raja-rani-s040-d008` — PDF **58→59 / printed 57→58** (`ராணி:`)
- `raja-rani-s044-d011` — PDF **62→63 / printed 61→62** (`ராஜா:`)
- `raja-rani-s046-d001` — PDF **64→65 / printed 63→64** (`பாபு:`)
- `raja-rani-s050-d001` — PDF **66→67 / printed 65→66** (`சாக்ரடீஸ்:`)
- `raja-rani-s051-d025` — PDF **69→70 / printed 68→69** (`சாக்:`)
- `raja-rani-s052-d011` — PDF **71→72 / printed 70→71** (`சாக்:`)

Cumulative cross-page dialogue records after Batch 005: **11**.

## Source-label / no-inference observations

No new non-colon source-label delimiter anomaly was found; the cumulative anomaly count remains **3**.

Exact source variants and abbreviations remain unnormalized, including `ராஜா`, `ராசா`, `ரா`, `சாக்ரடீஸ்`, `சாக்`, `கிரி`, `கிரீட்`, `கிரிட்`, `அனி`, `மெலி`, `ஞான`, `சம`, `சாந்`, `சமை` and `கர`.

Important exclusions:

- `s049`: the suicide-letter body and signature `ராணி.` are written material, not explicitly speaker-labelled dialogue.
- `s052`: after `[அவள் போனபிறகு]`, the unlabelled `கிரீட்டோ! உனக்குத் தெரியுமல்லவா?...` remains outside the dialogue layer.
- `s052`: after `[மெலிடஸ் உருவ பாபு திகைக்கிறான்.]`, the unlabelled `ஏ, மெலிடஸ், வா இங்கே...` remains outside the dialogue layer.
- `s052`: the source-unlabelled `சாந்தம், பாத்தியா உன் தம்பி செஞ்ச வேலையை?` remains unassigned; no speaker was inferred.

## Canonical-source status

No new canonical Tamil correction was required during this dialogue batch. The fidelity position remains unchanged:

- verified source pages: **75/79**
- review source pages: **4/79 — PDF 27, 48, 57, 74**
- verified screenplay pages: **66/70**
- blocked archival scenes: **8**

## Cumulative dialogue position

After Batch 005:

- eligible verified dialogue scenes: **50**
- blocked scenes: **8**
- scenes processed: **47/50**
- dialogue records: **862**
- zero-record scenes: **15** — `s008`, `s010`, `s014`, `s019`, `s020`, `s022`, `s027`, `s029`, `s030`, `s032`, `s037`, `s038`, `s042`, `s043`, `s048`
- cross-page records: **11**
- tracked non-colon source-label/delimiter anomalies: **3**

## Next activity

**Dialogue Batch 006:** skip blocked `s053`–`s055` and process the final eligible verified `scene-056.md` through `scene-058.md` in source order.

That batch should close the dialogue layer at **50/50 eligible scenes** while leaving all eight source-review-blocked scenes outside immutable dialogue production. After dialogue completion, proceed to the character/entity derivative gate rather than normalizing source labels inside dialogue records.
