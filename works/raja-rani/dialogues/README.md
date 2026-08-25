# ராஜா ராணி — immutable dialogue index

Status: **in progress — verified-source-only**.

This layer is downstream of the completed Raja Rani scene-text derivative phase. The verified canonical Tamil and verified scene derivatives remain the textual authorities; dialogue records are immutable structured references to explicitly speaker-labelled utterances only.

## Source gate

- archival scene segments: **58**
- verified scene-text eligible segments: **50**
- verified scene-text files complete: **50/50 eligible**
- blocked source-review segments: **8**
- blocked scene IDs: `raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013`, `raja-rani-s033`, `raja-rani-s039`, `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055`
- review source pages: PDF **27, 48, 57, 74**

No dialogue record may be created from a blocked scene until its complete source span is supported by verified Tamil.

## Core rules

- Only source-visible utterances with a **non-empty printed speaker label** become dialogue records.
- Source-unlabelled speech remains unlabelled and is **not** converted into a dialogue record even when the implied speaker appears obvious from context.
- `speaker_label` preserves the exact source form represented in the verified scene text. Forms such as `ராஜா`, `ராசா`, abbreviations, role labels and other source-visible variants are not normalized here.
- `speaker_delimiter` preserves the printed punctuation after the label rather than regularizing it.
- Character identity/label normalization belongs only to the later `characters/` derivative layer.
- Dialogue `text` is copied exactly from verified scene text after the printed speaker delimiter.
- A labelled utterance crossing a physical page boundary remains **one** record with multi-page `page_provenance` and `page_segments`.
- Narrative text, stage directions without a speaker label, decorative separators, written letters, song/performance cues and other unlabelled structures do not become dialogue records merely because an implied speaker can be inferred.
- A verified scene may legitimately have zero dialogue records.
- Archive IDs such as `raja-rani-s001-d001` are derivative identifiers only. The booklet prints no screenplay scene numbers and no dialogue numbers.

## Provenance

Each record links to:

- archival scene ID and ordinal;
- transition-audit ID `T001`–`T058`;
- exact verified `speaker_label`;
- exact printed speaker delimiter;
- exact verified utterance text;
- PDF page and mapped printed-page provenance;
- the verified scene derivative file.

## Storage

- `schema.json` — immutable record schema.
- `index.json` — work-level dialogue inventory and per-scene progress.
- `records/scene-###.json` — scene-sharded dialogue records created only for verified eligible scene derivatives.

## Dialogue Batch 001

Processed verified scenes `scene-001.md` through `scene-010.md`.

- processed scenes: **10**
- records: **203**
- zero-record scenes: `s008`, `s010`
- cross-page records: `raja-rani-s004-d006`, `raja-rani-s004-d023`, `raja-rani-s005-d010`
- tracked non-colon source-label/delimiter forms: `raja-rani-s004-d001`, `raja-rani-s004-d007`, `raja-rani-s007-d023`

Batch report: `../notes/dialogue-batch-001.md`.

## Dialogue Batch 002

Resumed after blocked `s011`–`s013` and processed verified `scene-014.md` through `scene-023.md`.

Per-scene counts:

- s014: 0
- s015: 36
- s016: 10
- s017: 48
- s018: 41
- s019: 0
- s020: 0
- s021: 50
- s022: 0
- s023: 36

Batch total: **221 records**.

New zero-record scenes: `s014`, `s019`, `s020`, `s022`.

New cross-page record:

- `raja-rani-s021-d048` — PDF 37→38 / printed 36→37

No new non-colon speaker-label delimiter anomaly was promoted. Exact label variants and abbreviations remain preserved without normalization.

Important no-inference exclusions include `ராணி வெளியிலே போர்டு பார்த்தேன்.` in `s015`, which has no printed speaker delimiter, plus the unlabelled `எஸ் கமின்...` / `சாப்புடு...டேய் கரண்ட்!...` material in the same scene.

Batch report: `../notes/dialogue-batch-002.md`.

## Dialogue Batch 003

Processed verified `scene-024.md` through `scene-032.md` and stopped before blocked `s033`.

Per-scene counts:

- s024: 32
- s025: 33
- s026: 1
- s027: 0
- s028: 64
- s029: 0
- s030: 0
- s031: 3
- s032: 0

Batch total: **133 records**.

New zero-record scenes: `s027`, `s029`, `s030`, `s032`.

No new cross-page record or non-colon speaker-label delimiter anomaly was added. Exact source variants such as `இந்தி`, `அகல்`, `முனி`, `ராஜ`, `ராசா`, `சாந்`, `சம`, and `வேலை` remain unnormalized.

In `s028`, the unlabelled PDF-46 continuation `இந்தா! அது வச்சு இருந்தேனே. அது எங்கே?` remains outside the immutable dialogue index rather than receiving a context-inferred speaker.

Batch report: `../notes/dialogue-batch-003.md`.

## Dialogue Batch 004

Skipped blocked `s033`, processed verified `scene-034.md` through `scene-038.md`, and stopped before blocked `s039`.

Per-scene counts:

- s034: 65
- s035: 27
- s036: 48
- s037: 0
- s038: 0

Batch total: **140 records**.

New zero-record scenes: `s037`, `s038`.

New cross-page record:

- `raja-rani-s035-d012` — PDF 52→53 / printed 51→52 (`ராஜா:`)

No new non-colon speaker-label delimiter anomaly was added. Exact source variants such as `ராசா`, `ராஜா`, `ஞான`, `ஞா`, `கர`, `சம` and `சாந்` remain unnormalized.

The unlabelled `மெள்ள, மெள்ள...` and `ஆ...பூச்சி, பூச்சி...` lines in `s034` remain outside the immutable dialogue inventory rather than receiving context-inferred speaker metadata.

Batch report: `../notes/dialogue-batch-004.md`.

## Current totals

- eligible dialogue scenes: **50**
- blocked scenes: **8**
- processed dialogue scenes: **34/50**
- immutable dialogue records: **697**
- zero-record scenes: **12** — `s008`, `s010`, `s014`, `s019`, `s020`, `s022`, `s027`, `s029`, `s030`, `s032`, `s037`, `s038`
- cross-page records: **5**
- tracked non-colon source-label/delimiter anomalies: **3**

## Next dialogue batch

Skip blocked `s039`, process verified **`scene-040.md` through `scene-052.md`** in source order, then stop before blocked `s053`–`s055`.

Do not create dialogue shards for blocked `s039`, `s053`, `s054` or `s055`. Preserve exact labels/delimiters, cross-page continuity and the no-inferred-speaker rule.
