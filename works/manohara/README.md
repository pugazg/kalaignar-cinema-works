# மனோகரா

Source-led archival work for the supplied screenplay/dialogue booklet `TVA_BOK_0010102_மனோகரா.pdf`.

The rendered scan is the controlling source for this edition. The PDF's OCR layer is useful only for navigation and must not be treated as canonical text.

## Verified source checkpoint

- source title: `மனோகரா`;
- printed credit: `திரைக்கதை வசனம்` / `மு. கருணாநிதி`;
- title-page publisher: `மூனா கானா பதிப்பகம்`;
- title-page address: `1/1 ஜக்கரியா காலணி 2-வது தெரு, சென்னை-24`;
- edition statement: `முதற்பதிப்பு : பிப்ரவரி 1954.`;
- rights statement: `உரிமை : ஆசிரியருக்கே.`;
- price: `விலை எட்டணா`;
- printer line: `Bharat Devi Press, 2/16, Mount Road, Madras-2.`;
- archive/source identifier from the supplied filename: `TVA_BOK_0010102`;
- PDF pages: **90**;
- file size: **30,684,695 bytes**;
- SHA-256: `87518fd8c290d7880aa2ddd9f2b5999c9d421d48fe1f02d61cf8e254393236a9`.

## Source boundaries

- PDF 1: illustrated front cover;
- PDF 2: title / screenplay-dialogue credit / publisher page;
- PDF 3: rights / first-edition date / price / printer page;
- PDF 4–5: `நாடகக் கதை` summary;
- PDF 6: `முன்னுரை`;
- PDF 7–88: screenplay/dialogue text;
- PDF 89: boxed back-matter advertisement/catalogue headed `ஒப்பிட்டுப் பாருங்கள்!`;
- PDF 90: back-cover advertisement for `முரசொலி`, with a later library/news-agent stamp over the printed advertisement.

The interior pagination supports `printed page = PDF page - 1` for the continuous book sequence. Section-opening folios are suppressed on PDF 4, 6 and 7, so the main screenplay occupies logical printed pp. **6–87**.

## Structural finding

This edition does **not** print numbered scene headings. Scene boundaries therefore must not be retroactively presented as source scene numbers. The source uses decorative star separators, parenthetical/bracketed stage transitions, bare location labels and continuous dialogue/action instead. `mapping.md` and `notes/scene-heading-audit.md` document that source structure.

The scan also contains an extended play-within-the-play sequence, explicit song/performance references, a war-proclamation/chant-like passage, and a separately printed letter. Song authorship is handled only in the separate `songs/` evidence layer and is never inferred from the screenplay/dialogue credit.

## Canonical Tamil — complete-verified

The complete source-order Tamil layer is stored in six verified archival batches:

- `transcription/parts/part-01-pdf-7-30.md` — PDF **7–30** / logical printed pp. **6–29** — **24 verified pages**;
- `transcription/parts/part-02-pdf-31-42.md` — PDF **31–42** / logical printed pp. **30–41** — **12 verified pages**;
- `transcription/parts/part-03-pdf-43-54.md` — PDF **43–54** / logical printed pp. **42–53** — **12 verified pages**;
- `transcription/parts/part-04-pdf-55-66.md` — PDF **55–66** / logical printed pp. **54–65** — **12 verified pages**;
- `transcription/parts/part-05-pdf-67-78.md` — PDF **67–78** / logical printed pp. **66–77** — **12 verified pages**;
- `transcription/parts/part-06-pdf-79-88.md` — PDF **79–88** / logical printed pp. **78–87** — **10 verified pages**.

Final canonical status: **82 verified / 0 draft / 0 review**.

## Visual fidelity audit — complete

Every canonical page PDF **7–88 / logical printed pp.6–87** has been compared against the rendered scan and passed its correction/recheck gate. There are **0 unresolved source readings**.

Part-level correction totals after final rechecks:

