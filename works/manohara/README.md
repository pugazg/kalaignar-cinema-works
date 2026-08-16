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
- final batch (`s056`–`s057`) added **10** records — `3 + 7`;
- direct rendered-scan reinspection of PDF **88 / printed p.87** was completed before closing the layer;
- cumulative cross-page dialogue records: **13**; the final batch adds none;
- cumulative source-label/delimiter anomaly records: **8**; the final batch adds none;
- `manohara-s056` leaves four empty-speaker `:` lines outside the dialogue inventory rather than assigning inferred speakers;
- `manohara-s057-d001` keeps the source-unlabelled continuation `பத்மா! என் இதயராணி. என்னை மன்னித்துவிடு.` inside the preceding explicit king's turn;
- `manohara-s024` is the sole zero-record scene;
- `speaker_label` remains exact source-visible text and has not been expanded or normalized;
- no dialogue record has been rewritten to a normalized character identity.

Dialogue policy, schema and final inventory are recorded in `dialogues/README.md`, `dialogues/schema.json` and `dialogues/index.json`.

## Character/entity index — complete-verified

The character layer is now closed across the complete 983-record dialogue inventory.

Final checkpoint:

- exact-label inventory: **111 distinct non-empty source labels** across all **57** scene shards;
- exact labels dispositioned: **111/111**;
- stable entities / role categories: **37**;
- verified entities: **36**;
- unresolved entities: **1**;
- verified source labels: **110**;
- unresolved source labels: **1 — `வர்மா`**;
- remaining unmapped labels: **0**;
- dialogue records modified by character normalization: **0**.

The final pass preserves context-reused shorthand as context-safe role entities instead of forcing false one-to-one identities. `அட்` crosses the real அக்ஷயன் and மனோகரன் in disguise; `வச` and `வசந்` cross வசந்தசேனை and வசந்தன்; `சேனா` crosses nested-play தேவசேனா and outer-story வசந்தசேனை; `வர்` crosses nested-play ஈஸ்வரி வர்மன் and outer-story கேசரிவர்மன்; and generic `தோழி` forms remain attendant/friend roles rather than one named woman.

The nested-play identities are explicitly dispositioned without collapsing them into the outer story: `அஜயன்`, `ஈஸ்வரி வர்மன்`, `உத்தம புருஷன்`, `கமலாவதி`, and `தேவசேனா` now have verified mappings. Scene 42's `வீர` is mapped to **வீரசிம்ஹன்** because உக்ரசேனன் addresses him as `வீரசிம்ஹா!` immediately before the response. `அரூபம்` / `அரூ` are mapped to **கேசரிவர்மன்** from source-internal continuity with the guru-created invisibility medicine established in scene 1 and described again by the invisible speaker in scene 39.

One label remains intentionally unresolved: `வர்மா` in `manohara-s008-d003`. The printed nested-play sequence does not justify assigning it confidently to ஈஸ்வரி வர்மன், உத்தம புருஷன், or another physical speaker without inference, so the source form remains explicit rather than being silently repaired.

Character policy and final files are under `characters/`: `README.md`, `schema.json`, `labels-inventory.json`, `entities-pilot.json`, `entities.json`, and `index.json`.

## Song / performance authorship gate — complete with unresolved authorship

The song/performance gate is closed for the evidence presently available. PDF **1–6** was visually inspected first: the booklet prints `திரைக்கதை வசனம் / மு. கருணாநிதி`, but **no lyricist heading, song-contributor list or item-level song credit**. The screenplay-dialogue credit is therefore not reused as lyric authorship.

Six source-visible occurrences were verified at PDF **9, 16, 30, 32, 37 and 41** and recorded in `songs/inventory.json`:

- `சந்தேகமில்லே` — named reference, authorship **unresolved**;
- nested-play `நிலாவிலே ! சல்லாபமே!!` — authorship **unresolved**;
- `வாழ்வதே மாது நான்` — authorship **unresolved**;
- `சிங்காரப் பைங்கிளியே... பேசு` — **review**, because external attributions conflict between உடுமலை நாராயண கவி and மு. கருணாநிதி;
- `பொழுது புலர்ந்தது` — **சுரபி, verified** from item-level official Saregama evidence;
- the PDF 41 `வசந்த விழாக் கொண்டாட்டம். பாட்டுகள்...` / Manoharan–Vijaya singing sequence — authorship **unresolved** and linked only by context, not guessed onto a soundtrack title.

Final gate totals: **6 occurrences / 1 verified / 1 review / 4 unresolved**. External evidence did **not** modify canonical Tamil, scene text or the 983 immutable dialogue records.

The booklet prints **no complete standalone lyric body** for any of the six occurrences. Accordingly there are **0 reconstructed Tamil song files**: missing lyrics are not imported from recordings, streaming services, record catalogs, websites, later editions or another booklet. `songs/README.md` documents the evidence policy and all dispositions.

## English translation — verified in progress

The English derivative under `translations/` now covers archival scenes **1–10 of 57**. These are archive navigation segments only; the booklet still prints no scene numbers.

The translation has **204/204 verified source-linked units** with **0 review / 0 draft**:

- **172 dialogue-kind units**;
- **30 stage-direction units**;
- **2 song-reference units**;
- **164/164 immutable labelled dialogue records** in completed scenes linked exactly once;
- **8 direct source-unlabelled spoken units**, all retaining `speaker_label: null`;
- **3 genuine cross-page English units**;
- translated source-visible song occurrences: `manohara-song-001` and `manohara-song-002`.

The verified scene-1 pilot remains the voice template: Kalaignar's repetition, rhetorical accumulation, metaphor, theatrical pauses, address vocabulary, comic/formal register differences and heightened invective are preserved rather than smoothed into generic fluent English.

The second scaling batch, scenes **6–10**, was checked directly against PDF **10–23 / logical printed pp.9–22**. It adds **166 verified units** and links all **133/133** labelled dialogue records in those scenes. Scene 8 retains the play-within-the-play as a distinct dramatic layer and keeps source-empty speaker fields unlabelled even where stage context suggests a likely speaker. Its two new cross-page units preserve the PDF **13→14** reported message and PDF **18→19** final accusation as single English units.

The scene-8 love-song reference `நிலாவிலே ! சல்லாபமே!!` is linked to `manohara-song-002`; only the source-visible title/refrain is translated and no missing lyrics are supplied. The exact `வர்மா` label remains unresolved and unchanged by translation.

`translations/PILOT_REVIEW.md`, `translations/BATCH_002_005_REVIEW.md`, and `translations/BATCH_006_010_REVIEW.md` record the verified translation decisions and integrity checks. No canonical Tamil, scene, dialogue, character or song-inventory record has been changed by the English layer.

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
| English translation | **verified in progress — 10/57 scenes, 204 verified units** |
| Reader / Reading Room integration | blocked / not-started |

## Next activity

**Translate and verify `manohara-s011`–`manohara-s015` using the same source-linked model and voice-preservation rules. Reinspect the rendered scan whenever a proclamation/chant boundary, unlabelled speech, courtly register, comic phrase, page crossing or rhetorical image is uncertain.**
