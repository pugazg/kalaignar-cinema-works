# ராஜா ராணி — immutable dialogue index

Status: **complete-verified — 58/58 scenes, 1,071 unique immutable labelled-dialogue records, 0 blocked scenes**.

This layer is downstream of verified canonical Tamil and verified scene derivatives. Dialogue records are immutable structured references to source-visible **speaker-labelled utterances only**. Character normalization and English translation never rewrite them.

## Final source gate

- archival scene segments: **58**
- verified scene-text segments: **58/58**
- blocked source-review segments: **0**
- immutable dialogue records: **1,071**
- zero-record scenes: **16**
- genuine cross-page dialogue records: **12**
- tracked source-label/delimiter anomalies: **3**

All former PDF 27, 48, 57 and 74 review restrictions were resolved by direct source review. See `../notes/final-source-review-resolution.md`.

## Core rules

- Only source-visible utterances with a **non-empty printed speaker label** become immutable dialogue records.
- Source-unlabelled speech remains unlabelled and is **not** converted into a dialogue record even when context suggests a speaker.
- `speaker_label` preserves the exact source form represented in verified scene text. Forms such as `ராஜா`, `ராசா`, abbreviations, role labels, voice labels and source-visible anomalies are not normalized here.
- `speaker_delimiter` preserves printed punctuation.
- Character identity normalization belongs only to `../characters/`.
- Dialogue `text` is copied from verified scene text after the printed delimiter.
- A labelled utterance crossing a physical page boundary remains **one** record with multi-page provenance and page segments.
- Narrative/stage text, letters, song cues and other unlabelled structures do not become dialogue records merely because implied ownership is obvious.
- A verified scene may legitimately contain zero dialogue records.
- IDs such as `raja-rani-s001-d001` are archive derivatives only; the booklet prints no scene/dialogue numbers.

## Final zero-record scenes

` s008, s010, s012, s014, s019, s020, s022, s027, s029, s030, s032, s037, s038, s042, s043, s048 `

## Final cross-page dialogue records

1. `raja-rani-s004-d006`
2. `raja-rani-s004-d023`
3. `raja-rani-s005-d010`
4. `raja-rani-s021-d048`
5. `raja-rani-s033-d049`
6. `raja-rani-s035-d012`
7. `raja-rani-s040-d008`
8. `raja-rani-s044-d011`
9. `raja-rani-s046-d001`
10. `raja-rani-s050-d001`
11. `raja-rani-s051-d025`
12. `raja-rani-s052-d011`

Tracked source-label/delimiter anomaly records remain:

- `raja-rani-s004-d001`
- `raja-rani-s004-d007`
- `raja-rani-s007-d023`

## T055 / T056 boundary correction

Final English QA discovered that the earlier scene-55 derivative had crossed its declared `end_before=T056` boundary and duplicated the complete `(முன்)` flashback already owned by scene 56. Its dialogue shard likewise duplicated five scene-56 utterances as `s055-d026`–`s055-d030`.

Final disposition:

- `scene-055.json`: **25** records (`d001`–`d025`);
- `scene-056.json`: **5** records;
- deleted duplicate scene-55 IDs: `s055-d026`–`s055-d030`;
- corrected unique dialogue corpus: **1,071**;
- canonical page transcription: **unchanged**.

Do not restore or reference the deleted duplicate IDs. Durable final QA: `../translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`.

## Source-unlabelled examples deliberately excluded

The no-inference rule remains permanent. Examples include:

- scene 15 unlabelled spoken material around `ராணி வெளியிலே போர்டு பார்த்தேன்.` and the `எஸ் கமின்...` / `சாப்புடு...டேய் கரண்ட்!...` spans;
- scene 28 continuation `இந்தா! அது வச்சு இருந்தேனே. அது எங்கே?`;
- scene 34 `மெள்ள, மெள்ள...` and `ஆ...பூச்சி, பூச்சி...`;
- scene 52 unlabelled Socrates/Crito transition speech and `சாந்தம், பாத்தியா உன் தம்பி செஞ்ச வேலையை?`;
- scene 53 final unlabelled voice-collage after the repeated `விதவை!` cries;
- scene 55 the long source-unlabelled Raja-context lament;
- scene 57 three unlabelled spoken spans around the final matchmaking sequence.

These are represented appropriately in the English layer as source-unlabelled spoken units, not backfilled into immutable dialogue metadata.

## Historical batch reports

The reports `../notes/dialogue-batch-001.md` through `dialogue-batch-006.md` record the staged construction of the dialogue layer. Their references to blocked scenes and then-current record totals are **historical checkpoints**, not current production state. Later direct source review added the formerly blocked scenes and final QA applied the T055/T056 boundary correction.

For current counts use only:

- `index.json`
- this README
- `../notes/final-source-review-resolution.md`
- `../translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`

## Downstream completion

- character layer: **80/80 exact labels → 44 verified entities/roles/collectives**;
- English screenplay layer: **58/58 scenes / 1,236 verified units / 1,071/1,071 dialogue links**.

The current production frontier is the separate English translation of the **11 numbered front-matter song bodies**. Dialogue records must remain unchanged during that phase.
