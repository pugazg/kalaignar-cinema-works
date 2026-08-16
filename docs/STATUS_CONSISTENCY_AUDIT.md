# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-08-16  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles the repository-level status registry with the current authoritative work metadata and documented reader/export checkpoints for the three archived cinema works currently present in the repository:

- `works/parasakthi/`
- `works/tirumbippaar/`
- `works/manohara/`

The main synchronization target was `data/works.json`. The work-specific `metadata.yaml` files remain the more detailed status authorities. This audit does not perform or authorize downstream Reading Room changes in any other repository.

## Result

**PASS — repository status registry synchronized for all three works.**

Before this audit, `data/works.json` still contained early intermediate states for Tirumbippaar and Manohara. In particular, Manohara was incorrectly represented as a draft transcription stopping at PDF 66, and Tirumbippaar was incorrectly represented as having no structured derivatives. Those stale states have now been replaced with the current verified checkpoints.

## Cross-work status matrix

| Layer | Parasakthi | Tirumbippaar! | Manohara |
|---|---|---|---|
| Structural mapping | verified | verified | verified |
| Canonical Tamil | verified, 54/54 pages | verified, 104/104 pages | complete-verified, 82/82 pages |
| Fidelity audit | complete | complete | complete |
| Scene derivatives | 46 observed scenes complete | 93/93 complete | 57/57 archival scenes complete-verified |
| Dialogue index | 642 records, complete-verified | 1,040 records, complete | 983 records, complete-verified |
| Character/entity layer | complete-verified | complete | complete-verified with one unresolved source label |
| Song/performance authorship | 14/14 verified | 3 verified / 5 unresolved | 1 verified / 1 review / 4 unresolved |
| English translation | 769 verified units | 1,321 verified units | 1,190 verified units |
| English reader/export | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS |
| EPUB | not required | complete-verified, QA PASS | not required |
| Required repository-internal work remaining | none | none | none |

## Work-specific reconciliation

### Parasakthi

The existing registry was already broadly aligned with the current work metadata. The synchronized registry now keeps the current completion state compactly and explicitly: 54 verified canonical pages, 46 observed scenes, 642 dialogue records, complete song/verse authorship and Tamil derivatives, 769 verified English units, and reader/export QA PASS.

The absent printed scene headings 23 and 34 and the documented source-number corrections around canonical scenes 43 and 48 remain preserved as source-specific structural facts rather than treated as inconsistencies.

### Tirumbippaar!

The old registry incorrectly stopped after the Tamil fidelity phase and marked scene, dialogue, character, song and English layers as `not-started`.

The synchronized registry now reflects the actual mature checkpoint:

- 104/104 canonical pages verified;
- 93/93 scene derivatives complete;
- 1,040 dialogue records;
- 45/45 exact speaker labels dispositioned into 39 verified entities/role categories;
- 8 song/performance occurrences, with 3 verified and 5 unresolved authorship dispositions;
- 1,321/1,321 verified English units;
- reader/export QA PASS;
- deterministic EPUB 3 package QA PASS.

The cropped lower printer-imprint continuation on PDF 2 remains an intentional unresolved source crop, not a project-status defect.

### Manohara

The old registry incorrectly described Manohara as an unfinished draft stopping at PDF 66 / logical printed p.65, with 60 draft pages, zero verified pages and all downstream layers blocked.

The synchronized registry now reflects the final repository checkpoint:

- 82/82 canonical pages complete-verified;
- full fidelity audit complete with zero unresolved source readings;
- 57/57 archival scene derivatives complete-verified;
- 983 immutable labelled-dialogue records complete-verified;
- 111/111 source labels dispositioned, with only `வர்மா` intentionally unresolved;
- 6 source-visible song/performance occurrences, with 1 verified, 1 review and 4 unresolved authorship dispositions;
- 1,190/1,190 verified English units;
- 983/983 immutable dialogue links in the English layer;
- 27 source-unlabelled spoken English units preserved as unlabelled;
- 17 genuine cross-page English units;
- reader preflight PASS and deterministic reader/export QA PASS.

The unresolved character/song evidence above remains intentionally unresolved because the archive does not have sufficient source-supported evidence to force a disposition. It is not considered incomplete transcription or translation work.

## Repository-internal conclusion

No required transcription, fidelity, scene, dialogue, character, translation or reader/export work remains for the three existing cinema works.

Future repository activity falls into one of two categories:

1. archive a newly supplied Kalaignar cinema source through the established workflow; or
2. perform optional additional packaging only when explicitly requested and useful.

Reading Room integration is a downstream publication activity and is deliberately outside this repository-only consistency audit.
