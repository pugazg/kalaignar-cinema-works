# அம்மையப்பன் — immutable dialogue layer

Status: **REVIEW READY**

Authority: the **63/63 complete-verified archive-only scene derivatives**, themselves derived only after the **105/105 dual-gate Tamil source verification** closed.

## Current build

- archive scenes represented: **63/63**
- immutable dialogue records: **910**
- distinct exact speaker-label strings: **57**
- multi-page immutable utterances: **24**
- zero-dialogue scene files retained as empty arrays: **6**
- source scene numbers invented: **0**
- alias/name normalization: **0**

Each explicit source `speaker : text` line starts one record.  Ordinary unlabelled text that follows remains part of that utterance until a hard structural boundary.  A physical PDF-page transition does not end an utterance; multi-page records carry `page_segments` and page provenance.

Text that occurs with no active explicit speaker is **not assigned by inference**.  It is preserved separately in `../notes/unlabelled-block-audit.json` for source-role review.

The character/entity index remains blocked until the unlabelled-block audit and final dialogue QA are closed.
