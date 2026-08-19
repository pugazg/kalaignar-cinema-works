# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-08-19  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles the repository-level status registry with the current authoritative work metadata for the four archival works currently represented in the repository:

- `works/parasakthi/`
- `works/tirumbippaar/`
- `works/manohara/`
- `works/kalaignar-thirai-isai-paadalgal/`

The central synchronization target is `data/works.json`. Work-specific metadata and audit documents remain the detailed authorities. This audit does not authorize changes in any other repository.

## Result

**PASS — repository status registry synchronized for all four works.**

The three screenplay works remain at their previously completed checkpoints. The new film-song anthology has now closed its Tamil transcription/fidelity gate at **54/54 complete-verified**.

## Cross-work status matrix

| Layer | Parasakthi | Tirumbippaar! | Manohara | Kalaignar Thirai Isai Paadalgal |
|---|---|---|---|---|
| Structural mapping | verified | verified | verified | verified |
| Canonical/source Tamil | verified, 54/54 pages | verified, 104/104 pages | complete-verified, 82/82 pages | 54/54 numbered songs complete-verified |
| Fidelity audit | complete | complete | complete | complete |
| Scene derivatives | 46 observed scenes complete | 93/93 complete | 57/57 archival scenes complete-verified | not applicable |
| Dialogue index | 642 records, complete-verified | 1,040 records, complete | 983 records, complete-verified | not applicable |
| Character/entity layer | complete-verified | complete | complete-verified with one unresolved source label | not applicable |
| Song/performance layer | 14/14 authorship verified | 3 verified / 5 unresolved | 1 verified / 1 review / 4 unresolved | 54/54 anthology-attributed lyric records verified |
| English translation | 769 verified units | 1,321 verified units | 1,190 verified units | not started; unblocked |
| English reader/export | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS | not started |
| EPUB | not required | complete-verified, QA PASS | not required | not started/not required yet |
| Required Tamil/source work remaining | none | none | none | none |

## Film-song anthology reconciliation

The supplied `கலைஞர் திரை இசைப் பாடல்கள்` anthology follows a PDF-specific page-driven rule: only actual numbered lyric pages or direct continuations create/process lyric files. The complete PDF classification is **194/194 pages scanned, 62 song-bearing pages, 132 ignored pages, 54 numbered songs**.

The final formerly not-started batch completed songs `026–054`. The last Tamil fidelity gate then reinspected the three original pilot drafts only:

- PDF 26 → song `001`;
- PDF 29 → song `002`;
- PDF 30 → song `003`.

Final dispositions:

- song `001`: corrected pilot `அறியாண்டி` to source-visible `அறியான்டி`; confirmed `வேணசெல்வம்`, `பெண்ணி`, and `ஏழைக்கிக்`;
- song `002`: direct visual recheck required no lyric correction;
- song `003`: resolved the two pilot uncertainty markers directly from the scan as `வந்தேன் தவழ்ந்தாய்?` and `பாழான எந்தன் வயிற்றில் பிறந்தாய் ராஜா!`.

The anthology status is now:

- song inventory: **54/54 complete-verified**;
- Tamil transcription: **54 verified / 0 draft / 0 review / 0 not-started**;
- Tamil fidelity audit: **complete**;
- unresolved Tamil song readings: **0**;
- English translation: **not started, now unblocked**.

Default attribution remains `anthology-attributed`: verification here means fidelity to what the 2024 anthology prints, not automatic original-film primary-source authorship verification.

## Existing screenplay works

### Parasakthi

- 54/54 canonical Tamil pages verified;
- 46 observed scene derivatives complete;
- 642 dialogue records complete-verified;
- 14/14 song/verse authorship occurrences verified;
- 769 verified English units;
- reader/export QA PASS.

### Tirumbippaar!

- 104/104 canonical pages verified;
- 93/93 scene derivatives complete;
- 1,040 dialogue records;
- 45/45 source speaker labels dispositioned into 39 verified entities/role categories;
- 8 song/performance occurrences with 3 verified / 5 unresolved authorship dispositions;
- 1,321 verified English units;
- reader/export and deterministic EPUB QA PASS.

The cropped lower printer-imprint continuation on PDF 2 remains an intentional unresolved source crop, not a project-status defect.

### Manohara

- 82/82 canonical pages complete-verified;
- fidelity audit complete with zero unresolved source readings;
- 57/57 archival scene derivatives complete-verified;
- 983 immutable labelled-dialogue records complete-verified;
- 111/111 source labels dispositioned, with only `வர்மா` intentionally unresolved;
- 6 source-visible song/performance occurrences with 1 verified / 1 review / 4 unresolved authorship dispositions;
- 1,190 verified English units;
- reader preflight and deterministic reader/export QA PASS.

## Repository-internal conclusion

No required Tamil/source transcription or fidelity work remains for any of the four current works.

For the anthology, the next repository-internal activity is optional-but-ready derivative work: define and review a source-linked English translation pilot before scaling to all 54 songs.

Reading Room integration remains a separate downstream publication activity and is outside this repository-only audit unless explicitly requested.
