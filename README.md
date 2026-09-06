# Kalaignar Cinema Works

A source-led archive of screenplay, dialogue, song, and related cinema writing credited to **Kalaignar M. Karunanidhi**.

The repository preserves source provenance, canonical transcription and derivative representations separately.

## Archival principles

1. **Primary source first.** The scanned publication controls canonical transcription.
2. **No silent correction.** Source anomalies stay documented.
3. **Page provenance is mandatory.** Transcribed, indexed and translated units remain traceable to PDF/printed pages.
4. **Uncertainty stays visible.** Interpretive pressure points are reviewed rather than guessed away.
5. **Source and derivatives are separate.** English translation never overwrites Tamil.
6. **Authorship is not inferred.** Mixed-credit material requires item-level evidence.
7. **Rights are not assumed.** No repository-wide public-domain/open-license claim is made.
8. **Current status mirrors must agree.** A major phase is not durably closed until work-local status and repository-wide current mirrors are synchronized.
9. **Historical Tamil glyph identity must be decoded, not visually imitated.** For older-print sources, use `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` where historical typeforms occur.

## Reusable onboarding for new cinema works

Read `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`, `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` when older Tamil typeforms may occur, `docs/ARCHIVAL_WORKFLOW.md`, `docs/SOURCE_POLICY.md`, `docs/TRANSCRIPTION_GUIDE.md`, `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`, and `docs/START_NEW_CINEMA_WORK_PROMPT.md` before starting a new work.

The preferred public reading destination is the **Kalaignar Digital Library / Reading Room at `https://nenjukkuneethi.org/read`**. Preserve each source's natural structure; do not force non-screenplay booklets into screenplay scenes.

## ராஜா ராணி status

`TVA_BOK_0017188_ராஜா_ராணி.pdf` is a **complete-verified bilingual archival work with deterministic reader/export and Reading Room payload QA PASS**.

- source scan: **80 PDF pages**; SHA-256 `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`;
- verified source / screenplay pages: **79/79 / 70/70**;
- scene derivatives: **58/58**;
- immutable dialogue records: **1,071**;
- labels / entities: **80/80 / 44**;
- English screenplay: **1,236 units**;
- numbered songs: **11/11 / 181 Tamil-English line-cues**;
- reader/export: **QA PASS**;
- Reading Room payload: **QA PASS**, `974,510` bytes, SHA-256 `ab1058cb5a22ba78e68938f50efc586cc53eb07ef544bdf3919bb3c4b8c46c9b`;
- site application: **not-applied**.

**Next:** no required Raja Rani repository-internal work remains; apply its payload in the separate Reading Room implementation repository only when explicitly authorized.

## மந்திரி குமாரி status

`TVA_BOK_0026144_மந்திரி_குமாரி.pdf` is a **14-page film story-and-song booklet** whose source-appropriate Tamil, English, bilingual reader and Reading Room integration payload are now complete-verified.

- source classification: **film story-and-song booklet**, not a full screenplay/dialogue book;
- direct printed Kalaignar credit: **`கதை, வசனம் : மு. கருணாநிதி`**;
- source SHA-256: `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`;
- canonical Tamil: **PDF 2–13, 12/12 pages complete-verified, 0 unresolved readings**;
- post-fidelity source corrections: **recorded, applied and reconciled**;
- story-summary Tamil derivative: **1/1 continuous record, PDF 3–5**;
- song/performance Tamil records: **15/15 complete-verified, PDF 6–13**;
- current-anthology relationship: **1 confirmed witness / 14 source-only blocks**;
- booklet item-level lyric authorship: **0 verified / 15 unresolved**;
- English story-summary translation: **1/1 / 13 logical units / 1 cross-page unit**;
- English performance translation: **15/15 / 52 sections / 234 Tamil-English line-cues / 0 mismatches**;
- bilingual reader/export: **complete-verified, QA PASS**;
- reader navigation: **16 natural source structures — 1 story summary + 15 performances**;
- reader performance mapping: **52 sections / 234 Tamil line-cues / 234 English line-cues / 0 mismatches**;
- synthetic screenplay scene IDs created: **0**;
- canonical Tamil changes caused by translation/reader/payload: **0**;
- authorship upgrades caused by downstream layers: **0**;
- Reading Room payload: **payload-complete-verified — QA PASS**;
- payload mode: **`source-linked-composition`**;
- payload source-link targets: **32**;
- payload: `works/manthiri-kumari/integrations/reading-room/reading-room.json`;
- payload bytes: **15,704**;
- payload SHA-256: `20a0db293b936757e7d01def336252f28543337f319dfae6ad7bf5ae886bab43`;
- Reading Room site application: **not-applied**.

