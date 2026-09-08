# நாம் — dialogue-index QA

Result: **PASS**

- source scenes covered: **45/45**;
- explicit source speaker labels owned exactly once: **590/590**;
- immutable dialogue records: **590**;
- distinct exact speaker-label strings: **45**;
- delimiter distribution matches preflight: **PASS — {':': 16, ':-': 573, '—': 1}**;
- multi-page utterances kept as one logical record: **8**;
- speaker-label normalization: **0**;
- inferred assignments for source-unlabelled text: **0**;
- unlabelled blocks preserved separately: **39**;
- location / written-text colon cues excluded from dialogue: **21**;
- occurrence-specific scene-41 em-dash speaker verdict: **PASS**;
- canonical Tamil modified: **0**;
- scene text modified: **0**.

`உன்மீனு` remains exactly as the source-explicit label; no alias repair occurs in this immutable layer. `கடிதத்தில்` remains written-text provenance rather than a speaker.

## Gate result

**Dialogue indexing CLOSED / COMPLETE-VERIFIED.** Character/entity indexing may now begin.

## Next activity

Begin Phase 7 character/entity indexing from the complete-verified immutable dialogue layer. Preserve all exact source speaker labels as immutable provenance, map label variants to character/entity IDs only in a separate alias layer, keep generic roles and source anomalies explicit, and run whole-work label/entity coverage QA before the song/authorship gate. Do not rewrite canonical Tamil, scene text, or dialogue records.
