# Starter Prompt — New Kalaignar Cinema Work

Copy the prompt below into a new chat, replace the placeholders where known, attach the new source PDF, and send it as the first instruction for a new cinema-work archival project.

---

Continue the **Kalaignar Cinema Works archival project** with a new cinema source.

GitHub repository:
`https://github.com/pugazg/kalaignar-cinema-works`

Branch:
`main`

Attached source PDF:
`<ATTACHED_FILENAME.pdf>`

Expected work/title, if known:
`<TITLE OR UNKNOWN — VERIFY FROM SCAN>`

Use the GitHub connector and work directly in the existing repository on `main`.

## MANDATORY STARTUP

Before making any repository change, read these documents completely:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
3. `docs/ARCHIVAL_WORKFLOW.md`
4. `docs/SOURCE_POLICY.md`
5. `docs/TRANSCRIPTION_GUIDE.md`
6. `docs/STATUS_CONSISTENCY_AUDIT.md`
7. repository root `README.md`
8. `data/works.json`

Then inspect the current repository and confirm whether this work has already been started under the same title, an alternate title, another filename, or an existing `works/<id>/` directory.

If work already exists, **continue it instead of creating duplicate files**. Read its work README, metadata, mapping, audits and current layer indexes before proceeding.

Use **Parasakthi**, **Tirumbippaar!**, and **Raja Rani** only as workflow/reference implementations. Never use their Tamil or English text as a source for this new work.

Reference emphasis:

- Parasakthi — complex source numbering / mixed verse handling;
- Tirumbippaar — mature whole-work reader/export and package QA;
- Raja Rani — glyph-sensitive adjudication, late-correction reconciliation, mixed screenplay + separately numbered songs, duplicate-boundary QA, and repository-wide synchronization.

## SOURCE AUTHORITY

The attached scan is the controlling source for this edition.

Do not rely on the filename alone for title, edition, year, credits, pagination or content boundaries.

Do not silently modernize, correct, normalize, reconstruct or improve the Tamil.

Preserve all source-supported:

- spelling and historical/colloquial forms;
- punctuation and ellipses;
- wording and repetition;
- exact speaker labels;
- scene numbers and scene-heading irregularities;
- stage directions and parentheticals;
- English code-switching;
- song/verse/chant/performance structures;
- letters, newspaper text, advertisements and other printed structures;
- unusual grammar and typographical forms.

Distinguish printed source text from:

- library stamps;
- handwriting;
- later annotations;
- bleed-through;
- physical damage/crops.

OCR or embedded text may assist navigation, but it is never canonical evidence.

Do not repair the source from:

- film audio;
- subtitles;
- web quotations;
- later editions;
- existing translations;
- memory;
- famous/familiar dialogue.

If a reading is uncertain, keep the uncertainty explicit instead of guessing.

## SONG / AUTHORSHIP RULE

A Kalaignar story/dialogue credit does **not** automatically establish lyric authorship for every song in the booklet.

Do not assign song authorship from proximity or memory.

If later external evidence is used for item-level authorship, document it separately and never use it to supply missing canonical lyrics.

If the source contains an independently numbered song corpus outside the screenplay, preserve those song IDs as songs. Do not force them into archival scene IDs merely because a screenplay translation layer later exists.

## FIRST ACTIVITY — SOURCE INTAKE AND STRUCTURAL MAPPING

For this first activity, do **not** rush into full canonical transcription.

Inspect the entire attached scan and complete the source-intake + structural-mapping gate.

### A. Verify source identity

Record:

- exact visible title;
- exact printed Kalaignar credit(s);
- source/archive identifier if present;
- original attached filename;
- PDF page count;
- file size;
- SHA-256;
- explicit edition statement, if any;
- explicit publication year, if any;
- publisher/imprint exactly as visible;
- any cropped/incomplete imprint text without reconstruction;
- whether the PDF is image-only or has embedded text.

Do not infer year/edition from PDF creation metadata.

### B. Inspect the entire scan

Identify:

- cover/title/credit pages;
- foreword/preface/introduction or other front matter;
- main screenplay/dialogue range;
- printed pagination and PDF↔printed-page relationship;
- scene/section numbering system;
- all scene starts/headings visible enough to map;
- numbering gaps, repeats or out-of-order headings;
- songs, verse, chants, performance references;
- letters/news/advertisements/other embedded structures;
- blank/back-matter/catalogue pages;
- missing, duplicated, cropped, damaged or unreadable scan pages.

Do not repair numbering anomalies simply to make the sequence neat.

### C. Repository initialization

If the work is genuinely new, choose a stable lowercase ASCII work ID and create the initial archival skeleton as appropriate, including at minimum:

- `works/<work-id>/README.md`
- `works/<work-id>/metadata.yaml`
- `works/<work-id>/mapping.md`
- relevant `notes/` audit file(s) if required

Add an initial work entry to `data/works.json`.

Update the root `README.md` to register the new work and its actual intake status when the repository-level work list changes.

If the new work materially changes the project checkpoint, also refresh:

- `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`;
- `docs/STATUS_CONSISTENCY_AUDIT.md`.

