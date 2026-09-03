# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-09-03  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles repository-level status mirrors with the current authoritative work metadata for all six archival works represented in `data/works.json`:

- `works/parasakthi/`
- `works/tirumbippaar/`
- `works/manohara/`
- `works/kalaignar-thirai-isai-paadalgal/`
- `works/manthiri-kumari/`
- `works/raja-rani/`

The central machine-readable synchronization target is `data/works.json`. Work-local indexes/metadata remain the detailed operational authorities, while root README and project handover/audit documents must mirror the same current checkpoint before a major phase is considered closed.

This audit does not authorize changes in any other repository.

## Result

**PASS — repository status registry and current project-level documentation synchronized across all six works.**

The previously stale Raja Rani shared state—75/79 source pages, 50 eligible scenes, 892 dialogue records, 74 labels / 42 entities and scene-1 pilot English—has been superseded throughout the active repository mirrors by the fully reconciled bilingual-text checkpoint.

## Cross-work status matrix

| Work | Tamil/source status | Scene/dialogue status | Character status | Song/performance status | English status | Reader / downstream |
|---|---|---|---|---|---|---|
| Parasakthi | 54/54 canonical pages verified | 46 observed scenes / 642 dialogue records | 69 source labels dispositioned | 14/14 song/verse authorship verified | 769 verified units | reader/export QA PASS |
| Tirumbippaar! | 104/104 canonical pages verified | 93/93 scenes / 1,040 dialogue records | 45/45 labels → 39 verified entities/roles | 3 verified / 5 unresolved occurrences | 1,321 verified units | reader/export + deterministic EPUB QA PASS |
| Manohara | 82/82 canonical pages complete-verified | 57/57 scenes / 983 dialogue records | 111 labels dispositioned; `வர்மா` intentionally unresolved | 1 verified / 1 review / 4 unresolved | 1,190 verified units | reader/export QA PASS; Reading Room ready |
| Kalaignar Thirai Isai Paadalgal | 54/54 numbered Tamil songs verified | not applicable | not applicable | 54 anthology-attributed lyric records | 54/54 songs / 1,105 mapped lines-cues | reader/export + Reading Room payload QA PASS |
| Manthiri Kumari | source intake + mapping complete; Tamil first pass not started | not applicable from this booklet source | not started | 15 song/performance blocks mapped structurally; derivative gate blocked pending Tamil | blocked pending verified Tamil | next: canonical Tamil first pass PDF 2–13 |
| Raja Rani | 79/79 source pages; 70/70 screenplay pages verified | 58/58 archival scenes / 1,071 unique dialogue records | 80/80 exact labels → 44 verified entities/roles/collectives | 11 numbered songs + 4 screenplay refs; 5 later-anthology Kalaignar-attributed / 6 unresolved | screenplay 58/58 / 1,236 units; numbered songs 11/11 / 67 sections / 181 mapped line-cues | next: deterministic bilingual reader/export QA |

## Raja Rani reconciliation

Raja Rani is the work that triggered this repository-wide anti-staleness audit.

### Source/Tamil checkpoint

- canonical/source pages: **79/79 verified**;
- screenplay pages: **70/70 verified**;
- blocked/review source pages: **0**;
- archival scene derivatives: **58/58 verified**;
- immutable dialogue corpus: **1,071 unique records**;
- zero-dialogue scenes: **16**;
- cross-page dialogue records: **12**;
- exact source labels: **80/80**;
- verified entities/roles/collectives: **44**.

Direct-scan verdicts that permanently closed the former review gate include:

- PDF 27: `இரவெல்லாம்`;
- PDF 48: `வந்தனா`, `திடீர்னு`;
- PDF 57: `முன்னுக்கு பின் முரணாயிகிட்டே போவது?`;
- PDF 74: `K. N. சங்கரன் ...` is a later non-canonical ownership/library stamp and is excluded from canonical screenplay text.

### T055/T056 derivative-boundary QA correction

Final screenplay QA found that the old scene-55 derivative duplicated the `(முன்)` flashback whose sole derivative owner is scene 56.

Final disposition:

- scene 55 immutable dialogue records: **25**;
- scene 56 immutable dialogue records: **5**;
- five duplicate old scene-55 records removed from eligibility;
- corrected unique dialogue corpus: **1,071**;
- canonical page transcription: **unchanged**.

### English screenplay checkpoint

