# ராஜா ராணி — immutable dialogue index

Status: **initialized — verified-source-only**.

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

## Initialization checkpoint

The scene-text phase closed at **50/50 eligible complete**, with the eight documented source-review exclusions unchanged. No dialogue records existed before this checkpoint.

The dialogue layer is now initialized with zero records and no completed dialogue scenes. This initialization does not reinterpret or modify canonical Tamil or scene derivatives.

## Next dialogue batch

Process verified scene derivatives **`scene-001.md` through `scene-010.md`** in source order.

For each scene:

1. inspect the verified scene text against its page-provenance comments;
2. emit one immutable record for each explicitly speaker-labelled utterance;
3. preserve exact speaker labels and delimiters;
4. retain cross-page utterances as one record;
5. leave source-unlabelled speech outside the dialogue index;
6. update `index.json` with record counts, zero-record scenes, cross-page records and any source-label/delimiter anomalies actually observed.

Stop before blocked `s011`–`s013`. Do not skip into later scenes within the same first batch.
