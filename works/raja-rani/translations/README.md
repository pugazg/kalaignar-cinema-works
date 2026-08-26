# ராஜா ராணி — English translation layer

**Canonical authority:** verified Tamil scene derivatives, immutable dialogue records, and the separately verified song/performance layer  
**Target language:** English (`en`)  
**Status:** **pilot-verified — scene 1 / 50 eligible verified scenes; 11 verified units**

This directory contains the source-linked English derivative of `ராஜா ராணி`. Nothing here repairs, modernizes, expands or overwrites the Tamil source layers.

The booklet prints **no numbered screenplay scenes**. Translation IDs such as `raja-rani-en-s001-u001` use the archive's derivative navigation segmentation only and must never be presented as source scene numbering.

Eight archival scenes remain outside English production because they intersect review-source pages: `s011`, `s012`, `s013`, `s033`, `s039`, `s053`, `s054`, `s055`.

## Files

- `schema.json` — scene-sharded source-linked translation schema.
- `index.json` — translation coverage and integrity checkpoint.
- `PILOT_REVIEW.md` — scene-1 fidelity/voice review and scaling rules.
- `records/scene-001.json` — verified pilot scene record.

The 11 numbered front-matter song bodies remain source structures outside the screenplay scene segmentation. They will be translated through a parallel song-linked translation set rather than being forced into invented scene IDs. Screenplay song references/performance cues may link to `songs/index.json` through `source_occurrence_id` when source evidence supports that relation.

## Translation principles

1. **Verified Tamil remains authoritative.** English fluency is never evidence for changing a Tamil reading.
2. **Exact source speaker labels remain metadata.** Every source-labelled utterance links to its immutable dialogue record; labels such as `டாக்டர்` / `டாக்`, `ராஜா` / `ராசா` are not normalized in translation metadata.
3. **Source-unlabelled speech remains unlabelled.** Where later scenes contain direct speech without an explicit source label, translation may preserve it as a source-linked unit with null `speaker_label` and null `source_record_id`; no speaker is invented.
4. **Stage directions stay source-bounded.** Do not add action, motivation, identity or scene closure not printed in the verified scene derivative.
5. **Rhetoric and colloquial force survive.** Repetition, hesitation, insults, rhetorical questions, comic timing, ellipses and abrupt syntax are retained when intelligible in English.
6. **Tamil forms of address may remain transliterated when translation would falsely specify a relationship or flatten register.** The pilot establishes `Amma` / `amma` and `Appa` in this way.
7. **Code-switching remains visible.** Source-visible English-derived forms such as `தேங்க்ஸ்` are not silently naturalized away when the switch itself carries source texture.
8. **Cross-page source units remain one English unit.** Page provenance and `english_page_segments` must mirror genuine physical source crossings.
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
- cross-page units: **0**;
- canonical Tamil modified: **no**;
- dialogue records modified: **no**;
- character/song derivatives modified by translation: **no**.

See `PILOT_REVIEW.md` for the voice and scaling checkpoint.

## Next batch

Translate verified `raja-rani-s002` through `raja-rani-s005` in source order, retaining all source-labelled dialogue links and all source-visible stage/performance material. Do not cross into blocked `s011`–`s013` in a later batch; translation batching must follow the verified-scene eligibility map.
