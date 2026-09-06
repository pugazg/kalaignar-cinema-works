# அம்மையப்பன் — English batch review: scenes 26–30

**Batch:** archival scenes `ammaiyappan-s026`–`ammaiyappan-s030`  
**Status:** **verified**  
**Source basis:** frozen 105/105 verified Tamil + 63/63 verified scene derivatives + closed dialogue/source-role/character/song evidence

## Batch result

Archival scenes **26–30** are translated and source-reconciled without changing canonical Tamil, scene text, dialogue evidence, character/entity evidence or the closed song/performance inventory.

- scenes verified: **5/5**
- translation units: **130/130 verified**
- dialogue-kind units: **110**
  - immutable explicit dialogue records linked: **107/107**
  - source-role supplement records linked: **3/3**
- stage/action units: **20**
- song-reference / literary-verse / japa / written-text units: **0**
- cross-page units: **5** — `ammaiyappan-en-s026-u012`, `ammaiyappan-en-s027-u023`, `ammaiyappan-en-s029-u022`, `ammaiyappan-en-s029-u036`, `ammaiyappan-en-s030-u008`
- retained song/performance occurrences encountered: **0**
- duplicate source ownership introduced: **0**
- source-visible structural stars translated as prose: **0**

## Scene reconciliation

| Scene | Explicit dialogue links | Source-role supplements | Stage/action | Total units | Result |
|---|---:|---:|---:|---:|---|
| 26 | 13 | 0 | 3 | 16 | PASS |
| 27 | 25 | 2 | 11 | 38 | PASS |
| 28 | 11 | 0 | 1 | 12 | PASS |
| 29 | 42 | 0 | 1 | 43 | PASS |
| 30 | 16 | 1 | 4 | 21 | PASS |
| **Total** | **107** | **3** | **20** | **130** | **PASS** |

## Live source-role correction to the stale handoff assumption

The prior scene-25 handoff text said the closed source-role layer had no supplements in scenes 26–30. Live `main` is authoritative, and direct inspection of `dialogues/source-role-resolved-records.json` showed that statement was stale. This batch therefore correctly includes the three already-closed supplements:

- `ammaiyappan-s027-r001` — Muthan's unlabelled sarcastic answer after `[சிரிக்கிறார்கள்]`;
- `ammaiyappan-s027-r002` — Tirisangu's `மானங்கெட்ட பெண்ணே!` immediately after his arrival cue;
- `ammaiyappan-s030-r001` — Velazhagan's unlabelled threat after he pushes Muthan into the prison.

All three retain `speaker_label_origin: source-context-attributed`; none is promoted into a printed colon-labelled record. No source evidence file was changed.

## Cross-page continuity

Five immutable source records remain single English units with full page provenance:

- scene 26 `ammaiyappan-s026-d010`: PDF **55 → 56** / printed **53 → 54**;
- scene 27 `ammaiyappan-s027-d017`: PDF **57 → 58** / printed **55 → 56**;
- scene 29 `ammaiyappan-s029-d022`: PDF **61 → 62** / printed **59 → 60**;
- scene 29 `ammaiyappan-s029-d035`: PDF **62 → 63** / printed **60 → 61**;
- scene 30 `ammaiyappan-s030-d007`: PDF **64 → 65** / printed **62 → 63**.

Each has one logical owner and `english_page_segments`; no page-boundary duplication was introduced.

## Scene 26 — political metaphor and frozen irregularity

Muthan's refusal to march preserves the source's honeycomb/fire-forest, flower-garden/storm and tiger/deer political imagery. `ammaiyappan-s026-d010` remains whole across PDF 55→56. The frozen `தோற்ப்பும்வரை` in `d011` is not silently repaired; the English follows the immediate marching context and records that decision in a note.

## Scene 27 — mixed ownership and source-context speech

The street confrontation preserves the exact source-label layer and two context-attributed supplements. `ammaiyappan-s027-d022` remains one immutable Velazhagan-labelled unit even though the frozen text contains the slap cue and additional `முத்தாயி? அத்தான்!...` tokens. The English does not reassign those tokens to a guessed speaker. Muthan's long freedom speech remains one cross-page record, including the source's marriage-fragrance / corpse-stench contrast.

## Scene 28 — accusation register

The Muthayi–Sumathi quarrel preserves exact label variants and the bitter money accusation. `கூறு போட்டு விட்டாயே எங்கள் காதல்` is translated as cutting their love to pieces, while `கிடைத்ததை வாயில் போட்டுக் கொண்டாய்` retains the accusation that Sumathi swallowed/kept what she received. No source wording is normalized.

## Scene 29 — dream, ritual vocabulary and embedded actions

The Sukhadev/Tirisangu/Vedalam sequence preserves ornamental dream language, `ottiyanam`, `thali`, `guru-puja`, Palayakkarar/Yuvraj/Kumar Raj register and the frozen comic irregularity `அவள் உங்க அப்பா...அதனால்!` without repair. Source-owned `(கொடுக்கிறான்)` and `[அழுகிறாள்]` remain inside their immutable dialogue records. Two cross-page records remain whole.

## Scene 30 — Purananuru poem inside immutable dialogue ownership

Muthan explicitly introduces a poem on the mothers of `புறநானூறு`. The complete printed passage belongs to `ammaiyappan-s030-d007`, so the English keeps it as **one dialogue unit** using semantic-poetic translation rather than manufacturing a separate literary-verse record. No external Purananuru text, title or attribution is imported. Dense frozen forms are handled only from immediate source context; `மதுவும் சுருவும்` is not silently normalized and is retained as `maduvum / suruvum` where necessary.

The later `மாங்குயில் கூவிடும் பூஞ்சோலை...` revolutionary-poetry fragment also remains inside its explicit Muthan dialogue record; it is translated only as printed and not externally expanded or attributed. Velazhagan's final unlabelled threat is linked through the already-closed `ammaiyappan-s030-r001` supplement.

## Song / verse / performance gate

The closed source-only song/performance inventory retains occurrences only in archival scenes **7, 10, 19, 40 and 59**. Scenes **26–30** therefore introduce **0** song/performance occurrence links. Scene 30's self-described poem remains dialogue-owned source text and does not alter the closed song/performance inventory.

## Integrity result

**PASS.** All **107** eligible explicit dialogue records and all **3** closed source-role supplements in scenes 26–30 are linked exactly once; source-bounded action is owned once; all five cross-page records remain whole; no frozen Tamil/dialogue/character/song file was modified.

**Next batch:** archival scenes **31–35**. The closed source-role layer contains **one** supplement in that range — `ammaiyappan-s035-r001`; the closed song/performance inventory contains **no retained occurrence** in scenes 31–35. Preserve exact speaker/page provenance and do not modify frozen source evidence.