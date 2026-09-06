# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-09-06  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles current repository-wide status mirrors with the authoritative work checkpoints for all **seven registered works**. `data/works.json`, root README, project handover and active work-local metadata/handovers must agree before a major phase is considered closed.

## Result

**PASS for Ammayappan's source/structured authority and English checkpoint through scene 30.** Canonical Tamil is **105/105 dual-gate complete-verified**; scene derivatives are **63/63**; dialogue authority is **1,009 explicit + 16 source-role supplements = 1,025 downstream units**; character/entity coverage is **1,025/1,025** and **62/62 exact labels**. English translation is now **30/63 scenes / 738 verified units**.

The scene-3 post-closure source form `பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......` remains a distinct பூங்காவனம் dialogue unit with its semicolon preserved exactly. Scene 5 `திரு; ...` remains the other source-explicit non-colon speaker delimiter. Neither form is normalized to a colon.

## Current work matrix

| Work | Source/Tamil | Structured text | English | Reader / integration |
|---|---|---|---|---|
| Parasakthi | 54/54 canonical pages verified | 46 observed scenes / 642 dialogue records | 769 verified units | reader/export QA PASS |
| Tirumbippaar! | 104/104 canonical pages verified | 93/93 scenes / 1,040 dialogue records | 1,321 verified units | reader/export + deterministic EPUB QA PASS |
| Manohara | 82/82 canonical pages verified | 57/57 scenes / 983 dialogue records | 1,190 verified units | reader/export QA PASS; Reading Room ready |
| Kalaignar Thirai Isai Paadalgal | 54/54 numbered Tamil songs verified | 54 song records | 54/54 songs / 1,105 line-cues | reader/export + Reading Room payload QA PASS; site not applied |
| Manthiri Kumari | PDF 2–13 canonical Tamil complete-verified; 12/12 pages; 0 unresolved | credits; PDF 3–5 story summary 1/1; PDF 6–13 performance records 15/15 | complete-verified — 13 prose units + 15/15 performances / 52 sections / 234 line-cues | bilingual reader QA PASS + Reading Room payload QA PASS; site not applied |
| Raja Rani | 79/79 source pages; 70/70 screenplay pages verified | 58/58 scenes / 1,071 dialogue records / 80 labels / 44 entities | screenplay 1,236 units + 11/11 songs / 181 song line-cues | bilingual reader QA PASS + Reading Room payload QA PASS; site not applied |
| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **verified through scene 30/63 / 738 units** | reader blocked pending complete English |

## Ammayappan current checkpoint

### Frozen source/Tamil authority

- canonical Tamil: **105/105 dual-gate complete-verified**;
- PDF 10 post-fidelity correction: `மாடம்` — commit `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`;
- canonical source-visible boundary inventory: **63**;
- distinct verified heading forms: **41**;
- scene derivatives: **63/63 complete-verified**;
- boundary ownership QA: **PASS — 0 gaps / 0 overlaps**;
- canonical PDF representation: **105/105 — PDF 5–109**;
- unresolved canonical markers / review pages: **0 / 0**.

### Dialogue and character authority

- explicit colon-labelled records: **1,009**;
- source-role supplements: **16**;
- downstream dialogue units: **1,025**;
- exact source labels: **62**;
- unresolved source-role blocks: **0**;
- alias normalization in source dialogue evidence: **0**;
- source punctuation normalization: **0**;
- character/entity index: **26/26 verified entities**;
- exact-label coverage: **62/62**;
- downstream dialogue-unit coverage: **1,025/1,025**;
- record-aware labels: `முத்`, `தன`;
- `முத்`: **80 முத்தன் / 97 முத்தாயி**;
- `தன`: **1 தனபதி / 9 தனவணிகர்**.

The earlier 1,024-unit / 15-supplement checkpoint is historical. Active current-status surfaces must use 1,025 / 16.

### Song/performance gate

- candidate hits reviewed: **64/64**;
- retained source-visible occurrences: **5** — scenes 7, 10, 19, 40, 59;
- unresolved authorship occurrences: **3**;
- source-attributed literary quotation occurrences: **1**;
- authorship-not-applicable japa occurrences: **1**;
- complete named song lyric blocks printed: **0**;
- standalone Tamil lyric files: **0**;
- external item-level evidence used: **no**.

