# Next Chat Prompt — அம்மையப்பன்

Continue the Kalaignar Cinema Works archival project directly in:

`pugazg/kalaignar-cinema-works`

Branch: `main`  
Active work: `works/ammaiyappan/` — **அம்மையப்பன்**

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work. Never reset, repeat, or reopen completed phases because this copied prompt contains an older checkpoint.

If `main` has advanced beyond the checkpoint recorded when this prompt was refreshed, the newer state controls.

## CONTROLLING SOURCE

`TVA_BOK_0064230_அம்மையப்பன்.pdf`

- PDF pages: **111**;
- bytes: **154,237,539**;
- SHA-256: `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`;
- image-only scan;
- canonical screenplay/dialogue: **PDF 5–109 / logical printed pp.3–107**;
- PDF 110–111: advertisement/back matter.

The rendered scan controls canonical Tamil. Do not reopen scan-level transcription or historical-glyph decisions without new source-backed evidence. For routine English continuation, the PDF does not need to be reattached unless a genuine scan-level ambiguity must be revisited.

## CURRENT CLOSED SOURCE AUTHORITY

### Canonical Tamil

- visual source fidelity: **105/105 PASS**;
- historical-Tamil-glyph verification: **105/105 PASS**;
- final dual-gate Tamil: **105/105 complete-verified**;
- unresolved canonical markers: **0**;
- locked PDF 107 heading: **`தூக்குமேடை`**; rejected `தாக்குமேடை` must not reappear.

### Scene derivatives

- canonical source-visible boundaries: **63**;
- distinct verified heading forms: **41**;
- archive-only scene derivatives: **63/63 complete-verified**;
- boundary ownership: **PASS — 0 gaps / 0 overlaps**;
- canonical pages represented: **105/105**;
- source-numbered scenes invented: **0**.

### Dialogue layer — corrected authority

- explicit colon-labelled records: **1,009**;
- source-role supplements: **16**;
- downstream dialogue units: **1,025**;
- exact source speaker labels: **62**;
- unresolved source-role blocks: **0**;
- source punctuation normalization: **0**.

The scene-3 source form `பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......` is a distinct பூங்காவனம் unit. The semicolon is source evidence and must not be normalized or swallowed into the preceding பலதேவர் utterance.

The other preserved source-explicit non-colon speaker form is scene 5 `திரு; ...`; preserve that semicolon too.

### Character/entity layer

- stable entities / role categories: **26**;
- exact-label coverage: **62/62**;
- downstream dialogue-unit coverage: **1,025/1,025**;
- unresolved entities: **0**;
- `முத்` → **80 முத்தன் / 97 முத்தாயி**;
- `தன` → **1 தனபதி / 9 தனவணிகர்**.

Use this only as a derivative identity aid. Exact Tamil labels remain provenance authority.

### Song / verse / performance gate

- candidates reviewed: **64/64**;
- retained source-visible occurrences: **5**;
- unresolved authorship occurrences: **3**;
- source-attributed literary quotation occurrences: **1**;
- authorship-not-applicable japa occurrences: **1**;
- complete named song lyric bodies printed: **0**;
- standalone Tamil lyric files: **0**.

Do not promote `கதை வசனம் / மு. கருணாநிதி` into lyric authorship. Do not reconstruct absent lyrics or verse from film audio, websites, subtitles, later editions or memory.

## ENGLISH TRANSLATION — CURRENT CHECKPOINT

The English schema/plan is already established. Do **not** recreate it.

Authoritative translation files include:

- `translations/schema.json`
- `translations/preflight.json`
- `translations/index.json`
- `translations/PILOT_REVIEW.md`
- `translations/BATCH_002_005_REVIEW.md`
- `translations/BATCH_006_010_REVIEW.md`
- `translations/BATCH_011_015_REVIEW.md`
- `translations/records/scene-001.json` through `scene-015.json`

Current verified English checkpoint:

- scenes verified: **15/63**;
- verified units: **355**;
- dialogue units: **303** = **295 explicit dialogue records + 8 source-role supplements**;
- stage/action units: **51**;
- standalone song-reference units: **1**;
- cross-page units: **3**;
- source-only song/performance occurrence links encountered through scene 15: **2** — `ammaiyappan-song-001`, `ammaiyappan-song-002`;
- canonical Tamil/dialogue/character/song evidence changed by English: **no**.

Batch 11–15 specifically establishes:

