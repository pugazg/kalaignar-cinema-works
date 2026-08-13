# Parasakthi — English translation layer

**Canonical authority:** verified Tamil transcription and immutable structured derivatives  
**Target language:** English (`en`)  
**Status:** in progress — scenes **1–5 verified**; scenes **6–10 in review**

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

## Verified coverage — scenes 1–5

Scene 1's four-unit pilot passed review first. The subsequent **66 units in scenes 2–5** have now also passed their deliberate second-pass review.

Verified cumulative state through scene 5: **70 units**.

Review refinements made before verification included:

- scene 2: the source direction `அண்ணியிடம் போதல்` no longer gains an English possessive not present in Tamil;
- scene 2: the unusual `தங்கையின் வாழ்விலே பொன் விழா?` remains question-shaped rather than being normalized into a more specific ceremony label;
- scene 4: `மாங்குயில்` is rendered naturally as `cuckoo`, while the Tamil source remains untouched;
- scene 3's semantically unusual elder-brother sentence and scene 5's compressed wartime newspaper line remain explicitly source-faithful rather than silently repaired.

## Second full batch — scenes 6–10 in review

This batch adds **66 review units**:

- scene 6 — **22**: 19 dialogue + 3 stage directions;
- scene 7 — **24**: 22 dialogue + 2 stage directions;
- scene 8 — **10**: 5 dialogue + 4 stage directions + 1 song;
- scene 9 — **1**: one cross-page rhetorical dialogue unit;
- scene 10 — **9**: 7 dialogue + 2 stage directions.

Cumulative translation state: **136 units — 70 verified / 66 review**.

### Review-sensitive decisions in scenes 6–10

- Scene 6's `முழுகாதிருக்கிற பெண்ணு` is rendered contextually as `a woman in her condition`, with the pregnancy euphemism documented rather than modernized in Tamil.
- Scene 7 preserves the source's explicit social language and the irony of begging as Gunasekaran's `first voice` on returning to Tamil Nadu.
- Scene 8's `ஓ ரசிக்கும் சீமானே` occurrence is one semantic-poetic unit spanning PDF 11→12. Its compressed line around `பெண்களின் வாழ்க்கையை இழந்தவர்கள் கோடி` is explicitly marked review-sensitive.
- Scene 9 remains one dialogue unit across PDF 12→13. The page break `நெஞ்சிலே / நஞ்சைக்` is retained through English page segments. The anomalous source word `வங்கத்திலே` is disclosed in notes rather than used to alter Tamil.
- Scene 10's source form `பெட்டிலே` is interpreted contextually as hospital `bed` only in English and recorded as such.

## Next activity

Perform a deliberate second-pass fidelity/editorial review of all **66 units in scenes 6–10**. If accepted, mark scenes 6–10 verified and begin the next English batch with canonical **scenes 11–15**, using the same immutable source-linking rules.