The source-linked payload preserves the booklet's natural `கதைச்சுருக்கம்` + 15-performance navigation, PDF-page provenance, source-visible cues, the block-11 anthology witness, and the unresolved item-level lyricist state. Performance 13 retains the printed heading `பார்த்திபன்—மந்திரிகுமாரி` while its internal source labels remain `பார்த்திபன்` / `அமுதவல்லி`.

**Next:** no required repository-internal Manthiri Kumari work remains. Apply the verified payload in the separate Reading Room implementation repository only when that repository is explicitly authorized for modification.

## அம்மையப்பன் status

`TVA_BOK_0064230_அம்மையப்பன்.pdf` has **closed canonical Tamil, closed structured derivatives, and active verified English translation**.

- canonical Tamil: **105/105 dual-gate complete-verified**;
- visual fidelity / historical-glyph audit: **105/105 / 105/105 PASS**;
- unresolved canonical markers: **0**;
- late PDF 10 heading correction: **`மாடம்`**, commit `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`;
- canonical source-visible scene boundaries: **63**;
- archive-only scene derivatives: **63/63 complete-verified**;
- boundary ownership: **PASS — 0 gaps / 0 overlaps / 105 pages represented**;
- explicit colon-labelled dialogue records: **1,009**;
- source-role supplements: **16**;
- downstream dialogue units: **1,025**;
- character/entity index: **26 entities / 62 exact labels / 1,025/1,025 dialogue-unit coverage**;
- post-closure source delimiter repairs: scene 3 `பூங் ; ...` and scene 5 `திரு; ...` remain exact non-colon source forms;
- song/performance authorship gate: **64/64 candidates reviewed / 5 retained source-visible occurrences / 0 standalone lyric files**;
- English translation: **pilot verified — scene 1/63 / 34 verified units**;
- reader/export: blocked pending complete English.

**Next:** translate and source-review archival scenes **2–5** using the verified scene-1 pilot voice rules and exact source/dialogue provenance.

## கலைஞர் திரை இசைப் பாடல்கள் status

The dedicated anthology work `works/kalaignar-thirai-isai-paadalgal/` is complete-verified for its numbered corpus.

- source: `TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`;
- source SHA-256: `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- numbered songs: **54/54 Tamil complete-verified**;
- English translation: **54/54 complete-verified**;
- reader/export: **QA PASS**;
- Reading Room payload: **QA PASS — 23 film groups / 54 songs / 1,105 paired line-cues**;
- site application: **not-applied**.

The anthology attribution tier remains separate from original-film primary-source verification.

**Next:** apply the verified payload in the separate Reading Room implementation repository only when explicitly authorized.

## மனோகரா status

`TVA_BOK_0010102_மனோகரா.pdf` has complete-verified Tamil, structured derivatives, English translation and reader/export.

- canonical Tamil: **82/82 pages**;
- archival scenes: **57/57**;
- dialogue records: **983**;
- character labels/entities: **111 / 37**;
- English: **1,190/1,190 units**;
- reader/export: **QA PASS**;
- Reading Room integration: ready.

**Next:** integrate the verified Manohara reader into the Reading Room while preserving its archival scene IDs as navigation rather than printed source numbering.

## Parasakthi status

Parasakthi has complete-verified canonical Tamil and source-linked English reader work.

- canonical Tamil: **54/54 pages**;
- scene layer: **46/46**;
- dialogue index: **642 records**;
- song/verse authorship: **14/14 verified**;
- English: **769/769 units**;
- reader/export: **QA PASS**.

**Next:** no required translation/reader activity remains; future public access should prioritize Reading Room integration.

## திரும்பிப்பார்! status

`TVA_BOK_0014652_திரும்பிப்பார்.pdf` is complete-verified through deterministic reader/export and EPUB packaging.

- canonical Tamil: **104/104 pages**;
- scenes: **93/93**;
- dialogue records: **1,040**;
- English: **1,321 verified units**;
- reader/export: **QA PASS**;
- EPUB 3: **QA PASS**, SHA-256 `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`.

**Next:** no required Tirumbippaar repository-internal translation/reader/package work remains.

## Status vocabulary

`not-started` · `draft` · `draft-complete` · `review` · `verified` · `pilot-verified` · `complete-verified` · `unresolved`

Translation status is independent of source-transcription verification status.
