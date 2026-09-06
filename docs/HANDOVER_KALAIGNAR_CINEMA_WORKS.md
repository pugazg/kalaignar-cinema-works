# Kalaignar Cinema Works — Master Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Primary branch: `main`  
Purpose: reusable handover for continuing the archive or onboarding a new Kalaignar cinema work

This is the project-level handover. **Live `main` is authoritative** over copied checkpoints and older handovers.

For a new work, read `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`, `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` when older Tamil typeforms occur, `docs/ARCHIVAL_WORKFLOW.md`, `docs/SOURCE_POLICY.md`, `docs/TRANSCRIPTION_GUIDE.md`, `docs/STATUS_CONSISTENCY_AUDIT.md`, and `docs/START_NEW_CINEMA_WORK_PROMPT.md`.

---

## 1. Project purpose and authority

This repository is a source-led archive of cinema writing credited to **Kalaignar M. Karunanidhi**. The scanned publication controls canonical text for the represented edition.

Authority order for textual questions:

1. rendered scan;
2. verified canonical Tamil;
3. verified scene/song/source-structure derivative;
4. immutable dialogue/song/etc. structured record;
5. translation;
6. reader/export/package;
7. website presentation.

A downstream layer must never silently repair an upstream layer. OCR, film audio, subtitles, web quotations, later editions, existing translations and memory are not canonical substitutes.

---

## 2. Reusable workflow

Proceed through these gates as applicable:

1. source intake;
2. structural mapping;
3. canonical Tamil first pass;
4. visual fidelity audit;
5. historical-Tamil-glyph audit where applicable;
6. scene/source-structure derivatives;
7. dialogue index;
8. character/entity index;
9. song/verse/performance authorship gate;
10. Tamil song derivatives only where full source text authorizes them;
11. English translation;
12. whole-work reader QA/export;
13. Reading Room integration;
14. optional standalone packaging only when separately useful/requested.

**Repository-wide status synchronization is a completion gate at every major phase.**

---

## 3. Rules that must survive every handover

- Preserve source-supported spelling, punctuation, exact speaker labels, scene-heading irregularities, repetition, code-switching, stage directions, performance structures and embedded texts.
- Historical Tamil glyph identity must be decoded from source evidence, not modern visual resemblance. Never global-replace historical glyph families.
- Scene numbering may be absent or irregular. Archive navigation IDs must never be presented as printed scene numbers.
- Unlabelled speech may receive downstream context attribution only when evidence supports it; this does not manufacture a printed label.
- Cross-page utterances remain one logical source unit with multi-page provenance.
- Decorative separators such as `★` or `* * *` are structural, not prose.
- Whole-work QA must catch duplicate derivative ownership.
- Story/dialogue credit is not lyric credit. Song authorship requires item-level evidence.
- Source-only performance cues stay source-only in English; absent lyrics must never be reconstructed.
- If a closed dialogue record owns embedded action or irregular internal text, keep that source ownership intact rather than splitting it for schema neatness.
- If a retained occurrence spans a performance cue and a separately labelled spoken token, each distinct printed span may be represented once while linking the same occurrence ID; do not duplicate a source span.

---

## 4. Repository-wide synchronization gate

At the end of each major phase reconcile at minimum:

### Work-local
- `works/<work-id>/metadata.yaml`;
- work README;
- active layer README/index/QA files;
- work-specific handover;
- next-chat prompt.

### Repository-wide
- `data/works.json`;
- root `README.md`;
- this master handover;
- `docs/STATUS_CONSISTENCY_AUDIT.md`;
- any shared guide whose reusable policy changed.

Historical checkpoint files may retain historical counts when clearly labelled historical.

---

## 5. Translation and reader architecture

For screenplay translation:

- use scene-sharded records;
- retain stable unit IDs and exact Tamil speaker labels;
- link explicit speech to immutable dialogue IDs;
- retain source-role origin for context-attributed supplements;
- preserve stage directions, written text, chants/japa, performance cues and other source structures distinctly;
- keep page provenance and cross-page units intact;
- link song/performance occurrence evidence without duplicating source spans;
- preserve source irregularity honestly.

Before declaring translation complete, perform whole-work reconciliation rather than trusting batch counts. Reader/export outputs should be generated from verified structured translation rather than maintained as an independent manual copy.

Non-scene sources must keep their natural model. For example, `மந்திரி குமாரி` uses one story-summary structure plus 15 performance blocks, not synthetic screenplay scenes.

---

## 6. Working style

When the user says **“Proceed with next activity”** and the next action is already documented:

- fetch live `main` first;
- continue without redundant questions;
- inspect authoritative source/derivative state;
- choose a meaningful bounded batch;
- fetch missing ranges if a large source read is truncated;
- complete source/content reconciliation and status synchronization before claiming completion;
- report exact commits/checkpoints.

A genuine source ambiguity can justify pausing; routine continuation does not.

---

## 7. Current high-level project checkpoint — 2026-09-06

