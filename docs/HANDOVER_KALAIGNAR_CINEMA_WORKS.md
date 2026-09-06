# Kalaignar Cinema Works — Master Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Primary branch: `main`  
Purpose: reusable handover for continuing the archive or onboarding a new Kalaignar cinema work

This document is the **project-level handover**. Work-specific handovers remain useful historical/checkpoint records, but current repository state always takes precedence over an older handover.

For a new work, also read:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` when older Tamil typeforms may occur
3. `docs/ARCHIVAL_WORKFLOW.md`
4. `docs/SOURCE_POLICY.md`
5. `docs/TRANSCRIPTION_GUIDE.md`
6. `docs/STATUS_CONSISTENCY_AUDIT.md`
7. `docs/START_NEW_CINEMA_WORK_PROMPT.md`

---

## 1. Project purpose

This repository is a source-led archive of cinema writing credited to **Kalaignar M. Karunanidhi**, including screenplay/dialogue booklets, songs/verse where source-supported, and downstream structured/translated reader derivatives.

The central rule is simple:

> **The scanned publication controls canonical text for that edition.**

Everything else—scene files, dialogue indexes, character mappings, song attribution, translation, reader exports, EPUB/PDF packages and web presentation—is downstream.

---

## 2. Mature reference implementations

### Parasakthi

Parasakthi demonstrates non-trivial scene-number anomalies, complete Tamil fidelity verification, scene/dialogue/character/song layers, source-linked English translation, whole-work reader QA and preservation of source-unlabelled material outside a simplistic speaker model. Use it for complex numbering and mixed song/verse handling, never as textual authority for another work.

### Tirumbippaar!

Tirumbippaar demonstrates full-scan mapping, 104-page fidelity audit, explicit post-fidelity correction history, immutable 1,040-record dialogue indexing, character mapping without rewriting labels, cautious song authorship, 1,321-unit English translation, whole-work reader reconciliation and deterministic EPUB QA. It also establishes the preference for Reading Room publication over unnecessary duplicate standalone packages.

### Raja Rani

Raja Rani demonstrates old-typeface source review, direct user scan verdicts, late-correction reconciliation through every dependent layer, **79/79 source pages / 70/70 screenplay pages**, **58/58 scene derivatives**, **1,071 immutable dialogue records**, **80/80 exact labels / 44 entities**, **1,236 screenplay English units**, and a separate **11/11 numbered-song / 181 line-cue** English layer. Its whole-work QA caught duplicated derivative ownership across scene 55/56 without changing canonical page text. It is also the clearest precedent for repository-wide anti-staleness synchronization.

---

## 3. Current reusable workflow

For each cinema work, proceed through these gates in order:

1. **Source intake**
2. **Structural mapping**
3. **Canonical Tamil first pass**
4. **Visual fidelity audit**
5. **Historical Tamil glyph audit where applicable**
6. **Scene/source-structure derivatives**
7. **Dialogue index**
8. **Character/entity index**
9. **Song/verse/performance authorship gate**
10. **Tamil song derivative files only where full source text supports them**
11. **English translation, if in scope**
12. **Whole-work reader QA/export**
13. **Reading Room integration**
14. **Optional standalone packaging only when separately useful/requested**

For older print, canonical Tamil is not complete merely because ordinary visual fidelity passes. Follow the historical-glyph guide occurrence by occurrence; never global-replace or modernize spelling merely because an old glyph resembles a modern character.

**Repository-wide status synchronization is a completion gate at every major phase.**

---

## 4. Source authority rules that must survive every handover

Preserve source-supported historical/colloquial spelling, punctuation, exact speaker labels, scene-heading irregularities, repetition, unusual grammar, typographical forms, code-switching, stage directions, song/performance structures and embedded texts.

Do not repair canonical text from OCR, subtitles, film audio, web quotations, later editions, existing translations, memory or familiar dialogue. If the scan does not support a reading, keep uncertainty visible.

For historical Tamil typeforms, **read character identity, not modern visual resemblance**. Encode the proven historical character identity in modern Unicode without modernizing the surrounding source word.

---

## 5. Important lessons learned

### A. Inspect the scan, not the filename
The filename does not establish edition, title-page wording, credits, pagination or exact content bounds.

### B. Map the whole source before transcribing
Whole-source mapping prevents wrong page formulas, missing sections and premature scene assumptions.

### C. Never trust progress metadata without physical coverage
A claimed range is not complete until every underlying page/unit actually exists.

### D. Verified text can still be corrected—but only from source evidence
Record consequential post-verification corrections explicitly and reconcile dependent derivatives before continuing.

### E. Scene numbering may be irregular or absent
Do not invent neat printed numbering. Archive-only navigation IDs must remain derivative metadata.

### F. Unlabelled speech is not labelled dialogue
Context may support a downstream role disposition, but it must not create a printed speaker label in immutable evidence.

### G. Cross-page utterances stay single units
Retain one logical record with multi-page provenance.

### H. Decorative separators are not prose
Never translate `★` into invented scene-ending text.

### I. Do not duplicate derivative ownership
Whole-work QA must detect duplicated source spans across adjacent derivative owners.

### J. Song authorship requires item-level evidence
Story/dialogue credit is not lyric credit.

### K. Distinct source structures need distinct derivative identities
Do not force independently numbered songs or non-scene booklet structures into screenplay scene IDs.

### L. QA should fail loudly
Missing links, duplicate IDs/ownership, order drift, synthetic content and inconsistent provenance should block closure.

### M. Stale shared documents are a project defect
Work-local indexes, `data/works.json`, root README, master handover and status audit must agree before a major phase is closed.

### N. Historical Tamil glyphs require their own pass
At minimum inspect `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`, while remaining alert for edition-specific forms and damaged type.

### O. Source-only performance evidence stays source-only in English
A cue that a song is being sung does not authorize importing absent lyrics. A literary fragment embedded in an immutable dialogue record should be linked to its occurrence evidence without duplicating the same source span as a second translation unit.

---

## 6. Repository architecture and authorities

```text
docs/
  ARCHIVAL_WORKFLOW.md
  SOURCE_POLICY.md
  TRANSCRIPTION_GUIDE.md
  HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md
  CINEMA_WORKS_PROCESSING_GUIDE.md
  HANDOVER_KALAIGNAR_CINEMA_WORKS.md
  STATUS_CONSISTENCY_AUDIT.md
  START_NEW_CINEMA_WORK_PROMPT.md
