# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

Current stage: **English translation in progress — canonical scenes 1–10 verified; scenes 11–15 in review**.

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

## Verified English coverage — scenes 1–10

Scenes **1–10** have passed deliberate second-pass review.

- scenes verified: **1–10**
- verified units: **136**

The scenes 6–10 review gate was completed **before** scenes 11–15 were created. The durable review checkpoint is `250f4ae975722c5d1a6dedb9a5dc81a783c3fedd`; comparison with the pre-review handover checkpoint showed modifications only within the English translation directory.

English-only review refinements in scenes 6–10 included:

- scene 6: removing an unsupported `let's` and an unstated `she` from elliptical source lines;
- scene 7: removing an unstated kinship address and the added phrase `to feed`;
- scene 8: restoring source action `விழுந்து` in English and retaining the song's compressed syntax;
- scene 9: changing `all morning` to `this morning` while keeping source anomalies explicitly documented;
- scene 10: retaining contextual hospital `bed` for `பெட்டிலே` in English only and avoiding invented bombing injuries.

No canonical Tamil or immutable structured source derivative was changed.

## Scenes 11–15 — current review batch

New review units: **88**.

Per-scene counts:

- scene 11 — **3**: 2 dialogue + 1 stage direction;
- scene 12 — **10**: 7 dialogue + 2 stage directions + 1 song;
- scene 13 — **32**: 26 dialogue + 6 stage directions;
- scene 14 — **19**: 16 dialogue + 3 stage directions;
- scene 15 — **24**: 16 dialogue + 6 stage directions + 2 songs.

Cumulative translation state:

- scenes started: **1–15**
- scenes verified: **1–10**
- scenes in review: **11–15**
- translation units: **224**
- verified: **136**
- review: **88**
- kinds: **176 dialogue / 42 stage direction / 6 song / 0 quoted verse**
- cross-page translation units: `parasakthi-en-s001-u004`, `parasakthi-en-s008-u002`, `parasakthi-en-s009-u001`, `parasakthi-en-s013-u028`, `parasakthi-en-s015-u023`

### Review-sensitive decisions in the current batch

- **Scene 11:** preserve unusual `வில்லுக்கொத்து போல`; verify the English handling of Kalyani's cash and sold jewellery without rewriting the Tamil.
- **Scene 12:** `parasakthi-song-004` / `பூமாலை` remains semantic-poetic; `வந்தேன் தவழ்ந்தாய்?`, `பாரான`, `தாலி அறுத்தவர்கள்`, and `தாசில் உத்தியோகம்` remain explicitly review-sensitive.
- **Scene 13:** preserve Marwari-shop dialect/code-switching without caricature; preserve `தம்பி முறை` kinship wordplay; keep d023 one PDF 16→17 unit; do not repair fragmentary d024.
- **Scene 14:** review `மாப்கரோஜ்` / `ரோஜ்` sound-play and `நாணயம்` as creditworthiness/reliability.
- **Scene 15:** retain unexplained `பாரா-2` transparently; preserve the Mariamman ritual image and Gunasekaran's social rhetoric; keep `parasakthi-song-005` and `parasakthi-song-006` as separate source occurrences even though both belong to soundtrack track 1.

## Exact next work

Perform the second-pass fidelity/editorial review of all **88 units in scenes 11–15**:

1. verify ordering and source links against `scenes/scene-11.md` through `scene-15.md`;
2. verify all dialogue IDs, exact labels and page provenance against `dialogues/records/scene-11.json` through `scene-15.json`;
3. verify stage-direction locators and ensure no action was invented;
4. verify `parasakthi-song-004`, `parasakthi-song-005` and `parasakthi-song-006` against the verified Tamil track derivatives and song inventory;
5. review each documented pressure point without normalizing the Tamil;
6. alter English only when the review identifies a genuine translation problem;
7. if accepted, mark scenes 11–15 and all 88 units `verified`;
8. synchronize translation/status manifests and handovers;
9. compare the resulting HEAD against the current checkpoint to confirm source/Tamil derivative immutability;
10. only then begin canonical **scenes 16–20**.

## Overall status

- Structural mapping: verified
- Canonical Tamil: verified
- Tamil fidelity audit: complete
- Scene/dialogue/character/song Tamil derivatives: complete as documented above
- English translation: **in-progress-review — scenes 1–15 / 224 units / scenes 1–10 verified / scenes 11–15 review**