- **Parasakthi** — complete-verified canonical/structured English reader work.
- **Tirumbippaar!** — complete-verified Tamil, structured derivatives, English translation, reader QA and deterministic EPUB QA. EPUB SHA-256 remains `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`.
- **Manohara** — complete-verified Tamil, 57/57 archival scenes, 983 dialogue records, 1,190 English units; reader/export QA PASS; Reading Room ready.
- **Kalaignar Thirai Isai Paadalgal** — 54/54 verified Tamil and English songs; reader/export and Reading Room payload QA PASS; site not applied.
- **Manthiri Kumari** — 12/12 canonical pages; one story-summary derivative + 15 performance records; English 13 story-summary units + 15 performances / 52 sections / 234 paired line-cues; bilingual reader and Reading Room payload QA PASS; item-level lyricist state remains 0 verified / 15 unresolved.
- **Raja Rani** — 79/79 source pages, 70/70 screenplay pages, 58/58 scene derivatives, 1,071 dialogues, 80 labels / 44 entities, 1,236 screenplay English units, 11/11 numbered songs / 181 line-cues; reader and Reading Room payload QA PASS.
- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **verified through scene 55/63 / 1,106 units**; next bounded batch **56–60**.

Current active mirrors use the corrected Ammayappan 1,025-unit source authority and scene-55 English checkpoint.

---

## 8. Ammayappan active checkpoint

Work: `works/ammaiyappan/`  
Source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

### Frozen source layers

- canonical Tamil: **105/105 dual-gate complete-verified**;
- PDF 10 source correction: `மாடம்`, commit `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`;
- source-visible boundaries / distinct heading forms: **63 / 41**;
- archive-only scene derivatives: **63/63**;
- boundary ownership: **PASS — 0 gaps / 0 overlaps / 105 pages**;
- dialogue index: **1,009 explicit + 16 supplements = 1,025 downstream units**;
- exact source speaker labels: **62**;
- unresolved source-role blocks / source punctuation normalizations: **0 / 0**;
- character/entity layer: **26 entities / 62/62 labels / 1,025/1,025 units**;
- song/performance gate: **5 retained occurrences**, scenes **7, 10, 19, 40, 59**; no full named lyric bodies and no standalone Tamil lyric files.

Post-closure delimiter authority remains unchanged: scene 3 `பூங் ; ...` and scene 5 `திரு; ...` are exact non-colon source forms.

### English through scene 55

- verified scenes: **55/63**;
- verified units: **1,106**;
- dialogue: **940** = **925 explicit + 15 source-role supplements**;
- stage/action: **163**;
- standalone song-reference: **2**;
- japa: **1**;
- cross-page: **25**;
- unique occurrence links: **4** — `ammaiyappan-song-001` through `ammaiyappan-song-004`;
- frozen Tamil/dialogue/character/song files modified by English: **no**;
- reader/export: blocked pending complete English.

### Batch 51–55 safeguards

Batch 51–55 is **71/71 verified units**: **57 explicit dialogue + 0 supplements + 14 stage/action**. New cross-page units are scene 51 `ammaiyappan-en-s051-u003` across PDF 89→90 / printed 87→88 and scene 52 `ammaiyappan-en-s052-u032` across PDF 92→93 / printed 90→91.

- Scene 51 keeps the cross-page Sukhadev record whole and preserves exact source labels.
- Scene 52 preserves coercive sexual rhetoric without euphemism, keeps source-owned embedded action/parenthetical cues inside immutable dialogue, and translates Sita/Kannagi/Silappathikaram references only as printed.
- Scene 52 retains uncertain `காப்பாரியிலே` by transliteration as `kāppāri`, handles other frozen irregular clusters with bounded notes rather than source repair, and preserves `கடமை, கண்ணியம், கட்டுப்பாடு` as **Duty, Dignity and Discipline**.
- Scene 53 keeps `(மூர்ச்சை தெளிந்து)` dialogue-owned, preserves `ஊடல்` register, retains frozen `வெள்ளாட்டி` as `vellatti`, and translates its bitterly sarcastic sexual-coercion rhetoric without euphemism or upstream repair.
- Scene 54 keeps `நாமார்க்கும் குடியல்லோம்: நமனை அஞ்சோம்!` embedded in Vedalam's immutable dialogue rather than manufacturing a separate literary-verse/song occurrence or importing an attribution.
- Scene 55 preserves the source's immediate execution order without adding procedure.
- The closed source-role layer contributes **0 supplements** in scenes 51–55; the closed song/performance inventory contributes **0 retained occurrences** there.

Earlier safeguards remain active. In particular, scene 40 `ammaiyappan-song-004` remains **character japa, not a soundtrack song**; no title, lyric body or lyricist is inferred.

**Exact next activity:** translate and source-review archival scenes **56–60** from the frozen verified derivatives. Scene 59 contains closed `source-context-attributed` supplement `ammaiyappan-s059-r001` and retained source-visible occurrence `ammaiyappan-song-005`. Preserve exact Tamil speaker labels and PDF/printed-page provenance, keep cross-page source units whole, and link the occurrence only to source-visible material. Do not reconstruct its absent lyrics, title or authorship and do not merge unnamed song identities without stronger evidence.

---

## 9. Downstream dispositions for completed works

- **Raja Rani:** no required repository-internal production work remains; its verified Reading Room payload should be applied only in the separate implementation repository when explicitly authorized.
- **Manthiri Kumari:** no required repository-internal production work remains; preserve its natural story-summary + 15-performance navigation and unresolved item-level authorship tiers when integrating externally.
- **Tirumbippaar!:** no required repository-internal translation/reader/package work remains.

The preferred public destination remains **`https://nenjukkuneethi.org/read` — Kalaignar Digital Library / Reading Room**.