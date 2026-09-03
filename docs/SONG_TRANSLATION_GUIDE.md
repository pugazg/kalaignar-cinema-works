# Kalaignar Cinema Works — Song Translation Guide

This guide governs English translation of verified Kalaignar song texts in `pugazg/kalaignar-cinema-works`.

It supplements `docs/SONG_ANTHOLOGY_PROCESSING_GUIDE.md` and the repository's source/transcription rules. The verified Tamil derivative remains authoritative; English is a separate source-linked layer.

The guide applies both to dedicated song anthologies and to independently bounded/numbered song corpora embedded in another cinema publication, such as front-matter songs in a screenplay booklet.

## 1. Translation goal

The target is **source-faithful literary English that retains Kalaignar's language, rhetoric and political-poetic force**. It is not a singable adaptation, modernization, paraphrase or rewrite.

A smoother English line is not automatically a better line. When fluency conflicts with a distinctive source image, repetition, turn of phrase, social register or rhetorical blow, preserve the source force first.

## 2. Voice-retention rules

- Preserve repetition as repetition. Do not collapse refrains, parallel constructions or repeated invocations.
- Preserve political and social satire directly. Do not soften class language, ridicule, accusation or anti-pretence rhetoric into neutral prose.
- Preserve concrete images before replacing them with abstract English. If the Tamil says a flower, flame, root, dust, honey, womb, bird, palace or buffalo calf, the English should normally retain that image.
- Preserve accumulations, contrasts and rhetorical questions. Do not summarize several source lines into one polished sentence.
- Preserve colloquial energy. Rustic or spoken forms must not be converted into formal literary English merely for elegance.
- Preserve culturally loaded words or performance terms by transliteration when a short English substitute would flatten the source. Explain such choices in translation notes rather than rewriting the lyric.
- Do not invent rhyme, metre or alliteration when doing so changes meaning. Echo sound-patterning only when it arises naturally without semantic loss.
- Do not import contemporary political vocabulary that the source does not use.

## 3. Source anomalies and unusual forms

English translation must never be used to repair Tamil.

If a verified Tamil witness contains an unusual, joined, colloquial or grammatically difficult form:

1. keep the Tamil source unchanged;
2. translate conservatively from the visible wording and context;
3. document any interpretive pressure point in the English record;
4. do not silently emend the Tamil to a familiar lyric, recording, subtitle or web version.

Where the morphology itself is anomalous and a clean English rendering would imply an unrecorded Tamil correction, retain the anomaly as far as readable English permits and note it explicitly.

## 4. Structural fidelity

- Retain source song number and film/publication provenance.
- Retain source page provenance.
- Retain stanza order and refrain order.
- Retain exact Tamil turn labels in source metadata; do not expand abbreviations or infer identities without evidence.
- Keep performance labels such as `தொகையறா`, `பாட்டு`, `பல்லவி`, `விருத்தம்`, `வசனம்` source-visible. A transliterated English display label may accompany them, but the source label remains authoritative.
- Prefer one English line/cue per Tamil lyric line/cue. Where syntax requires a different grouping, record the mapping explicitly and do not lose a source line.
- Preserve dialogue/song interleaving when a printed song block mixes spoken `வசனம்` and sung passages.
- A separately numbered song body is not a screenplay scene. Do not invent scene IDs merely because the work also has scene-sharded translation.

## 5. Translation modes

The default mode for songs is `semantic-poetic-source-faithful`.

This means:

- semantic meaning remains controlling;
- poetic imagery and rhetoric are preserved;
- the translation may be idiomatic English, but not at the cost of erasing Kalaignar's voice;
- the translation is not optimized to fit the original melody.

A future singable/adapted version, if ever requested, must be stored as a separate derivative and must not replace this translation layer.

## 6. Attribution discipline

Translation status and authorship status are separate.

A song that is `anthology-attributed` may have a `verified` English translation while still remaining only `anthology-attributed` for authorship. English metadata must not imply `primary-source-verified` unless separate evidence supports that status.

Likewise, a song whose lyricist is `unresolved` may still have a complete-verified translation. Translation must not infer authorship from style, political vocabulary, character identity, singer, scene context or similarity to another song.

If a screenplay performance cue has only a `review`-level relationship to a numbered song, translating the numbered song does not upgrade that performance link.

## 7. Translation record gate

Before a song translation becomes `verified`:

- the Tamil song must already be verified;
- every English line/cue must map to visible Tamil source text;
- refrain and turn labels must be checked;
- source page provenance must match the Tamil record;
- no Tamil line may disappear through paraphrase;
- no external lyric may be imported;
- translation notes must identify any deliberate retention of culturally specific or source-anomalous wording;
- authorship metadata must remain at the source-supported tier;
- performance links must remain at their pre-translation evidence tier.

A first approved translation sample may use `pilot-verified`. Scaling to the rest of a corpus must follow the same voice decisions unless a later review explicitly changes the translation policy.

## 8. Whole-corpus song QA

Before declaring a numbered-song or anthology-song translation corpus complete, run a whole-set QA rather than relying only on per-song status.

Verify at minimum:

- expected song IDs are present exactly once and in source order;
- every translated record points to the correct verified Tamil derivative;
- every source page set matches the Tamil record/inventory;
- all Tamil lines/cues are mapped exactly once unless an explicit many-to-one/one-to-many mapping is documented;
- no external/unprinted lyric line appears;
- source turn/performance labels are preserved;
- cross-page songs retain full provenance;
- authorship counts/statuses are unchanged by translation;
- screenplay performance links are not silently promoted;
- no song body has been forced into a synthetic screenplay scene identity.

Raja Rani is the standing precedent for a mixed-work song gate: its 11 numbered front-matter songs are translated separately from the 58-scene screenplay, and final QA verifies **67 sections / 181 Tamil-to-English line-cue mappings** while preserving 5 later-anthology Kalaignar attributions, 6 unresolved lyricists and the review-level scene-58/song-11 relation.

## 9. Completion and repository-wide synchronization gate

A complete song corpus is not a closed project phase until its current status is synchronized beyond the translation records themselves.

Update all relevant work-local surfaces:

- song translation `index.json`;
- song translation README;
- final whole-corpus song QA/review;
- work metadata and README;
- work handover / next-chat prompt when present;
- source song index/README when their `next_activity` or downstream-status fields change.

When the work-level checkpoint changes, also synchronize repository-wide mirrors:

- `data/works.json`;
- root `README.md`;
- `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md` when the project checkpoint or reusable lessons change;
- `docs/STATUS_CONSISTENCY_AUDIT.md`;
- any shared guide whose reusable policy changed.

Then sweep for obsolete `0/N`, pilot-only, blocked/review, prior-next-activity or old count language in **active** status/startup documents. Historical batch notes may retain historical counts when clearly identified as historical.

Do not declare the song-translation phase complete while a current repository-wide mirror still says the corpus is not started or partially translated.