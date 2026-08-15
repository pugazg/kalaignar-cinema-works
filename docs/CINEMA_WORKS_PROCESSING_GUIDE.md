# Kalaignar Cinema Works — Processing Guide

This is the reusable processing guide for archival work in `pugazg/kalaignar-cinema-works`.

It applies to a **new cinema-related source credited to Kalaignar M. Karunanidhi** unless a work-specific guide explicitly adds stricter rules. It consolidates the mature workflow learned from the completed **Parasakthi** and **Tirumbippaar!** projects.

This guide supplements:

- `docs/ARCHIVAL_WORKFLOW.md`
- `docs/SOURCE_POLICY.md`
- `docs/TRANSCRIPTION_GUIDE.md`

The scanned publication remains the controlling source at every stage.

---

## 1. Core principles

1. **Primary source first.** The attached scan controls canonical Tamil for that edition.
2. **Do not silently repair the source.** Preserve source-supported spelling, punctuation, wording, names, numbering, repetition, unusual grammar, typographical forms, English code-switching and structural irregularities.
3. **Separate source from derivatives.** Canonical Tamil, scene derivatives, dialogue records, character mappings, song metadata, translation and publication outputs are different layers.
4. **Preserve uncertainty.** If the scan cannot support a reading confidently, mark it instead of guessing.
5. **No source substitution.** Film audio, subtitles, web quotations, later editions, OCR, memory and existing English translations are not canonical evidence.
6. **No automatic authorship inference.** A song printed inside a Kalaignar dialogue booklet is not automatically a Kalaignar lyric.
7. **Traceability is mandatory.** Every canonical page and every structured derivative must remain traceable to the scan.
8. **Verification gates matter.** Do not build later layers on unverified Tamil.
9. **The public reader is downstream.** `https://nenjukkuneethi.org/read` is the preferred public Reading Room for completed Kalaignar archive works; the website does not become a new source authority.

---

## 2. Mandatory startup for every new cinema work

Before changing the repository:

1. Read this guide completely.
2. Read `docs/ARCHIVAL_WORKFLOW.md`.
3. Read `docs/SOURCE_POLICY.md`.
4. Read `docs/TRANSCRIPTION_GUIDE.md`.
5. Read `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`.
6. Inspect the repository root `README.md` and `data/works.json`.
7. Inspect the attached scan directly.
8. Search `works/` and repository metadata to confirm the work has not already been started under another filename/title.
9. If work already exists, continue it; do not create a duplicate work directory.
10. Use Parasakthi and Tirumbippaar only as **workflow/reference implementations**, never as textual authorities for a new work.

---

## 3. Repository layout for a new work

Use a stable lowercase ASCII work ID, for example:

```text
works/<work-id>/
```

A mature work may contain:

```text
works/<work-id>/
├── README.md
├── metadata.yaml
├── mapping.md
├── notes/
│   ├── fidelity-audit.md
│   ├── scene-heading-audit.md
│   ├── textual-notes.md
│   └── post-fidelity-corrections.md
├── transcription/
│   ├── README.md
│   ├── full-text.md
│   └── parts/
├── scenes/
│   ├── index.json
│   └── scene-*.md
├── dialogues/
│   ├── README.md
│   ├── schema.json
│   ├── index.json
│   └── records/
├── characters/
├── songs/
├── translations/
└── editions/
```

Not every source needs every directory. Create a layer only when the source supports it and the relevant gate is reached.

Also add/update the work entry in `data/works.json` when the intake checkpoint is established.

---

## 4. Phase 1 — source intake

Inspect the **actual scan**, not just the filename.

Record at minimum:

- original filename;
- source identifier, if printed or reliably embedded in the archive filename;
- byte size;
- PDF page count;
- SHA-256;
- visible title as printed;
- visible author/writer/credit statements exactly as printed;
- explicit edition statement, if present;
- explicit publication year, if present;
- publisher/imprint statements, including cropped/incomplete text exactly as visible;
- whether the PDF is image-only or has embedded text;
- front matter, main-text range and back matter;
- printed pagination system;
- any missing, duplicated, cropped, blank or damaged pages.

