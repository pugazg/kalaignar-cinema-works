# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-09-06  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles current repository-wide status mirrors with the authoritative work checkpoints for all **seven registered works**. `data/works.json`, root README, project handover and active work-local metadata/handovers must agree before a major phase is considered closed.

## Result

**PASS for Ammayappan's source/structured authority — canonical Tamil is 105/105 dual-gate complete-verified; scene derivatives are 63/63; dialogue authority is 1,009 explicit + 16 source-role supplements = 1,025 downstream units; character/entity coverage is 1,025/1,025 and 62/62 exact labels. English translation is verified through scene 15/63 at 355/355 current units.**

The scene-3 post-closure source form `பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......` is a distinct பூங்காவனம் dialogue unit. Its semicolon is preserved exactly. Scene 5 `திரு; ...` remains the other source-explicit non-colon speaker delimiter. Neither form is normalized to a colon.

## Current work matrix

| Work | Source/Tamil | Structured text | English | Reader / integration |
|---|---|---|---|---|
| Parasakthi | 54/54 canonical pages verified | 46 observed scenes / 642 dialogue records | 769 verified units | reader/export QA PASS |
| Tirumbippaar! | 104/104 canonical pages verified | 93/93 scenes / 1,040 dialogue records | 1,321 verified units | reader/export + deterministic EPUB QA PASS |
| Manohara | 82/82 canonical pages verified | 57/57 scenes / 983 dialogue records | 1,190 verified units | reader/export QA PASS; Reading Room ready |
| Kalaignar Thirai Isai Paadalgal | 54/54 numbered Tamil songs verified | 54 song records | 54/54 songs / 1,105 line-cues | reader/export + Reading Room payload QA PASS; site not applied |
| Manthiri Kumari | PDF 2–13 canonical Tamil complete-verified; 12/12 pages; 0 unresolved | credits; PDF 3–5 story summary 1/1; PDF 6–13 performance records 15/15 | complete-verified — 13 prose units + 15/15 performances / 52 sections / 234 line-cues | bilingual reader QA PASS + Reading Room payload QA PASS; site not applied |
| Raja Rani | 79/79 source pages; 70/70 screenplay pages verified | 58/58 scenes / 1,071 dialogue records / 80 labels / 44 entities | screenplay 1,236 units + 11/11 songs / 181 song line-cues | bilingual reader QA PASS + Reading Room payload QA PASS; site not applied |
| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **verified through scene 15/63 / 355 units** | reader blocked pending complete English |

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
- retained source-visible occurrences: **5**;
- unresolved authorship occurrences: **3**;
- source-attributed literary quotation occurrences: **1**;
- authorship-not-applicable japa occurrences: **1**;
- complete named song lyric blocks printed: **0**;
- standalone Tamil lyric files: **0**;
- external item-level evidence used: **no**.

### English translation gate

- schema/preflight: established;
- source numbering invented: **0**;
- verified scenes: **15/63**;
- verified English units: **355**;
- explicit dialogue links: **295/295**;
- source-role supplement links: **8/8**;
- stage/action units: **51**;
- standalone song-reference units: **1**;
- cross-page units: **3**;
- source-visible song/performance occurrence links encountered through scene 15: **2** — `ammaiyappan-song-001`, `ammaiyappan-song-002`;
- scene-3 `பூங் ; ...` supplement: preserved as source-explicit non-colon provenance;
- scene-5 `திரு; ...` supplement: preserved as source-explicit non-colon provenance;
- scene-7 unnamed Muthan–Muthayi performance: cue only; no lyric/title/authorship reconstruction;
- scene-10 Kambar occurrence: fragment kept inside immutable dialogue record `ammaiyappan-s010-d010`; no duplicate verse ownership;
- scene-11 context-attributed supplements `ammaiyappan-s011-r001` / `r002`: preserved without manufacturing printed labels;
- scene-15 `குரல்` record: kept whole across PDF 31→32 with page-segment provenance;
- retained song/performance occurrences in scenes 11–15: **0**;
- canonical Tamil/dialogue/character/song evidence changed by English: **no**.

**Next translation batch:** archival scenes **16–20**. Preserve the two closed source-role supplements in scene 17 and, in scene 19, translate only the source-visible singing-performance cue represented by `ammaiyappan-song-003`; do not reconstruct a song title or lyrics.

## Manthiri Kumari reconciliation checkpoint

