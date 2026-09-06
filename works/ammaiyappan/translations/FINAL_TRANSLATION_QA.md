# அம்மையப்பன் — Final English translation reconciliation

Status: **PASS — English translation complete and source-linked**

This checkpoint closes the English translation layer for all **63 archival scene derivatives** of `அம்மையப்பன்`. The booklet itself prints no scene numbers; archival scene IDs remain navigation derivatives only.

## Final corpus census

- archival scene derivatives translated and verified: **63 / 63**
- verified English units: **1,210 / 1,210**
- dialogue-kind English units: **1,025**
  - immutable explicit colon-labelled dialogue records linked: **1,009 / 1,009**
  - closed source-role supplement records linked: **16 / 16**
- stage/action units: **181**
- standalone song-reference units: **3**
- japa units: **1**
- standalone literary-verse units: **0**
- written-text units: **0**
- genuine cross-page English units: **28**
- unique retained song/performance occurrences linked: **5 / 5**
- source-visible structural stars translated as prose: **0**
- canonical Tamil changes caused by English: **0**
- scene/dialogue/character/song evidence changes caused by English: **0**

The final dialogue census exactly matches the closed source authority: **1,009 explicit records + 16 source-role supplements = 1,025 downstream dialogue units**.

## Whole-work linkage reconciliation

PASS:

- all 63 translation scene records exist from `translations/records/scene-001.json` through `scene-063.json`;
- all 1,009 immutable explicit dialogue records are linked exactly once across the completed English layer;
- all 16 closed source-role supplements are linked exactly once and retain their original provenance (`source-context-attributed` or source-explicit non-colon delimiter as applicable);
- no source-role supplement is promoted into a printed colon label;
- scene 3 `பூங் ; ...` and scene 5 `திரு; ...` preserve their exact non-colon source provenance;
- all 181 separately owned stage/action spans remain source-bounded rather than being converted into dialogue;
- all 28 genuine cross-page English units remain one logical unit with multi-page provenance where required;
- no archive scene ordinal is presented as a source-printed scene number;
- decorative `★` / `* * *` remains structural and is never turned into invented prose.

## Song / verse / performance reconciliation

The closed source-only inventory contains exactly five retained occurrences, and all five are represented in the completed English layer:

1. `ammaiyappan-song-001` — scene 7 — Muthan–Muthayi love-song performance nearing its end; no printed title or lyric body.
2. `ammaiyappan-song-002` — scene 10 — source-attributed Kambar literary fragment inside immutable Sukhadev dialogue; no external reconstruction.
3. `ammaiyappan-song-003` — scene 19 — source-visible cue that Muthan is singing; no printed title or lyric body.
4. `ammaiyappan-song-004` — scene 40 — Sukhadev's `முத்தாயி` japa/performance cue; represented as character japa, not soundtrack authorship.
5. `ammaiyappan-song-005` — scene 59 — Muthan requests the lovers' old song and a separate cue shows Muthayi singing through tears as he walks toward the gallows; no printed title, lyric body or authorship.

English does not merge unnamed song identities without stronger source evidence, does not reconstruct absent lyrics, and does not upgrade the booklet's `கதை வசனம் / மு. கருணாநிதி` credit into lyric authorship.

The long Purananuru-related poem in scene 30 and the short closing stanza in scene 63 remain inside their immutable dialogue records because that is where the verified source ownership lies. Neither is split merely for schema neatness, and no external literary text is imported.

## Source-irregularity and register safeguards retained

Across the completed layer:

- frozen or uncertain Tamil forms are handled by bounded context, transliteration or translator notes rather than silent upstream correction;
- source rhetoric around caste/class, religion, sexuality, coercion, political liberation and social satire is not euphemized;
- kinship/register terms such as `Aththan`, cultural/religious terms such as `japa`, `nishta`, `tandava`, and other source-significant forms are retained where ordinary English would erase source force;
- exact Tamil speaker labels remain metadata authority even when character/entity resolution supplies English context;
- mixed-content immutable dialogue records keep embedded action, verse, address cues or internal irregularities inside the source-owned record.

## Final scenes 61–63

The final batch contributes **22 verified units**: **16 explicit dialogue + 6 stage/action**, with no source-role supplements, no retained song/performance occurrence and no new cross-page unit.

- scene 61 remains action-only; the rescue/mistaken-prisoner sequence creates no invented speech;
- scene 62 preserves the source's masked-prisoner revelation, Sukhadev's halting explanation, Maappillaithaasar's atonement speech and the final parallel `speech ends; life ends` action without external expansion;
- scene 63 preserves the mother-recognition sequence, `Aththan` / `Amma` register shifts, the liberation rhetoric, the embedded closing stanza and the frozen `அண்ணலின் விலங்கொடிப்ப ோம்` pressure point without changing Tamil evidence.

Detailed batch QA is in `BATCH_061_063_REVIEW.md`.

## Validation scope

This **PASS** is a whole-work source/linkage and count reconciliation based on the frozen source authority, completed translation records and batch QA. It does **not** claim an executable JSON-schema validator or CI run unless such a validator/check is separately executed and recorded.

## Disposition

**PASS — English translation is complete-verified at 63/63 scenes and 1,210 units.**

The next production phase is **whole-work English reader/export preflight**, generated from the verified structured translation rather than maintained as an independent manual copy. Reader work must preserve archival scene IDs as navigation only, exact source provenance, all five source-visible occurrence links, and the completed 1,025-unit dialogue authority.
