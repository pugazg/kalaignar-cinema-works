# மனோகரா — English translation layer

**Canonical authority:** verified Tamil transcription, complete scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **verified in progress — archival scenes 1–40 / 57, 818/818 units verified**

This directory contains an interpretive English derivative of the verified Tamil source. Nothing here repairs, normalizes, expands or overwrites the canonical Tamil.

The booklet prints **no scene numbers**. Translation identifiers such as `manohara-en-s001-u001` use the archive's existing 57-scene navigation segmentation only; they must never be presented as source scene numbering.

## Files

- `schema.json` — scene-sharded source-linked translation schema adapted to Manohara's unnumbered-source structure.
- `index.json` — translation coverage and integrity checkpoint.
- `PILOT_REVIEW.md` — scene-1 fidelity/voice review and scaling rules.
- `BATCH_002_005_REVIEW.md` — scenes 2–5.
- `BATCH_006_010_REVIEW.md` — scenes 6–10.
- `BATCH_011_015_REVIEW.md` — scenes 11–15.
- `BATCH_016_020_REVIEW.md` — scenes 16–20.
- `BATCH_021_025_REVIEW.md` — scenes 21–25.
- `BATCH_026_030_REVIEW.md` — scenes 26–30.
- `BATCH_031_035_REVIEW.md` — scenes 31–35.
- `BATCH_036_040_REVIEW.md` — scenes 36–40.
- `records/scene-001.json` through `records/scene-040.json` — verified English scene records.

## Translation principles

1. **Tamil remains authoritative.** English fluency is never evidence for changing a verified Tamil reading.
2. **Kalaignar's rhetoric must survive translation.** Repetition, verbal escalation, parallel clauses, insults, metaphor, theatrical pauses, questions and abrupt sentence rhythm are preserved where English can carry them.
3. **Every source-labelled utterance remains linked to its immutable dialogue record.** Exact Tamil `speaker_label` metadata is never normalized or replaced by character names.
4. **Stage directions do not gain action or identity.** Translate only what the verified scene supplies.
5. **Character voice is not homogenized.** Formal courtly speech, colloquial speech, reverential address, comic diction and heightened invective remain distinguishable in English.
6. **Culturally specific images are not automatically domesticated.** Terms such as `Gurudeva`, `Swami`, `Bhadrakali`, `Athaan`, `Rakshasi`, `Chandali`, `Yama`, `sadir`, `Purananuru`, `Kalingathu Parani`, `abhishekam`, `sanjeevi` and source image-words may remain where substitution would flatten the text.
7. **Cross-page source units remain one English unit.** Page provenance and English page segments preserve physical source boundaries.
8. **Song/performance material is limited to what this booklet prints.** No absent lyric is imported from recordings, web pages, record catalogs, subtitles or another booklet.
9. **Source-unlabelled speech remains unlabelled.** Translation does not manufacture a speaker or dialogue-record ID, even where context strongly suggests one.
10. **Decorative `★` separators remain structural.** They are not converted into invented prose such as `(Scene ends.)`.
11. **External authorship metadata is not translation text.** The song evidence layer may identify or qualify an occurrence, but cannot supply missing words.
12. **The play-within-the-play remains structurally distinct.** Translation does not collapse nested-play identities into outer-story identities.
13. **Printed letters remain written text.** Salutation, body and signature are translated as one source-visible written unit rather than converted into spoken dialogue.

## Verified pilot and scenes 1–25

The scene-1 pilot established the voice template: Kalaignar's repetitions, metaphors, address vocabulary and escalating invective remain visible. Scenes 2–25 then carried that template through the nested play, conspiracy, battle, romance, song references, comic registers, source-empty speaker fields and early court conflict.

Checkpoint after scene 25: **417 verified units / 329 immutable dialogue links / 11 source-unlabelled spoken units / 7 cross-page units / 5 translated song occurrences**.

The detailed decisions for those scenes remain in `PILOT_REVIEW.md` and the five batch reviews through `BATCH_021_025_REVIEW.md`.

## Verified batch — scenes 26–30

PDF **38–43 / logical printed pp.37–42** was directly reinspected. This batch adds **77 verified units: 60 dialogue-kind / 16 stage direction / 1 song-reference**, linking all **59/59 immutable dialogue records**.