Do not create empty advanced layers merely for completeness. `scenes/`, `dialogues/`, `characters/`, `songs/`, `translations/` and `editions/` should be created only when their gate is reached.

### D. Mapping requirements

`mapping.md` must record:

- PDF-page ↔ printed-page correspondence or formulas/ranges where valid;
- exact content boundaries;
- exact visible scene/section heading sequence;
- structural anomalies;
- distinct song/verse/chant/written-text structures;
- scan defects;
- front/back matter disposition;
- any source questions that still need verification.

If scene headings are numerous, create a dedicated scene-heading audit rather than compressing evidence into a vague count.

## STOP CONDITION FOR FIRST ACTIVITY

At the end of this first activity, do **not** claim canonical Tamil transcription has begun unless it actually has and the structural map is already complete.

The normal first checkpoint should be:

- source intake: complete;
- structural mapping: complete or verified as supported;
- canonical transcription: not-started;
- later derivatives: blocked/not-started.

Before declaring the first activity complete, verify that work-local metadata, `data/works.json`, root README and any affected project-level status docs all describe that same checkpoint.

Set the exact next activity to:

> **Canonical Tamil first-pass transcription from the rendered scan, in source order, with stable page anchors — followed later by a separate visual fidelity audit before any structured derivatives.**

## FUTURE PHASE RULES

When I later say **“Proceed with next activity”**, continue the documented next phase without asking a redundant question.

Use meaningful batches rather than defaulting to one page or one scene.

The normal future sequence is:

1. canonical Tamil first pass;
2. full visual fidelity audit;
3. scene-text derivatives;
4. dialogue index;
5. character/entity index;
6. song/performance authorship gate;
7. Tamil song derivatives only where complete source lyrics support them;
8. English translation if in scope;
9. whole-work reader QA/export;
10. integration into `https://nenjukkuneethi.org/read` as the preferred public Reading Room;
11. standalone PDF/EPUB/release packaging only when explicitly requested or independently useful.

### Mandatory synchronization after every major future phase

Do not report a phase complete until all relevant current mirrors have been reconciled.

Work-local minimum:

- work metadata/README;
- active layer index/README/QA/audit;
- work handover/next-chat prompt when present.

Repository-wide minimum when the checkpoint changes:

- `data/works.json`;
- root `README.md`;
- `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`;
- `docs/STATUS_CONSISTENCY_AUDIT.md`;
- any shared guide changed by a reusable lesson from the phase.

Run a stale-state sweep for superseded counts, old blocked/review states and obsolete next activities before closure. Historical batch notes may retain historical counts if clearly labelled historical; active status/startup documents may not.

### Dialogue rule

Only explicitly speaker-labelled utterances become immutable dialogue records. Source-unlabelled speech must remain unlabelled. A cross-page utterance remains one record with multi-page provenance.

Whole-work QA must also catch accidental duplicate source-span ownership across adjacent scene derivatives.

### Translation rule

Translation begins only from verified Tamil. Keep exact Tamil speaker labels as metadata, link labelled dialogue records exactly, preserve source-unlabelled speech without invented speakers, and never create absent lyrics or artificial `(Scene ends.)` text from decorative separators such as `★`.

Separately numbered song bodies remain separate song translation records, not synthetic scenes.

### Reading Room rule

For completed cinema works, prefer integration at:

`https://nenjukkuneethi.org/read`

Use verified structured repository data for Tamil/English reading and search. Do not treat the website as a new textual authority.

Preserve the work's natural source structures: screenplay scenes remain scenes; independently numbered songs remain songs/front-matter units.

Do not automatically create a print-ready PDF or additional publication package when the web reader is the intended destination.

## REPORT AFTER FIRST ACTIVITY

Report concisely but precisely:

- verified source title and printed credits;
- source identifier;
- PDF page count and SHA-256;
- edition/year statements actually visible;
- front matter / main text / back matter ranges;
- printed-pagination map;
- scene/section count and any anomalies;
- song/performance/written-text structural findings;
- scan defects or unresolved source questions;
- work ID and repository paths created/updated;
- files changed, including repository-wide mirrors synchronized;
- final `main` commit SHA;
- exact next activity.

Do not claim anything as verified unless the scan/repository work actually supports it.

---

## Short version

If a compact prompt is needed after the reusable docs already exist, use:

> Read `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`, `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`, `docs/ARCHIVAL_WORKFLOW.md`, `docs/SOURCE_POLICY.md`, `docs/TRANSCRIPTION_GUIDE.md`, and `docs/STATUS_CONSISTENCY_AUDIT.md` completely. Use the attached new Kalaignar cinema PDF as the controlling source and work directly in `pugazg/kalaignar-cinema-works` on `main`. Inspect the repository first to avoid duplicates. In this first activity, inspect the entire scan, verify source identity/checksum/credits/edition and content bounds, complete the full structural map and initialize the work metadata/skeleton. Do not silently normalize Tamil, infer song authorship, or begin downstream derivatives before their gates. Synchronize work-local state, `data/works.json`, root README and affected project-level status docs before claiming the checkpoint complete. Stop after intake/mapping and set canonical Tamil first-pass transcription as the next activity. The eventual preferred public destination is `https://nenjukkuneethi.org/read`, preserving each source's natural navigation structure.