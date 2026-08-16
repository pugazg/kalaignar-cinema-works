# மனோகரா — immutable dialogue index

Status: **in-progress**.

This layer is downstream of the **57/57 complete-verified archival scene-text derivatives**. The verified canonical Tamil and verified scene derivatives remain the textual authorities; dialogue records are immutable structured references to explicitly speaker-labelled utterances only.

## Core rules

- Only source-visible utterances with a **non-empty printed speaker label** become dialogue records.
- Source-unlabelled speech such as lines beginning only with `:` remains unlabelled and is **not** converted into a dialogue record.
- `speaker_label` preserves the exact printed label form used by the verified Tamil. It is not expanded, standardized or mapped to a character here.
- `speaker_delimiter` preserves the printed punctuation after that label. The booklet contains `:`, `;`, `,` and `-` forms in different places; those irregularities must not be silently normalized.
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

Dialogue indexing is complete through **scenes 1–20** (`manohara-s001`–`manohara-s020`). These twenty scene shards contain **279 immutable labelled-dialogue records**.

The fourth batch added **33 records** across scenes 16–20:

- `s016`: 12 records;
- `s017`: 1;
- `s018`: 7;
- `s019`: 3;
- `s020`: 10.

`manohara-s016` crosses the canonical Part 01 / Part 02 storage boundary, but no labelled utterance crosses that page boundary; records retain the verified PDF 30 and PDF 31 provenance separately. The source stage direction `(உள்ளேவந்து)` preceding the first `மனோகரன் :` line remains in the verified scene derivative and is not silently absorbed into the speaker label.

`manohara-s020` contains a deliberate unlabelled continuation after `[பொன் மூட்டையை அவனிடம் கொடுக்கிறாள்.]`: the lines beginning `பெளத்தாயனரே!... இன்னொரு காரியம்...` and continuing through the Padmavati/Rani/Prime Minister proposal have no printed speaker label, so they remain outside the immutable dialogue index even though the dramatic context strongly suggests the speaker. The next explicit `பெளத் :` line resumes indexed dialogue.

Cross-page dialogue records currently remain:

- `manohara-s001-d004` — PDF 7→8;
- `manohara-s015-d002` — PDF 28→29.

The source delimiter anomaly `manohara-s013-d009` remains preserved as `சிப்பாய் 2 - ...`, with `-` recorded rather than normalized.

Next batch: continue with **`manohara-s021`–`manohara-s025`**. Multiple scenes should continue to be handled per activity where density permits.

The character/entity index remains blocked until the complete dialogue inventory is established.
