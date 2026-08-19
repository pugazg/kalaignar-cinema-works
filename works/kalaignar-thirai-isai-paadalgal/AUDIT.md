# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Scope

This audit covers:

1. the complete PDF-specific song-presence scan;
2. line-level Tamil lyric verification for all **54 numbered songs**;
3. the source-linked English translation pilot for songs **001–003**;
4. the first scaled English translation batch, songs **004–011**;
5. the second scaled English translation batch, songs **012–018**.

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

The Tamil song corpus is **complete-verified**.

Final draft-gate review: `notes/FINAL_DRAFT_001_003_REVIEW.md`.  
Final formerly not-started batch review: `notes/FINAL_PAGE_BATCH_065_130_REVIEW.md`.

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
- scaled reviews: `translations/BATCH_004_011_REVIEW.md`, `translations/BATCH_012_018_REVIEW.md`.

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

Structural checks:

- verified Tamil files `song-012.md` through `song-018.md` are the only textual translation authorities;
- every visible Tamil lyric line/cue is represented in the corresponding English record;
- exact role/performance labels remain traceable;
- all seven records preserve PDF **44–50** provenance respectively;
- no verified Tamil file was changed;
- no singer was inferred where the source page prints none;
- no source anomaly was silently repaired through English;
- no external recording, subtitle, web lyric or alternate edition was used.

### Kalaignar-language fidelity checks

- `012`: Ammaiyappa/Aiyan address, paired opposites, honey/poison and fire/water paradoxes, king-to-`aandis` hierarchy, palanquin bearers/riders, toad-in-stone, sesame-oil and snake-fang venom remain explicit;
- `013`: repeated `paappa`, silver-sand play, sandalwood parrot, peacock, nectar-dove and repeated `sway` retain the child-song register;
- `014`: realm-of-love, `come running`, cloud/plumage, great gem, maiden dancing in the eyes, boundary of bliss, heart-veena and moon-of-love variation remain distinct;
- `015`: the sorrow reprise deliberately keeps matching English for repeated Tamil lines; song-on-the-breeze, honey-rain and the source-unassigned `lap` remain source-shaped;
- `016`: agal-lamp, sugarcane/rock-candy/fruit-nectar, red paddy, refined Tamil, Kaveri, casket of the learned and Dravida remain concrete; difficult `நீ... இராவிடம் இருள் சூழும் / என்ற நிலை தந்த` is documented rather than silently corrected;
- `017`: living portrait, epic of flavour, flame, storm/flower-garden, fallen divine statue and empty temple remain unsoftened;
- `018`: love-dove, tender-shoot body, repeated `come`, deer-skinned tiger, mango-cuckoo, sorrow-darkness, sleeping moon-maiden and love/deception reversal remain visible.

Detailed review: `translations/BATCH_012_018_REVIEW.md`.

## Current gate result

- Tamil transcription: **complete-verified — 54/54**;
- Tamil fidelity audit: **complete**;
- English translated: **18/54**;
- English pilot-verified: **3** (`001–003`);
- English verified: **15** (`004–018`);
- English draft/review: **0/0**;
- English not started: **36** (`019–054`);
- reader/export: **not started**.

Next translation batch: **019–025**, using the approved Kalaignar-language source-faithful rules and preserving cross-page provenance for `019`, `023` and `024`.
