# மருதநாட்டு இளவரசி — Whole-work English reconciliation

Result: **PASS — ENGLISH COMPLETE-VERIFIED**

## Whole-work coverage

- derivative units: **10/10** — unnumbered opening + source scenes 2–10;
- English translation units: **228**;
- immutable dialogue links: **208/208 exactly once**;
- non-dialogue source-linked units: **20**;
- translation unit IDs unique: **228/228**;
- missing / duplicate dialogue links: **0 / 0**;
- inferred source-unlabelled speakers: **0**;
- retained performance translation units: **0**, consistent with the Phase 8 zero-item gate.

## Unit composition

- dialogue: **208**;
- stage direction / setting: **14**;
- written text: **2**;
- narrative: **1**;
- source-unlabelled chant: **1**;
- structural separators: **2**.

## Cross-page reconciliation

Exactly five English units carry multi-page provenance, matching the five immutable multi-page dialogue records:

- `maruthanattu-ilavarasi-en-s003-u014`;
- `maruthanattu-ilavarasi-en-s007-u020`;
- `maruthanattu-ilavarasi-en-s008-u031`;
- `maruthanattu-ilavarasi-en-s008-u049`;
- `maruthanattu-ilavarasi-en-s010-u003`.

Result: **5/5 exact**.

## Source ownership checks

- every dialogue unit links one immutable dialogue ID;
- all 208 immutable dialogue IDs are used exactly once and in source segment order;
- non-dialogue units have no invented speaker or dialogue ID;
- all 20 non-dialogue source locators are unique;
- source scene numbers remain `null, 2–10`; no synthetic Scene 1 was introduced;
- the final `★` remains structural and produces no synthetic `(Scene ends.)` prose.

## Content-integrity checks

- empty translations: **0**;
- placeholder/TODO/TBD text: **0**;
- synthetic scene-end text: **0**;
- performance/song units invented after the zero-item gate: **0**;
- provenance outside PDF 2–22 / printed 1–21: **0**;
- upstream canonical/scene/dialogue/character/Phase-8 mutations caused by reconciliation: **0**.

## Gate result

**Phase 9 English translation CLOSED / COMPLETE-VERIFIED.**

## Next activity

Begin **Phase 14 whole-work reader/export layer**. Build deterministic Markdown, standalone HTML, machine-readable JSON, QA report and integrity manifest from the verified structured records. The reader builder must render every one of the 228 verified translation units exactly once and must re-check 208/208 immutable dialogue links, 5/5 cross-page units, source order and absence of synthetic content.
