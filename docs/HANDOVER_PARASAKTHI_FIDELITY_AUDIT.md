# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

Current stage: **Structured Derivatives — scene, dialogue and character indexes complete; per-song authorship gate next**.

## Canonical source state

- Source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- 58 PDF pages; PDF 4–57 / printed pp.3–56 are canonical dialogue/song pages; PDF 58 is back matter.
- Tamil canonical text: **54 verified / 0 review / 0 unresolved markers**.
- Never repair Tamil from film audio, subtitles, web copies, later editions or memory.

Final reviewer-assisted Part 01 readings remain:

- PDF 5: `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?`
- PDF 16: `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

## Scene structure — complete

- **46 observed canonical scenes**.
- Scene **23 absent**.
- Scene **34 absent**.
- PDF 49 source heading **48** → canonical scene **43**.
- PDF 57 source heading **43** → canonical final scene **48**.
- Scene 30 crosses PDF 35→36 across the Part 01 / Part 02 transcription-file boundary.
- Scene 33 spans PDF 38→42 because scene 34 is absent.
- All **46/46 observed scene derivatives are complete**.

## Dialogue index — complete-verified

Files:

- `works/parasakthi/dialogues/schema.json`
- `works/parasakthi/dialogues/index.json`
- `works/parasakthi/dialogues/records/scene-XX.json`

Final state:

- Observed scenes represented: **46 / 46**
- Dialogue records: **642**
- Zero-record observed scenes: **26, 29, 48**
- Missing headings: **23, 34**
- Existing dialogue records are immutable derivatives and must not be rewritten by later indexes.

The complete dialogue index has **11 verified cross-page records**:

- `parasakthi-s001-d001` — PDF 4→5
- `parasakthi-s009-d001` — PDF 12→13
- `parasakthi-s013-d023` — PDF 16→17
- `parasakthi-s028-d023` — PDF 33→34
- `parasakthi-s033-d053` — PDF 41→42
- `parasakthi-s042-d001` — PDF 48→49
- `parasakthi-s043-d003` — PDF 49→50
- `parasakthi-s043-d017` — PDF 50→51
- `parasakthi-s045-d001` — PDF 51→53
- `parasakthi-s045-d003` — PDF 53→54
- `parasakthi-s045-d018` — PDF 54→55

Source-label punctuation anomalies remain preserved in dialogue records:

- `parasakthi-s021-d040`
- `parasakthi-s025-d011`
- `parasakthi-s025-d017`

## Character index — complete-verified

Files:

- `works/parasakthi/characters/README.md`
- `works/parasakthi/characters/schema.json`
- `works/parasakthi/characters/labels-inventory.json`
- `works/parasakthi/characters/entities-pilot.json`
- `works/parasakthi/characters/entities.json`
- `works/parasakthi/characters/index.json`

### Final coverage

All **642 dialogue records** were surveyed for exact `speaker_label` values.

- Distinct exact source labels: **69**
- Explicit label dispositions: **69 / 69**
- Unmapped labels: **0**
- Entities: **48**
- Verified entities: **46**
- Review entities: **1**
- Unresolved entities: **1**
- Labels attached to verified entities: **66**
- Review labels: **1** — `ராக`
- Unresolved labels: **2** — `நொண்டி`, `நொ`
- Dialogue records modified by character indexing: **0**

### Character mapping rules that remain controlling

1. Never modify exact dialogue `speaker_label` values.
2. Character normalization belongs only in the character derivative.
3. Similar spelling alone does not prove identity.
4. Generic source labels may be represented as role/collective categories rather than one continuing person.
5. Ambiguity remains explicit rather than guessed away.
6. `supporting_records` are representative evidence anchors.

### Important completed decisions

- `குரல்` → **குணசேகரன்**: scene 43 explicitly locates the voice behind the goddess image and immediately has Gunasekaran emerge from there.
- `நாரா` → **நாராயணப் பிள்ளை**: scene 30 explicitly gives `ஜெனரல் மெர்ச்சண்ட் நாராயணப் பிள்ளை`.
- `காந்` / `காந்தா` → **காந்தா**.
- `பார்` / `பார்வதி` → **பார்வதி**.
- `கருப்` → **கருப்பன்**.
- `குப்` → **குப்பன்**.
- `நீதி` remains a **judge role**, not globally merged into சந்திரசேகரன், because the source does not explicitly identify every judicial occurrence as that same person.
- `டாக்டர்` / `டாக்`, `வியாபாரி` / `வியா`, `வீட்டுக்` / `வீட்`, and `பிச்சை` / `பிச்` are occupational-role categories; grouping does not assert one individual across unrelated scenes.
- `1வது` vs `1—வது` and `2வது` vs `2—வது` remain separate scene-specific ordinal roles.
- `ராக` → display form **இராகவன்** remains `review` / medium confidence because the source prints the vocative `இராகவா` and the nominative display form is a grammatical normalization.
- `நொண்டி` / `நொ` remain explicit unresolved labels. Scene 37 proves the speaker is Kalyani's brother but does not explicitly identify which brother; do not force a merge into ஞானசேகரன்.

## Exact next work — per-song authorship gate

`docs/ARCHIVAL_WORKFLOW.md` controls this stage: a song inside a Kalaignar-credited dialogue booklet is **not automatically a Kalaignar lyric**. Song-specific files require an explicit authorship field and source; if a song cannot be disambiguated, authorship must remain `unresolved`.

Before creating song-specific derivatives:

1. read current `works/parasakthi/mapping.md`, canonical transcription parts, and the booklet credits page;
2. inventory every song/verse block in canonical order with PDF/printed-page provenance and scene context;
3. distinguish unlabelled songs from explicitly speaker-labelled sung/verse dialogue already present in the dialogue index;
4. transcribe the printed lyric/song contributor credits exactly as source metadata;
5. attempt item-level authorship resolution using the booklet first;
6. if the booklet does not identify which lyricist wrote a particular block, set authorship `unresolved` unless a separately documented reliable source resolves it;
7. outside sources may resolve authorship metadata but must never alter canonical Tamil wording;
8. only after authorship disposition exists should individual song files or English song translations be created.

Known song/verse locations from the structural map include material around PDF pages **4, 8, 11–12, 14, 20–21, 31–32, 35, 40, 44–45, 56–57**. Treat this as a location aid, not as a complete authorship determination; verify each block against the canonical text and credits.

Recommended first song-authorship checkpoint:

- create `works/parasakthi/songs/README.md` if needed;
- define `songs/schema.json`;
- create an inventory of all candidate song/verse blocks with source page/scene provenance and provisional type (`unlabelled-song`, `speaker-labelled-verse`, `other-verse`);
- record booklet-wide lyric contributor credits separately from item-level authorship;
- do **not** infer per-song author from booklet-wide credits.

## Other stages

- Structural mapping: verified
- Canonical Tamil transcription: verified
- Tamil fidelity audit: complete
- Scene index: complete
- Scene text derivatives: complete
- Dialogue index: complete-verified
- Character index: complete-verified
- Per-song authorship mapping: **not-started — next**
- English translation: not-started
