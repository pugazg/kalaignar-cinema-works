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

Dialogue indexing is complete through **scenes 1–15** (`manohara-s001`–`manohara-s015`). These fifteen scene shards contain **246 immutable labelled-dialogue records**.

The third batch added **82 records** across scenes 11–15:

- `s011`: 26 records;
- `s012`: 16;
- `s013`: 13;
- `s014`: 6;
- `s015`: 21.

This batch introduced two important source-fidelity cases:

- `manohara-s013-d009` preserves the printed hyphen-delimited form `சிப்பாய் 2 - மீன் கொடி சாய்ந்துவிட்டது.` as an explicitly labelled dialogue record. The schema now allows `-` as a source delimiter rather than silently converting it to a colon.
- `manohara-s015-d002` is one cross-page utterance: Vijaya's labelled speech starts on PDF 28 / logical printed p.27 and continues onto PDF 29 / p.28. It remains one immutable record with two page segments.

The earlier embedded-play rule remains unchanged: source lines whose speaker field is empty and appears only as `:` stay outside the dialogue index, while non-empty printed descriptive labels remain exact source labels.

Cross-page records currently recorded: `manohara-s001-d004` and `manohara-s015-d002`.

Next batch: continue with **`manohara-s016`–`manohara-s020`**. Multiple scenes should continue to be handled per activity where density permits.

The character/entity index remains blocked until the complete dialogue inventory is established.