Do **not** derive publication year from PDF metadata. Do **not** complete cropped imprint text from outside knowledge.

### Binary policy

Do not upload the source PDF into the GitHub repository unless the user explicitly requests that and repository policy allows it. The textual archive must still record the source filename and cryptographic checksum.

---

## 5. Phase 2 — structural mapping gate

Create `mapping.md` before canonical transcription.

Map:

- PDF page ↔ printed page correspondence;
- title/credit/front-matter pages;
- main-text boundaries;
- scene/section/chapter headings exactly as printed;
- numbering gaps, repeats or out-of-order headings;
- location labels and unusual scene markers;
- songs, verse, chants, letters, newspaper blocks, advertisements and other distinct structures;
- back matter and unrelated material;
- cross-page structural continuities;
- scan defects.

### Critical rule: source numbering is evidence

Do not silently renumber scenes because a sequence looks wrong.

Parasakthi demonstrated that printed scene numbering can itself be anomalous. Tirumbippaar demonstrated that source headings can be misread on first pass and later corrected only by direct scan reinspection. Preserve the printed form in the canonical/source layer and document any separate canonical disposition explicitly.

### Scene-heading audit

For a screenplay/dialogue booklet, create a scene-heading audit when useful. Record every observed scene start and its exact heading/location text before scene derivatives are built.

---

## 6. Phase 3 — canonical Tamil transcription

Canonical transcription is **source-order text**, not a modernized screenplay.

For each page:

- transcribe only visible text;
- preserve exact scene headings;
- preserve speaker labels exactly;
- preserve punctuation, ellipses, brackets, parentheses and repetition;
- preserve stage directions and narrative text;
- preserve songs/verse/chant blocks in source position;
- preserve English code-switching exactly where source-supported;
- distinguish printed text from library stamps, handwriting, later annotations, bleed-through and damage;
- add a stable page anchor.

Recommended anchor:

```md
<!-- source: pdf=12 printed=4 status=draft -->
```

Where no printed page exists, omit that field rather than inventing one.

### OCR policy

OCR may assist navigation or first-pass comparison but is never canonical evidence. The rendered scan controls.

### Uncertainty

Use the existing uncertainty notation from `TRANSCRIPTION_GUIDE.md`. Do not hide doubt with a plausible word from memory or another edition.

---

## 7. Phase 4 — full visual fidelity audit

A page becomes `verified` only after complete visual comparison with the rendered scan.

Audit for:

- omitted/duplicated lines;
- speaker-label drift;
- Tamil character confusions;
- punctuation and numeral errors;
- stage-direction omissions;
- scene-heading errors;
- page-boundary errors;
- song/verse lineation;
- source-visible English terms;
- accidental normalization;
- first-pass storage gaps.

Maintain `notes/fidelity-audit.md` with batch checkpoints.

### Post-verification corrections

A later scan-supported correction to verified Tamil is allowed, but it must be explicit. For consequential corrections, record the change in `notes/post-fidelity-corrections.md` rather than silently rewriting history.

Do not let a translation interpretation drive a Tamil correction. Reopen the scan.

---

## 8. Gate order for structured derivatives

The normal order is:

1. source intake;
2. structural mapping;
3. canonical Tamil transcription;
4. fidelity audit;
5. scene-text derivatives;
6. dialogue index;
7. character/entity index;
8. song/performance authorship gate and Tamil song derivatives where source-supported;
9. English translation;
10. whole-work reader QA/export;
11. Reading Room integration;
12. optional standalone packages/releases when explicitly useful.

Later layers must never overwrite earlier authorities.

---

## 9. Scene-text derivatives

Create one derivative file per **observed/canonical scene disposition** using verified Tamil only.

Requirements:

- preserve source order;
- preserve page anchors;
- include the exact scene heading/source structure;
- assemble cross-part scenes correctly;
- do not duplicate material at part boundaries;
- do not add artificial closing text for decorative separators such as `★`;
- keep structural stars/separators structural unless they are actual textual content.

