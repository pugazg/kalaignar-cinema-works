# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Scope

This audit covers:

1. the complete PDF-specific song-presence scan;
2. line-level Tamil lyric verification for all **54 numbered songs**;
3. the source-linked English translation pilot for songs **001–003**;
4. the first scaled English translation batch, songs **004–011**;
5. the second scaled English translation batch, songs **012–018**;
6. the third scaled English translation batch, songs **019–025**;
7. the fourth scaled English translation batch, songs **026–032**;
8. the fifth scaled English translation batch, songs **033–039**.

The rendered scan controls Tamil. Verified Tamil song files control the English derivative. No external recording, lyric website, subtitle, alternate edition, or soundtrack-memory reconstruction is used to repair either layer.

## Full-PDF page classification

**PASS — 194/194 pages scanned.**

- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs located: **54/54**;
- final song-bearing page: **130**.

Authoritative ledger: `notes/FULL_PDF_SONG_PAGE_SCAN.md`  
Machine map: `songs/page-map.json`

## Final Tamil lyric fidelity status

- draft: **0**;
- verified: **54** (`001–054`);
- review: **0**;
- not started: **0**;
- unresolved Tamil song readings: **0**.

The Tamil song corpus is **complete-verified** and immutable translation input.

## Cross-page Tamil records

The following verified songs span more than one song-bearing page and remain one file each:

- `009` — PDF 38–39;
- `019` — PDF 53–54;
- `023` — PDF 58–59;
- `024` — PDF 62–63;
- `036` — PDF 86–87;
- `037` — PDF 90–91;
- `051` — PDF 121–122;
- `052` — PDF 123–124.

## English translation authority

- guide: `docs/SONG_TRANSLATION_GUIDE.md`;
- schema: `translations/schema.json`;
- index: `translations/index.json`;
- pilot review: `translations/PILOT_REVIEW.md`;
- scaled reviews: `translations/BATCH_004_011_REVIEW.md`, `translations/BATCH_012_018_REVIEW.md`, `translations/BATCH_019_025_REVIEW.md`, `translations/BATCH_026_032_REVIEW.md`, `translations/BATCH_033_039_REVIEW.md`.

The approved mode is **`semantic-poetic-source-faithful`**. English must retain Kalaignar's language, rhetoric, repetition, political/social force, concrete imagery, colloquial energy and source-specific constructions. It is not a singable adaptation.

## Pilot gate — songs 001–003

**PASS — 3/3 `pilot-verified`.**

The pilot established voice baselines for rustic social satire, romantic image chains and maternal/class lament while preserving song IDs, PDF provenance, source labels and exact line mapping.

## First scaled gate — songs 004–011

**PASS — 8/8 `verified`.**

The `நாம்` group confirmed the voice rules across folk devotion/social satire, romantic duet, female lament, comic mythic performance, rationalist/agricultural politics, praise/reform rhetoric and political endurance. Song `009` retains PDF **38–39** as one English source-provenance record.

Detailed review: `translations/BATCH_004_011_REVIEW.md`.

## Second scaled gate — songs 012–018

**PASS — 7/7 `verified`.**

The `அம்மையப்பன்` group preserved devotional paradox, child-address, romantic duet/reprise, Tamil/Kaveri/Dravida image density, architectural grief and love-lament imagery without changing the verified Tamil source.

Detailed review: `translations/BATCH_012_018_REVIEW.md`.

## Third scaled gate — songs 019–025

**PASS — 7/7 `verified`.**

The batch preserved theatre-ticket comedy and sound-play, unemployment/rank reversal, chastity imagery, jewel-dove romance, source song/dialogue alternation and card-suit language, public-welfare-as-medicine rhetoric, and Ayarpadi Kanna devotional flirtation. Multi-page English provenance remains one-record/complete for `019` = **53–54**, `023` = **58–59**, `024` = **62–63**.

Detailed review: `translations/BATCH_019_025_REVIEW.md`.

## Fourth scaled gate — songs 026–032

**PASS — 7/7 `verified`.**

The batch preserved romantic image chains, `eduppu`/`pann`/`yaazh`, Tamil-address lullaby, source-split lyric forms, intoxication sound-play, martial exhortation and the anthology's own printed Thirukkural wording.

Detailed review: `translations/BATCH_026_032_REVIEW.md`.

## Fifth scaled gate — songs 033–039

**PASS — 7/7 `verified`.**

Structural checks:

- verified Tamil files `song-033.md` through `song-039.md` are the only textual translation authorities;
- every visible Tamil lyric line, refrain cue and printed turn/structural label is represented in the corresponding English record;
- multi-page English provenance remains one-record/complete for `036` = **86–87** and `037` = **90–91**;
- no verified Tamil file was changed;
- no source anomaly was silently repaired through English;
- no external recording, subtitle, web lyric or alternate edition was used.

### Kalaignar-language fidelity checks

- `033`: triple cheek/bowl/colour/sign repetition, youth-feast, forceful bird, burning moon and the paired **two fish / two honeys / two deer / two skies** sequence remain visible;
- `034`: paper boat, three-person shared sinking, ritual/public image chain, social abandonment, no place for the poor, no god in any temple, literal **death at six, death at a hundred**, and final Amma/mother call remain unsoftened;
- `035`: `வட்டி / அசல்` remains **interest / principal**, the joined source form `கனியேமலரே` remains conservative **fruit-flower**, and cheek/fruit-lip/marriage plus love-shoot/`பருவம்` imagery remain source-shaped;
- `036`: **justice for the heart / sword for the shoulder**, Bharathi/Buddha/Gandhi/Arignar Anna rhetoric, direct caste/religion challenge, duty/rights/humanity and corruption/mirror/blame/pillar warning remain explicit across PDF 86–87;
- `037`: **people / sceptre**, people cooking in burning fire, kings on the road, `sirukodindha`, bungalow/sour-kaadi street-life satire, pearl/mucus and gem reversals, `kuthuk-kallu`, and **survive by dying** remain explicit across PDF 90–91;
- `038`: direct **O Tamil**, thousand crescents, wave-sea, sun procession, Podhigai breeze, literature/youth/old-age duration chain and source-pressure `Ponni nadiyaan` remain visible;
- `039`: `kurinji`, honey-waist, rock-candy/milk/sugarcane-plough imagery, `iyal / isai / koothu / Muthamizh`, three fruits, `mukti`, pearl-rain, two-lamps embrace/extinguish pressure and **Tamil Mother** remain culturally audible.

Detailed review: `translations/BATCH_033_039_REVIEW.md`.

## Current gate result

- Tamil transcription: **complete-verified — 54/54**;
- Tamil fidelity audit: **complete**;
- English translated: **39/54**;
- English pilot-verified: **3** (`001–003`);
- English verified: **36** (`004–039`);
- English draft/review: **0/0**;
- English not started: **15** (`040–054`);
- reader/export: **not started**.

Next translation batch: **040–046**, using the approved Kalaignar-language source-faithful rules.
