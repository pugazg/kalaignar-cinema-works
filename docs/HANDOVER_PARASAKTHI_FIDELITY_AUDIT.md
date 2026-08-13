# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

Current stage: **Structured Derivatives — Tamil/source layers complete; English translation scene 1 verified and scenes 2–5 in review**.

## Canonical source state

- Source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- 58 PDF pages; PDF 4–57 / printed pp.3–56 are canonical dialogue/song pages; PDF 58 is back matter.
- Tamil canonical text: **54 verified / 0 review / 0 unresolved markers**.
- Never repair Tamil from film audio, subtitles, web copies, later editions, memory or English translation choices.

Final reviewer-assisted Part 01 readings remain:

- PDF 5: `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?`
- PDF 16: `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

## Completed Tamil/source derivatives

### Scene structure

- **46 observed canonical scenes**.
- Scene **23 absent**.
- Scene **34 absent**.
- PDF 49 source heading **48** → canonical scene **43**.
- PDF 57 source heading **43** → canonical final scene **48**.
- Scene 30 crosses PDF 35→36 across the Part 01 / Part 02 file boundary.
- Scene 33 spans PDF 38→42 because scene 34 is absent.
- Scene derivatives: **46/46 complete**.

### Dialogue index — complete-verified

- Records: **642** across all 46 observed scenes.
- Zero-record observed scenes: **26, 29, 48**.
- Cross-page records: **11**.
- Dialogue records are immutable derivatives for all later work.
- Exact source-label punctuation anomalies remain preserved in `parasakthi-s021-d040`, `parasakthi-s025-d011`, and `parasakthi-s025-d017`.

### Character index — complete-verified

- Distinct exact source labels: **69**.
- Explicit dispositions: **69/69**.
- Entities: **48**.
- Verified entities: **46**.
- Review label: `ராக`.
- Unresolved labels: `நொண்டி`, `நொ`.
- Do not force `நொண்டி` / `நொ` into ஞானசேகரன் without explicit source evidence.

### Song / verse layer — complete-verified

- Canonical song/verse occurrence records: **14**.
- Authorship verified: **14/14**.
- Soundtrack compositions: **11**.
- Source-faithful Tamil soundtrack derivatives: **11/11** under `works/parasakthi/songs/tracks/`.
- Separate quoted literary verse: **1** under `works/parasakthi/songs/quoted-verses/`.
- Scene 15 retains two canonical occurrence boundaries inside the one track `தேசம் ஞானம் கல்வி`.
- Scene 47 remains a reprise occurrence of scene 33's `புது பெண்ணின் மனதை`.
- Scene 28's Bharathidasan quotation remains outside the soundtrack set.

No canonical Tamil, scene file, dialogue record or character mapping has been modified by translation work.

## English translation layer — current checkpoint

Files:

- `works/parasakthi/translations/README.md`
- `works/parasakthi/translations/schema.json`
- `works/parasakthi/translations/index.json`
- `works/parasakthi/translations/records/scene-01.json`
- `works/parasakthi/translations/records/scene-02.json`
- `works/parasakthi/translations/records/scene-03.json`
- `works/parasakthi/translations/records/scene-04.json`
- `works/parasakthi/translations/records/scene-05.json`

Translation principles remain controlled by `translations/README.md` and `translations/schema.json`:

- Tamil remains authoritative.
- Every English unit is source-linked.
- Exact Tamil identifiers, including `speaker_label`, remain immutable metadata.
- Stage directions do not gain invented action.
- Dialogue preserves rhetorical force rather than being flattened for fluency.
- Songs use semantic-poetic translation, not singable rewriting.
- Translation status is independent of Tamil verification.
- English must never be used to retroactively repair Tamil.

### Scene 1 — verified

The four-unit pilot passed the fidelity/editorial review and is now **verified**:

1. `parasakthi-en-s001-u001` — opening stage direction.
2. `parasakthi-en-s001-u002` — `வாழ்க வாழ்கவே` / `parasakthi-song-001`.
3. `parasakthi-en-s001-u003` — transition stage direction.
4. `parasakthi-en-s001-u004` — dialogue `parasakthi-s001-d001`, exact label `தங்கப்பன்`, PDF 4→5 / printed pp.3→4.

Retain these reviewed decisions:

- `இரங்கூன்` → `Rangoon`; `மலேயா` → `Malaya`.
- `இலங்கை தீவு` → `the island of Ceylon` as a period-readable English rendering only.
- The song remains semantic, not singable.
- `பண்ணிகர்` remains untouched in Tamil; English `melodious` is explicitly documented as a contextual rendering.
- Refrain fragments remain fragments rather than being silently reconstructed.
- The Thangappan speech remains one unit across the PDF 4→5 source break.

### Scenes 2–5 — first full batch in review

New review units: **66**.

Per-scene counts:

- scene 2 — **46**: 41 dialogue + 5 stage directions;
- scene 3 — **10**: 8 dialogue + 2 stage directions;
- scene 4 — **2**: 1 stage direction + 1 song;
- scene 5 — **8**: 5 dialogue + 3 stage directions.

Cumulative English state:

- scenes started: **1–5**
- scenes verified: **1**
- scenes in review: **2, 3, 4, 5**
- translation units: **70**
- verified units: **4**
- review units: **66**
- kinds: **55 dialogue / 13 stage direction / 2 song / 0 quoted verse**
- cross-page English units: `parasakthi-en-s001-u004`

### Important representation/review decisions

- Scene 4's speaker-labelled `இல் வாழ்வினிலே` is represented as **one song unit** linked to `parasakthi-song-002`, not duplicated as eight English dialogue units. Exact source labels `தங்`, `கல்`, `இரு` remain inline in the English song lines.
- Scene 2 colloquial/code-switched speech is translated for meaning while source labels remain exact metadata.
- Scene 3's unusual canonical sentence `உலகில் ஒரு அண்ணன் இருந்து பெண்ணைப் பிறந்தால் பெரும் துயர் என்பார்கள்` is not repaired; the conservative English rendering is explicitly noted for review.
- Scene 5's compressed newspaper line around `இரங்கூன் கடலோரங்களில் எதிரிகள் கப்பல்கள் இந்தியா போய்ச் சேரவில்லை` is translated without adding a causal relationship not explicit in the Tamil.

## Exact next work — second-pass review scenes 2–5

Review all **66** units in `translations/records/scene-02.json` through `scene-05.json` against their immutable source layers.

Review procedure:

1. verify unit ordering against each scene file;
2. verify every dialogue `source_record_id`, exact `speaker_label`, and PDF/printed-page provenance;
3. verify all stage-direction locators and make sure no action was invented;
4. review colloquial/code-switched English in scene 2 for tone without normalizing the Tamil;
5. review scene 3's semantically unusual line conservatively rather than repairing it;
6. review scene 4 as a semantic song translation, retaining speaker labels and refrain fragment behavior;
7. review scene 5's war-news wording without supplying unstated causal syntax;
8. change English only where the review identifies a real translation problem;
9. if the batch passes, set all 66 units and scenes 2–5 to `verified` and update the translation index/tracking files;
10. then begin the next translation batch with canonical **scenes 6–10**.

## Overall stage status

- Structural mapping: verified
- Canonical Tamil transcription: verified
- Tamil fidelity audit: complete
- Scene index: complete
- Scene text derivatives: complete
- Dialogue index: complete-verified
- Character index: complete-verified
- Song/verse inventory: complete
- Song authorship mapping: complete-verified
- Song-specific Tamil derivatives: complete-verified — 11/11
- Separate quoted-verse derivatives: complete-verified — 1
- English translation: **in-progress-review — scenes 1–5 / 70 units / scene 1 verified**
