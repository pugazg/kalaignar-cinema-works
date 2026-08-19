# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Scope

This audit covers:

1. the complete PDF-specific song-presence scan;
2. line-level Tamil lyric verification for all **54 numbered songs**;
3. the source-linked English translation pilot for songs **001–003**;
4. the first scaled English translation batch, songs **004–011**;
5. the second scaled English translation batch, songs **012–018**;
6. the third scaled English translation batch, songs **019–025**;
7. the fourth scaled English translation batch, songs **026–032**.

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
- scaled reviews: `translations/BATCH_004_011_REVIEW.md`, `translations/BATCH_012_018_REVIEW.md`, `translations/BATCH_019_025_REVIEW.md`, `translations/BATCH_026_032_REVIEW.md`.

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

Structural checks:

- verified Tamil files `song-026.md` through `song-032.md` are the only textual translation authorities;
- every visible Tamil lyric line and refrain cue is represented in the corresponding English record;
- exact role/performance labels remain traceable for song `030`;
- all seven source records retain their single-page provenance: **65, 66, 67, 70, 73, 74, 77**;
- no singer is inferred for `027`, whose verified source page prints no separate voice line;
- no verified Tamil file was changed;
- no source anomaly was silently repaired through English;
- no external recording, subtitle, web lyric, alternate edition or alternate Thirukkural witness was used.

### Kalaignar-language fidelity checks

- `026`: sky-flower grove, honeyed moon, open-subject breeze line, jasmine creeper, overflowing dam, wave-surge, quenched fire, uncloying nectar and sweet mango-fruit remain concrete;
- `027`: `இதழ் பறித்து` remains plucked lips; north-wind chill, intimate `di`, conservative `eduppu`, `pann` / `yaazh`, attempted embrace and lightning-like disappearance remain source-shaped;
- `028`: **O Tamil**, lullaby vocables, golden lamp, wave-struck mother's heart, moon, cloud-seeing peacock and colloquial closing `pa` remain visible;
- `029`: repeated `இருக்குது` architecture, price-question, net-in-eyes, the source split `பழக் / குலை` as `fruit- / cluster`, statue, waist/youth/arrow and pleasure-poem imagery remain uncompressed;
- `030`: water/fire impossibilities, spinning world/body, `kalagam / kalayam` commotion/pot sound-play, heaven/dizziness, colloquial maiden-girl, source-unexpanded `one on the cheek`, and exact role labels remain intact;
- `031`: repeated martial exhortations, warrior-conch, armies, head-giving, mother's honour, hill-like shoulder, enemy feet, warriors' non-flower-plucking hands, raised sword, `vengai` tiger-king and battlefield command remain explicit; `குமலைப்`, `அஞ்சுகத்தின்`, and `புறப்படடா` are documented pressure points rather than normalized forms;
- `032`: **one woman for one man**, the anthology's own printed Thirukkural wording, life-as-boat, unforgettable Veda, youth-as-fading-costume, repeated storm warning and oarless-boat analogy remain source-led.

Detailed review: `translations/BATCH_026_032_REVIEW.md`.

## Current gate result

- Tamil transcription: **complete-verified — 54/54**;
- Tamil fidelity audit: **complete**;
- English translated: **32/54**;
- English pilot-verified: **3** (`001–003`);
- English verified: **29** (`004–032`);
- English draft/review: **0/0**;
- English not started: **22** (`033–054`);
- reader/export: **not started**.

Next translation batch: **033–039**, using the approved Kalaignar-language source-faithful rules and preserving cross-page provenance for songs `036` and `037`.