data/
  works.json
works/<work-id>/
  README.md
  metadata.yaml
  mapping.md
  notes/
  transcription/
  scenes/
  dialogues/
  characters/
  songs/
  translations/
  editions/
```

Authority order for text questions:

1. rendered scan;
2. verified canonical Tamil;
3. verified scene/song/source-structure derivative;
4. immutable dialogue/song/etc. structured records;
5. translation;
6. reader/export/package;
7. website presentation.

A downstream layer must never silently repair an upstream layer.

---

## 7. Repository-wide synchronization gate

At the end of every major phase, reconcile at minimum:

### Work-local
- `works/<work-id>/metadata.yaml`;
- `works/<work-id>/README.md`;
- active layer README/index/QA/audit files;
- work-specific handover and next-chat prompt.

### Repository-wide
- `data/works.json`;
- root `README.md`;
- `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`;
- `docs/STATUS_CONSISTENCY_AUDIT.md`;
- any shared guide whose reusable policy changed.

Then sweep for superseded counts, obsolete blocked/review states and stale next activities. Historical checkpoint files may retain historical numbers when clearly labelled historical.

---

## 8. Translation and reader architecture

For mature screenplay translation:

- use scene-sharded translation records;
- retain stable unit IDs and exact Tamil speaker labels;
- link labelled dialogue to immutable dialogue IDs;
- retain source-role origin for context-attributed supplements without creating printed labels;
- preserve stage directions, written text, chants, performance cues and other source structures distinctly;
- keep page provenance and cross-page logical units intact;
- link song/performance occurrence evidence without duplicating source ownership;
- preserve source irregularity honestly.

Before declaring translation complete, perform whole-work reconciliation rather than trusting batch counts.

Reader/export outputs must be generated from verified structured translation, not manually maintained copies. Non-scene sources such as `மந்திரி குமாரி` must keep their natural model: its reader uses **1 story-summary unit + 15 performance blocks**, not synthetic scenes.

---

## 9. Public Reading Room direction

Preferred public destination:

**`https://nenjukkuneethi.org/read` — Kalaignar Digital Library / Reading Room**

Use each work's natural navigation model, expose verified Tamil/English where supported, preserve page/source provenance and exact source order, and treat search/filter/card metadata purely as presentation. Do not automatically create another PDF/EPUB merely because reader work is complete.

---

## 10. Working style for future chats

When the user says **“Proceed with next activity”** and the next action is already documented:

- continue without redundant questions;
- fetch live `main` first;
- choose a meaningful bounded batch;
- inspect authoritative source/derivative state before writing;
- complete content QA and repository-wide synchronization before claiming the batch complete;
- if a large source read is truncated, fetch the missing range rather than summarizing unseen content;
- report exact commits/checkpoints after writes.

A genuine source ambiguity can justify pausing; routine workflow continuation does not.

---

## 11. Starting a new cinema work

Use `docs/START_NEW_CINEMA_WORK_PROMPT.md`. Normally stop the first new-work activity after source intake, full structural mapping and initial skeleton/status synchronization. If the work already exists, continue its live state instead.

---