- source: **14 PDF pages**, image-only, SHA-256 `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`;
- canonical range: **PDF 2–13**;
- canonical Tamil: **12/12 pages complete-verified**;
- unresolved canonical readings: **0**;
- direct user post-fidelity scan corrections: **recorded, applied and reconciled**;
- source subdivision form: **`தொகையறா`** where applicable;
- credits layer: **complete-verified**;
- story-summary Tamil derivative: **complete-verified — PDF 3–5 / 1 continuous record / 0 synthetic scene IDs / 0 immutable dialogue IDs**;
- source-linked performance records: **15/15 complete-verified — PDF 6–13, 8/8 source pages**;
- missing / duplicate performance record IDs: **0 / 0**;
- current anthology relationship: **1 confirmed existing witness / 14 source-only blocks**;
- booklet item-level lyric authorship: **0 verified / 15 unresolved**;
- English story-summary translation: **1/1 complete-verified**;
- English story-summary logical units: **13**;
- English story-summary cross-page units: **1**;
- English performance translation records: **15/15 complete-verified**;
- English performance sections: **52**;
- Tamil performance lines/cues mapped: **234**;
- English performance lines/cues mapped: **234**;
- line/cue mapping mismatches: **0**;
- cross-page translated performance records: **7 — 002, 004, 006, 007, 009, 011, 013**;
- source-visible `தொகையறா` / `பாட்டு`, `(வசனம்)` and other performance/refrain cues: **preserved**;
- performance 13 heading/turn-label mismatch: **preserved — heading `பார்த்திபன்—மந்திரிகுமாரி`, internal labels `பார்த்திபன்` / `அமுதவல்லி`**;
- authorship upgrades introduced by translation: **0**;
- canonical Tamil changed by translation: **no**;
- synthetic screenplay scene IDs created by translation: **0**;
- external/unprinted lyric lines imported: **0**;
- final translation QA: **PASS**;
- deterministic bilingual reader/export: **complete-verified, QA PASS**;
- reader navigation: **16 natural source structures — 1 story summary + 15 performance blocks**;
- reader performance sections: **52**;
- reader Tamil/English performance line-cues: **234 / 234**;
- reader line/cue mismatches: **0**;
- reader cross-page performance records: **7**;
- reader preserves **1 confirmed anthology witness / 14 source-only blocks** and **0 verified / 15 unresolved** item-level lyricists;
- canonical Tamil changed by reader construction: **no**;
- synthetic screenplay scene IDs created by reader construction: **0**;
- Reading Room integration payload: **complete-verified — QA PASS**;
- payload mode: **source-linked-composition**;
- payload path: `works/manthiri-kumari/integrations/reading-room/reading-room.json`;
- payload source/translation targets: **32**;
- payload story-summary units: **13**;
- payload performance blocks / sections / line-cues: **15 / 52 / 234**;
- payload bytes: **15,704**;
- payload SHA-256: `20a0db293b936757e7d01def336252f28543337f319dfae6ad7bf5ae886bab43`;
- payload QA errors / warnings: **0 / 0**;
- payload authorship upgrades: **0**;
- payload synthetic screenplay scene IDs: **0**;
- Reading Room site application: **not-applied**.

There is **no remaining required Manthiri Kumari repository-internal transcription, structured-derivative, translation, reader/export or Reading Room-payload work**. The only downstream action is to apply the verified payload in the separate Kalaignar Digital Library / Reading Room implementation repository when that repository is explicitly authorized for modification. The site must preserve the natural story-summary + 15-performance navigation, source/page provenance, source-visible cues, cross-witness disposition and unresolved item-level lyric-authorship state.

## Raja Rani final reconciliation

- source pages: **79/79 verified**;
- screenplay pages: **70/70 verified**;
- archival scenes: **58/58**, blocked 0;
- immutable dialogue records: **1,071**;
- exact labels / entities: **80/80 / 44**;
- screenplay English: **58/58 scenes / 1,236 units / 1,071 links**;
- numbered-song English: **11/11 / 67 sections / 181 Tamil-English line-cues**;
- deterministic bilingual reader/export: **QA PASS** over **200 authoritative inputs**;
- reader Markdown SHA-256: `6437a0a39cebbaf17ab63f76f7aef6f9f62eb3c4abbd07864974d47be20902c8`;
- reader HTML SHA-256: `c24ea9ab0f1ee77b3bc795b3134e4ad8bed78f00d6a8f896f9749052ff074ec6`;
- reader JSON SHA-256: `76827d570f3079c04463e3142a9edf32f35c1497e2b820bfa467f8203d7441e2`;
- Reading Room payload: **QA PASS**, **974,510 bytes**, SHA-256 `ab1058cb5a22ba78e68938f50efc586cc53eb07ef544bdf3919bb3c4b8c46c9b`;
- site application: **not-applied**.

Permanent Raja Rani safeguards remain unchanged: T055/T056 duplicate IDs are absent; songs 3/5/6/7/8 remain later-anthology Kalaignar-attributed, songs 1/2/4/9/10/11 unresolved; scene 58 → song 11 remains review-level; screenplay ordinals remain archival navigation only.

## Repository-wide synchronization rule

A major phase is not complete while an active current-status document still advertises the prior checkpoint. At phase closure synchronize work-local metadata/README/index/QA/handover plus `data/works.json`, root README, master handover/status audit and any shared guide changed by reusable lessons. Historical batch records may retain their historical state when clearly labelled historical.

## Conclusion

Ammayappan's canonical Tamil and structured source-derived layers are **closed and synchronized to the corrected 1,025-unit authority**. English translation is verified through **scene 15/63 at 355 current units**. The current bounded activity is **translate and source-review archival scenes 16–20**, preserving scene-17 source-role supplements and the scene-19 source-only singing cue without changing frozen Tamil evidence.