A scene derivative is a convenient view of canonical text, not a new textual authority.

---

## 10. Dialogue index

Only explicitly speaker-labelled source utterances become immutable dialogue records.

Each record should preserve:

- stable dialogue ID;
- canonical scene;
- exact Tamil `speaker_label`;
- exact Tamil dialogue text;
- PDF/printed-page provenance;
- cross-page segmentation metadata when one labelled utterance spans pages.

### Do not invent speakers

Unlabelled speech remains unlabelled. Do not assign a speaker merely because context makes the identity obvious.

This is a major lesson from both completed works: source-visible speech and performance sometimes sit outside the simple labelled-dialogue model. Preserve that distinction.

### Cross-page rule

A labelled utterance that crosses a page remains **one dialogue record**, not two.

### Zero-dialogue scenes

A scene can legitimately contain no labelled dialogue. Record zero rather than manufacturing records from narrative, newspaper text, letters, songs or unlabelled speech.

---

## 11. Character/entity index

The character layer maps exact source speaker labels to characters, roles or collectives **without rewriting dialogue records**.

Rules:

- inventory all exact labels first;
- preserve spelling variants and anomalies;
- map variants only when source/context supports the relationship;
- generic labels may remain roles/collectives;
- reused labels such as `குரல்` may represent different contextual voices and should not automatically become one named character;
- document `verified`, `review` or `unresolved` dispositions.

The character index is interpretive metadata, not canonical speaker normalization.

---

## 12. Song, verse and performance authorship gate

Do not infer lyric authorship from:

- Kalaignar's story/dialogue credit;
- proximity to dialogue;
- performer identity;
- soundtrack memory;
- a film-wide lyricist list without item-level mapping.

Create a source-visible song/performance inventory first.

For each occurrence record:

- scene/page provenance;
- source-visible title or fragment;
- whether full lyrics are actually printed;
- performance context;
- authorship status;
- evidence source.

External public metadata may establish item-level authorship only when the match is sufficiently exact and separately documented. It must not supply missing canonical lyrics.

### Tamil song derivatives

Create standalone Tamil lyric files only when the source actually contains a complete or clearly bounded lyric body appropriate for extraction. Do not manufacture lyric files from a title or fragment.

---

## 13. English translation gate

English translation starts only after the corresponding Tamil source unit is verified.

Translation rules:

- source-linked and scene-sharded;
- exact Tamil speaker label retained as metadata;
- labelled dialogue links immutable dialogue IDs;
- source-unlabelled speech receives no invented speaker/dialogue ID;
- stage directions, written text, chants, song references and full songs remain distinct unit kinds;
- preserve rhetoric, repetition, satire, code-switching and source irregularity;
- explain uncertainty in notes instead of silently repairing Tamil;
- keep one translation unit for a source unit that crosses pages;
- do not invent absent lyrics;
- do not add `(Scene ends.)` for decorative `★` separators.

### Translation QA lessons

Whole-work reconciliation must detect:

- duplicate stage actions;
- units out of source order;
- missing/duplicate immutable dialogue links;
- synthetic scene-end text;
- inconsistent unit IDs;
- missing cross-page provenance;
- source-unlabelled speech accidentally assigned to a speaker;
- placeholder/editorial text leaking into the reader.

A QA gate should fail loudly rather than silently accommodate corrupted assumptions.

---

## 14. Whole-work reader/export layer

Once translation is complete, build a deterministic reader layer from verified structured records.

Preferred generated forms:

- Markdown;
- standalone HTML;
- machine-readable JSON;
- QA report;
- integrity manifest.

The reader builder must verify the whole work, not simply concatenate files.

Minimum QA:

- expected scenes exactly once and in canonical order;
- all verified units unique and sequential;
- immutable dialogue links complete and unique;
- cross-page unit list exact;
- song/verse occurrence links valid;
- provenance in source bounds;
- no synthetic `★`-derived prose;
- no placeholder text;
- every unit rendered exactly once in reader output.

Generated reader files remain downstream derivatives.

---

