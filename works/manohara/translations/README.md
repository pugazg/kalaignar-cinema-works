# மனோகரா — English translation layer

**Canonical authority:** verified Tamil transcription, complete scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **verified in progress — archival scenes 1–25 / 57, 417/417 units verified**

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
- `records/scene-001.json` through `records/scene-025.json` — verified English scene records.

## Translation principles

1. **Tamil remains authoritative.** English fluency is never evidence for changing a verified Tamil reading.
2. **Kalaignar's rhetoric must survive translation.** Repetition, verbal escalation, parallel clauses, insults, metaphor, theatrical pauses, questions and abrupt sentence rhythm are preserved where English can carry them.
3. **Every source-labelled utterance remains linked to its immutable dialogue record.** Exact Tamil `speaker_label` metadata is never normalized or replaced by character names.
4. **Stage directions do not gain action or identity.** Translate only what the verified scene supplies.
5. **Character voice is not homogenized.** Formal courtly speech, colloquial speech, reverential address, comic diction and heightened invective remain distinguishable in English.
6. **Culturally specific images are not automatically domesticated.** Terms such as `Gurudeva`, `Swami`, `Bhadrakali`, `Athaan`, `Rakshasi`, `Chandali`, `Yama`, `sadir` and source image-words may remain or be lightly carried into English where substitution would flatten the text.
7. **Cross-page source units remain one English unit.** Page provenance and English page segments preserve physical source boundaries.
8. **Song/performance material is limited to what this booklet prints.** No absent lyric is imported from recordings, web pages, record catalogs, subtitles or another booklet.
9. **Source-unlabelled speech remains unlabelled.** Translation does not manufacture a speaker or dialogue-record ID, even where context strongly suggests one.
10. **Decorative `★` separators remain structural.** They are not converted into invented prose such as `(Scene ends.)`.
11. **External authorship metadata is not translation text.** The song evidence layer may identify or qualify an occurrence, but cannot supply missing words.
12. **The play-within-the-play remains structurally distinct.** Translation does not collapse nested-play identities into outer-story identities.

## Verified pilot and early scaling — scenes 1–10

The verified scene-1 pilot established the voice template: Kalaignar's repetitions, metaphors, address vocabulary and escalating invective remain visible. Scenes 2–5 then carried that template through Vasantha Sena's ambition, `சந்தேகமில்லே` wordplay, Padmavathi's pleading and the nested-play setup.

Scenes 6–10 expanded the model across the extended play-within-the-play, source-empty speaker fields and heightened martial rhetoric. Scene 8 keeps all empty-speaker passages unlabelled even when dramatic context suggests a likely speaker, preserves the unresolved exact label `வர்மா`, and links only the source-visible `நிலாவிலே ! சல்லாபமே!!` reference to `manohara-song-002` without reconstructing lyrics.

Checkpoint after scene 10: **204 verified units / 164 immutable dialogue links / 3 cross-page units / 2 translated song occurrences**.

## Verified batch — scenes 11–15

PDF **23–30 / logical printed pp.22–29** was directly reinspected. This batch adds **104 verified units: 81 dialogue / 1 chant / 22 stage direction**, linking all **82/82 immutable dialogue records**.

Key decisions include:

- the `முரசறைவோன்` war proclamation is a `chant` unit while retaining its dialogue-record link;
- Vasanthan's `வைக்கோற் போர்` / `அக்கப் போர்` parody and recurring `சந்தேகமில்லே` remain visible;
- the broken sword-hilt action is one cross-page unit across PDF **23→24**;
- `புகழுடம்பு` remains the classical `body of fame` image;
- Muthu Vijayan's `வாய் வீச்சு / வாள் வீச்சு` exchange remains a tongue-swing / sword-swing wordplay pair;
- the battle result remains one continuous stage unit across PDF **27→28**;
- `அஸ்தமித்து விட்டார்` remains `He has set`, preserving the sunset metaphor for death;
- Vijaya's first long confrontation with Manoharan preserves spear-eyes, fruit, tender-creeper, skylark/vulture and freedom-breeze/slavery-cyclone imagery;
- `manohara-s015-d002` remains one dialogue unit across PDF **28→29**.

`BATCH_011_015_REVIEW.md` records the full fidelity decisions.

## Verified batch — scenes 16–20

PDF **30–33 / logical printed pp.29–32** was checked directly. This batch adds **44 verified units: 34 dialogue-kind / 8 stage direction / 2 song-reference**, linking **33/33 immutable dialogue records**.

`வாழ்வதே மாது நான்` is linked to `manohara-song-003`; `சிங்காரப் பைங்கிளியே... பேசு` is linked to `manohara-song-004`. Only source-visible titles are translated. The latter's disputed external authorship remains `review` in the song layer.

Scene 17 preserves Rajapriyan's long mock-sentencing cadence through its marriage-reveal ending. Scene 18 keeps the golden-creeper, golden-rose, diamond-dewdrop, `sadir-dance`, honey-wave and eye-written-love-epic imagery at the source's deliberately heightened register.

Scene 20 contains a source-unlabelled conspiracy continuation after the gold sack is handed over. It remains `speaker_label: null` rather than being assigned to Vasantha Sena by inference.

## Verified batch — scenes 21–25

PDF **33–37 / logical printed pp.32–36** was checked directly. This batch adds **65 verified units: 52 dialogue-kind / 12 stage direction / 1 song-reference**, linking **50/50 immutable dialogue records**.

Important source safeguards:

- scene 21's `வந்துவிட்டேனம்மா` and quoted `மனோகரா!` are source-unlabelled and remain null-speaker units;
- `manohara-s021-d017` remains one cross-page English unit across PDF **34→35**;
- `கரும்பு / துரும்பு`, `வாள் / வால்`, `தேளின் கொடுக்கே`, and the vulture/wolf/python accumulation remain visible rather than being flattened;
- the source's literal `???` in Manoharan's scene-21 line remains visible;
- scene 23 keeps the roof-tearing-god proverb rather than replacing it with an English proverb;
- scene 24 correctly remains a **zero-labelled-dialogue scene**, represented only by its source-visible location/action and `பொழுது புலர்ந்தது` song reference;
- `பொழுது புலர்ந்தது` is linked to `manohara-song-005`; only the title is translated. The separate song evidence layer's verified Surabi authorship does not alter source text;
- scene 25 preserves Vasantha Sena's insinuating court manoeuvre and the king's Paramasiva/Ganga image.

`BATCH_021_025_REVIEW.md` records the batch-level review.

## Current coverage

- archival scenes expected: **57**;
- scenes translated/verified: **25/57**;
- verified English units: **417**;
- unit mix: **339 dialogue / 72 stage direction / 5 song-reference / 1 chant / 0 written-text**;
- immutable dialogue links: **329/329** for completed scenes;
- direct source-unlabelled spoken units: **11**, all with null speaker metadata;
- translated song occurrences: **5 — `manohara-song-001` through `manohara-song-005`**;
- cross-page English units: **7**;
- review/draft units: **0**;
- structural stars translated as prose: **0**;
- canonical Tamil modified: **no**;
- scene files modified: **no**;
- immutable dialogue records modified: **no**;
- character/song inventories modified by translation: **no**.

## Next activity

Translate and verify **`manohara-s026`–`manohara-s030`** with the same source-linked model and voice-preservation rules. Reinspect the rendered scan whenever a page crossing, empty speaker field, performance/song boundary, courtly address, comic phrase or rhetorical image is uncertain.
