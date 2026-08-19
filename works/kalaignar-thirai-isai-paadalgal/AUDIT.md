# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Scope

This audit covers:

1. the complete PDF-specific song-presence scan;
2. line-level Tamil lyric verification for all **54 numbered songs**;
3. the source-linked English translation pilot for songs **001–003**;
4. the first scaled English translation batch, songs **004–011**;
5. the second scaled English translation batch, songs **012–018**;
6. the third scaled English translation batch, songs **019–025**.

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
- scaled reviews: `translations/BATCH_004_011_REVIEW.md`, `translations/BATCH_012_018_REVIEW.md`, `translations/BATCH_019_025_REVIEW.md`.

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

Structural checks:

- verified Tamil files `song-019.md` through `song-025.md` are the only textual translation authorities;
- every visible Tamil lyric/dialogue line and refrain cue is represented in the corresponding English record;
- exact source speaker/performance divisions remain traceable;
- multi-page English provenance remains one-record/complete for `019` = **53–54**, `023` = **58–59**, `024` = **62–63**;
- no verified Tamil file was changed;
- no source anomaly was silently repaired through English;
- no external recording, subtitle, web lyric or alternate edition was used.

### Kalaignar-language fidelity checks

- `019`: theatre-ticket hawker rhythm, price patter, floor/stain imagery, `ட்ராமா / வெங்கட்ராமா`, `kaali / naarkaali`, dance/song/sulking/reunion, dressing-scene torch, house-full and other source-driven sound jokes remain visible; unresolvable sound chains are transliterated rather than replaced by invented English comedy;
- `020`: unemployment remains explicit, vanishing like morning dew; unexpected good life, strangers-as-kin and the `seemaatti` mistaken-status turn are preserved;
- `021`: ocean-girdled world, crowing/pecking, chastity, end-age catastrophe, `thaazhi` vessel and **grammar of chastity** remain unsoftened;
- `022`: jewel-dove, heart leaping toward the beloved, flower-spreading bed, `Poomaane`, rose enclosure/jasmine garden and Raja/Rani intimacy remain concrete;
- `023`: the source's song/dialogue alternation remains intact; cat/world and curtain/moon ridicule, Harishchandra sarcasm, bundled-sugarcane pressure point and Clavar/Daiman/Ispade card language remain source-shaped;
- `024`: **body of fame**, collective sacrifice, idle body-as-cage, pandaaram/paradesi/Govinda, walking corpse, temple of knowledge, working comrade and public-welfare-as-medicine remain a continuous social-political chain;
- `025`: Ayarpadi Kanna, Mayakkara/Jaalakkara/Bhagavane, Bhama, burning-ember love, lightning-waist, honey-seeping cheek and spear-shaming eyes remain explicit.

Detailed review: `translations/BATCH_019_025_REVIEW.md`.

## Current gate result

- Tamil transcription: **complete-verified — 54/54**;
- Tamil fidelity audit: **complete**;
- English translated: **25/54**;
- English pilot-verified: **3** (`001–003`);
- English verified: **22** (`004–025`);
- English draft/review: **0/0**;
- English not started: **29** (`026–054`);
- reader/export: **not started**.

Next translation batch: **026–032**, using the approved Kalaignar-language source-faithful rules.