## 12. Work-specific handovers

A work-specific handover should preserve repository/branch, source identity/checksum, exact bounds, current phase, closed counts, unresolved items, source anomalies, cross-page cases, authoritative files, immutable layers, exact next activity and startup order.

Older handovers are historical checkpoints and never override newer live `main`.

---

## 13. Current high-level project checkpoint — 2026-09-06

- **Parasakthi** — complete-verified canonical/structured English reader work.
- **Tirumbippaar!** — complete-verified Tamil, structured derivatives, English translation, reader QA and deterministic EPUB QA.
- **Manohara** — complete-verified Tamil, 57/57 scenes, 983 dialogue records, 1,190 English units; reader/export QA PASS; Reading Room ready.
- **Kalaignar Thirai Isai Paadalgal** — 54/54 verified Tamil and English songs; reader/export and Reading Room payload QA PASS; site not applied.
- **Manthiri Kumari** — 12/12 canonical PDF 2–13 pages; 1 story-summary record + 15 performance records; English 13 prose units + 15/15 performances / 52 sections / 234 paired line-cues; bilingual reader and Reading Room payload QA PASS; item-level lyricists remain 0 verified / 15 unresolved; site not applied.
- **Raja Rani** — 79/79 source pages, 70/70 screenplay pages, 58/58 scene derivatives, 1,071 dialogues, 80 labels / 44 entities, 1,236 screenplay English units, 11/11 numbered songs / 181 line-cues; reader and Reading Room payload QA PASS; site not applied.
- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; source-only song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **verified through scene 15/63 / 355 units**; next bounded batch **16–20**.

Current active mirrors use the post-correction 1,025-unit authority and scene-15 English checkpoint.

---

## 14. Raja Rani downstream disposition

No required Raja Rani production work remains in this repository. Its verified Reading Room payload is `works/raja-rani/integrations/reading-room/reading-room.json`, SHA-256 `ab1058cb5a22ba78e68938f50efc586cc53eb07ef544bdf3919bb3c4b8c46c9b`. Apply it only in the separate Reading Room implementation repository when explicitly authorized.

---

## 15. Manthiri Kumari downstream disposition

No required Manthiri Kumari production work remains here. Its verified payload is `works/manthiri-kumari/integrations/reading-room/reading-room.json`, **15,704 bytes**, SHA-256 `20a0db293b936757e7d01def336252f28543337f319dfae6ad7bf5ae886bab43`. Preserve its natural story-summary + 15-performance navigation and unresolved authorship tiers when the separate Reading Room implementation is authorized.

---

## 16. Ammayappan active checkpoint

Work path: `works/ammaiyappan/`  
Source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

- canonical Tamil: **105/105 dual-gate complete-verified**;
- unresolved canonical markers / review pages: **0 / 0**;
- PDF 10 source correction: `மாடம்`, commit `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`;
- scene segmentation: **PASS — 63 boundaries / 63/63 derivatives**;
- distinct current heading forms: **41**;
- boundary ownership: **PASS — 0 gaps / 0 overlaps / 105 pages**;
- dialogue index: **1,009 explicit + 16 supplements = 1,025 downstream units**;
- exact source speaker labels: **62**;
- source-role unresolved: **0**;
- source punctuation normalization: **0**;
- character/entity layer: **26 entities / 62/62 labels / 1,025/1,025 units**;
- song/performance source gate: **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**;
- English translation: **scene 15/63 / 355 verified units**;
- English dialogue coverage: **295 explicit + 8 source-role supplements = 303 dialogue units**;
- English stage/action units: **51**;
- English song-reference units: **1**;
- English cross-page units: **3**;
- source-only occurrences linked in English: **2** — `ammaiyappan-song-001`, `ammaiyappan-song-002`;
- reader/export: blocked pending complete English.

Post-closure delimiter authority remains unchanged: scene 3 `பூங் ; ...` and scene 5 `திரு; ...` are preserved as exact non-colon source forms.

Batch 11–15 source safeguards:

- scene 11 retains both context-attributed source-role supplements (`ammaiyappan-s011-r001`, `ammaiyappan-s011-r002`) without inventing printed labels;
- scene 11 keeps the final fight narration, including its embedded warning, as scene narration rather than duplicate dialogue ownership;
- scene 15 keeps `ammaiyappan-s015-d001` as one cross-page `குரல்` unit across PDF 31→32 with page-segment provenance;
- irregular/fragmentary forms are not silently normalized for English fluency;
- the closed song inventory contains no retained occurrence in scenes 11–15.

**Exact next activity:** translate and source-review archival scenes **16–20**. Preserve the two closed source-role supplements in scene 17 and, in scene 19, translate only the source-visible singing-performance cue represented by `ammaiyappan-song-003`; do not reconstruct a song title or lyrics.