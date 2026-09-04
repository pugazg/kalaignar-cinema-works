# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-09-04  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles current repository-wide status mirrors with the authoritative work checkpoints for all six registered works. `data/works.json`, root README, project handover and active work-local metadata/handovers must agree before a major phase is considered closed.

## Result

**PASS — current status mirrors synchronized across all six works at the Manthiri Kumari English-translation completion checkpoint.**

## Current work matrix

| Work | Source/Tamil | Structured text | English | Reader / integration |
|---|---|---|---|---|
| Parasakthi | 54/54 canonical pages verified | 46 observed scenes / 642 dialogue records | 769 verified units | reader/export QA PASS |
| Tirumbippaar! | 104/104 canonical pages verified | 93/93 scenes / 1,040 dialogue records | 1,321 verified units | reader/export + deterministic EPUB QA PASS |
| Manohara | 82/82 canonical pages verified | 57/57 scenes / 983 dialogue records | 1,190 verified units | reader/export QA PASS; Reading Room ready |
| Kalaignar Thirai Isai Paadalgal | 54/54 numbered Tamil songs verified | 54 song records | 54/54 songs / 1,105 line-cues | reader/export + Reading Room payload QA PASS; site not applied |
| Manthiri Kumari | PDF 2–13 canonical Tamil complete-verified; 12/12 pages; 0 unresolved | credits; PDF 3–5 story summary 1/1; PDF 6–13 performance records 15/15 | complete-verified — 13 prose units + 15/15 performances / 52 sections / 234 line-cues | next: deterministic bilingual reader/export |
| Raja Rani | 79/79 source pages; 70/70 screenplay pages verified | 58/58 scenes / 1,071 dialogue records / 80 labels / 44 entities | screenplay 1,236 units + 11/11 songs / 181 song line-cues | bilingual reader QA PASS + Reading Room payload QA PASS; site not applied |

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
- deterministic bilingual reader/export: **ready / not-started**;
- Reading Room integration: **blocked pending reader/export QA**.

The exact next repository-internal activity is to **build and QA a deterministic bilingual reader/export layer from the complete-verified Tamil and English story-summary/performance structures**, preserving the booklet's natural story-summary + performance navigation, page provenance, source-visible cues, cross-witness disposition and unresolved item-level lyric-authorship state. Do not invent screenplay scenes.

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

The Manthiri Kumari **English translation phase is closed and synchronized**: one continuous story-summary translation and all 15 source-linked performance translations are complete-verified, with whole-layer QA PASS and no source-authority or authorship drift. The next repository-internal phase is deterministic bilingual reader/export construction and QA. Raja Rani continues to have no required repository-internal archival, translation, reader/export or Reading Room-payload work remaining; its payload is ready for the separate public-site implementation repository only when explicitly authorized.
