# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-09-06  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles current repository-wide status mirrors with the authoritative work checkpoints for all **seven registered works**. `data/works.json`, root README, project handover and active work-local metadata/handovers must agree before a major phase is considered closed.

## Result

**PASS for Ammayappan's source/structured authority and English checkpoint through scene 60.** Canonical Tamil is **105/105 dual-gate complete-verified**; scene derivatives are **63/63**; dialogue authority is **1,009 explicit + 16 source-role supplements = 1,025 downstream units**; character/entity coverage is **1,025/1,025** and **62/62 exact labels**. English translation is now **60/63 scenes / 1,188 verified units**.

The scene-3 post-closure source form `பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......` remains a distinct பூங்காவனம் dialogue unit with its semicolon preserved exactly. Scene 5 `திரு; ...` remains the other source-explicit non-colon speaker delimiter. Neither form is normalized to a colon.

## Current work matrix

| Work | Source/Tamil | Structured text | English | Reader / integration |
|---|---|---|---|---|
| Parasakthi | 54/54 canonical pages verified | 46 observed scenes / 642 dialogue records | 769 verified units | reader/export QA PASS |
| Tirumbippaar! | 104/104 canonical pages verified | 93/93 scenes / 1,040 dialogue records | 1,321 verified units | reader/export + deterministic EPUB QA PASS |
| Manohara | 82/82 canonical pages verified | 57/57 scenes / 983 dialogue records | 1,190 verified units | reader/export QA PASS; Reading Room ready |
| Kalaignar Thirai Isai Paadalgal | 54/54 numbered Tamil songs verified | 54 song records | 54/54 songs / 1,105 line-cues | reader/export + Reading Room payload QA PASS; site not applied |
| Manthiri Kumari | PDF 2–13 canonical Tamil complete-verified; 12/12 pages; 0 unresolved | credits; story summary 1/1; performance records 15/15 | 13 prose units + 15/15 performances / 52 sections / 234 line-cues | bilingual reader + Reading Room payload QA PASS; site not applied |
| Raja Rani | 79/79 source pages; 70/70 screenplay pages verified | 58/58 scenes / 1,071 dialogues / 80 labels / 44 entities | screenplay 1,236 units + 11/11 songs / 181 line-cues | bilingual reader + Reading Room payload QA PASS; site not applied |
| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **scene 60/63 / 1,188 units** | reader blocked pending final English + whole-work reconciliation |

## Ammayappan current checkpoint

### Frozen source/Tamil authority

- canonical Tamil: **105/105 dual-gate complete-verified**;
- PDF 10 post-fidelity correction: `மாடம்` — commit `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`;
- source-visible boundaries / distinct headings: **63 / 41**;
- scene derivatives: **63/63 complete-verified**;
- boundary ownership: **PASS — 0 gaps / 0 overlaps / 105 pages represented**;
- unresolved canonical markers / review pages: **0 / 0**.

### Dialogue / character authority

- explicit colon-labelled records: **1,009**;
- source-role supplements: **16**;
- downstream dialogue units: **1,025**;
- exact source labels: **62**;
- unresolved source-role blocks: **0**;
- source punctuation normalizations: **0**;
- character/entity index: **26/26 verified entities**;
- exact-label / dialogue-unit coverage: **62/62 / 1,025/1,025**;
- `முத்`: **80 முத்தன் / 97 முத்தாயி**;
- `தன`: **1 தனபதி / 9 தனவணிகர்**.

### Song/performance gate

- candidates reviewed: **64/64**;
- retained source-visible occurrences: **5** — scenes **7, 10, 19, 40, 59**;
- unresolved authorship: **3**;
- source-attributed literary quotation: **1**;
- authorship-not-applicable character japa: **1**;
- complete named lyric blocks / standalone Tamil lyric files: **0 / 0**.

### English translation gate

- verified scenes: **60/63**;
- verified units: **1,188**;
- dialogue units: **1,009** = **993 explicit + 16 source-role supplements**;
- stage/action units: **175**;
- standalone song-reference units: **3**;
- japa units: **1**;
- cross-page units: **28**;
- unique occurrence links through scene 60: **5** — `ammaiyappan-song-001` through `ammaiyappan-song-005`;
- structural stars translated as prose: **0**;
- canonical Tamil/dialogue/character/song evidence changed by English: **no**.

Batch **56–60** reconciliation is **PASS**:

| Scene | Explicit dialogue | Source-role supplements | Stage/action | Song-reference | Total |
|---|---:|---:|---:|---:|---:|
| 56 | 33 | 0 | 8 | 0 | 41 |
| 57 | 3 | 0 | 0 | 0 | 3 |
| 58 | 11 | 0 | 2 | 0 | 13 |
| 59 | 14 | 1 | 1 | 1 | 17 |
| 60 | 7 | 0 | 1 | 0 | 8 |
| **Total** | **68** | **1** | **12** | **1** | **82** |

Batch safeguards:

- scene 56 keeps `ammaiyappan-en-s056-u031` and `ammaiyappan-en-s056-u037` whole across their page boundaries; no mythological or lexical gaps are externally repaired;
- scene 58 keeps the three-page `ammaiyappan-en-s058-u006` whole and preserves its anti-prestige, religious-hypocrisy and **Self-Respect** rhetoric without softening;
- `ammaiyappan-s059-r001` is linked once as `source-context-attributed` Muthan speech; it is not manufactured as a printed label or merged into immutable `d008`;
- `ammaiyappan-song-005` is linked only to two distinct printed spans: Muthan's source-visible request in `d014` and the separate cue that Muthayi sings through tears while he walks toward the gallows;
- no title, lyric body or authorship is reconstructed for `ammaiyappan-song-005`, and no unnamed song identities are merged without stronger evidence;
- scene 60 preserves the political force of `விடுதலை விரும்பி` as **seeker of freedom**;
- no frozen Tamil/dialogue/character/song evidence was modified.

**Next translation batch:** final archival scenes **61–63**. After scene 63, perform whole-work English reconciliation before starting reader/export work.

## Stable downstream checkpoints for other works

- **Manthiri Kumari:** 12/12 canonical pages; story summary 1/1; performance records 15/15; English 13 prose units + 15 performances / 52 sections / 234 paired line-cues; bilingual reader and Reading Room payload QA PASS; item-level lyricists 0 verified / 15 unresolved; site not applied.
- **Raja Rani:** 79/79 source pages; 70/70 screenplay pages; 58/58 scenes; 1,071 dialogues; 80 labels / 44 entities; 1,236 screenplay English units; 11/11 songs / 181 line-cues; reader and Reading Room payload QA PASS; site not applied.
- **Tirumbippaar!:** 104/104 canonical pages; 93/93 scenes; 1,040 dialogues; 1,321 English units; deterministic EPUB QA PASS, SHA-256 `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`.

## Repository-wide synchronization rule

A major phase is not complete while an active current-status document still advertises the prior checkpoint. Synchronize work-local metadata/README/index/QA/handover plus `data/works.json`, root README, master handover/status audit and any shared guide changed by reusable lessons. Historical checkpoint files may retain historical numbers when clearly labelled historical.

## Conclusion

Ammayappan's canonical Tamil and structured source-derived layers remain **closed at the corrected 1,025-unit authority**. English translation is verified through **scene 60/63 at 1,188 units**. The next bounded activity is the final source-scene batch **61–63**, followed by whole-work English reconciliation before reader/export.