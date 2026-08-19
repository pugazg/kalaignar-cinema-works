# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Scope

This audit covers:

1. the complete PDF-specific song-presence scan;
2. line-level Tamil lyric verification for all **54 numbered songs**;
3. the source-linked English translation pilot for songs **001–003**;
4. the first scaled English translation batch, songs **004–011**.

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

The last Tamil gate directly resolved the early pilot records without outside text: song `001` corrected `அறியாண்டி` → source-visible `அறியான்டி`; song `002` required no lyric correction; song `003` resolved `வந்தேன் தவழ்ந்தாய்?` and `பாழான எந்தன் வயிற்றில் பிறந்தாய் ராஜா!` from PDF 30.

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

## PDF-specific Tamil processing rule

For this PDF only, process actual numbered lyric pages/direct continuations and ignore every other page for lyric-file creation. Do not import missing lyrics from elsewhere.

## English translation authority

- guide: `docs/SONG_TRANSLATION_GUIDE.md`;
- schema: `translations/schema.json`;
- index: `translations/index.json`;
- pilot review: `translations/PILOT_REVIEW.md`;
- first scaled review: `translations/BATCH_004_011_REVIEW.md`.

The approved mode is **`semantic-poetic-source-faithful`**. English must retain Kalaignar's language, rhetoric, repetition, political/social force, concrete imagery, colloquial energy and source-specific constructions. It is not a singable adaptation.

## Pilot gate — songs 001–003

**PASS — 3/3 `pilot-verified`.**

Pilot checks passed:

- each source Tamil song was already verified;
- every record preserves song ID, anthology number and PDF provenance;
- every Tamil lyric line/cue has an explicit English mapping;
- exact source turn/performance labels remain traceable;
- no Tamil source file was modified;
- no external lyric/audio source was imported;
- attribution remains `anthology-attributed`.

The pilot established voice baselines for rustic social satire, romantic image chains and maternal/class lament.

## First scaled gate — songs 004–011

**PASS — 8/8 `verified`.**

Structural checks:

- verified Tamil files `song-004.md` through `song-011.md` are the only textual translation authorities;
- every visible Tamil lyric line is represented in the corresponding English record;
- role/performance labels and abbreviated refrain cues remain source-linked;
- song `009` retains PDF **38–39** as one cross-page provenance record;
- no verified Tamil file was changed by the English batch;
- no source anomaly was silently repaired through English;
- no external recording, subtitle, web lyric or alternate edition was used.

### Kalaignar-language fidelity checks

- `004`: folk-devotional vocabulary, water/cloud/rain reasoning, Kodumpavi, colloquial speech and the tax grievance remain visible together;
- `005`: yaazh/doe/breeze/sky/moon/Tamil-epic/unpainted-painting imagery and doubled verbs remain intact;
- `006`: the `மணம்` fragrance/marriage wordplay is made visible, while the veena/thunderbolt/garden/vine/cyclone/pollen/dark-house imagery remains concrete;
- `007`: the earlier yaazh image turns into grief through `a yaazh that plucks an unreturning sorrow`, singing ghost and inscribed-page imagery;
- `008`: source-anomalous names/forms are transliterated rather than normalized; `Dei`, kichili fruit, consumption, monkey/moustache/tail taunts and Bhimasena remain direct;
- `009`: ignorance-as-wasteland, knowledge-as-plough-point, science/ploughing, field labour, Nandanar versus hands-and-legs labour, golden queen/comrade and common granary remain a single rationalist/agricultural chain;
- `010`: fourfold `வாழ்க`, Arignar, buffalo/worm/eagle/mouse/tiger images, rights/reform rhetoric and `பகுத்தறிவு` remain explicit; possible title/wordplay expressions are conservatively transliterated;
- `011`: snake, prison, torture, Socrates, deathless Gandhi, honey/scorpion, battlefront death, arrogance, army, fury and slander remain unsoftened.

Detailed review: `translations/BATCH_004_011_REVIEW.md`.

## Current gate result

- Tamil transcription: **complete-verified — 54/54**;
- Tamil fidelity audit: **complete**;
- English translated: **11/54**;
- English pilot-verified: **3** (`001–003`);
- English verified: **8** (`004–011`);
- English draft/review: **0/0**;
- English not started: **43** (`012–054`);
- reader/export: **not started**.

Next translation batch: **012–018** (`அம்மையப்பன்`), using the approved Kalaignar-language source-faithful rules.
