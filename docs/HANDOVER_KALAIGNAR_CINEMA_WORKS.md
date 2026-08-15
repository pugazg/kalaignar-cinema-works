# Kalaignar Cinema Works — Master Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Primary branch: `main`  
Purpose: reusable handover for continuing the archive or onboarding a new Kalaignar cinema work

This document is the **project-level handover**. Work-specific handovers remain useful historical/checkpoint records, but current repository state always takes precedence over an older handover.

For a new work, also read:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `docs/SOURCE_POLICY.md`
4. `docs/TRANSCRIPTION_GUIDE.md`
5. `docs/START_NEW_CINEMA_WORK_PROMPT.md`

---

## 1. Project purpose

This repository is a source-led archive of cinema writing credited to **Kalaignar M. Karunanidhi**, including screenplay/dialogue booklets, songs/verse where source-supported, and downstream structured/translated reader derivatives.

The central rule is simple:

> **The scanned publication controls canonical text for that edition.**

Everything else—scene files, dialogue indexes, character mappings, song attribution, translation, reader exports, EPUB/PDF packages and web presentation—is downstream.

---

## 2. Mature reference implementations

Two works currently provide the strongest reference patterns.

### Parasakthi

Parasakthi demonstrates:

- non-trivial scene-number anomalies that must be documented rather than casually normalized;
- complete Tamil fidelity verification;
- scene/dialogue/character/song derivative layers;
- song/verse authorship mapping;
- complete source-linked English translation;
- whole-work reader QA and reproducible Markdown/HTML/JSON outputs;
- preservation of source-unlabelled performance/dialogue outside a simplistic speaker model.

Use Parasakthi to understand complex numbering and mixed song/verse handling. **Never reuse its text as authority for another film.**

### Tirumbippaar!

Tirumbippaar demonstrates:

- full-scan structural mapping before transcription;
- 93-scene scene-heading audit;
- 104-page visual Tamil fidelity audit;
- post-fidelity scan corrections recorded explicitly;
- immutable 1,040-record dialogue indexing;
- character label/entity mapping without normalizing dialogue labels;
- cautious song/performance authorship with unresolved occurrences left unresolved;
- complete source-linked English translation;
- whole-work reader reconciliation that caught synthetic scene endings, source-order drift and duplicate stage actions;
- deterministic reader outputs and EPUB package QA;
- explicit preference for Reading Room publication at `https://nenjukkuneethi.org/read` rather than unnecessary additional standalone packages.

Use Tirumbippaar to understand the current mature pipeline and QA discipline. **Never reuse its text as authority for another film.**

---

## 3. Current reusable workflow

For each new cinema work, proceed through these gates in order:

1. **Source intake**
2. **Structural mapping**
3. **Canonical Tamil first pass**
4. **Visual fidelity audit**
5. **Scene-text derivatives**
6. **Dialogue index**
7. **Character/entity index**
8. **Song/verse/performance authorship gate**
9. **Tamil song derivative files only where full source text supports them**
10. **English translation, if in scope**
11. **Whole-work reader QA/export**
12. **Reading Room integration**
13. **Optional standalone packaging/release only when separately useful/requested**

The detailed rules are in `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`.

---

## 4. Source authority rules that must survive every handover

Do not silently modernize, correct, normalize, reconstruct or improve the Tamil.

Preserve source-supported:

- historical/colloquial spelling;
- punctuation and ellipses;
- exact speaker labels;
- scene-heading irregularities;
- repetition;
- unusual grammar;
- typographical forms;
- English code-switching;
- stage directions;
- song/performance structures;
- printed letters/news/advertisements/other embedded text.

Do not repair canonical text from:

- OCR;
- subtitles;
- film audio;
- web quotations;
- later editions;
- existing translations;
- memory;
- familiar famous dialogue.

If the scan does not support a reading, keep uncertainty visible.

---

## 5. Important lessons learned

### A. Inspect the scan, not the filename

The filename may identify the item but does not establish edition, title-page wording, credits, pagination or even exact content boundaries.

### B. Map the whole source before transcribing

A full-scan map prevents incorrect page formulas, missing sections and premature scene assumptions.

### C. Never trust progress metadata without checking physical coverage

Tirumbippaar exposed an early storage gap even though a claimed range appeared complete. Verify that every claimed page is actually present in stored transcription.

### D. Verified text can still be corrected—but only from the scan

If later derivative work exposes a suspicious reading, reopen the rendered scan. Record substantive post-verification corrections explicitly.

### E. Scene numbering is not always clean

Do not force a neat sequence onto printed anomalies. Source numbering and any canonical disposition are separate pieces of evidence.

### F. Unlabelled speech is not labelled dialogue

Do not manufacture a speaker ID because context makes the speaker obvious. The dialogue index should represent what the source explicitly labels.

### G. Cross-page utterances stay single units

A dialogue or translation unit crossing a page boundary remains one logical record with multi-page provenance.

### H. Decorative separators are not prose

Do not turn `★` or similar separators into `(Scene ends.)` or other invented reader text.

### I. Do not duplicate stage action

Inline parenthetical action already represented within a dialogue should not be recreated as a separate standalone unit unless the source also prints it separately.

### J. Song authorship requires item-level evidence

