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

Dialogue indexing is complete through **scenes 1–30** (`manohara-s001`–`manohara-s030`). These thirty scene shards contain **388 immutable labelled-dialogue records**.

The sixth batch added **59 records** across scenes 26–30:

- `s026`: 10 records;
- `s027`: 4;
- `s028`: 10;
- `s029`: 6;
- `s030`: 29.

`manohara-s026-d002` preserves the source's comma-delimited label `பிரதானி2,` instead of silently normalizing it to a colon. It is added to the source-label/delimiter anomaly ledger.

`manohara-s027` intentionally leaves the quoted instruction `“விஜயா உன் கணவனை சாந்தப் படுத்து!”` outside the immutable dialogue index because the source presents it after the stage cue `(விஜயாவிடம்)` without a new printed speaker label.

`manohara-s030` crosses the canonical Part 02 / Part 03 storage boundary. No single labelled utterance crosses the PDF 42→43 page boundary, so records remain page-local. Within PDF 42, however, the source-attached directions `[பல்லைக் கடித்து]......` and `[கட்டாரியை உருவுகிறான்]` remain embedded in the corresponding Vasanthi and Manoharan dialogue records because the same labelled utterance continues after each direction without a new speaker label.

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

Next batch: continue with **`manohara-s031`–`manohara-s035`**. Multiple scenes should continue to be handled per activity where density permits.

The character/entity index remains blocked until the complete dialogue inventory is established.
