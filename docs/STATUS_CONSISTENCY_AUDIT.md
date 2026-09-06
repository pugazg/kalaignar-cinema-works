# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-09-06  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles current repository-wide status mirrors with the authoritative work checkpoints for all **seven registered works**. `data/works.json`, root README, project handover and active work-local metadata/handovers must agree before a major phase is considered closed.

## Result

**PASS for Ammayappan's source/structured authority and English checkpoint through scene 40.** Canonical Tamil is **105/105 dual-gate complete-verified**; scene derivatives are **63/63**; dialogue authority is **1,009 explicit + 16 source-role supplements = 1,025 downstream units**; character/entity coverage is **1,025/1,025** and **62/62 exact labels**. English translation is now **40/63 scenes / 979 verified units**.

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
| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **scene 40/63 / 979 units** | reader blocked pending complete English |

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

The earlier 1,024-unit / 15-supplement checkpoint is historical. Active current-status surfaces use **1,025 / 16**.

### Song/performance gate

- candidates reviewed: **64/64**;
- retained source-visible occurrences: **5** — scenes **7, 10, 19, 40, 59**;
- unresolved authorship: **3**;
- source-attributed literary quotation: **1**;
- authorship-not-applicable character japa: **1**;
- complete named lyric blocks / standalone Tamil lyric files: **0 / 0**;
- external item-level evidence used: **no**.

### English translation gate

- verified scenes: **40/63**;
- verified units: **979**;
- dialogue units: **840** = **826 explicit + 14 source-role supplements**;
- stage/action units: **136**;
- standalone song-reference units: **2**;
- japa units: **1**;
- cross-page units: **22**;
- unique occurrence links through scene 40: **4** — `ammaiyappan-song-001` through `ammaiyappan-song-004`;
- structural stars translated as prose: **0**;
- canonical Tamil/dialogue/character/song evidence changed by English: **no**.

Batch **36–40** reconciliation is **PASS**:

| Scene | Explicit dialogue | Source-role supplements | Stage/action | Japa | Total |
|---|---:|---:|---:|---:|---:|
| 36 | 23 | 0 | 5 | 0 | 28 |
| 37 | 16 | 0 | 0 | 0 | 16 |
| 38 | 8 | 0 | 1 | 0 | 9 |
| 39 | 16 | 0 | 2 | 0 | 18 |
| 40 | 17 | 0 | 1 | 1 | 19 |
| **Total** | **80** | **0** | **9** | **1** | **90** |

Batch safeguards:

- live closed source-role evidence has **0 supplements** in scenes 36–40;
- scene 37 `ammaiyappan-s037-d003` is the sole new cross-page source record and remains one English unit across PDF 80→81;
- scene 36 preserves exact `தன` source labels and keeps embedded child action plus `ஆராரோ` inside immutable merchant dialogue `d008`; the closed song inventory does not authorize a separate occurrence there;
- scene 38 preserves embedded source-owned actions and the printed `குறவன்` social/community label without euphemistic replacement;
- scene 39's Purananuru mention stays a rhetorical reference only; no external verse is imported;
- scene 40 `ammaiyappan-song-004` is represented only as source-visible character japa: one opening japa/nishta cue plus the separately printed labelled `முத்தாயி...முத்தாயி...` dialogue span linked to the same occurrence; no soundtrack title, lyric body or lyricist is inferred;
- frozen/uncertain scene-40 forms are handled by notes/transliteration rather than upstream Tamil repair.

**Next translation batch:** archival scenes **41–45**. The closed source-role layer has **0 supplements** in that range and the closed song/performance inventory has **0 retained occurrences** there. Preserve exact speaker/page provenance and whole cross-page source units.

## Stable downstream checkpoints for other works

- **Manthiri Kumari:** 12/12 canonical pages; story summary 1/1; performance records 15/15; English 13 prose units + 15 performances / 52 sections / 234 paired line-cues; bilingual reader and Reading Room payload QA PASS; item-level lyricists 0 verified / 15 unresolved; site not applied.
- **Raja Rani:** 79/79 source pages; 70/70 screenplay pages; 58/58 scenes; 1,071 dialogues; 80 labels / 44 entities; 1,236 screenplay English units; 11/11 songs / 181 line-cues; reader and Reading Room payload QA PASS; site not applied.
- **Tirumbippaar!:** 104/104 canonical pages; 93/93 scenes; 1,040 dialogues; 1,321 English units; deterministic EPUB QA PASS, SHA-256 `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`.

## Repository-wide synchronization rule

A major phase is not complete while an active current-status document still advertises the prior checkpoint. Synchronize work-local metadata/README/index/QA/handover plus `data/works.json`, root README, master handover/status audit and any shared guide changed by reusable lessons. Historical checkpoint files may retain historical numbers when clearly labelled historical.

## Conclusion

Ammayappan's canonical Tamil and structured source-derived layers remain **closed at the corrected 1,025-unit authority**. English translation is verified through **scene 40/63 at 979 units**. The next bounded activity is **scenes 41–45** without changing frozen source evidence.