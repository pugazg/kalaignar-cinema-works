# Parasakthi — English translation layer

**Canonical authority:** verified Tamil transcription and immutable structured derivatives  
**Target language:** English (`en`)  
**Status:** in progress — scenes **1–15 verified**

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

## Verified coverage — scenes 1–15

Scenes **1–15** have now passed deliberate second-pass review: **224 verified units**.

Cumulative verified state:

- scenes started: **1–15**;
- scenes verified: **1–15**;
- scenes in review: **none**;
- translation units: **224**;
- verified: **224**;
- review: **0**;
- kinds: **176 dialogue / 42 stage direction / 6 song / 0 quoted verse**.

### Scenes 6–10 review checkpoint

The scenes 6–10 pass reviewed all **66 units** against canonical scene files, immutable dialogue records, page provenance and the verified scene-8 song derivative. English-only corrections were made where the review found genuine additions, omissions or over-resolution; no Tamil/source file was changed.

Review refinements included:

- scene 6: `புறப்படு சீக்கிரம்` no longer gains `let's`; the elliptical `நீ சொன்ன படியெல்லாம் கேட்டிரு` no longer gains an unstated `she`;
- scene 7: `சரிதாம்போ` no longer gains an unstated kinship address, and `பிள்ளைக் குட்டிக்காரன்` no longer gains `to feed`;
- scene 8: the closing stage direction again includes the source action `விழுந்து` (`falls`); the compressed third stanza of `ஓ ரசிக்கும் சீமானே` remains unsmoothed;
- scene 9: `காலையிலே` is `this morning`, while anomalous `வங்கத்திலே`, unclear `தகுதி? போக்கியதை?`, and the PDF 12→13 break remain explicitly documented;
- scene 10: hospital `பெட்டிலே` remains contextually `bed` in English only, and the bombing direction stays broad rather than inventing an injury.

### Scenes 11–15 review checkpoint

The second pass reviewed all **88 units** in scenes 11–15 against the verified scene derivatives, immutable dialogue records, page provenance, and the verified Tamil song derivatives for `பூமாலை` and `தேசம் ஞானம் கல்வி`.

English-only refinements made during this review:

- **scene 13:** `திண்ணை` is rendered consistently as `raised veranda`; the awkward literal `merit a cow has` was tightened to `good fortune a cow has` while keeping the source metaphor;
- **scene 14:** an added English endearment was removed from `அதெல்லாம் முடியாதம்மா`; `நாணயம்` is expressed naturally through trustworthiness/creditworthiness rather than as `coin`;
- **scene 15:** `மண்ணைப் போச்சே` is rendered idiomatically as `gone to waste`; standalone stage directions avoid the misleading modern English age-sense of `minors` for `மைனர்கள்`, while exact Tamil labels remain immutable metadata.

No English smoothing was allowed to erase source pressure points. The following remain explicitly documented:

- scene 11 `வில்லுக்கொத்து போல` and the compressed cash/jewellery account;
- scene 12 `வந்தேன் தவழ்ந்தாய்?`, difficult `பாரான`, the tali image, and `தாசில் உத்தியோகம்`;
- scene 13 Marwari-shop dialect, `நீப்பன்—`, kinship wordplay, cross-page d023 pronoun instability, and fragmentary d024;
- scene 14 `மாப்கரோஜ்` / `ரோஜ்` sound-play;
- scene 15 unexplained `பாரா-2`, the Mariamman earth-flinging image, Gunasekaran's social monologue, and the two separately preserved song occurrences from soundtrack track 1.

## Song representation through scene 15

- Scene 12 `parasakthi-song-004` / `பூமாலை` remains one verified semantic-poetic unit on PDF 14.
- Scene 15 `parasakthi-song-005` (`குதம்பாய்`, PDF 19→20) and `parasakthi-song-006` (`தாண்டவக்கோனே`, PDF 20) remain two verified translation units because the verified Tamil derivative preserves them as distinct source occurrences, even though soundtrack evidence places both inside one composition.

## Next activity

Create the next source-linked English batch for canonical **scenes 16–20** at `review` status, preserving the same schema and immutable source-linking rules. After that batch is created, perform a deliberate second-pass review before verification.
