# Project handover — அம்மையப்பன்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/ammaiyappan/`

## Live-main rule

Treat live GitHub `main` and the rendered controlling scan as authoritative over copied checkpoints. Preserve newer durable work; do not reset or repeat completed phases because an older prompt says otherwise.

## Current authority — post-closure dialogue correction

The scene-3 source form `பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......` is a distinct பூங்காவனம் dialogue unit with its source semicolon preserved. It is represented in `dialogues/source-role-resolved-records.json` and must not be swallowed into the preceding பலதேவர் utterance.

Current downstream structured authority:

- explicit colon-labelled dialogue records: **1,009**;
- source-role-resolved dialogue supplements: **16**;
- downstream dialogue units: **1,025**;
- exact source speaker-label strings: **62**;
- unresolved source-role blocks: **0**;
- source punctuation normalization: **0**;
- character/entity coverage: **1,025/1,025**;
- exact-label coverage: **62/62**.

The other preserved source-explicit non-colon form is scene 5 `திரு; ...`. Neither semicolon may be normalized to a colon.

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
9. `works/ammaiyappan/PROJECT_HANDOVER.md`
10. `works/ammaiyappan/NEXT_CHAT_PROMPT.md`
11. `works/ammaiyappan/metadata.yaml`
12. `works/ammaiyappan/transcription/index.json`
13. `works/ammaiyappan/transcription/full-text.md`
14. `works/ammaiyappan/notes/FINAL_TAMIL_QA.md`
15. `works/ammaiyappan/scenes/index.json`
16. `works/ammaiyappan/notes/scene-boundary-ownership-qa.md`
17. `works/ammaiyappan/dialogues/final-index.json`
18. `works/ammaiyappan/dialogues/source-role-resolved-records.json`
19. `works/ammaiyappan/notes/dialogue-final-qa.json`
20. `works/ammaiyappan/characters/index.json`
21. `works/ammaiyappan/characters/entities.json`
22. `works/ammaiyappan/characters/labels-inventory.json`
23. `works/ammaiyappan/characters/record-aware-dispositions.json`
24. `works/ammaiyappan/characters/muth-record-dispositions.json`
25. `works/ammaiyappan/songs/index.json`
26. `works/ammaiyappan/songs/inventory.json`
27. `works/ammaiyappan/songs/candidate-disposition.json`
28. `works/ammaiyappan/songs/credits.json`
29. `works/ammaiyappan/translations/README.md`
30. `works/ammaiyappan/translations/preflight.json`
31. `works/ammaiyappan/translations/schema.json`
32. `works/ammaiyappan/translations/index.json`
33. `works/ammaiyappan/translations/PILOT_REVIEW.md`
34. completed `works/ammaiyappan/translations/BATCH_*_REVIEW.md` files

Also inspect any newer work-local audit/status file added after this handover.

## Controlling source

`TVA_BOK_0064230_அம்மையப்பன்.pdf`

- PDF pages: **111**;
- bytes: **154,237,539**;
- SHA-256: `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`;
- image-only scan;
- main screenplay/dialogue: **PDF 5–109 / logical printed pp.3–107**;
- PDF 110–111: advertisement/back matter.

Printed identity: `அம்மையப்பன்`; `கதை வசனம்` / `மு. கருணாநிதி`; `முதற் பதிப்பு`, `செப்டம்பர், 1954`; `முரசொலி பதிப்பகம்`, `சென்னை-14`.

## Structural/source locks

- source-numbered scenes: **none**;
- canonical source-visible boundaries used by the scene derivative layer: **63**;
- distinct verified heading forms in the current derivative mapping: **41**;
- archive scene ordinals are derivative navigation only;
- preserve additional source-visible local headings found during transcription even if an earlier intake ledger is narrower;
- PDF 56 / p.54: **`பழுதார் வீதி`**;
- PDF 107 / p.105: **`தூக்குமேடை`** — direct user verdict; reject `தாக்குமேடை`.

## Canonical Tamil and scene-text derivatives — CLOSED

Canonical Tamil:

- visual fidelity: **105/105 PASS**;
- historical glyph audit: **105/105 PASS**;
- final dual-gate Tamil: **105/105 complete-verified**;
- unresolved canonical markers: **0**;
- post-fidelity direct-scan correction: PDF 10 heading `மாடம்`, commit `a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9`.

Scene layer:

- segmentation preflight: **PASS — 63 source-visible canonical boundaries**;
- earlier intake ledger: **58/58 reconciled**;
- canonical additions beyond intake: **5**;
- archive-only scene files: **63/63 complete-verified**;
- source scene numbers invented: **0**;
- boundary ownership QA: **PASS — 0 gaps, 0 overlaps**;
- canonical page representation: **105/105 — PDF 5–109**;
- scene derivative commit: `6a764137616879d08f5a1ff14431caafa87b11eb`.

## Phase gates

- source/canonical Tamil gates: **closed**;
- scene-text derivatives: **closed-verified**;
- dialogue index: **complete-source-role-resolved — 1,025/1,025 downstream units**;
- character/entity index: **complete-verified-reconciled — 26 entities / 62 exact labels / 1,025 units**;
- song/performance authorship gate: **complete-verified-source-only — 64/64 candidates reviewed; 5 retained occurrences; 0 standalone lyric files**;
- English translation: **verified through scene 30/63 — 738/738 current units**;
- reader/export: **blocked pending complete English**.

## Dialogue-index closure — FINAL QA PASS, post-correction authority