- scene 11: `ammaiyappan-s011-r001` and `ammaiyappan-s011-r002` remain source-context-attributed supplements; neither becomes a printed speaker label;
- scene 11: the final fight narration, including the embedded warning to Muthan, remains scene narration rather than duplicate immutable dialogue;
- scene 15: `ammaiyappan-s015-d001` (`குரல்`) remains one cross-page English unit across PDF 31→32 with both page segments;
- difficult frozen forms such as `பாரிக்கா`, `மால் நன்னோரம்`, `அகாதி`, `திருக்கிட்டு` and the fragmentary scene-15 opening are not silently repaired;
- the closed source-only song inventory has no retained occurrence in scenes 11–15.

Earlier safeguards remain active:

- scene 3 `பூங் ; ...` → source-explicit non-colon provenance;
- scene 5 `திரு; ...` → source-explicit non-colon provenance;
- scene 7 `ammaiyappan-song-001` → printed performance cue only, no absent title/lyrics;
- scene 10 `ammaiyappan-song-002` → Kambar-attributed printed fragment linked inside its immutable dialogue record, no duplicate verse unit.

## MANDATORY STARTUP

Before further changes, read the current versions of:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
3. `docs/ARCHIVAL_WORKFLOW.md`
4. `docs/SOURCE_POLICY.md`
5. `docs/TRANSCRIPTION_GUIDE.md`
6. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
7. `docs/STATUS_CONSISTENCY_AUDIT.md`
8. `works/ammaiyappan/README.md`
9. `works/ammaiyappan/PROJECT_HANDOVER.md`
10. this `works/ammaiyappan/NEXT_CHAT_PROMPT.md`
11. `works/ammaiyappan/metadata.yaml`
12. `works/ammaiyappan/scenes/index.json`
13. `works/ammaiyappan/dialogues/final-index.json`
14. `works/ammaiyappan/dialogues/source-role-resolved-records.json`
15. `works/ammaiyappan/characters/index.json`
16. `works/ammaiyappan/characters/entities.json`
17. `works/ammaiyappan/songs/index.json`
18. `works/ammaiyappan/songs/inventory.json`
19. `works/ammaiyappan/translations/README.md`
20. `works/ammaiyappan/translations/index.json`
21. `works/ammaiyappan/translations/schema.json`
22. `works/ammaiyappan/translations/PILOT_REVIEW.md`
23. all completed `works/ammaiyappan/translations/BATCH_*_REVIEW.md` files
24. verified translation records already completed through scene 15.

Also inspect any newer Ammaiyappan audit/status file added after this prompt.

## TRANSLATION RULES

- Translate from verified Tamil evidence only.
- Preserve archive scene ID and PDF/printed-page provenance.
- Keep exact Tamil speaker labels and source-role origin in metadata.
- Do not rewrite source semicolons as Tamil colons.
- Keep cross-page source units whole.
- Preserve dialogue, stage direction, narration/action, verse/performance, japa and written-text distinctions.
- Do not silently modernize, censor, euphemize, expand, repair or improve the source.
- Preserve rhetorical force, repetition, social register, irony, religious/political vocabulary and deliberate roughness.
- When one English equivalent would be irresponsible, transliterate the key term and add a concise translator note.
- Preserve source uncertainty as uncertainty.
- Translate only source-visible song/verse/performance material authorized by the closed source gate.
- If an occurrence is embedded inside an immutable dialogue record, link the occurrence in that unit rather than duplicating the same source span.
- Decorative `★` is structural and must not become invented prose.
- Archive scene IDs are derivative navigation only; do not present them as printed scene numbers.

## DO NOT REOPEN

Unless live `main` contains newer explicit source-backed evidence, do not redo:

- the 105/105 Tamil transcription;
- historical-glyph verification;
- 63-scene segmentation;
- dialogue extraction;
- `முத்` / `தன` identity audits;
- character/entity reconciliation;
- song/performance source-authorship gate;
- already verified English scenes 1–15.

If English work exposes a genuine source defect, isolate it as a post-closure correction and repair only the smallest affected derivative chain with dependent QA.

## EXACT NEXT ACTIVITY

> **Fetch live `main`; confirm the English checkpoint is 15/63 scenes and 355 verified units; then translate and source-review archival scenes 16–20. Preserve the two closed source-role supplements in scene 17. Scene 19 contains `ammaiyappan-song-003`, a source-visible cue that Muthan is singing; translate only that printed cue and do not reconstruct a title or lyric body. Keep exact speaker/page provenance and cross-page units whole. After the batch synchronize `translations/index.json`, translation QA, work-local status, `data/works.json`, root/master status mirrors, this prompt, and report the new live HEAD.**
