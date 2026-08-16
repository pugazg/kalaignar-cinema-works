# மனோகரா — immutable dialogue index

Status: **in-progress**.

This layer is downstream of the **57/57 complete-verified archival scene-text derivatives**. The verified canonical Tamil and verified scene derivatives remain the textual authorities; dialogue records are immutable structured references to explicitly speaker-labelled utterances only.

## Core rules

- Only source-visible utterances with a **non-empty printed speaker label** become dialogue records.
- Source-unlabelled speech such as lines beginning only with `:` remains unlabelled and is **not** converted into a dialogue record.
- `speaker_label` preserves the exact printed label form used by the verified Tamil. It is not expanded, standardized or mapped to a character here.
- `speaker_delimiter` preserves the printed punctuation after that label. The booklet contains `:`, `;`, `,`, `-` and `.` forms in different places; those irregularities must not be silently normalized.
- Character identity/label normalization belongs only to the later `characters/` derivative layer.
- Dialogue `text` is copied exactly from verified scene text after the printed speaker delimiter. Label-attached parenthetical or stage material remains inside that immutable record text.
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

Dialogue indexing is complete through **scenes 1–35** (`manohara-s001`–`manohara-s035`). These thirty-five scene shards contain **467 immutable labelled-dialogue records**.

The seventh batch added **79 records** across scenes 31–35:

- `s031`: 7 records;
- `s032`: 1;
- `s033`: 46;
- `s034`: 12;
- `s035`: 13.

`manohara-s033` is the dense manipulation sequence spanning PDF 43–46. The source-visible speaker-label variants — including `வ. சே.`, `வ. சே`, `வ. சேனை`, `தோழி`, `தோ`, `அரசர்`, and `அர` — are preserved exactly rather than collapsed into normalized character names. No new delimiter anomaly or cross-page dialogue record is introduced in this batch.

Within `manohara-s033-d017`, the second paragraph beginning `இருட்டுவேளை! பத்மாவதியின் அந்தப்புரம்!` has no new speaker label and directly continues the preceding `வ. சே. :` utterance, so it remains inside the same immutable record rather than receiving an invented dialogue ID.

`manohara-s035-d013` similarly preserves Manoharan's final continuous utterance through the embedded source directions `[பத்மாவதியைக் கைது செய்ய வந்திருக்கும் சிப்பாய்களை நோக்கி]` and `[விஜயாவை நோக்கி]`; the closing `விஜயா! பார்த்துக்கொள்...வருகிறேன்` is not split off or assigned a synthetic new label.

The previously established zero-record scene remains `manohara-s024`.

Cross-page dialogue records currently are:

- `manohara-s001-d004` — PDF 7→8;
- `manohara-s015-d002` — PDF 28→29;
- `manohara-s021-d017` — PDF 34→35.

Recorded source-label/delimiter anomalies currently are:

- `manohara-s013-d009` — `சிப்பாய் 2 - ...`;
- `manohara-s021-d001` — `தோழி 1. ...`;
- `manohara-s021-d003` — `தோழி 2. ...`;
- `manohara-s026-d002` — `பிரதானி2, ...`.

Next batch: continue with **`manohara-s036`–`manohara-s040`**. Multiple scenes should continue to be handled per activity where density permits.

The character/entity index remains blocked until the complete dialogue inventory is established.
