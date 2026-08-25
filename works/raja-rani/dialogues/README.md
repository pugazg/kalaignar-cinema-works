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

Processed verified scenes:

- `scene-001.md` through `scene-010.md`
- **10/50 eligible scenes processed**
- **203 immutable labelled-dialogue records**

Per-scene counts:

- s001: 9
- s002: 21
- s003: 27
- s004: 23
- s005: 22
- s006: 13
- s007: 30
- s008: 0
- s009: 58
- s010: 0

Zero-record scenes: `s008`, `s010`.

Cross-page records:

- `raja-rani-s004-d006` — PDF 13→14
- `raja-rani-s004-d023` — PDF 14→15
- `raja-rani-s005-d010` — PDF 15→18

Tracked non-colon source-label/delimiter forms:

- `raja-rani-s004-d001` — `நாடகத் துவக்கத்திற்கு முன்பு குரல்.`
- `raja-rani-s004-d007` — `தமிழ்நாட்டுப் புலவர்.`
- `raja-rani-s007-d023` — `கீதாவின் தாய் தாயம்மாள்;`

Unlabelled ceremonial speech, written newspaper/letter text, unlabelled stage-linked speech and other implied-speaker material remain outside the immutable dialogue inventory.

Batch report: `../notes/dialogue-batch-001.md`.

## Current totals

- eligible dialogue scenes: **50**
- blocked scenes: **8**
- processed dialogue scenes: **10/50**
- immutable dialogue records: **203**
- zero-record scenes: **2**
- cross-page records: **3**
- tracked non-colon source-label/delimiter anomalies: **3**

## Next dialogue batch

Resume after blocked `s011`–`s013` and process verified **`scene-014.md` through `scene-023.md`** in source order.

Do not create shards for blocked `s011`–`s013`. Preserve exact labels/delimiters, cross-page continuity and the no-inferred-speaker rule.
