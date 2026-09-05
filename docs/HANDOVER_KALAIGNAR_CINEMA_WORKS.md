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

Three screenplay works now provide complementary mature reference patterns.

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

Use Tirumbippaar to understand the mature reader/export pipeline and QA discipline. **Never reuse its text as authority for another film.**

### Raja Rani

Raja Rani demonstrates:

- old-typeface / glyph-sensitive source review in which OCR and comparison transcripts remain candidate readings only;
- direct user scan verdicts preserved occurrence-by-occurrence;
- late source corrections reconciled through canonical pages, scenes, immutable dialogue, character mapping, song metadata and English;
- a fully unblocked **79/79 source-page / 70/70 screenplay-page** fidelity checkpoint;
- **58/58 archival scene derivatives**, **1,071 unique immutable dialogue records**, **80/80 exact source labels** and **44 verified entities/roles/collectives**;
- whole-screenplay English completion at **58/58 scenes / 1,236 verified units / 1,071 dialogue links**;
- detection and repair of a derivative ownership error where scene 55 duplicated the `(முன்)` flashback belonging to scene 56, without altering canonical page text;
- an independent numbered-song English layer for all **11/11** verified front-matter songs rather than forcing song bodies into screenplay scene IDs;
- numbered-song translation QA at **67 sections / 181 Tamil-to-English line-cue mappings**, while preserving the existing 5 later-anthology Kalaignar attributions and 6 unresolved lyricists;
- explicit synchronization of work-local state with `data/works.json`, root README and project-level documentation before a major phase is considered closed.

Use Raja Rani to understand late-correction reconciliation, mixed screenplay/song translation architecture and repository-wide anti-staleness discipline. **Never reuse its text as authority for another film.**

---

## 3. Current reusable workflow

For each new cinema work, proceed through these gates in order:

1. **Source intake**
2. **Structural mapping**
3. **Canonical Tamil first pass**
4. **Visual fidelity audit**
5. **Historical Tamil glyph audit when older typeforms may occur** — this is independent of visual fidelity and may require retrospective re-audit of previously visual-verified pages
6. **Scene-text derivatives**
7. **Dialogue index**
8. **Character/entity index**
9. **Song/verse/performance authorship gate**
10. **Tamil song derivative files only where full source text supports them**
11. **English translation, if in scope**
12. **Whole-work reader QA/export**
13. **Reading Room integration**
14. **Optional standalone packaging/release only when separately useful/requested**

For an older-print source that uses historical Tamil typeforms, canonical Tamil is not complete merely because the ordinary visual-fidelity gate passes. Follow `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`: identify character identity from source pixels, check the known reform-sensitive families occurrence-by-occurrence, avoid global replacement and spelling modernization, and leave unresolved identity under review.

**Repository-wide status synchronization is a completion gate at every major phase.** A phase is not closed merely because its content files exist.

The detailed rules are in `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`, supplemented by the historical-glyph guide for applicable older sources.

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

For historical Tamil typeforms, **read character identity, not modern visual resemblance**. A source-supported historical glyph should be encoded as its correct modern Unicode identity without modernizing the source word around it.

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

### I. Do not duplicate derivative ownership

Do not duplicate stage action or source passages across scene boundaries. Raja Rani's final QA showed that an entire flashback can be accidentally owned by two adjacent scene derivatives even when both files look internally plausible. Whole-work QA must check source-span ownership as well as per-file validity.

### J. Song authorship requires item-level evidence

Story/dialogue credit is not lyric credit. A film-wide contributor list does not automatically identify a specific song's lyricist.

### K. Distinct source structures need distinct derivative identities

A front-matter numbered song corpus should not be forced into screenplay scene IDs merely because screenplay translation already exists. Preserve the source's natural structure and link the layers explicitly.

### L. QA should fail loudly

The reader/export builder should reject missing links, duplicate IDs, duplicate source ownership, source-order regressions, synthetic content and inconsistent provenance instead of silently producing output.

### M. Stale shared documents are a project defect

A work-local index may be correct while root README, `data/works.json`, master handover or status audit still advertises an older checkpoint. Major-phase closure requires a repository-wide stale-state sweep and synchronization of every current mirror that could direct future work.

### N. Historical Tamil glyphs require their own explicit pass

Ordinary visual comparison can still misread an old metal-type glyph as the closest-looking modern character. For historical sources, explicitly decode glyph identity using enlarged/native source pixels and same-edition evidence. The known minimum families are `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`. This is a minimum set only. A systematic historical-glyph issue discovered after pages were previously called verified requires retrospective audit of the affected coverage.

