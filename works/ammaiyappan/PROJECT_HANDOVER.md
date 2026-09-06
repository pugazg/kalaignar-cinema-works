# Project handover — அம்மையப்பன்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/ammaiyappan/`

## Live-main rule

Treat live GitHub `main` and the rendered controlling scan as authoritative over copied checkpoints. Preserve newer durable work; do not reset or repeat completed phases because an older handover says otherwise.

## Controlling source

`TVA_BOK_0064230_அம்மையப்பன்.pdf`

- PDF pages: **111**;
- bytes: **154,237,539**;
- SHA-256: `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`;
- image-only scan;
- main screenplay/dialogue: **PDF 5–109 / logical printed pp.3–107**;
- PDF 110–111: advertisement/back matter.

Printed identity: `அம்மையப்பன்`; `கதை வசனம்` / `மு. கருணாநிதி`; `முதற் பதிப்பு`, `செப்டம்பர், 1954`; `முரசொலி பதிப்பகம்`, `சென்னை-14`.

## Mandatory startup

Before changing this work, read completely:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
3. `docs/ARCHIVAL_WORKFLOW.md`
4. `docs/SOURCE_POLICY.md`
5. `docs/TRANSCRIPTION_GUIDE.md`
6. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
7. `docs/STATUS_CONSISTENCY_AUDIT.md`
8. `works/ammaiyappan/README.md`
9. this `works/ammaiyappan/PROJECT_HANDOVER.md`
10. `works/ammaiyappan/NEXT_CHAT_PROMPT.md`
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
24. verified translation records through the current checkpoint.

Also inspect any newer work-local audit/status file added after this handover.

## Closed source authority

### Canonical Tamil / scene layer

- visual fidelity: **105/105 PASS**;
- historical-glyph audit: **105/105 PASS**;
- final dual-gate Tamil: **105/105 complete-verified**;
- unresolved canonical markers: **0**;
- PDF 10 direct-scan correction: **`மாடம்`**, commit `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`;
- source-numbered scenes: **none**;
- source-visible structural boundaries: **63**;
- distinct verified heading forms: **41**;
- archive-only scene derivatives: **63/63 complete-verified**;
- boundary ownership: **PASS — 0 gaps / 0 overlaps / 105 pages represented**;
- PDF 56 / printed 54: `பழுதார் வீதி`;
- PDF 107 / printed 105: **`தூக்குமேடை`**; reject `தாக்குமேடை`.

### Dialogue / character layer

The post-closure scene-3 source form `பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......` is a distinct பூங்காவனம் dialogue unit with its semicolon preserved. Scene 5 `திரு; ...` is the other source-explicit non-colon form. Neither may be normalized to a colon.

Current authority:

- explicit colon-labelled dialogue records: **1,009**;
- source-role supplements: **16**;
- downstream dialogue units: **1,025**;
- exact source speaker labels: **62**;
- unresolved source-role blocks: **0**;
- source punctuation normalizations: **0**;
- character entities / role categories: **26**;
- exact-label coverage: **62/62**;
- downstream dialogue coverage: **1,025/1,025**;
- record-aware `முத்`: **80 → முத்தன் / 97 → முத்தாயி**;
- record-aware `தன`: **1 → தனபதி / 9 → தனவணிகர்**.

Character identity is an English aid only; exact Tamil labels remain provenance authority.

### Song / verse / performance gate

- candidates reviewed: **64/64**;
- retained source-visible occurrences: **5** — archival scenes **7, 10, 19, 40, 59**;
- unresolved authorship occurrences: **3**;
- source-attributed literary quotation: **1**;
- authorship-not-applicable character japa: **1**;
- complete named lyric bodies printed: **0**;
- standalone Tamil lyric derivatives: **0**.

Do not promote `கதை வசனம் / மு. கருணாநிதி` into lyric authorship and do not import absent lyrics from film audio, websites, subtitles, later editions or memory.

## English translation — ACTIVE through scene 55

Current verified checkpoint:

- scenes: **55/63**;
- verified units: **1,106/1,106**;
- dialogue units: **940** = **925 explicit immutable dialogue links + 15 source-role supplements**;
- stage/action units: **163**;
- standalone song-reference units: **2**;
- japa units: **1**;
- cross-page units: **25**;
- unique source-visible song/performance occurrence links: **4** — `ammaiyappan-song-001` through `ammaiyappan-song-004`;
- canonical Tamil/dialogue/character/song evidence changed by English: **no**;
- reader/export: **blocked pending complete English**.

Current files include `translations/records/scene-001.json`–`scene-055.json`, all prior batch reviews, `BATCH_051_055_REVIEW.md`, and `translations/index.json`.

## Batch 51–55 safeguards

Batch 51–55 is **71/71 verified units**:

- 57 explicit dialogue links;
- 0 source-role supplements;
- 14 separate stage/action units;
- 2 cross-page units — `ammaiyappan-en-s051-u003` and `ammaiyappan-en-s052-u032`;
- 0 retained song/performance occurrences;
- 0 frozen source files modified.

Important decisions:

- scene 51 keeps the cross-page Sukhadev record whole across PDF 89→90 / printed 87→88;
- scene 52 preserves coercive sexual rhetoric without euphemism, keeps source-owned parentheticals/actions inside immutable dialogue, retains the printed Sita/Kannagi/Silappathikaram references without external expansion, transliterates uncertain `காப்பாரியிலே` as `kāppāri`, and keeps `ammaiyappan-s052-d027` whole across PDF 92→93 / printed 90→91;
- scene 52 preserves the rhetorical triad `கடமை, கண்ணியம், கட்டுப்பாடு` as **Duty, Dignity and Discipline** while leaving frozen source clusters unrepaired;
- scene 53 keeps `(மூர்ச்சை தெளிந்து)` dialogue-owned, preserves `ஊடல்` register and the source's bitterly sarcastic sexual-coercion rhetoric, retains frozen `வெள்ளாட்டி` as `vellatti`, and does not claim a repair for the irregular final marriage phrase;
- scene 54 keeps `நாமார்க்கும் குடியல்லோம்: நமனை அஞ்சோம்!` inside Vedalam's immutable dialogue rather than creating a new literary-verse or song occurrence;
- scene 55 translates the immediate execution order without adding legal/procedural detail;
- the closed source-role layer contributes no supplement in scenes 51–55 and the closed song/performance inventory contributes no retained occurrence there.

Earlier safeguards remain active, including scene-40 japa occurrence handling: `ammaiyappan-song-004` is a character japa cue, not a soundtrack song, and no title/lyrics/authorship are reconstructed.

Translation must preserve archive scene ID, PDF/printed-page provenance, exact speaker labels, source-role origin, cross-page ownership, source rhetoric/register and the closed song/performance evidence.

## Exact next activity

> **Fetch live `main`; confirm the English checkpoint is 55/63 scenes and 1,106 verified units; then translate and source-review archival scenes 56–60 from the frozen verified derivatives. Inspect the live closed source-role and song/performance layers before writing: scene 59 contains `ammaiyappan-s059-r001`, which must remain `source-context-attributed`, and retained occurrence `ammaiyappan-song-005`. Link the occurrence only to source-visible material; do not reconstruct its absent lyric body, title or authorship and do not merge unnamed song identities without stronger evidence. Preserve exact Tamil speaker labels and PDF/printed-page provenance, keep cross-page units whole, and do not modify frozen Tamil/dialogue/character/song evidence. After the batch synchronize translation/work/repository status mirrors and refresh this handover and `NEXT_CHAT_PROMPT.md`.**