- explicit colon-labelled records: **1,009**;
- exact source speaker-label strings: **62**;
- reviewed cross-page continuation candidates: **20/20 PASS**;
- source-role residual review: **complete**;
- source-role-resolved dialogue supplements: **16**;
- non-dialogue resolved source units: **6**;
- downstream dialogue units: **1,025**;
- unresolved source-role blocks: **0**;
- source scene numbers invented: **0**;
- alias normalization: **0**;
- source punctuation normalization: **0**;
- exceptional source delimiters `பூங் ; ...` and `திரு; ...`: preserved exactly;
- final authority: `dialogues/final-index.json` plus `dialogues/source-role-resolved-records.json`;
- final QA: `notes/dialogue-final-qa.json` plus the explicit post-closure semicolon repair history.

The scene-3 semicolon correction increased the earlier closure checkpoint from 1,024 to **1,025** downstream units and from 15 to **16** supplements. Historical commits/audit prose may record the earlier checkpoint, but active status must use the corrected totals.

## Character/entity closure — FINAL QA PASS, post-correction authority

- downstream dialogue units dispositioned: **1,025/1,025**;
- exact source speaker labels dispositioned: **62/62**;
- stable entities / role categories: **26**;
- verified entities: **26**;
- review entities: **0**;
- unresolved entities: **0**;
- record-aware exact labels: **2** — `முத்`, `தன`;
- record-aware units: **187**;
- `முத்`: **80 → முத்தன் / 97 → முத்தாயி**;
- `தன`: **1 → தனபதி / 9 → தனவணிகர்**;
- dialogue records modified by character reconciliation: **no**.

Use this layer only as an identity aid in English. Exact Tamil source labels remain the provenance authority.

## Song / verse / performance authorship closure — FINAL SOURCE GATE

- preflight candidate hits reviewed: **64/64**;
- retained source-visible occurrences: **5**, in archival scenes **7, 10, 19, 40 and 59**;
- unresolved authorship occurrences: **3**;
- source-attributed literary quotation occurrences: **1**;
- authorship-not-applicable japa occurrences: **1**;
- complete named song lyric bodies printed by the booklet: **0**;
- standalone Tamil lyric files authorized / created: **0 / 0**;
- external item-level evidence used: **no**;
- canonical Tamil changed by this gate: **no**.

The booklet's printed `கதை வசனம் / மு. கருணாநிதி` credit is not promoted into lyric authorship. English may translate only source-visible performance references, literary fragments, japa tokens and cues; absent song lyrics must not be reconstructed from film audio, websites, subtitles, later editions or memory.

## English translation — ACTIVE

Current files include:

- `translations/schema.json` — locked scene/unit schema;
- `translations/preflight.json` — authority and pilot preflight;
- `translations/records/scene-001.json`–`scene-030.json` — verified translations through scene 30;
- `translations/PILOT_REVIEW.md`;
- `translations/BATCH_002_005_REVIEW.md`;
- `translations/BATCH_006_010_REVIEW.md`;
- `translations/BATCH_011_015_REVIEW.md`;
- `translations/BATCH_016_020_REVIEW.md`;
- `translations/BATCH_021_025_REVIEW.md`;
- `translations/BATCH_026_030_REVIEW.md`;
- `translations/index.json` — active translation checkpoint.

Cumulative verified checkpoint through scene 30:

- verified scenes: **30/63**;
- verified units: **738**;
- dialogue units: **627** = **614 explicit immutable dialogue links + 13 source-role supplements**;
- stage/action units: **109**;
- standalone song-reference units: **2**;
- cross-page units: **16**;
- source-visible song/performance occurrence links so far: **3** — `ammaiyappan-song-001`, `ammaiyappan-song-002`, `ammaiyappan-song-003`;
- canonical Tamil/dialogue/character/song evidence changed by English: **no**.

Batch 26–30 establishes these additional decisions:

- the prior scene-25 handoff statement claiming zero source-role supplements in scenes 26–30 was stale; live `dialogues/source-role-resolved-records.json` controls and contains `ammaiyappan-s027-r001`, `ammaiyappan-s027-r002` and `ammaiyappan-s030-r001`;
- those three records remain `source-context-attributed` derivative provenance and are never promoted into printed colon-labelled speech;
- scene 26 keeps `ammaiyappan-s026-d010` whole across PDF 55→56 and preserves the source's political metaphor chain without normalizing frozen `தோற்ப்பும்வரை`;
- scene 27 keeps `ammaiyappan-s027-d017` whole across PDF 57→58 and retains immutable `ammaiyappan-s027-d022` ownership even though its source text contains the slap cue plus additional `முத்தாயி? அத்தான்!...` tokens;
- scene 29 keeps `ammaiyappan-s029-d022` and `ammaiyappan-s029-d035` whole across their page boundaries, preserves ritual/register terms such as `thali` and `guru-puja`, and does not repair frozen `அவள் உங்க அப்பா...அதனால்!`;
- scene 30 keeps its long Purananuru poem inside immutable dialogue record `ammaiyappan-s030-d007`; the English uses semantic-poetic translation but does not create a second verse owner or import external Purananuru text/attribution;
- scene 30's final unlabelled threat is linked through closed supplement `ammaiyappan-s030-r001`;
- the closed song/performance inventory has **no retained occurrence in scenes 26–30**, so no new song/performance occurrence link is introduced.

Translation must preserve archive scene ID and PDF/printed-page provenance, exact Tamil speaker labels, source-role origin, structural distinctions, rhetoric/register, and the closed song/performance evidence. It must not alter canonical Tamil or immutable dialogue evidence.

## Exact next activity

> **Translate and source-review archival scenes 31–35 from the frozen verified derivatives. The closed source-role layer contains one supplement in this range — `ammaiyappan-s035-r001`; the closed song/performance inventory has no retained occurrence in scenes 31–35. Preserve exact Tamil speaker labels, source-role origin and PDF/printed-page provenance, keep cross-page units whole, and do not modify frozen source evidence.**