## 15. Reading Room integration — preferred public destination

The preferred public reading surface is:

**Kalaignar Digital Library / Reading Room — `https://nenjukkuneethi.org/read`**

For a completed work, prepare structured data for integration rather than automatically creating another standalone PDF.

### Web-integration rules

1. Use verified repository structured data as authority.
2. Prefer JSON/source-linked records over scraping generated HTML.
3. Preserve the natural navigation model:
   - memoir/book → chapters/sections;
   - cinema dialogue/screenplay → scenes;
   - letters → letters/volumes;
   - commentary → source-specific units.
4. Tamil/English switching is presentation only; it must not rewrite either source layer.
5. Search indexes may cover scene text, dialogue, titles and full text, but search normalization must not alter canonical stored text.
6. Public counts must be derived from verified repository checkpoints.
7. Collection cards, labels, summaries, filters and icons are UI metadata only.
8. Keep source/page provenance available behind the reader interface.

### Standalone publication formats

Do **not** create a print-ready PDF, another EPUB, or another publication package simply because the reader layer is complete. Create one only when explicitly requested or when it serves a distinct archival/release purpose.

Existing packages may remain as reproducible artifacts, but the Reading Room is the preferred public destination.

---

## 16. GitHub and commit discipline

- Work directly on the requested branch, normally `main`.
- Inspect current repository state before creating files.
- Fetch the current blob SHA before updating an existing file.
- Do not make parallel writes to the same path.
- Keep commits understandable and phase-specific.
- Do not mix unrelated work into a source-fidelity commit.
- After a major phase, synchronize:
  - work `metadata.yaml`;
  - work `README.md`;
  - root `README.md` when project-level status changes;
  - `data/works.json`;
  - relevant layer README/index/audit files.
- Generated publication outputs should be reproducible and preferably built/validated by automation.

---

## 17. Batch-size guidance

Do not default to one page or one scene per user turn.

Choose batches based on risk and source density:

- intake/mapping: normally entire scan;
- fidelity audit: coherent page ranges, often 5–30 pages when legibility permits;
- scene derivatives: multiple scenes per batch unless a scene is exceptionally large;
- dialogue indexing: multiple scenes per batch;
- translation: multiple scenes per batch, with large pivotal scenes handled separately when needed;
- whole-work QA: entire work in one gate.

When the user says **“Proceed with next activity”**, continue the established plan without asking a redundant clarification unless a genuine source ambiguity blocks progress.

---

## 18. Handover discipline

At important checkpoints, keep a handover document that states:

- repository and branch;
- source filename and checksum;
- exact current phase;
- completed gates;
- unresolved items;
- authoritative files;
- known anomalies/corrections;
- immutable layers;
- exact next activity;
- startup order for a new chat.

Do not let an old handover override current repository state. Always inspect current `main` first.

For onboarding an entirely new cinema work, use:

- `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
- `docs/START_NEW_CINEMA_WORK_PROMPT.md`

---

## 19. Status vocabulary

Recommended statuses:

- `not-started`
- `draft`
- `draft-complete`
- `review`
- `verified`
- `pilot-verified`
- `complete`
- `complete-verified`
- `unresolved`

Keep statuses separate for source intake, mapping, transcription, fidelity audit, scene derivatives, dialogue index, character mapping, song authorship, translation, reader QA, Reading Room integration and optional publication packages.

---

## 20. Definition of done for a mature cinema work

A fully processed cinema work should, where supported by the source, have:

- source intake documented;
- structural map verified;
- complete canonical Tamil transcription;
- complete visual fidelity audit;
- scene derivatives complete;
- dialogue index complete;
- character/entity labels dispositioned;
- song/performance occurrences dispositioned with honest authorship status;
- English translation complete-verified if translation is in scope;
- whole-work reader QA PASS;
- structured data ready for `nenjukkuneethi.org/read`;
- no unresolved hidden source repairs;
- no duplicate or fabricated records;
- synchronized repository metadata.

Completion means the archive is **traceable, reproducible and honest about uncertainty**, not merely that text has been extracted.