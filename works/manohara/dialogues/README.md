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

Dialogue indexing is complete through **scenes 1–40** (`manohara-s001`–`manohara-s040`). These forty scene shards contain **676 immutable labelled-dialogue records**.

The eighth batch added **209 records** across scenes 36–40:

- `s036`: 88 records;
- `s037`: 17;
- `s038`: 50;
- `s039`: 37;
- `s040`: 17.

`manohara-s036` is the long court-confrontation segment spanning PDF 48–57 and crossing the canonical Part 03 / Part 04 storage boundary. Three labelled utterances cross page boundaries and remain single immutable records: `manohara-s036-d032` across PDF 51→52, `manohara-s036-d041` across PDF 52→53, and `manohara-s036-d077` across PDF 56→57. Source-attached directions and unlabelled continuations remain inside the preceding labelled record where no new speaker label intervenes.

The unlabelled collective cries under `(சபையோர்)` on PDF 55 remain outside the dialogue index because the source prints no speaker delimiter there. By contrast, the later explicit `சபையோர் :` line on PDF 56 is indexed and its immediately following unlabelled quoted continuation remains within the same record.

`manohara-s038` preserves the comic mock-darbar exchange exactly. The source line beginning only `: இப்ப நான் சொல்றபடி சொல்லணும்......` remains unindexed because its printed speaker field is empty.

`manohara-s039-d029` preserves the explicit source label `வசந்தசேனை மனதிற்குள் :` exactly rather than normalizing it to a character name or converting it to narrative. In `manohara-s040`, the separately printed Ugrasenan letter remains outside the dialogue index because it is a letter block, not an explicitly speaker-labelled utterance.

The previously established zero-record scene remains `manohara-s024`.

Cross-page dialogue records currently are:

- `manohara-s001-d004` — PDF 7→8;
- `manohara-s015-d002` — PDF 28→29;
- `manohara-s021-d017` — PDF 34→35;
- `manohara-s036-d032` — PDF 51→52;
- `manohara-s036-d041` — PDF 52→53;
- `manohara-s036-d077` — PDF 56→57.

Recorded source-label/delimiter anomalies currently are:

- `manohara-s013-d009` — `சிப்பாய் 2 - ...`;
- `manohara-s021-d001` — `தோழி 1. ...`;
- `manohara-s021-d003` — `தோழி 2. ...`;
- `manohara-s026-d002` — `பிரதானி2, ...`.

Next batch: continue with **`manohara-s041`–`manohara-s045`**. Multiple scenes should continue to be handled per activity where density permits.

The character/entity index remains blocked until the complete dialogue inventory is established.
