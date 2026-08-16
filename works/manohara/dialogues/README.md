# மனோகரா — immutable dialogue index

Status: **complete-verified**.

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
- `index.json` — work-level dialogue inventory and per-scene record counts.
- `records/scene-###.json` — scene-sharded dialogue records.

## Final checkpoint

Dialogue indexing is complete across **57/57 archival scenes** (`manohara-s001`–`manohara-s057`) with **983 immutable labelled-dialogue records**.

The final batch added **10 records**:

- `s056`: 3 records;
- `s057`: 7 records.

The rendered source scan for the final batch was reinspected directly on PDF **88 / printed p.87** before closing the dialogue layer.

`manohara-s056` preserves only the three source-visible non-empty speaker labels. Its four empty-speaker lines beginning only with `:` remain outside the dialogue index rather than being assigned to Kesari or Vasanthi by inference.

`manohara-s057-d001` preserves the source-supported continuation `பத்மா! என் இதயராணி. என்னை மன்னித்துவிடு.` inside the preceding explicit `அரசர் : அம்மா! விஜயா!` turn. The continuation has no new printed speaker label and is therefore not promoted to a separate dialogue record.

The final batch adds **no new cross-page dialogue records**. The cumulative cross-page set remains **13 records**:

- `manohara-s001-d004` — PDF 7→8;
- `manohara-s015-d002` — PDF 28→29;
- `manohara-s021-d017` — PDF 34→35;
- `manohara-s036-d032` — PDF 51→52;
- `manohara-s036-d041` — PDF 52→53;
- `manohara-s036-d077` — PDF 56→57;
- `manohara-s048-d007` — PDF 72→73;
- `manohara-s048-d039` — PDF 75→76;
- `manohara-s052-d012` — PDF 79→80;
- `manohara-s055-d008` — PDF 83→84;
- `manohara-s055-d014` — PDF 84→85;
- `manohara-s055-d020` — PDF 85→86;
- `manohara-s055-d024` — PDF 86→87.

Recorded source-label/delimiter anomalies remain **8**:

- `manohara-s013-d009` — `சிப்பாய் 2 - ...`;
- `manohara-s021-d001` — `தோழி 1. ...`;
- `manohara-s021-d003` — `தோழி 2. ...`;
- `manohara-s026-d002` — `பிரதானி2, ...`;
- `manohara-s050-d018` — `பத் , ...`;
- `manohara-s051-d007` — `அட்சயன் ; ...`;
- `manohara-s051-d009` — `அட் ; ...`;
- `manohara-s051-d010` — `சேனா ; ...`.

The sole zero-record scene remains `manohara-s024`.

The post-fidelity PDF 68 speaker-label repair remains documented in `../notes/post-fidelity-corrections.md`; no additional canonical Tamil correction was required while closing scenes 56–57.

## Next structured derivative

The complete dialogue inventory now unblocks the **character/entity index**. That layer may normalize source labels only through explicit derivative mappings; these 983 dialogue records remain immutable and must not be rewritten to normalized character names.
