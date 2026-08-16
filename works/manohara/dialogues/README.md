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

Dialogue indexing is complete through **scenes 1–55** (`manohara-s001`–`manohara-s055`). These fifty-five scene shards contain **973 immutable labelled-dialogue records**.

The eleventh batch added **109 records** across scenes 51–55:

- `s051`: 14 records;
- `s052`: 19;
- `s053`: 28;
- `s054`: 10;
- `s055`: 38.

The rendered source scan was reinspected directly across PDF **78–88** while constructing this batch.

Five newly indexed utterances cross physical page boundaries and remain single immutable records:

- `manohara-s052-d012` — PDF 79→80;
- `manohara-s055-d008` — PDF 83→84;
- `manohara-s055-d014` — PDF 84→85;
- `manohara-s055-d020` — PDF 85→86;
- `manohara-s055-d024` — PDF 86→87.

For the long `manohara-s055` speeches, `page_segments` follows the physical scan break directly, including source words divided by a page break (`பொறு`→`த்துக்கொண்டேன்`, `ஆண`→`வம்`, and `கட்டிப்`→`போட்டேன்`). No word is silently recombined inside page-specific provenance.

The cumulative cross-page set is now **13 records**:

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

`manohara-s052-d003` preserves Manoharan's unlabelled continuation after the beard-removal direction inside the preceding explicit `மனோ :` utterance. `manohara-s053-d018` likewise preserves `விடு என்னை... விடு என்னை.` with its intervening source direction inside the preceding explicit `வச :` turn.

In `manohara-s055-d003`, Ugrasenan's source-unlabelled continuation `உம் கண்ணீரால் குளிப்பாட்டு உன் பிள்ளைக் கனியமுதை!` remains within the preceding explicit `உக்ர :` utterance, together with the intervening source direction, rather than being promoted to a new inferred-speaker record.

Source lines beginning with an **empty** speaker field remain outside the dialogue index. This batch therefore does not infer speakers for, among others:

- the four empty-label lines in `manohara-s051`, including `: வெற்றிச் செய்தியோடு வந்திருப்பான்...` and `: என்ன அக்ஷயா?...`;
- `: மனோகரனுடைய குழந்தைக்கு நான் ஒரு முத்தம் கூட கொடுக்கக் கூடாதா?` in `manohara-s052`;
- the two empty-label Vasanthasena threats after `சேனா : நாசமா?` in `manohara-s052`.

`manohara-s051` introduces three exact semicolon-delimiter records:

- `manohara-s051-d007` — `அட்சயன் ; ...`;
- `manohara-s051-d009` — `அட் ; ...`;
- `manohara-s051-d010` — `சேனா ; ...`.

Recorded source-label/delimiter anomalies are now **8**:

- `manohara-s013-d009` — `சிப்பாய் 2 - ...`;
- `manohara-s021-d001` — `தோழி 1. ...`;
- `manohara-s021-d003` — `தோழி 2. ...`;
- `manohara-s026-d002` — `பிரதானி2, ...`;
- `manohara-s050-d018` — `பத் , ...`;
- `manohara-s051-d007` — `அட்சயன் ; ...`;
- `manohara-s051-d009` — `அட் ; ...`;
- `manohara-s051-d010` — `சேனா ; ...`.

The previously established zero-record scene remains `manohara-s024`.

The post-fidelity PDF 68 speaker-label repair remains documented in `../notes/post-fidelity-corrections.md`; no new canonical wording correction was required in this batch.

Next batch: complete dialogue indexing with **`manohara-s056`–`manohara-s057`**.

The character/entity index remains blocked until the complete dialogue inventory is established.
