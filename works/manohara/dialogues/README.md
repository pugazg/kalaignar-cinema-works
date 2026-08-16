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

Dialogue indexing is complete through **scenes 1–50** (`manohara-s001`–`manohara-s050`). These fifty scene shards contain **864 immutable labelled-dialogue records**.

The tenth batch added **97 records** across scenes 46–50:

- `s046`: 10 records;
- `s047`: 10;
- `s048`: 41;
- `s049`: 9;
- `s050`: 27.

The rendered source pages for this batch were reinspected directly across PDF **71–78** while constructing the dialogue shards. Two newly indexed utterances cross canonical page boundaries and remain single immutable records:

- `manohara-s048-d007` — PDF 72→73, beginning with the king's `அர : எதடி ஆண்டவன் கட்டளை?...` and continuing on the next page without a new speaker label;
- `manohara-s048-d039` — PDF 75→76, the king's extended lament beginning `வசந்தன்! அந்த வஞ்சகியின் மகன்...` and continuing across the page break.

The cumulative cross-page set is now **8 records**:

- `manohara-s001-d004` — PDF 7→8;
- `manohara-s015-d002` — PDF 28→29;
- `manohara-s021-d017` — PDF 34→35;
- `manohara-s036-d032` — PDF 51→52;
- `manohara-s036-d041` — PDF 52→53;
- `manohara-s036-d077` — PDF 56→57;
- `manohara-s048-d007` — PDF 72→73;
- `manohara-s048-d039` — PDF 75→76.

`manohara-s049-d008` keeps the immediately following unlabelled `இல்ல...இல்ல...` continuation within the preceding explicit `மனோ :` utterance, preserving the verified source sequence without creating a second inferred-speaker record.

`manohara-s050` preserves a new printed delimiter anomaly exactly: `பத் , தந்திரமாக தப்பிவிடுவது...` becomes `manohara-s050-d018` with `speaker_label` `பத்` and `speaker_delimiter` `,`. The following source line beginning only `: தம்பி மனோகரனிடம் சொல்—...` remains outside the dialogue index because the printed speaker field is empty; it is not assigned to Padmavati or any other inferred speaker.

Recorded source-label/delimiter anomalies are now **5**:

- `manohara-s013-d009` — `சிப்பாய் 2 - ...`;
- `manohara-s021-d001` — `தோழி 1. ...`;
- `manohara-s021-d003` — `தோழி 2. ...`;
- `manohara-s026-d002` — `பிரதானி2, ...`;
- `manohara-s050-d018` — `பத் , ...`.

The previously established zero-record scene remains `manohara-s024`.

The post-fidelity PDF 68 speaker-label repair remains documented in `../notes/post-fidelity-corrections.md`; no additional canonical Tamil correction was required in this batch.

Next batch: continue with **`manohara-s051`–`manohara-s055`**. Multiple scenes should continue to be handled per activity where density permits.

The character/entity index remains blocked until the complete dialogue inventory is established.
