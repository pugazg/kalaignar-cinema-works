# ராஜா ராணி — English translation layer

**Canonical authority:** verified Tamil scene derivatives, immutable dialogue records, and the separately verified song/performance layer  
**Target language:** English (`en`)  
**Status:** **in-progress-verified — scenes 1–10 / 50 eligible verified scenes; 234 verified units**

This directory contains the source-linked English derivative of `ராஜா ராணி`. Nothing here repairs, modernizes, expands or overwrites the Tamil source layers.

The booklet prints **no numbered screenplay scenes**. Translation IDs such as `raja-rani-en-s001-u001` use the archive's derivative navigation segmentation only and must never be presented as source scene numbering.

Eight archival scenes remain outside English production because they intersect review-source pages: `s011`, `s012`, `s013`, `s033`, `s039`, `s053`, `s054`, `s055`.

## Files

- `schema.json` — scene-sharded source-linked translation schema.
- `index.json` — translation coverage and integrity checkpoint.
- `PILOT_REVIEW.md` — scene-1 fidelity/voice review and scaling rules.
- `BATCH_002_005_REVIEW.md` — verified review for scenes 2–5.
- `BATCH_006_010_REVIEW.md` — verified review for scenes 6–10.
- `records/scene-001.json` through `records/scene-010.json` — verified scene records.

The 11 numbered front-matter song bodies remain source structures outside the screenplay scene segmentation. They will be translated through a parallel song-linked translation set rather than being forced into invented scene IDs. Screenplay song references/performance cues may link to `songs/index.json` through `source_occurrence_id` when source evidence supports that relation.

## Translation principles

1. **Verified Tamil remains authoritative.** English fluency is never evidence for changing a Tamil reading.
2. **Exact source speaker labels remain metadata.** Every source-labelled utterance links to its immutable dialogue record; labels such as `டாக்டர்` / `டாக்`, `ராஜா` / `ராசா` are not normalized in translation metadata.
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
14. **Blocked review-source scenes stay blocked.** English translation does not become a vehicle for reconstructing PDF 27, 48, 57 or 74.

## Pilot and Batch 002–005

The scene-1 pilot established the voice rules with **11 verified units / 9 immutable dialogue links**. Scenes 2–5 then added **98 verified units** and **93/93** dialogue links, including three genuine cross-page units and the verified scene-4 performance link to `raja-rani-song-perf-001`.

See `PILOT_REVIEW.md` and `BATCH_002_005_REVIEW.md`.

## Batch 006–010 coverage

Scenes `raja-rani-s006` through `raja-rani-s010` add **125 verified units**:

- dialogue-kind: **105** — 101 immutable dialogue links + 4 source-unlabelled spoken units;
- stage direction: **18**;
- written text: **2**;
- new song/performance units: **0**;
- new genuine cross-page units: **1** — the newspaper letter in scene 9, PDF 22→23.

The batch links all **101/101** immutable dialogue records in scenes 6–10. Scenes 8 and 10 correctly have zero immutable dialogue records but retain their verified source-visible stage/narrative content.

Scene 7 keeps Samarasam's rambling anti-war speech, the `டாட்டர்` / `டாக்டர்` daughter-doctor misunderstanding, and the exact long source label `கீதாவின் தாய் தாயம்மாள்` without normalizing the immutable dialogue metadata.

Scene 9 preserves newspaper headlines and the Leela letter as written text, while four directly printed but source-unlabelled spoken spans remain null-speaker dialogue-kind units. The letter stays one source-linked unit across PDF **22→23**. The `படி` read/step joke, the `ராஜா` name/title misunderstanding and source-visible code-switching remain explicit.

Current cumulative state:

- eligible verified scenes translated: **10/50**;
- verified English units: **234**;
- unit mix: **207 dialogue / 24 stage direction / 1 performance cue / 2 written text**;
- immutable dialogue records linked in completed scenes: **203/203**;
- source-unlabelled spoken units: **4**;
- cross-page English units: **4**;
- translated screenplay song/performance occurrences: **1**;
- canonical Tamil modified: **no**;
- scene/dialogue/character/song source derivatives modified by translation: **no**.

See `BATCH_006_010_REVIEW.md` for the detailed checkpoint.

## Next batch

Skip blocked `raja-rani-s011`–`raja-rani-s013` and translate verified `raja-rani-s014` through `raja-rani-s018` in source order. Preserve exact dialogue linkage, source-unlabelled speech, stage/performance structure and physical page crossings; do not invent speakers, lyrics, scene endings or authorship.