Satyaseelar's `விண்மீன் / மின்மினி` remains **star / firefly**. Scene 27's unlabelled instruction to Vijaya remains `speaker_label: null`. Scene 28 keeps `சுயபுத்தி சூரணம்` as **Suyabuddhi Chooranam** and preserves the `incurable disease` joke. Scene 29 retains **invisibility medicine** and **sanjeevi** without modernizing the source's medicinal register.

Scene 30 links the source-visible spring-festival performance to `manohara-song-006`; no absent lyrics or external song title are imported. Vasanthan's water/flower word-loop stays intentionally repetitive, while the source's insults and Manoharan's threats are not softened. `BATCH_026_030_REVIEW.md` records the full batch decisions.

## Verified batch — scenes 31–35

PDF **43–48 / logical printed pp.42–47** was directly reinspected. This batch adds **94 verified units: 79 dialogue-kind / 15 stage direction**, linking **79/79 immutable dialogue records**.

Manoharan's self-respect / valour / disgrace escalation in scene 31 remains rhetorical rather than flattened. Scene 33 preserves the Ugrasenan portrait, midnight trap, staged suicide and Vasantha Sena's knife-as-`last kiss` reversal. The interrupted `பல நாள் திருடன் ஒரு நாள்...` proverb remains incomplete because the source itself stops there.

Scene 34 retains `களங்கம்...களங்கம்!` as **stain... stain!** and keeps the statue-smashing action separate. Scene 35 preserves Rajapriyan's repeated **sense! sense!** punchline and Vijaya's repeated pleading. `BATCH_031_035_REVIEW.md` records the batch review.

## Verified batch — scenes 36–40

PDF **48–65 / logical printed pp.47–64** was directly reinspected. This batch adds **230 verified units: 210 dialogue-kind / 19 stage direction / 1 written-text**, linking all **209/209 immutable dialogue records**.

Scene 36 is preserved as the rhetorical centre of the screenplay. Its **88 labelled dialogue records** are not condensed. The long court speeches retain their repetition, image chains, cultural references and violent rhetorical escalation. `Purananuru`, `Kalingathu Parani` and `abhishekam` remain explicit; Padmavathi's womb / corpse / royal-fortune / grave imagery and Vijaya's rose / jasmine / suffering-waves / desert / dark-room / sorrow-lotus chain likewise remain visible.

Three new genuine cross-page dialogue units retain physical page segments: `manohara-en-s036-u035` across PDF **51→52**, `manohara-en-s036-u044` across **52→53**, and `manohara-en-s036-u080` across **56→57**.

Scene 38 preserves the prison, beauty satire and mock-durbar registers separately. The source-empty line `: இப்ப நான் சொல்றபடி சொல்லணும்......` remains null-speaker as `manohara-en-s038-u023`. The mock honorific chain collapses into the saltless-gruel `paraak! paraak!` joke without being rewritten.

Scene 39 retains the Ahalya / Tara / Vasantha comparison, the king's mad-you / mad-me / mad-country escalation, Vasantha Sena's exact inner-thought label and the invisibility-medicine sequence. Scene 40 preserves Ugrasenan's complete printed letter as one `written-text` unit, the `ஓலை / சாவோலை` letter/death-letter turn, and the thorn-with-thorn strategy proverb.

`BATCH_036_040_REVIEW.md` records the full decisions and integrity checks.

## Current coverage

- archival scenes expected: **57**;
- scenes translated/verified: **40/57**;
- verified English units: **818**;
- unit mix: **688 dialogue / 122 stage direction / 6 song-reference / 1 chant / 1 written-text**;
- immutable dialogue links: **676/676** for completed scenes;
- direct source-unlabelled spoken units: **13**, all with null speaker metadata;
- translated song occurrences: **6 — `manohara-song-001` through `manohara-song-006`**;
- cross-page English units: **10**;
- review/draft units: **0**;
- structural stars translated as prose: **0**;
- canonical Tamil modified: **no**;
- scene files modified: **no**;
- immutable dialogue records modified: **no**;
- character/song inventories modified by translation: **no**.

## Next activity

Translate and verify **`manohara-s041`–`manohara-s045`** with the same source-linked model and voice-preservation rules. Reinspect the rendered scan whenever a page crossing, empty speaker field, letter/performance boundary, courtly address, comic phrase or rhetorical image is uncertain.
