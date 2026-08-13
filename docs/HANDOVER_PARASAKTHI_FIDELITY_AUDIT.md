# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

Current stage: **English translation in progress — canonical scenes 1–15 verified; no English units currently in review**.

## Canonical/source state — immutable

- Source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- 58 PDF pages; PDF 4–57 / printed pp.3–56 are canonical dialogue/song pages; PDF 58 is back matter.
- Canonical Tamil: **54 verified / 0 review / 0 unresolved markers**.
- Scene derivatives: **46/46 complete**; headings 23 and 34 are absent.
- Canonical scene 43 retains source heading 48; canonical final scene 48 retains source heading 43.
- Dialogue index: **642 complete-verified records**.
- Character index: **69/69 labels disposed across 48 entities**; `ராக` remains review and `நொண்டி` / `நொ` unresolved.
- Song authorship: **14/14 verified**.
- Tamil soundtrack derivatives: **11/11 complete-verified**, plus one separate Bharathidasan quoted-verse derivative.

Never use English translation, film audio, subtitles, web copies or later editions to repair the Tamil source.

## Translation files

- `works/parasakthi/translations/README.md`
- `works/parasakthi/translations/schema.json`
- `works/parasakthi/translations/index.json`
- `works/parasakthi/translations/records/scene-01.json` through `scene-15.json`

Translation rules:

- Tamil remains authoritative.
- Every English unit is source-linked.
- Exact Tamil `speaker_label` values remain immutable metadata.
- Stage directions may not gain invented action.
- Dialogue keeps rhetorical force, repetition, code-switching and social/political language where meaningful.
- Songs are semantic-poetic translations, never singable rewrites unless a separate future derivative explicitly says so.
- Cross-page source records remain one translation unit where the source record is one unit.
- English statuses (`draft`, `review`, `verified`) are independent from Tamil verification.

## Verified English coverage — scenes 1–15

Scenes **1–15** have passed deliberate second-pass review.

- scenes verified: **1–15**
- verified units: **224**
- review units: **0**
- kinds: **176 dialogue / 42 stage direction / 6 song / 0 quoted verse**
- cross-page translation units: `parasakthi-en-s001-u004`, `parasakthi-en-s008-u002`, `parasakthi-en-s009-u001`, `parasakthi-en-s013-u028`, `parasakthi-en-s015-u023`

### Scenes 6–10 review checkpoint

The scenes 6–10 review gate was completed **before** scenes 11–15 were created. The durable review checkpoint was `250f4ae975722c5d1a6dedb9a5dc81a783c3fedd`.

English-only refinements in scenes 6–10 included:

- scene 6: removing an unsupported `let's` and an unstated `she` from elliptical source lines;
- scene 7: removing an unstated kinship address and the added phrase `to feed`;
- scene 8: restoring source action `விழுந்து` in English and retaining the song's compressed syntax;
- scene 9: changing `all morning` to `this morning` while keeping source anomalies explicitly documented;
- scene 10: retaining contextual hospital `bed` for `பெட்டிலே` in English only and avoiding invented bombing injuries.

### Scenes 11–15 review checkpoint

All **88 units** in scenes 11–15 were reviewed against canonical scene files, immutable dialogue records, page provenance, and the verified Tamil song derivatives for `parasakthi-song-004`, `parasakthi-song-005` and `parasakthi-song-006`.

English-only refinements made during this pass:

- **scene 13:** `திண்ணை` is rendered consistently as `raised veranda`; the literal `merit a cow has` was tightened to `good fortune a cow has` while preserving the cow metaphor;
- **scene 14:** an added English endearment was removed from `அதெல்லாம் முடியாதம்மா`; `நாணயம்` is expressed through trustworthiness/creditworthiness rather than `coin`;
- **scene 15:** `மண்ணைப் போச்சே` is rendered idiomatically as `gone to waste`; standalone stage directions avoid the misleading modern age-sense of `minors` for `மைனர்கள்` while exact Tamil labels remain immutable.

The following source pressure points remain explicitly documented rather than repaired:

- scene 11 `வில்லுக்கொத்து போல` and the compressed cash/jewellery account;
- scene 12 `வந்தேன் தவழ்ந்தாய்?`, difficult `பாரான`, `தாலி அறுத்தவர்கள்`, and `தாசில் உத்தியோகம்`;
- scene 13 Marwari-shop dialect, `நீப்பன்—`, kinship wordplay, cross-page d023 first-/third-person instability, and fragmentary d024;
- scene 14 `மாப்கரோஜ்` / `ரோஜ்` sound-play;
- scene 15 unexplained `பாரா-2`, the Mariamman ritual image, Gunasekaran's social rhetoric, and the two separately preserved source occurrences within soundtrack track 1.

No canonical Tamil or immutable structured source derivative was changed by either English review pass.

## Exact next work

Create the next source-linked English translation batch for canonical **scenes 16–20** at `review` status:

1. read the verified canonical scene files `scene-16.md` through `scene-20.md`;
2. source-link every dialogue to immutable `dialogues/records/scene-16.json` through `scene-20.json`;
3. preserve exact Tamil speaker labels and page provenance;
4. link any song or quoted-verse occurrences to the verified songs inventory/derivatives;
5. keep cross-page records as single translation units with page segmentation where needed;
6. translate stage directions without adding action;
7. record interpretive choices in notes rather than modifying Tamil;
8. create the batch at `review` status;
9. only after the batch exists, perform a separate deliberate second-pass before verification.

## Overall status

- Structural mapping: verified
- Canonical Tamil: verified
- Tamil fidelity audit: complete
- Scene/dialogue/character/song Tamil derivatives: complete as documented above
- English translation: **in-progress-verified — scenes 1–15 / 224 units / 224 verified / 0 review**