Story/dialogue credit is not lyric credit. A film-wide contributor list does not automatically identify a specific song's lyricist.

### K. QA should fail loudly

The reader/export builder should reject missing links, duplicate IDs, source-order regressions, synthetic content and inconsistent provenance instead of silently producing output.

---

## 6. Repository architecture and authorities

Common authoritative locations:

```text
docs/
  ARCHIVAL_WORKFLOW.md
  SOURCE_POLICY.md
  TRANSCRIPTION_GUIDE.md
  CINEMA_WORKS_PROCESSING_GUIDE.md
  HANDOVER_KALAIGNAR_CINEMA_WORKS.md
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
2. verified canonical Tamil transcription;
3. verified scene derivative;
4. immutable dialogue/song/etc. structured records;
5. translation;
6. reader/export/package;
7. website presentation.

A downstream layer must not silently repair an upstream layer.

---

## 7. Metadata synchronization

At the end of a major phase, reconcile at least:

- `works/<work-id>/metadata.yaml`;
- `works/<work-id>/README.md`;
- `data/works.json`;
- root `README.md` when the public project checkpoint changes;
- the relevant layer's README/index/audit files.

Do not let counts drift between README text and machine-readable indexes.

Where possible, derive generated status from authoritative indexes and validate with automated QA.

---

## 8. Translation and reader architecture

For a mature translation layer:

- use scene-sharded translation records;
- keep stable unit IDs;
- retain exact Tamil speaker labels as metadata;
- link labelled dialogue to immutable dialogue IDs;
- leave source-unlabelled speech unlabelled;
- distinguish dialogue, stage direction, chant, song/song-reference, written text and other legitimate source structures;
- retain page provenance;
- keep cross-page source units whole;
- preserve source irregularity honestly.

Before declaring translation complete, perform whole-work reconciliation rather than trusting batch counts.

Reader/export outputs should be generated from verified structured translation records, not manually maintained copies.

---

## 9. Public Reading Room direction

The preferred public destination for completed works is:

**`https://nenjukkuneethi.org/read` — Kalaignar Digital Library / Reading Room**

For cinema works:

- use **scene-based navigation**;
- expose Tamil source text and English where verified;
- support title/dialogue/full-text search;
- derive counts from repository checkpoints;
- preserve source/page provenance behind the interface;
- keep exact speaker labels and source order intact in archival data;
- treat collection cards, summaries, icons, filters and search indexes as presentation metadata only.

Do not automatically create a print-ready PDF or another standalone EPUB after the reader layer is complete. Create additional packages only when the user explicitly requests them or they serve a distinct release/archive purpose.

Existing reproducible packages may remain in the repository.

---

## 10. Working style for future chats

The user frequently continues a project by saying **“Proceed with next activity.”**

When the next activity is already documented:

- continue without asking a redundant question;
- choose a meaningful batch rather than one page by default;
- inspect source and repository state first;
- complete bookkeeping for the finished batch before claiming completion;
- do not report a layer complete if index/README/metadata remain stale;
- if a large scene/file read is truncated, fetch the missing range rather than summarizing unseen content;
- report exact commits/checkpoints after writes.

A genuine source ambiguity can justify a pause; routine workflow continuation does not.

---

## 11. Starting a new cinema work

Use `docs/START_NEW_CINEMA_WORK_PROMPT.md`.

The first activity should normally stop after **source intake + full structural mapping + initial repository skeleton/status synchronization**.

Do not rush directly into large-scale transcription before the map is verified.

If the repository already contains the work, abandon the new-work initialization path and continue the existing state instead.

---

## 12. Work-specific handovers

A work-specific handover should be created/refreshed when a project becomes lengthy or is likely to move to another chat.

It must contain:

- repository/branch;
- source filename and SHA-256;
- exact source bounds;
- current phase;
- completed gates and counts;
- unresolved items;
- known scan/source anomalies;
- cross-page/cross-part special cases;
- authoritative files;
- layers that must remain immutable;
- exact next activity;
- startup order.

### Historical handovers

Older handovers such as Tirumbippaar's initial fidelity-audit handover are historical checkpoints. They do not override current `main` after later phases have completed.

Always inspect current repository state.

---

## 13. Current high-level project checkpoint

At the time this master handover was introduced:

- **Parasakthi** has complete-verified canonical/structured English reader work and serves as a mature reference implementation.
- **Tirumbippaar!** has complete-verified Tamil, scene/dialogue/character/song disposition, English translation, whole-work reader QA, and deterministic EPUB package QA.
- Tirumbippaar's preferred public destination is now explicitly the Reading Room at `nenjukkuneethi.org/read`.
- reusable project rules now live in `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`.

Do not infer the status of a future work from these examples. Inspect that work independently.

---

## 14. Exact next activity for the overall project

For the **next newly supplied Kalaignar cinema source**:

1. use the reusable starter prompt;
2. inspect the source scan and existing repository state;
3. establish source identity/checksum and content boundaries;
4. complete a full structural map;
5. create/update the work skeleton and metadata;
6. stop before canonical transcription unless the mapping gate is genuinely complete;
7. set the next activity explicitly to canonical Tamil first-pass transcription.

The goal is not speed alone. The goal is a repeatable archive where every later reader can trace each derivative back to the scanned edition.