---

## 6. Repository architecture and authorities

Common authoritative locations:

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
2. verified canonical Tamil transcription;
3. verified scene/song derivative;
4. immutable dialogue/song/etc. structured records;
5. translation;
6. reader/export/package;
7. website presentation.

A downstream layer must not silently repair an upstream layer.

For **status/progress** questions, live work indexes and metadata control, but all current project mirrors should be synchronized before a phase is declared complete.

---

## 7. Repository-wide synchronization gate

At the end of every major phase, reconcile all relevant current surfaces before claiming completion.

Minimum work-local surfaces:

- `works/<work-id>/metadata.yaml`;
- `works/<work-id>/README.md`;
- the active layer's README/index/QA/audit files;
- work-specific handover and next-chat prompt when they exist.

Minimum repository-wide surfaces when the checkpoint materially changes:

- `data/works.json`;
- root `README.md`;
- `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md` when the project checkpoint/reference lessons change;
- `docs/STATUS_CONSISTENCY_AUDIT.md`;
- any shared processing/translation guide whose reusable policy changed because of the completed work.

Before closure, perform a stale-state sweep for superseded counts, blocked/review statuses, prior next activities and obsolete completion language. Historical batch/checkpoint files may retain their dated historical state when clearly labelled historical; active startup/status files may not.

Do not let counts drift between README text and machine-readable indexes. Where possible, derive generated status from authoritative indexes and validate with automated QA.

---

## 8. Translation and reader architecture

For a mature translation layer:

- use scene-sharded translation records for screenplay material;
- use separate source-linked song records for independently numbered song bodies;
- keep stable unit IDs;
- retain exact Tamil speaker/turn labels as metadata;
- link labelled dialogue to immutable dialogue IDs;
- leave source-unlabelled speech unlabelled;
- distinguish dialogue, stage direction, chant, song/song-reference, written text and other legitimate source structures;
- retain page provenance;
- keep cross-page source units whole;
- preserve source irregularity honestly.

Before declaring translation complete, perform whole-work reconciliation rather than trusting batch counts.

Reader/export outputs should be generated from verified structured translation records, not manually maintained copies. If a work contains both translated screenplay scenes and independently translated numbered songs, the reader/export model must include both without pretending the songs are source-numbered scenes.

For a source that is not scene-structured, such as `மந்திரி குமாரி`, the reader/export layer must preserve that natural source model. Its verified reader therefore uses **1 story-summary unit + 15 performance blocks**, not synthetic screenplay scenes.

---

## 9. Public Reading Room direction

The preferred public destination for completed works is:

**`https://nenjukkuneethi.org/read` — Kalaignar Digital Library / Reading Room**

For cinema works:

- use the work's natural navigation model;
- for screenplays, use **scene-based navigation**;
- expose separately numbered songs/verse as distinct source structures where present;
- expose Tamil source text and English where verified;
- support title/dialogue/full-text search as appropriate;
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
- complete content QA **and repository-wide synchronization** for the finished phase before claiming completion;
- do not report a layer complete if index/README/metadata/shared mirrors remain stale;
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

Older handovers are historical checkpoints. They do not override current `main` after later phases have completed.

Always inspect current repository state.

---

## 13. Current high-level project checkpoint — 2026-09-05

