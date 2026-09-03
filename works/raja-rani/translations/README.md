# ராஜா ராணி — English translation layer

**Canonical authority:** verified Tamil scene derivatives, immutable dialogue records, and the separately verified song/performance layer  
**Target language:** English (`en`)  
**Status:** **in-progress-verified — 30 / 58 verified scenes; 715 verified units**

This directory contains the source-linked English derivative of `ராஜா ராணி`. Nothing here repairs, modernizes, expands or overwrites the Tamil source layers.

The booklet prints **no numbered screenplay scenes**. Translation IDs such as `raja-rani-en-s001-u001` use the archive's derivative navigation segmentation only and must never be presented as source scene numbering.

The final direct-scan resolution pass has now verified **all 58 archival scenes**. There are **0 source-blocked scenes**. The durable source-resolution record is `../notes/final-source-review-resolution.md`.

## Files

- `schema.json` — scene-sharded source-linked translation schema.
- `index.json` — translation coverage and integrity checkpoint.
- `PILOT_REVIEW.md` — scene-1 fidelity/voice review and scaling rules.
- `BATCH_002_005_REVIEW.md` — verified review for scenes 2–5.
- `BATCH_006_010_REVIEW.md` — verified review for scenes 6–10.
- `BATCH_014_018_REVIEW.md` — verified review for scenes 14–18.
- `BATCH_019_023_REVIEW.md` — verified review for scenes 19–23.
- `BATCH_024_034_REVIEW.md` — verified 10-scene review for scenes 24–32 and 34; scene 33 was still source-blocked when that historical batch ran and was therefore correctly absent.
- verified English scene records currently cover scenes **1–10, 14–32 and 34**.

The 11 numbered front-matter song bodies remain source structures outside the screenplay scene segmentation. They will be translated through a parallel song-linked translation set rather than being forced into invented scene IDs. Screenplay song references/performance cues may link to `songs/index.json` through `source_occurrence_id` when source evidence supports that relation.

## Translation principles

1. **Verified Tamil remains authoritative.** English fluency is never evidence for changing a Tamil reading.
2. **Exact source speaker labels remain metadata.** Every source-labelled utterance links to its immutable dialogue record; labels such as `டாக்டர்` / `டாக்`, `ராஜா` / `ராசா`, the source-exact scene-17 `தர்யம்`, and later exact labels such as `மனம்`, `நிழல்`, `ஞானக்கண் குரல்`, `ராஜாவின் குரல்`, and `சமரசம் குரல்` are not normalized in translation metadata.
3. **Source-unlabelled speech remains unlabelled.** It may be preserved as a source-linked dialogue-kind unit with null `speaker_label` and null `source_record_id`; no speaker is invented.
4. **Stage directions stay source-bounded.** Do not add action, motivation, identity or scene closure not printed in the verified scene derivative.
5. **Rhetoric and colloquial force survive.** Repetition, hesitation, insults, rhetorical questions, comic timing, ellipses and abrupt syntax are retained when intelligible in English.
6. **Tamil forms of address may remain transliterated when translation would falsely specify a relationship or flatten register.** `Amma`, `Appa`, `thambi`, `athaan` and similar source-bearing terms may remain where useful.
7. **Code-switching remains visible.** Source-visible English-derived forms are not silently naturalized away when the switch itself carries source texture.
8. **Cross-page source units remain one English unit.** Page provenance and `english_page_segments` mirror genuine physical source crossings.
9. **Songs are distinct translation units.** Complete printed lyric bodies use semantic-poetic translation; cue-only or reference-only occurrences never receive missing lyrics.
10. **Authorship status is not translation content.** The five later-anthology Kalaignar attributions remain evidence metadata only; the six unresolved numbered-song authorships stay unresolved.
11. **Decorative star/rule separators remain structural.** They do not become invented prose such as `(Scene ends.)`.
12. **Written material remains written text.** Letters, newspaper matter and similar source blocks are not converted into dialogue merely because a character reads or reacts to them.
13. **Embedded dramas remain structurally distinct.** `சேரன் செங்குட்டுவன்`, the `அகல்யா` rehearsal and `சாக்ரடீஸ்` identities and registers are not collapsed into outer-film identities.
14. **Source uncertainty is never reconstructed through English.** All former review pages are now directly resolved, but this rule remains permanent if a new dispute is discovered.
15. **Production batch size is 10 verified scenes per iteration**, processed in source order among scenes not yet translated.

## Verified batch history

- Pilot scene 1: **11 units / 9 dialogue links**.
- Scenes 2–5: **98 units / 93 dialogue links**.
- Scenes 6–10: **125 units / 101 dialogue links**, including four source-unlabelled spoken units, two written-text units and one new cross-page unit.
- Scenes 14–18: **153 units / 135 dialogue links**, including four source-unlabelled spoken units and one performance cue.
- Scenes 19–23: **96 units / 86 dialogue links / 10 stage directions**, with two new genuine cross-page units.
- Batch 24–34: **232 units / 198 dialogue links / 3 source-unlabelled spoken units / 31 stage directions**; s033 was correctly skipped under the source status that existed at that time.

See the corresponding `BATCH_*_REVIEW.md` files for exact source-fidelity decisions and per-scene counts.

## Final source-review resolution

The user's direct PDF review has now resolved every formerly bounded source limitation:

- PDF 27: exact form **`இரவெல்லாம்`**;
- PDF 48: exact forms **`வந்தனா`** and **`திடீர்னு`**;
- PDF 57: exact phrase **`முன்னுக்கு பின் முரணாயிகிட்டே போவது?`**;
- PDF 74: the `K. N. சங்கரன் ...` material is confirmed as a non-canonical ownership/library stamp; the screenplay runs directly from `ராஜா: விதவை.` to `சாந்: வித்தாரக்கள்ளி! விநாசகாரி`.

Current source derivative census is **58/58 verified scenes, 1,076 immutable dialogue records, 80/80 exact source labels and 44 verified entities/roles/collectives**.

## Current cumulative English state

- verified scenes translated: **30/58**;
- verified English units: **715**;
- unit mix: **633 dialogue / 78 stage direction / 2 performance cues / 2 written text**;
- immutable dialogue records linked in translated scenes: **622/622**;
- source-unlabelled spoken units: **11**;
- cross-page English units: **6**;
- translated screenplay song/performance occurrences: **2**;
- front-matter numbered song translations started: **0/11**.

## Next 10-scene iteration

Translate in source order:

`raja-rani-s011`, `s012`, `s013`, `s033`, `s035`, `s036`, `s037`, `s038`, `s039`, `s040`.

There is now **no blocked-scene skip**. Preserve exact dialogue linkage, source-unlabelled speech, stage/performance structure and physical page crossings. Do not invent speakers, lyrics, scene endings or authorship.
