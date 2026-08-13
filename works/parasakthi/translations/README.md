# Parasakthi — English translation layer

**Canonical authority:** verified Tamil transcription and immutable structured derivatives  
**Target language:** English (`en`)  
**Status:** in progress — scenes **1–10 verified**

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

Scenes **1–10** have now passed deliberate second-pass review.

Verified cumulative state through scene 10: **136 units**.

- verified units: **136**
- review units: **0**
- kinds: **109 dialogue / 24 stage direction / 3 song / 0 quoted verse**

The scenes 6–10 pass reviewed all **66 units** against the canonical scene files, immutable dialogue records, page provenance and the verified song derivative for scene 8. English-only corrections were made where the review found genuine additions, omissions or over-resolution; no Tamil/source file was changed.

### Scene 6 review decisions

- `முழுகாதிருக்கிற பெண்ணு` remains `a woman in her condition`, preserving the period pregnancy euphemism.
- `புறப்படு சீக்கிரம்` no longer gains the earlier review's first-person plural `let's leave`.
- the elliptical `மாப்புள்ளே நீ சொன்ன படியெல்லாம் கேட்டிரு` no longer supplies an unstated `she`; its uncertainty is documented in the translation note.

### Scene 7 review decisions

- begging and prostitution remain explicit.
- Gunasekaran's irony about Tamil Nadu's `first voice` remains intact.
- `சரிதாம்போ` is kept non-specific rather than adding a kinship address not explicit in the source.
- `பிள்ளைக் குட்டிக்காரன்` is `I have children`; the earlier contextual addition `to feed` was removed.
- Jolly's social/moral vocabulary and code-switches remain source-led rather than modernized.

### Scene 8 review decisions

- `parasakthi-song-003` / `ஓ ரசிக்கும் சீமானே` remains one verified semantic-poetic unit across PDF **11→12**.
- the compressed third stanza around `பெண்களின் வாழ்க்கையை இழந்தவர்கள் கோடி` remains deliberately unsmoothed.
- the closing stage direction now explicitly retains `விழுந்து` (`falls`) before Thangappan's death.

### Scene 9 review decisions

- the entire Gunasekaran monologue remains one verified cross-page unit across PDF **12→13**.
- `english_page_segments` still preserve the source break `நெஞ்சிலே / நஞ்சைக்`.
- anomalous `வங்கத்திலே` remains untouched in Tamil; English stays context-neutral as `in this land`.
- the unclear `தகுதி? போக்கியதை?` remains explicitly documented rather than over-resolved.
- `காலையிலே` is now `this morning`; the earlier `all morning` added duration not present in the source.

### Scene 10 review decisions

- `பெட்டிலே` remains contextually rendered as hospital `bed`, with the Tamil unchanged.
- the opening bombing direction is kept broad and does not invent a specific injury.
- grief/hospital dialogue remains source-linked and rhetorically direct.

## Next activity

Create the next source-linked English translation batch for canonical **scenes 11–15** at `review` status, using the same schema and immutable-source discipline. Only after that batch exists should its own deliberate second-pass review begin.
