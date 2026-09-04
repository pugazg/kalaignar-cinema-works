# மந்திரி குமாரி — English translation layer

Source: `TVA_BOK_0026144_மந்திரி_குமாரி.pdf`  
Target language: English  
Status: **complete-verified — QA PASS**

This layer translates only the **verified source-linked Tamil derivatives** of the Manthiri Kumari story-and-song booklet. It does not convert the booklet into a screenplay, infer absent lyric authorship, import external lyrics, or repair canonical Tamil through English interpretation.

## Translation checkpoint

### Story summary

- source: verified continuous PDF **3–5** `கதைச்சுருக்கம்`;
- record: `story-summary.json`;
- logical prose units: **13**;
- cross-page units: **1**;
- synthetic screenplay scene IDs: **0**.

### Songs / performances

- records: `performances/001.json`–`015.json`;
- performance records: **15/15**;
- sections: **52**;
- Tamil source lines/cues: **234**;
- English lines/cues: **234**;
- mapping mismatches: **0**;
- cross-page records: **002, 004, 006, 007, 009, 011, 013**.

Source-visible `தொகையறா` / `பாட்டு`, `(வசனம்)` and refrain/performance cues remain represented. Performance 13 retains its printed heading `பார்த்திபன்—மந்திரிகுமாரி` while the internal turn labels remain `பார்த்திபன்` / `அமுதவல்லி`.

## Evidence boundary

- item-level lyric authorship verified: **0/15**;
- item-level lyric authorship unresolved: **15/15**;
- confirmed current-anthology witness: **1/15**, block 11 ↔ `kalaignar-song-001`;
- source-only against the current anthology: **14/15**;
- authorship upgrades caused by translation: **0**;
- canonical Tamil changed by translation: **no**.

## Downstream completion

The deterministic bilingual reader under `../editions/bilingual/` is **complete-verified — QA PASS**.

The source-linked Reading Room composition under `../integrations/reading-room/` is also **payload-complete-verified — QA PASS**:

- payload mode: `source-linked-composition`;
- source-link targets: **32**;
- payload bytes: **15,704**;
- payload SHA-256: `20a0db293b936757e7d01def336252f28543337f319dfae6ad7bf5ae886bab43`;
- site application: **not-applied**.

## Next activity / disposition

No required repository-internal translation, reader/export, or Reading Room-payload work remains. Apply the verified payload in the separate Reading Room implementation repository only when that repository is explicitly authorized.
