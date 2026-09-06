# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-09-06  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles current repository-wide status mirrors with the authoritative work checkpoints for all **seven registered works**. `data/works.json`, root README, project handover and active work-local metadata/handovers must agree before a major phase is considered closed.

## Result

**PASS for Ammayappan's source/structured authority and English checkpoint through scene 55.** Canonical Tamil is **105/105 dual-gate complete-verified**; scene derivatives are **63/63**; dialogue authority is **1,009 explicit + 16 source-role supplements = 1,025 downstream units**; character/entity coverage is **1,025/1,025** and **62/62 exact labels**. English translation is now **55/63 scenes / 1,106 verified units**.

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
| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **scene 55/63 / 1,106 units** | reader blocked pending complete English |

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

- verified scenes: **55/63**;
- verified units: **1,106**;
- dialogue units: **940** = **925 explicit + 15 source-role supplements**;
- stage/action units: **163**;
- standalone song-reference units: **2**;
- japa units: **1**;
- cross-page units: **25**;
- unique occurrence links through scene 55: **4** — `ammaiyappan-song-001` through `ammaiyappan-song-004`;
- structural stars translated as prose: **0**;
- canonical Tamil/dialogue/character/song evidence changed by English: **no**.

Batch **51–55** reconciliation is **PASS**:

| Scene | Explicit dialogue | Source-role supplements | Stage/action | Total |
|---|---:|---:|---:|---:|
| 51 | 4 | 0 | 1 | 5 |
| 52 | 33 | 0 | 8 | 41 |
| 53 | 17 | 0 | 3 | 20 |
| 54 | 2 | 0 | 2 | 4 |
| 55 | 1 | 0 | 0 | 1 |
| **Total** | **57** | **0** | **14** | **71** |

Batch safeguards:

- live closed source-role evidence contributes **0 supplements** in scenes 51–55;
- the closed song/performance inventory has **0 retained occurrences** in scenes 51–55;
- scene 51 `ammaiyappan-en-s051-u003` remains one cross-page dialogue across PDF 89→90 / printed 87→88;
- scene 52 preserves coercive sexual rhetoric without euphemism, keeps source-owned action/parenthetical cues inside immutable dialogue, retains printed Sita/Kannagi/Silappathikaram references without external expansion, and transliterates uncertain `காப்பாரியிலே` as `kāppāri` rather than claiming a source repair;
- scene 52 `ammaiyappan-en-s052-u032` remains one cross-page dialogue across PDF 92→93 / printed 90→91; irregular frozen clusters are handled only by bounded notes/context;
- scene 52 preserves `கடமை, கண்ணியம், கட்டுப்பாடு` as the rhetorical triad **Duty, Dignity and Discipline**;
- scene 53 keeps `(மூர்ச்சை தெளிந்து)` dialogue-owned, preserves `ஊடல்`, retains frozen `வெள்ளாட்டி` as `vellatti`, and translates its sarcastic sexual-coercion rhetoric without euphemism;
- scene 54 keeps `நாமார்க்கும் குடியல்லோம்: நமனை அஞ்சோம்!` inside immutable Vedalam dialogue and does not manufacture a literary-verse/song occurrence;
- scene 55 preserves the immediate execution order without adding procedure;
- no frozen Tamil/dialogue/character/song evidence was modified.

**Next translation batch:** archival scenes **56–60**. Scene 59 contains closed source-context-attributed supplement `ammaiyappan-s059-r001` and retained source-visible occurrence `ammaiyappan-song-005`. Preserve exact speaker/page provenance and whole cross-page source units; link the occurrence only to printed source-visible material, without reconstructing absent lyrics, title or authorship or merging unnamed song identities without stronger evidence.

## Stable downstream checkpoints for other works

- **Manthiri Kumari:** 12/12 canonical pages; story summary 1/1; performance records 15/15; English 13 prose units + 15 performances / 52 sections / 234 paired line-cues; bilingual reader and Reading Room payload QA PASS; item-level lyricists 0 verified / 15 unresolved; site not applied.
- **Raja Rani:** 79/79 source pages; 70/70 screenplay pages; 58/58 scenes; 1,071 dialogues; 80 labels / 44 entities; 1,236 screenplay English units; 11/11 songs / 181 line-cues; reader and Reading Room payload QA PASS; site not applied.
- **Tirumbippaar!:** 104/104 canonical pages; 93/93 scenes; 1,040 dialogues; 1,321 English units; deterministic EPUB QA PASS, SHA-256 `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`.

## Repository-wide synchronization rule

A major phase is not complete while an active current-status document still advertises the prior checkpoint. Synchronize work-local metadata/README/index/QA/handover plus `data/works.json`, root README, master handover/status audit and any shared guide changed by reusable lessons. Historical checkpoint files may retain historical numbers when clearly labelled historical.

## Conclusion

Ammayappan's canonical Tamil and structured source-derived layers remain **closed at the corrected 1,025-unit authority**. English translation is verified through **scene 55/63 at 1,106 units**. The next bounded activity is **scenes 56–60**, with scene-59 source-role and source-visible performance provenance handled without changing frozen source evidence.