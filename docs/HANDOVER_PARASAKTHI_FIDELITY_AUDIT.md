# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

Current stage: **Structured Derivatives — Tamil/source layers complete; English translation pilot for canonical scene 1 is in review**.

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
- Scene 30 crosses PDF 35→36 across the Part 01 / Part 02 file boundary.
- Scene 33 spans PDF 38→42 because scene 34 is absent.
- Scene derivatives: **46/46 complete**.

## Dialogue index — complete-verified

- Records: **642** across all 46 observed scenes.
- Zero-record observed scenes: **26, 29, 48**.
- Cross-page records: **11**.
- Dialogue records are immutable derivatives for all later work.
- Exact source-label punctuation anomalies remain preserved in `parasakthi-s021-d040`, `parasakthi-s025-d011`, and `parasakthi-s025-d017`.

## Character index — complete-verified

- Distinct exact source labels: **69**.
- Explicit dispositions: **69/69**.
- Entities: **48**.
- Verified entities: **46**.
- Review label: `ராக`.
- Unresolved labels: `நொண்டி`, `நொ`.
- Do not force `நொண்டி` / `நொ` into ஞானசேகரன் without explicit source evidence.

## Song / verse layer — complete-verified

- Canonical song/verse occurrence records: **14**.
- Authorship verified: **14/14**.
- Soundtrack compositions: **11**.
- Source-faithful Tamil soundtrack derivatives: **11/11** under `works/parasakthi/songs/tracks/`.
- Separate quoted literary verse: **1** under `works/parasakthi/songs/quoted-verses/`.
- Scene 15 retains two canonical occurrence boundaries inside the one track `தேசம் ஞானம் கல்வி`.
- Scene 47 remains a reprise occurrence of scene 33's `புது பெண்ணின் மனதை`.
- Scene 28's Bharathidasan quotation remains outside the soundtrack set.

No canonical Tamil, scene file, dialogue record or character mapping was modified by the song layer.

## English translation layer — scene 1 pilot in review

Files:

- `works/parasakthi/translations/README.md`
- `works/parasakthi/translations/schema.json`
- `works/parasakthi/translations/index.json`
- `works/parasakthi/translations/records/scene-01.json`

Translation principles are controlled by `translations/README.md` and `translations/schema.json`:

- Tamil remains authoritative.
- Every English unit is source-linked.
- Exact Tamil identifiers, including `speaker_label`, remain immutable metadata.
- Stage directions do not gain invented action.
- Dialogue preserves rhetorical force rather than being flattened for fluency.
- Songs use semantic-poetic translation, not singable rewriting.
- Translation status is independent of Tamil verification.
- English must never be used to retroactively repair Tamil.

### Pilot state

Canonical scene: **1**  
Pilot status: **review**  
Translation units: **4**  
Verified units: **0**  
Review units: **4**

Units:

1. `parasakthi-en-s001-u001` — `stage-direction` — opening scene direction — PDF 4 / printed p.3.
2. `parasakthi-en-s001-u002` — `song` — source occurrence `parasakthi-song-001` / `வாழ்க வாழ்கவே` — PDF 4 / printed p.3.
3. `parasakthi-en-s001-u003` — `stage-direction` — transition after dance/song and before the speech — PDF 4 / printed p.3.
4. `parasakthi-en-s001-u004` — `dialogue` — source record `parasakthi-s001-d001`, exact source label `தங்கப்பன்`, PDF 4→5 / printed pp.3→4.

### Pilot decisions to retain unless review changes them

- `இரங்கூன்` is rendered `Rangoon` and `மலேயா` as `Malaya`.
- `இலங்கை தீவு` is rendered `the island of Ceylon` as a period-readable English place name; source metadata remains untouched.
- The song is translated semantically and preserves line order; it is not rewritten for rhyme or meter.
- The compressed printed song form `பண்ணிகர்` remains untouched in Tamil; the pilot renders its contextual sense as `melodious` and records that choice in a translation note.
- Refrain fragments such as `(வாழ்க` are represented as English refrain cues rather than silently completed.
- The Thangappan dialogue stays one unit. Its translated page segments intentionally mirror the source break inside `அவ்வளவு / ஏன்?`, while the combined English text reads naturally as `Why go that far?`.

## Exact next work — review pilot, then scenes 2–5

First perform a deliberate translation review of all four scene-1 units against their immutable Tamil sources:

1. compare `u001` and `u003` to `scenes/scene-01.md`;
2. compare `u002` to `songs/tracks/11-vaazhga-vaazhgave.md` and the canonical scene;
3. compare `u004` to `dialogues/records/scene-01.json`, including both page segments;
4. check names, historical place-name choices, metaphors, political/geographic terminology, punctuation and rhetorical force;
5. change English only where needed; never change Tamil;
6. if the four units pass review, set all four to `verified`, set scene 1 / pilot to `verified`, and update `translations/index.json`;
7. only after that verification, begin the first full translation batch with canonical **scenes 2–5**.

For scenes 2–5, continue to distinguish `dialogue`, `stage-direction`, `song`, and `quoted-verse` units and preserve immutable source record/occurrence IDs plus page provenance.

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
- English translation: **pilot-review — scene 1 / 4 units**