- Part 01 — **89** corrections;
- Part 02 — **43**;
- Part 03 — **48**;
- Part 04 — **63**;
- Part 05 — **69**;
- Part 06 — **68 final corrections**.

Part 06's initial full-range audit recorded **63** corrections. After those were applied, the mandatory second complete visual comparison found **5 additional scan-supported corrections**. Those were applied before verification. The final Part 06 record is `notes/fidelity-audit-part06-final.md`.

During dialogue preparation for `manohara-s042`, direct reinspection of PDF 68 exposed one stored application omission for an item already recorded in the Part 05 Batch 11 audit: the source label is `வ. சே. : வசந்தா!`, not `வ. சே : வசந்தா!`. The canonical Part 05 text and `scene-042.md` were corrected before dialogue extraction. The correction is documented in `notes/post-fidelity-corrections.md`; the canonical page remains verified and no other wording or structure changed.

Important final-page disposition: `பத்மா! என் இதயராணி. என்னை மன்னித்துவிடு.` continues the king's speech without a printed speaker label; it is not converted into an invented/new speaker label in the canonical text.

## Scene derivative layer — complete-verified

The verified transition audit contains **57 principal source-visible transition dispositions** (`T001`–`T057`). These are used as the start points for **57 archival scene segments** in `scenes/index.json`.

This is a derivative navigation system only. The booklet still has **no source scene numbers**. IDs such as `manohara-s001` and filenames such as `scene-001.md` must never be presented as numbers printed by the source.

Final scene checkpoint:

- archival scene segments indexed: **57/57**;
- scene index: **complete**;
- scene-text derivatives: **57/57 complete-verified**;
- completed: `manohara-s001`–`manohara-s057`;
- five genuine source continuities across canonical storage-part boundaries were preserved rather than converted into false scene breaks: `s016`, `s030`, `s036`, `s041`, and `s051`;
- no source scene numbers, synthetic endings, or duplicate boundary separators were introduced.

The segmentation policy and safeguards are documented in `scenes/README.md`.

## Dialogue index — complete-verified

The dialogue layer under `dialogues/` is now complete across all **57 archival scenes**.

Final checkpoint:

- dialogue scene shards completed: **57/57** — `manohara-s001` through `manohara-s057`;
- immutable explicitly speaker-labelled dialogue records: **983**;
- cumulative cross-page dialogue records: **13**;
- cumulative source-label/delimiter anomaly records: **8**;
- `manohara-s024` is the sole zero-record scene;
- `speaker_label` remains exact source-visible text and has not been expanded or normalized;
- no dialogue record has been rewritten to a normalized character identity.

Dialogue policy, schema and final inventory are recorded in `dialogues/README.md`, `dialogues/schema.json` and `dialogues/index.json`.

## Character/entity index — complete-verified

The character layer is closed across the complete 983-record dialogue inventory:

- exact-label inventory: **111 distinct non-empty source labels**;
- exact labels dispositioned: **111/111**;
- stable entities / role categories: **37**;
- verified entities / labels: **36 / 110**;
- unresolved entities / labels: **1 / 1 — `வர்மா`**;
- remaining unmapped labels: **0**;
- dialogue records modified by character normalization: **0**.

Context-reused shorthand remains context-safe instead of being forced into false identities. The nested-play identities stay distinct from the outer story, and `வர்மா` in `manohara-s008-d003` remains unresolved because the printed sequence does not support a safe physical-speaker assignment without inference.

Character policy and final files are under `characters/`.

## Song / performance authorship gate — complete with unresolved authorship

PDF **1–6** was visually inspected first: the booklet prints `திரைக்கதை வசனம் / மு. கருணாநிதி`, but **no lyricist heading, song-contributor list or item-level song credit**. The screenplay-dialogue credit is therefore not reused as lyric authorship.

Six source-visible occurrences were verified at PDF **9, 16, 30, 32, 37 and 41**. Final gate totals are **6 occurrences / 1 verified / 1 review / 4 unresolved**. `பொழுது புலர்ந்தது` is the sole item with verified lyricist evidence (**சுரபி**); `சிங்காரப் பைங்கிளியே... பேசு` remains in review because external attributions conflict. No external evidence modified canonical Tamil, scene text or dialogue records.

