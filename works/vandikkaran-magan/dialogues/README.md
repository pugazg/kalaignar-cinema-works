# வண்டிக்காரன் மகன் — immutable dialogue layer

**Status:** **COMPLETE-VERIFIED / RECONCILED / QA PASS**

Built from the closed 72/72 source-led scene derivatives without rewriting canonical Tamil or scene files. A late structural-collision audit corrected a parser defect that had treated some explicit speaker-labelled lines ending in parenthetical action as stage directions.

## Coverage

- immutable dialogue records: **773**;
- legacy IDs preserved: **744/744**; append-only repair records: **29**;
- exact source speaker labels: **38**;
- zero-dialogue scenes: **15**; cross-page records: **3**;
- delimiters: **`:—` 765 / `:` 8**;
- 31 structural collisions reviewed: **29 spoken records restored / 2 action-only labels excluded**;
- unlabelled text assigned to speakers: **0**; label normalizations: **0**.

See `../notes/dialogue-structural-collision-audit.json` and `../notes/dialogue-index-qa.json`.

## Downstream

Character/entity and song/performance layers remain closed against this 773-record authority. English translation links **773/773 exactly once** and is **72/72 COMPLETE-VERIFIED**; deterministic English reader/export is **COMPLETE-VERIFIED / QA PASS** without modifying this immutable layer.

**Next:** Build and verify the deterministic source-linked Reading Room payload for `வண்டிக்காரன் மகன்` from the closed 72-scene Tamil/source structure and the complete-verified 1,181-unit English reader/export. Preserve source scene IDs and PDF/printed provenance; retain all 773 immutable dialogue links, 27 source-unlabelled spoken units, 58 cross-page units and all 9 verified song/performance occurrence identities; preserve unresolved item-level lyric authorship; do not modify closed Tamil, scene, dialogue, character, song/performance or translation authorities; and do not modify the separate Reading Room implementation repository unless explicitly authorized.