- verified archival scenes: **58/58**;
- verified English units: **1,236**;
- immutable dialogue links: **1,071/1,071**;
- unit mix: **1,090 dialogue-kind / 137 stage direction / 4 performance cue / 5 written text**;
- source-unlabelled spoken units: **19**;
- cross-page English units: **15**;
- draft/review screenplay units: **0**.

### Numbered-song English checkpoint

All **11/11** verified numbered front-matter Tamil song bodies now have separate source-linked English records under `works/raja-rani/translations/songs/`.

Whole-set song QA:

- translated songs: **11/11**;
- translation sections: **67**;
- Tamil-to-English mapped line/cue entries: **181/181**;
- mode: **`semantic-poetic-source-faithful`**;
- authorship unchanged: **5 later-anthology Kalaignar-attributed / 6 unresolved**;
- original-booklet item-level lyricist credits: **0**;
- scene 58 → song 11 contextual performance relation remains **review-level**, not promoted by translation.

The dedicated QA record is `works/raja-rani/translations/songs/FINAL_NUMBERED_SONG_TRANSLATION_QA.md`.

## Other completed work checkpoints

### Parasakthi

- 54/54 canonical Tamil pages verified;
- 46 observed scene derivatives complete;
- 642 dialogue records complete-verified;
- 14/14 song/verse authorship occurrences verified;
- 769 verified English units;
- deterministic reader/export QA PASS.

### Tirumbippaar!

- 104/104 canonical pages verified;
- 93/93 scene derivatives complete;
- 1,040 dialogue records;
- 45/45 exact source speaker labels dispositioned into 39 verified entities/role categories;
- 8 song/performance occurrences with 3 verified / 5 unresolved authorship dispositions;
- 1,321 verified English units;
- reader/export and deterministic EPUB QA PASS.

The cropped lower printer-imprint continuation on PDF 2 remains an intentional unresolved source crop, not a project-status defect.

### Manohara

- 82/82 canonical pages complete-verified;
- fidelity audit complete with zero unresolved source readings;
- 57/57 archival scene derivatives complete-verified;
- 983 immutable labelled-dialogue records complete-verified;
- 111 source labels dispositioned, with only `வர்மா` intentionally unresolved;
- 6 source-visible song/performance occurrences with 1 verified / 1 review / 4 unresolved authorship dispositions;
- 1,190 verified English units;
- reader preflight and deterministic reader/export QA PASS.

### Kalaignar Thirai Isai Paadalgal

- physical source: 194 PDF pages;
- 62 song-bearing / 132 ignored pages;
- 54/54 numbered Tamil songs complete-verified;
- 54/54 English songs complete-verified;
- 1,105/1,105 English line-cue mappings;
- reader/export QA PASS;
- Reading Room payload QA PASS at 23 film groups / 54 songs / 1,105 paired lines-cues / 8 cross-page songs.

### Manthiri Kumari

- 14-page film story-and-song booklet;
- source intake and structural mapping complete;
- story summary PDF 3–5;
- 15 song/performance blocks across PDF 6–13;
- canonical Tamil transcription remains not started;
- no structured derivative or English layer should advance before verified Tamil.

## Repository-wide synchronization rule

A major phase is **not complete** while any active current-status document still points to the prior phase.

At every major checkpoint, reconcile at least:

### Work-local

- `works/<work-id>/metadata.yaml`;
- `works/<work-id>/README.md`;
- active layer README/index/QA/audit files;
- work-specific handover and next-chat prompt, when present.

### Repository-wide

- `data/works.json`;
- root `README.md`;
- `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md` when project status or reusable lessons changed;
- this `docs/STATUS_CONSISTENCY_AUDIT.md`;
- shared processing/translation guides when the completed phase establishes a reusable rule.

Before declaring closure, search for superseded counts, stale blocked/review language, old next activities and prior completion labels. Historical batch/checkpoint documents may preserve their historical state when clearly labelled as historical; current startup/status surfaces may not.

## Repository-internal conclusion

The repository registry now reflects all six works and the current Raja Rani bilingual-text checkpoint.

No required Raja Rani source/Tamil, scene, dialogue, character, screenplay-English or numbered-song-English production remains. Its next repository-internal activity is **deterministic whole-work bilingual reader/export QA**, consuming both the 58 verified screenplay records and the separately structured 11 numbered-song translations. Reading Room integration preparation follows only after that QA gate passes.

Any later completion of that reader/export phase must trigger this same repository-wide synchronization gate again.