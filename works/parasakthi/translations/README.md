# Parasakthi — English translation layer

**Canonical authority:** verified Tamil transcription and its immutable structured derivatives  
**Target language:** English (`en`)  
**Status:** in progress — scene 1 verified; scenes 2–5 in review

This directory contains interpretive English derivatives. Nothing in this layer is allowed to repair, normalize, or overwrite the verified Tamil source.

## Translation principles

1. **Tamil remains authoritative.** A smoother English rendering is never evidence that the Tamil should be changed.
2. **Every unit is source-linked.** Each translation record carries canonical scene, source path, source record/occurrence ID where one exists, and PDF/printed-page provenance.
3. **Exact source identifiers stay exact.** Dialogue `speaker_label` values remain exactly as represented in the dialogue index. Character normalization, when useful, is a separate reference to the character index.
4. **Stage directions do not gain action.** Translate only the action/context present in the verified source.
5. **Dialogue preserves rhetorical force.** Repetition, questions, exclamations, metaphors, code-switching and social/political language should not be flattened merely for fluency.
6. **Songs are semantic translations, not singable rewrites.** Preserve source line order and stanza structure where practical; do not introduce rhyme, meter or imagery not present in the Tamil.
7. **Quoted verse stays distinct from soundtrack song.** Authorship and source-kind distinctions from the completed song layer remain intact.
8. **Cross-page source units remain one unit.** `english_page_segments` may be used to show how an English rendering aligns to a source utterance that crosses a page anchor.
9. **Translation status is independent.** `draft`, `review`, and `verified` refer only to the English derivative, never to Tamil source status.
10. **No external text substitution.** Web translations, subtitles, film dialogue, published English versions or audio memory must not replace source-linked translation work.

## Storage

- `schema.json` — translation unit schema.
- `index.json` — translation checkpoint / scene coverage manifest.
- `records/scene-XX.json` — source-linked translation units grouped by canonical scene.

There is intentionally no second human-readable English screenplay file yet. An assembled reading view can be generated later from verified translation records.

## Scene 1 pilot — verified

The four-unit pilot was reviewed for fidelity and editorial consistency and is now `verified`:

1. opening stage direction;
2. soundtrack occurrence `parasakthi-song-001` / `வாழ்க வாழ்கவே`;
3. transition stage direction before the speech;
4. dialogue record `parasakthi-s001-d001` under the exact label `தங்கப்பன்`.

The Thangappan utterance remains one translation unit across PDF **4→5** / printed **3→4**, with aligned English page segments. The notably interpretive song rendering `பண்ணிகர்` → `melodious` remains explicitly disclosed in the unit notes rather than hidden.

## First full batch — scenes 2–5 in review

The first full batch adds **66 review units**:

- scene 2 — **46 units**: 41 dialogue + 5 stage directions;
- scene 3 — **10 units**: 8 dialogue + 2 stage directions;
- scene 4 — **2 units**: 1 stage direction + 1 song;
- scene 5 — **8 units**: 5 dialogue + 3 stage directions.

Cumulative translation state: **70 units total — 4 verified / 66 review**.

### Representation decisions established in this batch

- Scene 4's entire speaker-labelled `இல் வாழ்வினிலே` verse is represented as **one song translation unit** linked to `parasakthi-song-002`. The exact Tamil speaker labels `தங்`, `கல்`, `இரு` are retained inline in the English lines. The same source text is not duplicated as eight separate English dialogue units.
- Colloquial and code-switched speech in scene 2 is translated for meaning while exact Tamil `speaker_label` values remain immutable metadata.
- Semantically unusual source wording is not silently repaired. Scene 3's `உலகில் ஒரு அண்ணன் இருந்து பெண்ணைப் பிறந்தால் பெரும் துயர் என்பார்கள்` is translated conservatively and explicitly noted for review.
- Scene 5's compressed newspaper line around `இரங்கூன் கடலோரங்களில் எதிரிகள் கப்பல்கள் இந்தியா போய்ச் சேரவில்லை` is translated without inventing a causal relationship not stated in the Tamil.

## Next activity

Perform a second-pass fidelity/editorial review of all **66 units in scenes 2–5**. If accepted, mark those scenes `verified` and begin the next English translation batch with canonical **scenes 6–10**, using the same schema and source-linking rules.
