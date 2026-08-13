# Parasakthi — English translation layer

**Canonical authority:** verified Tamil transcription and immutable structured derivatives  
**Target language:** English (`en`)  
**Status:** in progress — scenes **1–20 verified**

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

## Verified coverage — scenes 1–20

Scenes **1–20** have passed deliberate second-pass review: **311 verified units**.

- scenes started: **1–20**;
- scenes verified: **1–20**;
- scenes in review: **none**;
- translation units: **311**;
- verified: **311**;
- review: **0**;
- kinds: **250 dialogue / 54 stage direction / 7 song / 0 quoted verse**.

The review gates remain cumulative:

- scenes 6–10: **66 units** second-pass verified;
- scenes 11–15: **88 units** second-pass verified;
- scenes 16–20: **87 units** second-pass verified.

### Scenes 16–20 review checkpoint

The second pass checked all **87 units** against the verified scene derivatives, immutable dialogue records, page provenance, the verified scene-17 song derivative, and the song inventory.

English-only refinements included:

- **scene 16:** tightened the following-year wording while retaining the carved-statue, `பாழும் தெய்வம்`, and infant-in-arms source images;
- **scene 17:** refined the lullaby opening while preserving `மாமன்மார் மூவர் தம்பி`, `பாலாடை`, `சீதனம்`, the PDF 21→22 occurrence, the unlabelled conscience block, and `சுமைதாங்கி / சோகம் தாங்கி` wordplay;
- **scene 18:** changed the over-specific English diagnosis to generic `fits` for period `காக்கா வலிப்பு`; source forms such as `டேபின்` remain unresolved rather than guessed;
- **scene 19:** corrected the split-name handling of `நந்த / கோபாலன்` and `வேணு / கோபாலன்`, and kept four unlabelled performed blocks scene-located without inventing dialogue IDs, soundtrack occurrences or authorship;
- **scene 20:** corrected `பொறுக்கவா?` to the source-nearer `Why—to scavenge?`; opaque forms such as `எய்ட் நாட்திரீ` and `கொட்டாபுளி`, plus the final arrest ambiguity, remain explicitly documented.

No canonical Tamil, scene file, dialogue record, character record or Tamil song derivative was changed.

## Next activity

Create the next source-linked English review batch covering canonical **scenes 21–25**, but only for the observed scenes **21, 22, 24 and 25**. Canonical **scene 23 is absent and must not be invented**. After creating that batch, perform the same deliberate second-pass review before verification.
