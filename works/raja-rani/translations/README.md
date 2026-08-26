# ராஜா ராணி — English translation layer

**Canonical authority:** verified Tamil scene derivatives, immutable dialogue records, and the separately verified song/performance layer  
**Target language:** English (`en`)  
**Status:** **in-progress-verified — scenes 1–5 / 50 eligible verified scenes; 109 verified units**

This directory contains the source-linked English derivative of `ராஜா ராணி`. Nothing here repairs, modernizes, expands or overwrites the Tamil source layers.

The booklet prints **no numbered screenplay scenes**. Translation IDs such as `raja-rani-en-s001-u001` use the archive's derivative navigation segmentation only and must never be presented as source scene numbering.

Eight archival scenes remain outside English production because they intersect review-source pages: `s011`, `s012`, `s013`, `s033`, `s039`, `s053`, `s054`, `s055`.

## Files

- `schema.json` — scene-sharded source-linked translation schema.
- `index.json` — translation coverage and integrity checkpoint.
- `PILOT_REVIEW.md` — scene-1 fidelity/voice review and scaling rules.
- `BATCH_002_005_REVIEW.md` — verified review for scenes 2–5.
- `records/scene-001.json` through `records/scene-005.json` — verified scene records.

The 11 numbered front-matter song bodies remain source structures outside the screenplay scene segmentation. They will be translated through a parallel song-linked translation set rather than being forced into invented scene IDs. Screenplay song references/performance cues may link to `songs/index.json` through `source_occurrence_id` when source evidence supports that relation.

## Translation principles

1. **Verified Tamil remains authoritative.** English fluency is never evidence for changing a Tamil reading.
2. **Exact source speaker labels remain metadata.** Every source-labelled utterance links to its immutable dialogue record; labels such as `டாக்டர்` / `டாக்`, `ராஜா` / `ராசா` are not normalized in translation metadata.
3. **Source-unlabelled speech remains unlabelled.** Where later scenes contain direct speech without an explicit source label, translation may preserve it as a source-linked unit with null `speaker_label` and null `source_record_id`; no speaker is invented.
4. **Stage directions stay source-bounded.** Do not add action, motivation, identity or scene closure not printed in the verified scene derivative.
5. **Rhetoric and colloquial force survive.** Repetition, hesitation, insults, rhetorical questions, comic timing, ellipses and abrupt syntax are retained when intelligible in English.
6. **Tamil forms of address may remain transliterated when translation would falsely specify a relationship or flatten register.** The pilot establishes `Amma` / `amma` and `Appa`; Batch 002–005 also retains `thambi`, `athaan` and other context-bearing forms where useful.
7. **Code-switching remains visible.** Source-visible English-derived forms such as `தேங்க்ஸ்` and `அமெச்சூர்ஸ்` are not silently naturalized away when the switch itself carries source texture.
8. **Cross-page source units remain one English unit.** Page provenance and `english_page_segments` mirror genuine physical source crossings.
9. **Songs are distinct translation units.** Complete printed lyric bodies use semantic-poetic translation; cue-only or reference-only occurrences never receive missing lyrics.
10. **Authorship status is not translation content.** The five later-anthology Kalaignar attributions remain evidence metadata only; the six unresolved numbered-song authorships stay unresolved.
11. **Decorative star/rule separators remain structural.** They do not become invented prose such as `(Scene ends.)`.
12. **Written material remains written text.** Letters, newspaper matter and similar source blocks are not converted into dialogue merely because a character reads or reacts to them.
13. **Embedded dramas remain structurally distinct.** `சேரன் செங்குட்டுவன்`, the `அகல்யா` rehearsal and `சாக்ரடீஸ்` identities and registers are not collapsed into outer-film identities.
14. **Blocked review-source scenes stay blocked.** English translation does not become a vehicle for reconstructing PDF 27, 48, 57 or 74.

## Pilot coverage

`raja-rani-s001` / PDF 10 / printed p.9:

- units: **11**;
- dialogue-kind units: **9**;
- stage-direction units: **2**;
- immutable dialogue records linked: **9/9**;
- source-unlabelled spoken units: **0**;
- song/performance units: **0**;
- cross-page units: **0**.

See `PILOT_REVIEW.md` for the initial voice checkpoint.

## Batch 002–005 coverage

Scenes `raja-rani-s002` through `raja-rani-s005` add **98 verified units**:

- dialogue: **93**;
- stage direction: **4**;
- performance cue: **1**;
- cross-page units: **3**.

The batch links all **93/93** immutable dialogue records in those scenes. Cumulative completed-scene dialogue linkage is therefore **102/102**.

Scene 4 keeps the `சேரன் செங்குட்டுவன்` embedded-play boundary explicit and represents Rani's ticket-selling singing direction as `raja-rani-song-perf-001`, securely linked by the song inventory to numbered song 3. No front-matter lyric is imported into the screenplay scene.

Scene 5 keeps Cheran's long Purananuru-inspired recitation as one immutable dialogue-linked English unit across PDF **15→16→17→18**, with page segments preserving the physical scan boundaries. The translation keeps source rhetoric and cultural vocabulary instead of substituting wording from an outside Purananuru edition.

Current cumulative state:

- eligible verified scenes translated: **5/50**;
- verified English units: **109**;
- unit mix: **102 dialogue / 6 stage direction / 1 performance cue**;
- immutable dialogue records linked in completed scenes: **102/102**;
- source-unlabelled spoken units: **0**;
- cross-page English units: **3**;
- translated screenplay song/performance occurrences: **1**;
- canonical Tamil modified: **no**;
- scene/dialogue/character/song source derivatives modified by translation: **no**.

See `BATCH_002_005_REVIEW.md` for the detailed batch checkpoint.

## Next batch

Translate verified `raja-rani-s006` through `raja-rani-s010` in source order, then stop before blocked `s011`–`s013`. Preserve exact dialogue linkage, source-unlabelled speech, stage/performance structure and physical page crossings; do not invent speakers, lyrics, scene endings or authorship.
