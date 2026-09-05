# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-09-04  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles current repository-wide status mirrors with the authoritative work checkpoints for all **seven registered works**. `data/works.json`, root README, project handover and active work-local metadata/handovers must agree before a major phase is considered closed.

## Result

**PASS — current status mirrors synchronized across all seven works at the Ammayappan visual-fidelity checkpoint: first pass 105/105 assembled through PDF 109, PDF 5–64 visually verified (60/105), 45 draft pages, 0 review pages, and 68 open first-pass readings; next PDF 65 / logical p.63.**

## Current work matrix

| Work | Source/Tamil | Structured text | English | Reader / integration |
|---|---|---|---|---|
| Parasakthi | 54/54 canonical pages verified | 46 observed scenes / 642 dialogue records | 769 verified units | reader/export QA PASS |
| Tirumbippaar! | 104/104 canonical pages verified | 93/93 scenes / 1,040 dialogue records | 1,321 verified units | reader/export + deterministic EPUB QA PASS |
| Manohara | 82/82 canonical pages verified | 57/57 scenes / 983 dialogue records | 1,190 verified units | reader/export QA PASS; Reading Room ready |
| Kalaignar Thirai Isai Paadalgal | 54/54 numbered Tamil songs verified | 54 song records | 54/54 songs / 1,105 line-cues | reader/export + Reading Room payload QA PASS; site not applied |
| Manthiri Kumari | PDF 2–13 canonical Tamil complete-verified; 12/12 pages; 0 unresolved | credits; PDF 3–5 story summary 1/1; PDF 6–13 performance records 15/15 | complete-verified — 13 prose units + 15/15 performances / 52 sections / 234 line-cues | bilingual reader QA PASS + Reading Room payload QA PASS; site not applied |
| Raja Rani | 79/79 source pages; 70/70 screenplay pages verified | 58/58 scenes / 1,071 dialogue records / 80 labels / 44 entities | screenplay 1,236 units + 11/11 songs / 181 song line-cues | bilingual reader QA PASS + Reading Room payload QA PASS; site not applied |
| Ammayappan | source intake 111/111; structural map verified; Tamil first pass **105/105 draft-complete; PDF 5–64 fidelity-verified (60/105); 45 draft; 68 open markers** | scene/dialogue/character blocked pending complete verified Tamil | blocked | blocked |

## Ammayappan canonical-Tamil first-pass closure checkpoint

- source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`;
- PDF pages: **111**;
- source SHA-256: `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`;
- main screenplay/dialogue: **PDF 5–109 / logical printed pp.3–107 — 105 pages**;
- PDF 110–111: advertisement/back matter, excluded from canonical screenplay;
- structural intake map: **verified — 58 heading/transition occurrences / 37 distinct forms**;
- source-numbered scenes: **none**;
- locked PDF 56 / printed p.54: **`பழுதார் வீதி`**;
- locked PDF 107 / printed p.105: **`தூக்குமேடை`**; rejected `தாக்குமேடை` absent;
- canonical Tamil first pass: **draft-complete — 105/105 pages**;
- continuous assembled transcription: `works/ammaiyappan/transcription/full-text.md` through **PDF 109**;
- assembly QA: `works/ammaiyappan/transcription/ASSEMBLY_QA.md` — **PASS**;
- source anchors: **105 / exact PDF 5→109 order / 0 missing / 0 duplicate**;
- rendered-scan fidelity audit: **in-progress — PDF 5–64 / logical pp.3–62 verified**;
- verified / draft / review pages: **60 / 45 / 0**;
- open first-pass uncertainty markers: **68**;
- scene / dialogue / character derivatives: **blocked pending complete verified Tamil**;
- song/performance authorship gate: **not-started**;
- English translation / reader / Reading Room integration: **blocked**.

The canonical Tamil first-pass transcription and assembly gate remains closed. The separate source-fidelity gate is now active. Exact next activity: **continue at PDF 65 / logical printed p.63 and adjudicate the remaining 68 uncertainty markers in source order**. Structured derivatives remain blocked until all 105 pages pass.

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

The current **Ammayappan canonical-Tamil first-pass closure is synchronized repository-wide**. Ammayappan has **111/111 source pages inspected**, a verified intake map for the **PDF 5–109 / logical pp.3–107** screenplay body, and **105/105 draft first-pass pages** assembled into one continuous `full-text.md`. Assembly QA is **PASS** with **105 exact page anchors, 0 missing and 0 duplicate**; the locked `பழுதார் வீதி` and `தூக்குமேடை` readings are preserved and rejected `தாக்குமேடை` is absent. There are **116 explicit unresolved first-pass readings** and **0/105 verified pages**. The next repository activity is the separate rendered-scan visual fidelity audit from **PDF 5**, and no structured derivative is unblocked until all 105 canonical pages pass that audit.