- **Parasakthi** — complete-verified canonical/structured English reader work.
- **Tirumbippaar!** — complete-verified Tamil, scene/dialogue/character/song disposition, English translation, reader QA and deterministic EPUB package QA.
- **Manohara** — complete-verified Tamil, 57/57 scenes, 983 dialogue records and 1,190 English units; deterministic reader/export QA PASS; Reading Room integration ready.
- **Kalaignar Thirai Isai Paadalgal** — 54/54 verified Tamil and English songs; reader/export and Reading Room payload QA PASS; site not applied.
- **Manthiri Kumari** — 14-page story-and-song booklet; canonical Tamil PDF 2–13 complete-verified at 12/12 pages with 0 unresolved readings; credits, 1 continuous PDF 3–5 story-summary record and all 15 PDF 6–13 performance records complete-verified; cross-witness disposition remains 1 confirmed current-anthology witness / 14 source-only and booklet item-level lyricists remain 0 verified / 15 unresolved; English translation complete-verified at 1 story-summary record / 13 prose units plus 15/15 performance records / 52 sections / 234 Tamil-English line-cue pairs; deterministic bilingual reader/export complete-verified with QA PASS over 16 natural source structures and 234/234 paired performance line-cues; Reading Room integration payload complete-verified with QA PASS, source-linked composition mode, 32 linked source/translation targets, 15,704-byte payload and SHA-256 `20a0db293b936757e7d01def336252f28543337f319dfae6ad7bf5ae886bab43`; site application not applied.
- **Raja Rani** — 79/79 source pages and 70/70 screenplay pages verified; 58/58 scene derivatives; 1,071 immutable dialogue records; 80/80 labels / 44 entities; screenplay English 58/58 at 1,236 units; numbered-song English 11/11 at 67 sections / 181 mapped line-cues; deterministic bilingual reader/export QA PASS; Reading Room payload QA PASS; site application not applied.
- **Ammayappan** — 111-page image-only screenplay/dialogue source; first pass **105/105** assembled with QA PASS; visual source-fidelity audit has **PDF 5–74 passed (70/105)**; historical-Tamil-glyph audit is now a separate mandatory gate and is **0/105 formally cleared at gate introduction**; final dual-gate verified pages **0/105**; PDF 5–74 require retrospective glyph backfill, PDF 75–109 require both audits together; 29 unresolved first-pass readings; structured derivatives remain blocked.

The active Ammayappan work-local README, metadata, transcription README/index, project handover, historical-glyph audit, `data/works.json`, root README, this master handover and `docs/STATUS_CONSISTENCY_AUDIT.md` are synchronized to the dual-gate terminology and counts.

---

## 14. Raja Rani downstream disposition

No required Raja Rani production work remains inside `pugazg/kalaignar-cinema-works`.

Its verified Reading Room payload is:

`works/raja-rani/integrations/reading-room/reading-room.json`

Payload SHA-256: `ab1058cb5a22ba78e68938f50efc586cc53eb07ef544bdf3919bb3c4b8c46c9b`.

Only when the separate Kalaignar Digital Library / Reading Room implementation repository is explicitly authorized for modification should that payload be applied there. The public site must preserve source-numbered songs separately from archival-only screenplay scene navigation, retain provenance, and keep song authorship/performance-link evidence tiers unchanged.

For repository-internal work, continue with another work's documented next activity rather than reopening Raja Rani solely to create an additional standalone format.

---

## 15. Manthiri Kumari downstream disposition

No required Manthiri Kumari production work remains inside `pugazg/kalaignar-cinema-works`.

Its verified Reading Room payload is:

`works/manthiri-kumari/integrations/reading-room/reading-room.json`

Payload size: **15,704 bytes**.  
Payload SHA-256: `20a0db293b936757e7d01def336252f28543337f319dfae6ad7bf5ae886bab43`.

The payload preserves **1 continuous story summary + 15 performance blocks**, source/page provenance, source-visible cues, the **1 confirmed current-anthology witness / 14 source-only** disposition, and the **0 verified / 15 unresolved** item-level lyric-authorship state. Performance ordinals remain archival source-order navigation rather than printed source numbering, and no screenplay scenes are invented.

Only when the separate Kalaignar Digital Library / Reading Room implementation repository is explicitly authorized for modification should this payload be applied there. Site application status remains **not-applied**.

---

## 16. Ammayappan active checkpoint

Work path: `works/ammaiyappan/`  
Source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

- canonical first pass: **105/105 draft-complete**;
- assembly QA: **PASS — 105 anchors / 0 missing / 0 duplicate**;
- visual source-fidelity: **80/105 — PDF 5–84 / logical pp.3–82 passed**;
- historical-Tamil-glyph audit: **80/105 — PDF 5–84 / logical pp.3–82 passed**;
- final dual-gate Tamil verified: **80/105**;
- retrospective glyph backfill: **PDF 5–74 CLOSED**;
- forward PDF 75–84 combined audit: **10/10 PASS**, commit `0da97f94e829bef9b387bf59be580933b97ed122`;
- remaining range: **PDF 85–109 = 25 pages**;
- open first-pass uncertainty markers: **19 — markers 98–116**;
- structured derivatives / English / reader: **blocked pending 105/105 dual-gate verified Tamil**.

**Exact next activity:** resume at **PDF 85 / logical printed p.83**, performing rendered-scan visual source-fidelity verification and the historical-Tamil-glyph audit together; adjudicate markers 98–116 only from source evidence.
