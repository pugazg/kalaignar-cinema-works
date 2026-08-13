# Parasakthi — English translation layer

**Canonical authority:** verified Tamil transcription and immutable structured derivatives  
**Target language:** English (`en`)  
**Status:** in progress — scenes **1–10 verified**; scenes **11–15 in review**

This directory contains interpretive English derivatives. Nothing here may repair, normalize, or overwrite the verified Tamil source.

## Translation principles

1. **Tamil remains authoritative.** Smoother English is never evidence for changing Tamil.
2. **Every unit is source-linked.** Preserve canonical scene, source path, record/occurrence ID where available, and PDF/printed-page provenance.
3. **Exact identifiers stay exact.** Tamil `speaker_label` values remain immutable metadata.
4. **Stage directions do not gain action.** Translate only what the verified source supplies.
5. **Dialogue preserves rhetorical force.** Repetition, questions, code-switching, metaphors and political/social rhetoric are not flattened merely for fluency.
6. **Songs are semantic translations, not singable rewrites.** Preserve line/stanza order where practical; do not invent rhyme, metre or imagery.
7. **Quoted verse remains distinct from soundtrack song.**
8. **Cross-page source units remain one translation unit.** Use `english_page_segments` when page-boundary alignment matters.
9. **Translation status is independent.** `draft`, `review`, `verified` refer only to English.
10. **No external text substitution.** Web translations, subtitles, film audio or later English versions do not replace source-linked work.

## Storage

- `schema.json` — translation-unit schema.
- `index.json` — coverage/status manifest.
- `records/scene-XX.json` — source-linked English units grouped by canonical scene.

There is intentionally no separate assembled English screenplay yet. A reading view can be generated later from verified records.

## Verified coverage — scenes 1–10

Scenes **1–10** have passed deliberate second-pass review: **136 verified units**.

The scenes 6–10 pass reviewed all **66 units** against canonical scene files, immutable dialogue records, page provenance and the verified scene-8 song derivative. English-only corrections were made where the review found genuine additions, omissions or over-resolution; no Tamil/source file was changed.

Review refinements included:

- scene 6: `புறப்படு சீக்கிரம்` no longer gains `let's`; the elliptical `நீ சொன்ன படியெல்லாம் கேட்டிரு` no longer gains an unstated `she`;
- scene 7: `சரிதாம்போ` no longer gains an unstated kinship address, and `பிள்ளைக் குட்டிக்காரன்` no longer gains `to feed`;
- scene 8: the closing stage direction again includes the source action `விழுந்து` (`falls`); the compressed third stanza of `ஓ ரசிக்கும் சீமானே` remains unsmoothed;
- scene 9: `காலையிலே` is `this morning`, while anomalous `வங்கத்திலே`, unclear `தகுதி? போக்கியதை?`, and the PDF 12→13 break remain explicitly documented;
- scene 10: hospital `பெட்டிலே` remains contextually `bed` in English only, and the bombing direction stays broad rather than inventing an injury.

## New review batch — scenes 11–15

Canonical scenes **11–15** now have source-linked English review records: **88 new units**.

Per-scene counts:

- scene 11 — **3**: 2 dialogue + 1 stage direction;
- scene 12 — **10**: 7 dialogue + 2 stage directions + 1 song;
- scene 13 — **32**: 26 dialogue + 6 stage directions;
- scene 14 — **19**: 16 dialogue + 3 stage directions;
- scene 15 — **24**: 16 dialogue + 6 stage directions + 2 songs.

Cumulative translation state:

- scenes started: **1–15**;
- scenes verified: **1–10**;
- scenes in review: **11–15**;
- translation units: **224**;
- verified: **136**;
- review: **88**;
- kinds: **176 dialogue / 42 stage direction / 6 song / 0 quoted verse**.

### Scene 11 review pressure points

- The source simile `வில்லுக்கொத்து போல` is kept conservatively as `together like a bundle of bows`; it is not replaced by a smoother invented image.
- The account of Kalyani's cash and jewellery is translated so that English does not imply literally selling money, while the source sequence remains untouched.

### Scene 12 review pressure points

- `பூமாலை` / `parasakthi-song-004` is one semantic-poetic unit on PDF 14.
- The unusual source person-shift `வந்தேன் தவழ்ந்தாய்?` remains visible in English rather than being silently repaired.
- `பாரான எந்தன் வயிற்றில்` is documented as semantically difficult.
- `தாலி அறுத்தவர்கள்` retains the period tali image, and `தாசில் உத்தியோகம்` remains the source's culturally specific `Tahsildar's post` comparison rather than being generalized.

### Scene 13 review pressure points

- The Marwari-shop dialogue retains its source-linked dialect/code-switching without inventing a caricatured English accent.
- The kinship joke around `தம்பி முறை` remains a kinship claim, not a modernized or sexualized inference.
- `parasakthi-s013-d023` remains one cross-page unit across PDF **16→17**. Its repeated first-person forms and later third-person shift are deliberately preserved and noted.
- The policeman's following line, `நீ மெட்ராசுக்கு மேயராக வர்ற காலத்திலே மிருகத்தையெல்லாம் மனுஷனுக்கு.`, remains fragmentary in English; no missing verb is invented.

### Scene 14 review pressure points

- `மாப்கரோஜ் மகராஜ்` is transliterated so Venu's following sound-play can remain visible.
- `மண்ணாங்கட்டி` is rendered dismissively as `rubbish`, while `ரோஜ்` remains as sound-play rather than being over-explained.
- `நாணயம்` in Venu's credit offer is rendered as reliability/creditworthiness, not literally as coin.

### Scene 15 review pressure points

- The unexplained source token `பாரா-2` is retained transparently as `[para-2]` with a note.
- The Mariamman-temple earth-flinging image remains source-specific rather than being replaced with a generic curse.
- Gunasekaran's `பைத்தியக்கார உலகம்` monologue retains its blunt sequence of hunger, theft, punishment and deception.
- Soundtrack track 1 appears as two structurally distinct verified source occurrences: `parasakthi-song-005` (`குதம்பாய்`, PDF 19→20) and `parasakthi-song-006` (`தாண்டவக்கோனே`, PDF 20). They therefore remain two semantic-poetic translation units even though they belong to one soundtrack composition.

## Next activity

Perform a deliberate second-pass fidelity/editorial review of all **88 units in scenes 11–15**. Verify ordering, dialogue IDs and exact labels, stage-direction locators, song occurrence links and page provenance. Change English only where a genuine translation problem is found. **Do not begin scenes 16–20 until that review is complete.**
