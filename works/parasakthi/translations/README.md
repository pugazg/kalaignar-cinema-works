# Parasakthi — English translation layer

**Canonical authority:** verified Tamil transcription and its immutable structured derivatives  
**Target language:** English (`en`)  
**Status:** pilot in review — canonical scene 1

This directory contains interpretive English derivatives. Nothing in this layer is allowed to repair, normalize, or overwrite the verified Tamil source.

## Translation principles

1. **Tamil remains authoritative.** A smoother English rendering is never evidence that the Tamil should be changed.
2. **Every unit is source-linked.** Each translation record carries canonical scene, source path, source record/occurrence ID where one exists, and PDF/printed-page provenance.
3. **Exact source identifiers stay exact.** Dialogue `speaker_label` values remain exactly as represented in the dialogue index. Character normalization, when useful, is a separate reference to the character index.
4. **Stage directions do not gain action.** Translate only the action/context present in the verified source.
5. **Dialogue preserves rhetorical force.** Repetition, questions, exclamations, metaphors and social/political language should not be flattened merely for fluency.
6. **Songs are semantic translations, not singable rewrites.** Preserve source line order and stanza structure where practical; do not introduce rhyme, meter or imagery not present in the Tamil.
7. **Quoted verse stays distinct from soundtrack song.** Authorship and source-kind distinctions from the completed song layer remain intact.
8. **Cross-page source units remain one unit.** `english_page_segments` may be used to show how an English rendering aligns to a source utterance that crosses a page anchor.
9. **Translation status is independent.** `draft`, `review`, and `verified` refer only to the English derivative, never to Tamil source status.
10. **No external text substitution.** Web translations, subtitles, film dialogue, published English versions or audio memory must not replace source-linked translation work.

## Storage

- `schema.json` — translation unit schema.
- `index.json` — translation checkpoint / scene coverage manifest.
- `records/scene-XX.json` — source-linked translation units grouped by canonical scene.

The pilot deliberately avoids a second human-readable English screenplay file so that there is only one English text authority during schema validation. An assembled reading view can be generated later from verified translation records.

## Pilot — scene 1

The first pilot contains four units:

1. opening stage direction from `scenes/scene-01.md`;
2. soundtrack occurrence `parasakthi-song-001` / `வாழ்க வாழ்கவே`;
3. transition stage direction before the speech;
4. dialogue record `parasakthi-s001-d001` spoken under the exact label `தங்கப்பன்`.

The Thangappan utterance remains one translation unit and retains its PDF **4→5** / printed **3→4** source provenance.

All four units are currently `review`: the source linkage and semantic rendering have been checked once, but they are not yet declared `verified` English.

## Review conventions established by the pilot

- Historical place names may be rendered in period-readable English where unambiguous (`இரங்கூன்` → `Rangoon`, `மலேயா` → `Malaya`).
- Poetic compression may require a semantic English phrase; any materially interpretive choice should be noted on the unit rather than hidden.
- The song phrase printed as `பண்ணிகர்` is not altered in Tamil. The pilot English renders its contextual sense as `melodious` and records that choice in a translation note.
- Source refrain fragments such as `(வாழ்க` are represented as refrain cues in English rather than treated as missing prose.

## Next activity

Review the four scene-1 pilot units for translation fidelity and editorial consistency. If accepted, mark them `verified` and begin the first full translation batch with canonical scenes **2–5**, using the same schema and source-linking rules.
