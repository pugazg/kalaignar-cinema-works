# Parasakthi — English Translation Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-14

This document is the continuation entry point for a new chat. Read it before doing any translation work.

## 1. Current English state

The Tamil/source archive and non-English structured derivatives remain complete and immutable. The active derivative is English translation.

- scenes started: **1–22, 24–25**
- scenes verified: **1–20**
- scenes in review: **21, 22, 24, 25**
- canonical scene **23 is absent and has no translation record**
- translation units: **407**
- verified units: **311**
- review units: **96**
- kinds: **333 dialogue / 67 stage-direction / 7 song / 0 quoted-verse**
- status: **`in-progress-review`**

The exact next activity is a deliberate second-pass review of all **96 units** in observed scenes **21, 22, 24 and 25**. Do not begin the next translation batch until this review is complete.

## 2. Completed review gates

- scenes 6–10: **66/66** second-pass verified;
- scenes 11–15: **88/88** second-pass verified;
- scenes 16–20: **87/87** second-pass verified.

English remains an interpretive derivative. No completed review has modified canonical Tamil, scene derivatives, dialogue records, character mappings, song inventory or Tamil song derivatives.

## 3. New review batch — observed scenes 21–25

The source-linked batch has now been created at `review` status. Canonical scene **23 is absent and was not invented**.

Per-scene counts:

- scene 21 — **44** units: 40 dialogue + 4 stage directions;
- scene 22 — **16** units: 11 dialogue + 5 stage directions;
- scene 24 — **7** units: 6 dialogue + 1 stage direction;
- scene 25 — **29** units: 26 dialogue + 3 stage directions.

Batch total: **96 units** — **83 dialogue + 13 stage directions**. The verified song inventory has no song or quoted-verse occurrence in these four scenes.

### Scene 21 review pressure points

- Venu's rice/wheat discussion develops into a double meaning around being alone versus paired; do not flatten it into ordinary food advice.
- Preserve `மூச்சிக்கு முப்பத்திரண்டு` as the source's numerical hyperbole.
- Preserve the kinship progression `அண்ணா / மாமா / அத்தான்`; current English retains `mama` and `athan` rather than falsely mapping each to one English relation.
- The source's predatory `கருநாகம்`, `கனி`, and `செவ்விதழைச் சுவைக்க` imagery is retained as source framing; do not add action beyond the text.
- `parasakthi-s021-d040` has a known source-label punctuation anomaly (`கல் !`); exact label metadata remains unchanged.

### Scene 22 review pressure points

- Stage directions use `young men` for `மைனர்கள்` to avoid the modern English age/legal sense of `minors`; exact Tamil labels remain immutable.
- `ஒட்டையை வீணு அலட்டிக்கிட்டே?` is colloquial and should not be over-normalized.
- `கள்ளப்புருஷன்` must retain the defamatory accusation that provokes Gunasekaran.
- Preserve the paired rhetoric `சந்தர்ப்பம் ... சமுதாயம் ...` in Gunasekaran's widowhood line.

### Scene 24 review pressure point

The source says Chandrasekar asked `them` to come and then immediately says `we'll leave tomorrow`. The current English preserves that sequence rather than silently reconciling the travel logic.

### Scene 25 review pressure points

- Preserve the black-market satire and the source's jarring `கன்னிப் பொண்ணு` comparison.
- Preserve the tali/`black` rhetoric without converting it into an external economic explanation.
- `நூல்` is a deliberate thread/book homonym. Current English retains `nool` until C.G.T. explicitly resolves the joke.
- `parasakthi-s025-d011` and `parasakthi-s025-d017` have explicit source speaker prefixes without the usual colon; exact label metadata remains unchanged.
- Kalyani's `ஏதாவது` request trails off and remains incomplete in English.

## 4. Canonical/source state — immutable

- source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- 58 PDF pages; canonical dialogue/song range PDF **4–57** / printed pp. **3–56**
- canonical Tamil: **54 verified / 0 review / 0 unresolved markers**
- observed scene headings: **46**
- headings **23 and 34 are absent**
- dialogue index: **642 complete-verified records**
- song authorship: **14/14 verified**
- Tamil soundtrack derivatives: **11/11 complete-verified**, plus one separate quoted-verse derivative

Critical rule: English translation must never repair, normalize or overwrite the Tamil source. Do not use film audio, subtitles, web copies, later editions or memory to change canonical Tamil.

## 5. Translation rules

1. Tamil remains authoritative.
2. Every English unit remains source-linked with scene, record/occurrence where available, and PDF/printed-page provenance.
3. Exact Tamil speaker labels remain immutable metadata.
4. Stage directions gain no invented action.
5. Preserve repetition, questions, metaphors, code-switching, social vocabulary and rhetorical force where meaningful.
6. Songs are semantic-poetic translations, not singable rewrites.
7. Never invent song occurrence boundaries or authorship.
8. Cross-page source units remain one translation unit.
9. Unlabelled canonical material may be source-located directly; do not manufacture dialogue IDs merely to fit the index.
10. Interpretive choices and unresolved source forms belong in `translation.notes`.

## 6. Exact next activity

Second-pass all **96 review units** in:

- `works/parasakthi/translations/records/scene-21.json`
- `scene-22.json`
- `scene-24.json`
- `scene-25.json`

Review each unit against its verified canonical scene text, immutable dialogue record, exact speaker label and page provenance. Check the pressure points above. Change **English only** where a genuine translation problem is found.

If the pass succeeds, mark all 96 units and the four scene records `verified`, synchronize all status surfaces, and compare the resulting HEAD against the pre-batch checkpoint to confirm source/Tamil immutability. **Only then begin the next batch.**

## 7. Continuation prompt

> Read `docs/HANDOVER_PARASAKTHI_ENGLISH_TRANSLATION.md` and continue exactly from there. Second-pass all 96 English units in scenes 21, 22, 24 and 25; scene 23 is absent and must not be invented. Do not begin the next batch until the review is complete.