### English translation gate

- schema/preflight: established;
- source numbering invented: **0**;
- verified scenes: **30/63**;
- verified English units: **738**;
- dialogue units: **627** = **614 explicit links + 13 source-role supplements**;
- stage/action units: **109**;
- standalone song-reference units: **2**;
- cross-page units: **16**;
- source-visible song/performance occurrence links encountered through scene 30: **3** — `ammaiyappan-song-001`, `ammaiyappan-song-002`, `ammaiyappan-song-003`;
- source-visible structural stars translated as prose: **0**;
- canonical Tamil/dialogue/character/song evidence changed by English: **no**.

Batch **26–30** reconciliation is **PASS**:

| Scene | Explicit dialogue | Source-role supplements | Stage/action | Total |
|---|---:|---:|---:|---:|
| 26 | 13 | 0 | 3 | 16 |
| 27 | 25 | 2 | 11 | 38 |
| 28 | 11 | 0 | 1 | 12 |
| 29 | 42 | 0 | 1 | 43 |
| 30 | 16 | 1 | 4 | 21 |
| **Total** | **107** | **3** | **20** | **130** |

Batch safeguards:

- the scene-25 handoff's statement that scenes 26–30 contained no supplements was stale; live source-role authority identifies `ammaiyappan-s027-r001`, `ammaiyappan-s027-r002` and `ammaiyappan-s030-r001`, all preserved as source-context-attributed derivative provenance;
- five new cross-page units remain single logical owners: scene 26 d010, scene 27 d017, scene 29 d022 and d035, scene 30 d007;
- scene 26 preserves its political metaphor chain and does not silently repair frozen `தோற்ப்பும்வரை`;
- scene 27 keeps immutable d022 ownership despite its embedded slap/action and additional printed tokens, and keeps both context-attributed supplements distinct from printed labels;
- scene 29 preserves exact source/register terms and embedded source-owned action without repairing frozen `அவள் உங்க அப்பா...அதனால்!`;
- scene 30 retains the self-described Purananuru poem inside immutable d007 as one dialogue unit; no external poem text or attribution is imported and no duplicate literary-verse owner is created;
- the closed song/performance inventory has **0 retained occurrences in scenes 26–30**, so no new song/performance occurrence link is introduced.

**Next translation batch:** archival scenes **31–35**. The closed source-role layer contains **one** supplement in that range — `ammaiyappan-s035-r001`; the closed song/performance inventory contains **no retained occurrence** there. Continue from frozen verified derivatives with exact speaker/source-role/page provenance and whole cross-page units.

## Stable downstream checkpoints for other works

- **Manthiri Kumari:** 12/12 canonical pages; story summary 1/1; performance records 15/15; English 13 prose units + 15 performances / 52 sections / 234 paired line-cues; bilingual reader and Reading Room payload QA PASS; item-level lyricists remain 0 verified / 15 unresolved; site not applied.
- **Raja Rani:** 79/79 source pages; 70/70 screenplay pages; 58/58 scene derivatives; 1,071 dialogues; 80 labels / 44 entities; 1,236 screenplay English units; 11/11 numbered songs / 181 line-cues; reader and Reading Room payload QA PASS; site not applied.
- **Tirumbippaar!:** 104/104 canonical pages; 93/93 scenes; 1,040 dialogues; 1,321 English units; deterministic EPUB QA PASS, SHA-256 `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`.

## Repository-wide synchronization rule

A major phase is not complete while an active current-status document still advertises the prior checkpoint. At phase closure synchronize work-local metadata/README/index/QA/handover plus `data/works.json`, root README, master handover/status audit and any shared guide changed by reusable lessons. Historical batch records may retain their historical state when clearly labelled historical.

## Conclusion

Ammayappan's canonical Tamil and structured source-derived layers remain **closed at the corrected 1,025-unit authority**. English translation is verified through **scene 30/63 at 738 current units**. The next bounded activity is **translate and source-review archival scenes 31–35** without changing frozen source evidence.