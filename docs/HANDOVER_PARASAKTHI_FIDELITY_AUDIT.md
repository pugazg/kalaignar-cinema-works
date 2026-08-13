# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

Current stage: **Structured Derivatives — character index pilot verified; systematic label expansion next**.

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

## Dialogue index — complete

Files:

- `works/parasakthi/dialogues/schema.json`
- `works/parasakthi/dialogues/index.json`
- `works/parasakthi/dialogues/records/scene-XX.json`

Final state:

- Status: **complete-verified**
- Observed scenes represented: **46 / 46**
- Dialogue records: **642**
- Zero-record observed scenes: **26, 29, 48**
- Missing headings: **23, 34**
- Existing dialogue records must remain immutable during character indexing.

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

## Character index — pilot verified

Files:

- `works/parasakthi/characters/README.md`
- `works/parasakthi/characters/schema.json`
- `works/parasakthi/characters/labels-inventory.json`
- `works/parasakthi/characters/entities-pilot.json`
- `works/parasakthi/characters/index.json`

### Complete exact-label inventory

All 642 dialogue records have been surveyed for their exact `speaker_label` values.

- Dialogue records surveyed: **642**
- Observed scenes surveyed: **46**
- Distinct exact source labels: **69**
- Inventory status: **complete**

`labels-inventory.json` records every exact label and the canonical scenes in which it occurs. This is an inventory only; it does not imply that similar labels belong to the same entity.

### Pilot mapping

The first character pilot is **verified** and intentionally conservative:

- Pilot entities: **8**
- Exact labels mapped: **18**
- Exact labels remaining for review: **51**
- Dialogue records modified: **0**

Verified pilot entities:

1. `parasakthi-char-gunasekaran` — **குணசேகரன்** — labels: `குண`
2. `parasakthi-char-kalyani` — **கல்யாணி** — labels: `கல்யாணி`, `கல்யா`, `கல்`
3. `parasakthi-char-chandrasekaran` — **சந்திரசேகரன்** — labels: `சந்`, `சந்திர`, `சேகர்`
4. `parasakthi-char-gnanasekaran` — **ஞானசேகரன்** — labels: `ஞான`, `ஞா`
5. `parasakthi-char-saraswati` — **சரஸ்வதி** — labels: `சரஸ்`, `சர`
6. `parasakthi-char-thangappan` — **தங்கப்பன்** — labels: `தங்கப்பன்`, `தங்`
7. `parasakthi-char-manickam-pillai` — **மாணிக்கம் பிள்ளை** — labels: `மாணிக்கம்`, `மாணிக்`, `மாணி`, `மணி`
8. `parasakthi-char-vimala` — **விமலா** — label: `விம`

`entities-pilot.json` contains representative supporting dialogue record IDs and scene coverage for every mapping.

### Character mapping rules

These rules are controlling for the next pass:

1. **Never modify the exact dialogue `speaker_label`.** Character mapping is a separate derivative.
2. Similar spelling alone is not sufficient evidence for merging labels.
3. Named-character mappings should be based on direct source context, self-identification, family/scene continuity, or repeated unambiguous usage.
4. Generic labels may become `role` or `collective` entities rather than named characters.
5. If a label is still ambiguous, retain it as `unresolved`; do not force a mapping to reduce the unresolved count.
6. Representative `supporting_records` should be preserved for every verified mapping.
7. The final character index may contain verified entities alongside explicit unresolved label records.

A deliberate example: `நொண்டி` and `நொ` are **not** included in the ஞானசேகரன் pilot mapping even though narrative context may suggest an identity. Resolve them only during the evidence pass if the source continuity is sufficiently explicit.

## Exact next work — expand the remaining 51 labels

Continue from `characters/index.json` and `characters/labels-inventory.json`.

For each remaining exact source label:

1. find every scene in `labels-inventory.json`;
2. inspect the corresponding dialogue record(s) and, when necessary, the verified scene derivative for context;
3. decide whether the label maps to a named character, a generic role, a collective, or must remain unresolved;
4. add or extend a stable entity only when the evidence is sufficient;
5. preserve the exact label string as a variant — never rename it in dialogue data;
6. record confidence/status and representative evidence IDs;
7. keep a running mapped/unresolved label count.

Recommended order for the expansion pass:

- first resolve straightforward recurring named/role labels such as `வேணு`, `நாரா`, `காந்`/`காந்தா`, `பூசாரி`, `பார்`/`பார்வதி`, `டாக்`/`டாக்டர்`, `கருப்`, `ஜாலி`;
- then resolve clear occupational/generic labels (`போலீஸ்`, `நீதி`, `வக்`, `வியாபாரி`/`வியா`, etc.);
- finally review ambiguous abbreviations/collectives and leave any unsupported identity as unresolved.

Do not mark the character index `complete-verified` until all 69 exact labels have an explicit disposition: mapped to a verified/review entity or retained as unresolved.

## Other stages

- Scene index: complete
- Scene text derivatives: complete
- Dialogue index: complete-verified
- Character index: **pilot-verified / expansion pending**
- Per-song authorship mapping: not started
- English translation: not started
