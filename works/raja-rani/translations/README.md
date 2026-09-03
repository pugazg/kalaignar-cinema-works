# ராஜா ராணி — English translation layer

**Canonical authority:** verified Tamil scene derivatives, immutable dialogue records, and the separately verified song/performance layer  
**Target language:** English (`en`)  
**Status:** **in-progress-verified — 20 / 50 eligible verified scenes; 483 verified units**

This directory contains the source-linked English derivative of `ராஜா ராணி`. Nothing here repairs, modernizes, expands or overwrites the Tamil source layers.

The booklet prints **no numbered screenplay scenes**. Translation IDs such as `raja-rani-en-s001-u001` use the archive's derivative navigation segmentation only and must never be presented as source scene numbering.

Eight archival scenes remain outside English production because they intersect review-source pages: `s011`, `s012`, `s013`, `s033`, `s039`, `s053`, `s054`, `s055`.

## Files

- `schema.json` — scene-sharded source-linked translation schema.
- `index.json` — translation coverage and integrity checkpoint.
- `PILOT_REVIEW.md` — scene-1 fidelity/voice review and scaling rules.
- `BATCH_002_005_REVIEW.md` — verified review for scenes 2–5.
- `BATCH_006_010_REVIEW.md` — verified review for scenes 6–10.
- `BATCH_014_018_REVIEW.md` — verified review for scenes 14–18.
- `BATCH_019_023_REVIEW.md` — verified review for scenes 19–23.
- `records/scene-001.json` through `records/scene-010.json`, plus `records/scene-014.json` through `records/scene-023.json` — verified scene records, excluding blocked scenes 11–13.

The 11 numbered front-matter song bodies remain source structures outside the screenplay scene segmentation. They will be translated through a parallel song-linked translation set rather than being forced into invented scene IDs. Screenplay song references/performance cues may link to `songs/index.json` through `source_occurrence_id` when source evidence supports that relation.

## Translation principles

1. **Verified Tamil remains authoritative.** English fluency is never evidence for changing a Tamil reading.
2. **Exact source speaker labels remain metadata.** Every source-labelled utterance links to its immutable dialogue record; labels such as `டாக்டர்` / `டாக்`, `ராஜா` / `ராசா`, and the source-exact scene-17 `தர்யம்` occurrence are not normalized in translation metadata.
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

## Batch 014–018 coverage

After skipping blocked scenes 11–13, verified scenes 14–18 add **153 verified units**:

- dialogue-kind: **139** — 135 immutable dialogue links + 4 source-unlabelled spoken units;
- stage direction: **13**;
- performance cue: **1** — scene 16, linked to `raja-rani-song-perf-002`;
- written text: **0**;
- new genuine cross-page units: **0**.

All **135/135** immutable dialogue records in scenes 14–18 are linked. Post-Correction-005 reconciliation also keeps scene 15's source borrowing `கிரஷ்` visible as `Crush` in English and preserves the one-off exact source speaker label `தர்யம்` on scene 17 unit `raja-rani-en-s017-u017`; other `தாயம்` occurrences remain unchanged because they are separate source occurrences.

See `BATCH_014_018_REVIEW.md` for the detailed checkpoint.

## Batch 019–023 coverage

Verified scenes 19–23 add **96 verified units**:

- dialogue: **86** — all **86/86** immutable dialogue records in scenes 21 and 23;
- stage direction: **10**;
- source-unlabelled spoken units: **0**;
- performance cue / written text / song: **0**;
- new genuine cross-page units: **2** — scene 21's pigeon stage direction across PDF 35→36 and immutable dialogue `raja-rani-s021-d048` across PDF 37→38.

Scenes 19, 20 and 22 legitimately contain no immutable dialogue records and remain one source-parenthetical/stage unit each. Scene 21 retains the repeated `நீ` address as `nee`, exact source label variants, and the peace/quarrel signboard wordplay without normalizing Tamil. Scene 23 preserves source-visible `டேட்`, the playful `ட்ராமா, கீமா`, and the `பாடம்` / `பணம்` contrast.

See `BATCH_019_023_REVIEW.md` for the detailed checkpoint.

## Current cumulative state

- eligible verified scenes translated: **20/50**;
- verified English units: **483**;
- unit mix: **432 dialogue / 47 stage direction / 2 performance cues / 2 written text**;
- immutable dialogue records linked in translated scenes: **424/424**;
- source-unlabelled spoken units: **8**;
- cross-page English units: **6**;
- translated screenplay song/performance occurrences: **2**;
- front-matter numbered song translations started: **0/11**;
- canonical Tamil modified by translation: **no**;
- scene/dialogue/character/song source derivatives modified by translation: **no**.

## Next batch

Translate verified `raja-rani-s024` through `raja-rani-s028` in source order. Preserve exact dialogue linkage, source-unlabelled speech, stage/performance structure and physical page crossings. Scene 27 legitimately has zero immutable dialogue records. Do not invent speakers, lyrics, scene endings or authorship.
