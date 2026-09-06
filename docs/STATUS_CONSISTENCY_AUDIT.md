# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-09-06  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles current repository-wide status mirrors with the authoritative work checkpoints for all **seven registered works**. `data/works.json`, root README, project handover and active work-local metadata/handovers must agree before a major phase is considered closed.

## Result

**PASS for Ammayappan's source/structured authority and English checkpoint through scene 35.** Canonical Tamil is **105/105 dual-gate complete-verified**; scene derivatives are **63/63**; dialogue authority is **1,009 explicit + 16 source-role supplements = 1,025 downstream units**; character/entity coverage is **1,025/1,025** and **62/62 exact labels**. English translation is now **35/63 scenes / 889 verified units**.

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
| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **verified through scene 35/63 / 889 units** | reader blocked pending complete English |

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
- verified scenes: **35/63**;
- verified English units: **889**;
- dialogue units: **760** = **746 explicit links + 14 source-role supplements**;
- stage/action units: **127**;
- standalone song-reference units: **2**;
- cross-page units: **21**;
- source-visible song/performance occurrence links encountered through scene 35: **3** — `ammaiyappan-song-001`, `ammaiyappan-song-002`, `ammaiyappan-song-003`;
- source-visible structural stars translated as prose: **0**;
- canonical Tamil/dialogue/character/song evidence changed by English: **no**.

Batch **31–35** reconciliation is **PASS**:

| Scene | Explicit dialogue | Source-role supplements | Stage/action | Total |
|---|---:|---:|---:|---:|
| 31 | 7 | 0 | 1 | 8 |
| 32 | 0 | 0 | 1 | 1 |
| 33 | 30 | 0 | 2 | 32 |
| 34 | 4 | 0 | 0 | 4 |
| 35 | 91 | 1 | 14 | 106 |
| **Total** | **132** | **1** | **18** | **151** |

Batch safeguards:

- scene 32 is action-only and creates no invented dialogue;
- five new cross-page units remain single logical owners: scene 33 d020 plus scene 35 d014, d034, d074 and d087;
- scene 33 preserves the conscience/worm/peacock metaphor, embedded source-owned actions and only the printed Layla–Majnun/Qays reference; no external story material is imported;
- scene 34 keeps frozen `வாட்டமா நான்?` visible by transliteration rather than speculative repair;
- scene 35 links `ammaiyappan-s035-r001` only as source-context-attributed Tirisangu provenance and does not manufacture a printed speaker label;
- scene 35 preserves exact `முத்` / `திரி` source ownership, source irregularities, `oppari`, `Ardhanarishvaras`, the retail/wholesale joke, cross-dressing, mistaken abduction, ring exchange and Rama/Sita/Lakshmana forest-life humour without altering frozen evidence;
- the closed song/performance inventory has **0 retained occurrences in scenes 31–35**, so no new song/performance occurrence link is introduced.

**Next translation batch:** archival scenes **36–40**. Inspect the live closed source-role layer and `songs/inventory.json` before writing. Scene **40** contains a retained source-visible song/performance occurrence; represent only booklet-supported material and do not reconstruct absent lyrics or authorship.

## Stable downstream checkpoints for other works

- **Manthiri Kumari:** 12/12 canonical pages; story summary 1/1; performance records 15/15; English 13 prose units + 15 performances / 52 sections / 234 paired line-cues; bilingual reader and Reading Room payload QA PASS; item-level lyricists remain 0 verified / 15 unresolved; site not applied.
- **Raja Rani:** 79/79 source pages; 70/70 screenplay pages; 58/58 scene derivatives; 1,071 dialogues; 80 labels / 44 entities; 1,236 screenplay English units; 11/11 numbered songs / 181 line-cues; reader and Reading Room payload QA PASS; site not applied.
- **Tirumbippaar!:** 104/104 canonical pages; 93/93 scenes; 1,040 dialogues; 1,321 English units; deterministic EPUB QA PASS, SHA-256 `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`.

## Repository-wide synchronization rule

A major phase is not complete while an active current-status document still advertises the prior checkpoint. At phase closure synchronize work-local metadata/README/index/QA/handover plus `data/works.json`, root README, master handover/status audit and any shared guide changed by reusable lessons. Historical batch records may retain their historical state when clearly labelled historical.

## Conclusion

Ammayappan's canonical Tamil and structured source-derived layers remain **closed at the corrected 1,025-unit authority**. English translation is verified through **scene 35/63 at 889 current units**. The next bounded activity is **translate and source-review archival scenes 36–40** without changing frozen source evidence; scene 40's retained performance occurrence must remain source-only.