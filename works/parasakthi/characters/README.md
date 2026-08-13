# பராசக்தி — character index

**Stage:** structured derivatives  
**Authority:** completed 642-record dialogue index  
**Status:** complete-verified

This directory maps the booklet's exact dialogue `speaker_label` values to stable character/entity identifiers. It is a separate derivative layer: **no dialogue record is rewritten, normalized, or relabelled**.

## Files

- `schema.json` — entity/mapping schema.
- `labels-inventory.json` — complete inventory of all exact speaker labels in the 642 dialogue records.
- `entities-pilot.json` — preserved first evidence-backed pilot.
- `entities.json` — complete character/role/collective disposition for all 69 exact source labels.
- `index.json` — final character-index checkpoint.

## Final coverage

The completed dialogue layer contains **642 records across 46 observed scenes** and **69 distinct exact `speaker_label` strings**. The character layer now has an explicit disposition for **69/69 labels**:

- **48 entities** total;
- **46 verified entities**;
- **1 review entity**;
- **1 unresolved entity**;
- **66 labels** attached to verified entities;
- **1 review label** — `ராக`;
- **2 unresolved labels** — `நொண்டி`, `நொ`;
- **0 unmapped labels**.

`complete-verified` means coverage and provenance are complete and checked; it does **not** mean uncertain identities were guessed into certainty.

## Mapping policy

1. The exact `speaker_label` inside `dialogues/records/` is immutable.
2. Multiple exact variants are merged only when source context supports the identity.
3. Similar spelling alone is not enough to merge labels.
4. Generic labels may be represented as `role` or `collective` entities. Where a label such as `ஒரு`, `வந்த`, or `மற்ற` is reused for different unnamed people, the entity represents the **source role-label category**, not one continuing person.
5. Ambiguity remains explicit. `நொண்டி` / `நொ` are not merged into ஞானசேகரன் even though later narrative continuity strongly suggests that identity, because the source never explicitly names the role in scene 37.
6. `supporting_records` are representative evidence anchors, not exhaustive utterance lists.
7. `scenes` is the union of scenes containing the mapped exact labels.

## Important evidence decisions

- `குரல்` → **குணசேகரன்**: scene 43 explicitly places the voice behind the goddess image and immediately has Gunasekaran emerge from that position.
- `நாரா` → **நாராயணப் பிள்ளை**: scene 30 explicitly gives `ஜெனரல் மெர்ச்சண்ட் நாராயணப் பிள்ளை`.
- `காந்` / `காந்தா` → **காந்தா**; `பார்` / `பார்வதி` → **பார்வதி**; `கருப்` → **கருப்பன்**; `குப்` → **குப்பன்** through direct recurring address/context.
- `நீதி` remains a **judge role** rather than being globally merged into சந்திரசேகரன். Scene 47 establishes that Chandrasekaran wrote Kalyani's judgment, but the source does not explicitly identify every `நீதி` occurrence—especially the later Gunasekaran hearing—as the same person.
- `டாக்டர்` / `டாக்`, `வியாபாரி` / `வியா`, `வீட்டுக்` / `வீட்`, and `பிச்சை` / `பிச்` are occupational-role categories; grouping their label forms does not assert one individual across unrelated scenes.
- `1வது` vs `1—வது` and `2வது` vs `2—வது` remain separate scene-specific ordinal roles; punctuation variants were not merged by appearance alone.
- `ராக` maps to **இராகவன்** at `review` / medium confidence because the printed source gives the vocative `இராகவா`; the nominative display form is a grammatical normalization.
- `நொண்டி` / `நொ` remain an explicit unresolved entity.

## Dialogue integrity

The character index only points back to the 642 dialogue records. It does not add normalized speaker names to those records and does not alter their Tamil, punctuation, scene provenance, or page provenance.

## Next activity

With scene, dialogue, and character derivatives complete, proceed to the **per-song authorship gate**. The booklet credits multiple song/lyric contributors, so identify each song/verse block and resolve authorship from the printed credits or separately cited reliable evidence before creating song-specific derivative files or translations.
