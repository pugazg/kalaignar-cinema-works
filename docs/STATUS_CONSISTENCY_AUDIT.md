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

The three screenplay works remain at their completed checkpoints. The film-song anthology has now closed both its Tamil and English source-linked gates at **54/54 complete-verified**.

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
| English translation | 769 verified units | 1,321 verified units | 1,190 verified units | complete-verified — 54/54 songs |
| English reader/export | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS — 54 songs / 1,105 lines-cues |
| Reading Room payload | downstream | downstream | ready | complete-verified, QA PASS — 23 film groups / 54 songs; site not applied |
| EPUB | not required | complete-verified, QA PASS | not required | not started/not required yet |
| Required Tamil/source work remaining | none | none | none | none |

## Film-song anthology reconciliation

The supplied `கலைஞர் திரை இசைப் பாடல்கள்` anthology follows a PDF-specific page-driven Tamil rule: only actual numbered lyric pages or direct continuations create/process lyric files. The complete PDF classification is **194/194 pages scanned, 62 song-bearing pages, 132 ignored pages, 54 numbered songs**.

Tamil status:

- song inventory: **54/54 complete-verified**;
- Tamil transcription: **54 verified / 0 draft / 0 review / 0 not-started**;
- Tamil fidelity audit: **complete**;
- unresolved Tamil song readings: **0**.

The English layer is separately source-linked under `works/kalaignar-thirai-isai-paadalgal/translations/` and follows `docs/SONG_TRANSLATION_GUIDE.md`.

Final English status:

- mode: **`semantic-poetic-source-faithful`**;
- translation: **54/54 complete-verified**;
- pilot-verified: **3** (`001–003`);
- verified: **51** (`004–054`);
- draft/review/not-started: **0/0/0**;
- final scaled review: `translations/BATCH_047_054_REVIEW.md`.

The English policy retains Kalaignar's language rather than smoothing it into generic lyric English. Across the completed corpus it preserves political/social rhetoric, colloquial and folk speech, culture-bearing Tamil vocabulary, performance terminology, literal image chains, repetition and difficult verified source forms.

Final-batch safeguards include **sons of the soil**, `naam / naan` lip-position wordplay, `kalaignan`, `udanpirappe`, caste/religion and sledgehammer rhetoric, mother-warrior battlefield imagery, `mullai / bhava / jathi / veena`, the two-page `machaan` duet with `saivam / asaivam` wordplay, Kannagi/Classical-Tamil family imagery, the deliberately segmented poem structure of `053`, and `aanpaal / paayiram / water upon red earth` in `054`.

Multi-page English provenance remains complete for all eight cross-page song records: `009` (38–39), `019` (53–54), `023` (58–59), `024` (62–63), `036` (86–87), `037` (90–91), `051` (121–122), and `052` (123–124).

No verified Tamil song file was changed by the English translation layer. Default attribution remains `anthology-attributed`; English verification does not convert the 2024 anthology's attribution into automatic original-film primary-source verification.

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

No required Tamil/source transcription, Tamil fidelity, or English song-translation work remains for the anthology.

The anthology English reader/export is **complete-verified with QA PASS**. A deterministic Reading Room payload is also **complete-verified with QA PASS** at 23 film groups / 54 songs / 1,105 paired Tamil-English lines-cues / 8 cross-page songs, with zero warnings/errors or text drift. The separate public-site implementation remains not applied and requires explicit cross-repository authorization.

Reading Room integration remains a separate downstream publication activity and is outside this repository-only audit unless explicitly requested.
