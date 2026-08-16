# மனோகரா — immutable dialogue index

Status: **in-progress**.

This layer is downstream of the **57/57 complete-verified archival scene-text derivatives**. The verified canonical Tamil and verified scene derivatives remain the textual authorities; dialogue records are immutable structured references to explicitly speaker-labelled utterances only.

## Core rules

- Only source-visible utterances with a **non-empty printed speaker label** become dialogue records.
- Source-unlabelled speech such as lines beginning only with `:` remains unlabelled and is **not** converted into a dialogue record.
- `speaker_label` preserves the exact printed label form used by the verified Tamil. It is not expanded, standardized or mapped to a character here.
- `speaker_delimiter` preserves the printed punctuation after that label. The booklet contains `:`, `;` and `,` forms in different places; those irregularities must not be silently normalized.
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

Dialogue indexing is complete through **scenes 1–10** (`manohara-s001`–`manohara-s010`). These ten scene shards contain **164 immutable labelled-dialogue records**.

The second batch added **133 records** across scenes 6–10:

- `s006`: 18 records;
- `s007`: 13;
- `s008`: 58;
- `s009`: 36;
- `s010`: 8.

`manohara-s008` contains the embedded play. Source lines whose printed speaker field is empty and appears only as `:` remain outside the dialogue index. By contrast, non-empty descriptive labels actually printed before a colon — for example `நாடகம் பார்க்கும் ராஜப்பிரியன்`, `நாடகம் பார்க்கும் வசந்தசேனா`, `நாடக தேவசேனா`, and `நாடகம் பார்க்கும் வசந்தன்` — are retained exactly as source speaker labels, without normalizing them to character names.

The existing cross-page record remains `manohara-s001-d004`, whose labelled utterance begins on PDF 7 / logical printed p.6 and continues onto PDF 8 / printed p.7.

Next batch: continue with **`manohara-s011`–`manohara-s015`**. Multiple scenes should continue to be handled per activity where density permits.

The character/entity index remains blocked until the complete dialogue inventory is established.