The booklet prints no complete standalone lyric body for any occurrence, so there are **0 reconstructed Tamil song files**. `songs/README.md` documents the evidence policy and all dispositions.

## English translation — verified in progress

The English derivative now covers archival scenes **1–45 of 57**. These are archive navigation segments only; the booklet still prints no scene numbers.

Current checkpoint: **923/923 verified source-linked units / 0 review / 0 draft**:

- **781 dialogue-kind units**;
- **134 stage-direction units**;
- **6 song-reference units**;
- **1 chant unit**;
- **1 written-text unit**;
- **767/767 immutable labelled dialogue records** in completed scenes linked exactly once;
- **15 direct source-unlabelled spoken units**, all retaining `speaker_label: null`;
- **10 genuine cross-page English units**;
- all **6** source-visible song/performance occurrences translated at the reference level.

The verified scene-1 pilot remains the voice template: Kalaignar's repetition, rhetorical accumulation, metaphor, theatrical pauses, address vocabulary, comic/formal register differences and heightened invective are preserved rather than smoothed into generic fluent English.

The latest requested batch **41–45** was checked directly against PDF **65–71 / logical printed pp.64–70** and adds **105 verified units**, linking all **91/91 immutable labelled dialogue records** in those five scenes. `BATCH_041_045_REVIEW.md` records the source and voice decisions.

Scene 41 retains the false-physician comic chain from `taking my life` through Yama-Dharma and Yama's buffalo, and keeps `உமது பெயர்?` as a null-speaker unit rather than assigning it from context. Scene 42 retains the counterfeit ascetic register, Bhagavan, the `world is a drama` turn, Mahalakshmi, Nalayini and Vasanthan's half-remembered devotional recitation. The printed `மறவு பெண்ணாசை மறக்கவேண்டும்` is translated as it stands rather than silently corrected from outside literary knowledge.

Scene 43 keeps the saffron-robes / knife-bearing-army / opened-sluice imagery and the strength-of-mind versus military-strength contrast. Scene 44 preserves the `ஆண்டவன் / ஆண்டு கொண்டிருப்பவன்` Lord/ruler turn, the cloud / jasmine / rose accumulation and the military/sexual invasion-surrender double meaning. Scene 45 keeps the source-undelimited `ஆள்......அப்படியா......` as another null-speaker unit and preserves Padmavathi's diamond-cradle / straw-enclosure and flower-feet / earth-to-gold / golden-mansion-to-dust reversals.

No canonical Tamil, scene, dialogue, character or song-inventory record has been changed by the English layer.

## Status

| Layer | Status |
|---|---|
| Source intake | complete |
| Structural mapping | verified |
| Numbered-scene disposition | not-applicable — none printed |
| Canonical Tamil | **complete-verified — 82/82 pages** |
| Visual fidelity audit | **complete — 82/82 pages** |
| Archival scene index | **complete — 57 derivative segments** |
| Scene-text derivatives | **complete-verified — 57/57** |
| Dialogue index | **complete-verified — 57/57 scenes, 983 records** |
| Character index | **complete-verified — 111/111 labels dispositioned, 37 entities, 1 unresolved label** |
| Song/performance authorship | **complete-with-unresolved-authorship — 6 occurrences; 1 verified / 1 review / 4 unresolved** |
| Tamil song lyric derivatives | **0 — no complete lyric body printed** |
| English translation | **verified in progress — 45/57 scenes, 923 verified units** |
| Reader / Reading Room integration | blocked / not-started |

## Next activity

**Translate and verify `manohara-s046`–`manohara-s050` using the same source-linked model and voice-preservation rules. Reinspect the rendered scan whenever a page crossing, empty speaker field, courtly address, colloquial/comic phrase or rhetorical image is uncertain.**
