# Raja Rani — character / entity mapping checkpoint

## Scope

This checkpoint completes the character/entity derivative for the **74 exact non-empty speaker labels** preserved in the completed verified dialogue layer.

Controlling derivative inputs:

- `works/raja-rani/characters/labels-inventory.json`
- `works/raja-rani/dialogues/index.json`
- `works/raja-rani/dialogues/records/scene-###.json`
- verified scene text under `works/raja-rani/scenes/`
- source-visible PDF-9 cast roster as an outer-film identity anchor only

The eight source-review-blocked archival scenes remain excluded from verified character evidence: `s011`, `s012`, `s013`, `s033`, `s039`, `s053`, `s054`, `s055`.

## Completion result

- immutable dialogue records considered: **892/892**
- eligible verified dialogue scenes: **50/50**
- distinct exact source labels: **74**
- exact labels dispositioned: **74/74**
- entities / role categories / collectives: **42**
- verified entities: **42**
- review entities: **0**
- unresolved entities: **0**
- verified labels: **74**
- review labels: **0**
- unresolved labels: **0**
- dialogue records modified: **none**
- output: `works/raja-rani/characters/entities.json`

## Important context-sensitive decisions

### `ரா` is Rani, not Raja

Spelling similarity was not used. In scene 45 the exact label `ரா` answers Raja's flower/pottu offer and includes feminine-stage-direction evidence such as `[அழுகிறாள்.]`. It therefore maps to the Rani entity. Raja's own exact source forms are `ராஜா`, `ராசா`, and `ராஜ`.

### `தாய்` is Thayammal

Scene 52 removes what would otherwise be an abbreviation ambiguity: immediately before `தாய்:` the source stage direction says `(பாபு தயங்க. கீதாவின் தாய் உள்ளே இருந்து ஓடிவந்து)`. This establishes the `தாய்` label as Geetha's mother, joining the source forms `கீதாவின் தாய் தாயம்மாள்`, `தா`, `தாயம்`, and `தாயம்மாள்`.

### `சங்` is Sangaran

Scene 57 explicitly introduces `(கரண்ட், சங்கரன், கண்ணம்மா மூவரும் வருதல்.)`; the subsequent `சங்:` utterance is therefore mapped to `சங்கரன்`.

### `ரெள 2` remains a role label

Scene 7 states that several rowdies have planned to drug the tea, immediately followed by `ரெள 2:`. The downstream preferred role name is `ரெளடி 2`, but the immutable dialogue label remains exactly `ரெள 2`.

### `வேலை` is context-sensitive

The exact short label `வேலை` appears in more than one household/work setting. It is therefore dispositioned as a verified **worker/servant role category**, together with the explicit role form `வேலைக்காரன்`, rather than falsely asserting one physical individual across every occurrence.

### `மன்` is not silently merged with `மன்னர்கள்`

The plural `மன்னர்கள்` is a collective. The scene-4 `மன்` utterance is dispositioned separately as an unnamed king role because the source context supports a single speaking king but does not identify which individual king it is.

## Embedded dramatic identities

The archival mapping keeps nested-performance identities distinct from outer-film characters:

- `சேரன் செங்குட்டுவன்` section: சேரன் செங்குட்டுவன், வேண்மாள், வில்லவன், கனகர், விஜயர், கனக விஜயர், தமிழ்நாட்டுப் புலவர், மன்னர்கள், unnamed king, வீரர்கள் and the pre-performance voice;
- `அகல்யா` rehearsal: அகல்யா, இந்திரன், முனிவர் and `ராமர் வேஷ ராமன்`;
- `சாக்ரடீஸ்` drama: சாக்ரடீஸ், மெலிடஸ், அனிடஸ், கிரீட்டோ, நீதிபதி, சிறைக் காவலர் and மக்கள்.

Outer-film Raja/Rani/Current/etc. remain their own entities even when they participate in rehearsals or staged-performance framing.

## Integrity rules confirmed

1. Every one of the **74** exact labels appears exactly once in the entity mapping's `source_labels` coverage.
2. No dialogue `speaker_label`, delimiter, text, page provenance or record ID was changed.
3. Similar spelling alone was never sufficient to merge labels.
4. Role/collective dispositions are used where the source does not establish a named physical person.
5. No blocked-scene wording was used to fill a character gap.
6. Character normalization exists only downstream in `characters/entities.json`.

## Next gate

The character/entity derivative is complete. The next structured activity is the **song/performance inventory and item-level authorship gate**.

The source prints 11 numbered `பாட்டு` blocks in PDF 4–9 and a film-wide PDF-9 `பாடல்கள்:` roster, but that roster must **not** be promoted to item-level authorship. Each song/performance occurrence must be inventoried first; authorship is verified only where the source or a separately justified witness provides item-level evidence.
