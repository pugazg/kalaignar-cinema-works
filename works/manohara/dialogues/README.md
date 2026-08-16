# மனோகரா — immutable dialogue index

Status: **in-progress**.

This layer is downstream of the **57/57 complete-verified archival scene-text derivatives**. The verified canonical Tamil and verified scene derivatives remain the textual authorities; dialogue records are immutable structured references to explicitly speaker-labelled utterances only.

## Core rules

- Only source-visible utterances with a **non-empty printed speaker label** become dialogue records.
- Source-unlabelled speech such as lines beginning only with `:` remains unlabelled and is **not** converted into a dialogue record.
- `speaker_label` preserves the exact printed label form used by the verified Tamil. It is not expanded, standardized or mapped to a character here.
- `speaker_delimiter` preserves the printed punctuation after that label. The booklet contains `:`, `;`, `,`, `-` and `.` forms in different places; those irregularities must not be silently normalized.
- Character identity/label normalization belongs only to the later `characters/` derivative layer.
- Dialogue `text` is copied exactly from verified scene text after the printed label delimiter. Label-attached parenthetical or stage material remains inside that immutable record text.
- A labelled utterance crossing a page boundary remains **one** record with multi-page `page_provenance` and `page_segments`.
- Narrative text, stage directions without a speaker label, decorative separators, letters, song/performance references and other unlabelled structures do not become dialogue records merely because their implied speaker is obvious.
- A scene may legitimately have zero dialogue records.
- Archive IDs such as `manohara-s001-d001` are derivative identifiers only. The booklet itself prints no scene numbers and no dialogue numbers.

## Provenance

Each record links to:

- archival scene ID and ordinal;
- transition-audit ID `T001`–`T057`;
- exact verified `speaker_label`;
- exact printed speaker delimiter;
- exact verified utterance text;
- PDF page and mapped logical printed-page provenance;
- the verified scene derivative file.

The `printed_page` field stores the verified logical interior printed-page number used throughout the Manohara mapping. A folio may be suppressed in the scan even though the logical printed-page number is known from the continuous sequence.

## Storage

- `schema.json` — immutable record schema.
- `index.json` — work-level dialogue checkpoint and per-scene record counts.
- `records/scene-###.json` — scene-sharded dialogue records.

## Current checkpoint

Dialogue indexing is complete through **scenes 1–25** (`manohara-s001`–`manohara-s025`). These twenty-five scene shards contain **329 immutable labelled-dialogue records**.

The fifth batch added **50 records** across scenes 21–25:

- `s021`: 37 records;
- `s022`: 3;
- `s023`: 1;
- `s024`: 0;
- `s025`: 9.

`manohara-s021` introduces two source-visible period-delimited speaker labels, `தோழி 1.` and `தோழி 2.`. These are preserved as `manohara-s021-d001` and `manohara-s021-d003` with `speaker_delimiter: "."`; the schema now permits the period delimiter rather than silently rewriting it as a colon.

The same scene also contains source-unlabelled speech `வந்துவிட்டேனம்மா` and `“மனோகரா!”`. They remain outside the immutable dialogue index because the source prints no speaker label for them.

`manohara-s021-d017` is a cross-page record: Manoharan's labelled utterance begins on PDF 34 / logical printed p.33, continues through the attached stage direction `(கையிலுள்ள போர்வாளைக் கண்டு)`, and resumes on PDF 35 / p.34 without a new speaker label. It is therefore preserved as one record with two page segments.

`manohara-s024` is the first zero-record scene in this work. It contains the `“பொழுது புலர்ந்தது” பாட்டு` reference and narrative action only, with no explicitly speaker-labelled utterance; its shard is retained with `record_count: 0` rather than manufacturing dialogue.

Cross-page dialogue records currently are:

- `manohara-s001-d004` — PDF 7→8;
- `manohara-s015-d002` — PDF 28→29;
- `manohara-s021-d017` — PDF 34→35.

Recorded source-label/delimiter anomalies currently are:

- `manohara-s013-d009` — `சிப்பாய் 2 - ...`;
- `manohara-s021-d001` — `தோழி 1. ...`;
- `manohara-s021-d003` — `தோழி 2. ...`.

Next batch: continue with **`manohara-s026`–`manohara-s030`**. Multiple scenes should continue to be handled per activity where density permits.

The character/entity index remains blocked until the complete dialogue inventory is established.
