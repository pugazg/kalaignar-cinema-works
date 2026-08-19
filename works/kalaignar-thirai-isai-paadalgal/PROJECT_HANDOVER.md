# Project handover — கலைஞர் திரை இசைப் பாடல்கள்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup

Read current `README.md`, `metadata.yaml`, `PROGRESS.md`, `AUDIT.md`, `notes/FULL_PDF_SONG_PAGE_SCAN.md`, `notes/FINAL_DRAFT_001_003_REVIEW.md`, `songs/page-map.json`, `songs/index.json`, `translations/README.md`, `translations/index.json`, `translations/PILOT_REVIEW.md`, `translations/BATCH_004_011_REVIEW.md`, `translations/BATCH_012_018_REVIEW.md`, `translations/BATCH_019_025_REVIEW.md`, `translations/BATCH_026_032_REVIEW.md`, `translations/BATCH_033_039_REVIEW.md`, and `docs/SONG_TRANSLATION_GUIDE.md` before changing this work. Current GitHub `main` is authoritative.

## Controlling source

`TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`

- 194 physical PDF pages;
- SHA-256 `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- image-only source;
- rendered scan controls Tamil readings.

## Critical Tamil rule — this PDF only

Process only actual numbered lyric pages/direct continuations. Ignore every non-song page for lyric-file creation. Multi-page lyrics remain one song file. Never import absent lyrics from elsewhere.

The full PDF is classified at **62 song-bearing / 132 ignored pages / 54 numbered songs**. Tamil lyric-file work is complete; do not reopen film-section batching as the processing driver.

## Tamil checkpoint

- verified: `001–054` — **54/54**;
- draft/review/not-started: **0/0/0**;
- Tamil song transcription: **complete-verified**;
- Tamil fidelity audit: **complete**;
- unresolved Tamil song readings: **0**.

Cross-page verified Tamil records are `009`, `019`, `023`, `024`, `036`, `037`, `051`, and `052`.

## English translation checkpoint

English translation is **in progress**.

Authoritative English-layer files:

- `docs/SONG_TRANSLATION_GUIDE.md`;
- `translations/schema.json`;
- `translations/index.json`;
- `translations/README.md`;
- `translations/PILOT_REVIEW.md`;
- `translations/BATCH_004_011_REVIEW.md`;
- `translations/BATCH_012_018_REVIEW.md`;
- `translations/BATCH_019_025_REVIEW.md`;
- `translations/BATCH_026_032_REVIEW.md`;
- `translations/BATCH_033_039_REVIEW.md`;
- `translations/records/song-001.json` through `song-039.json`.

Counts:

- source songs: **54/54 Tamil verified**;
- English translated total: **39/54**;
- English pilot-verified: **3** (`001–003`);
- English verified: **36** (`004–039`);
- English draft/review: **0/0**;
- English not started: **15** (`040–054`).

Completed scaled batches:

- `004–011` — `நாம்` — **8/8 verified**;
- `012–018` — `அம்மையப்பன்` — **7/7 verified**;
- `019–025` — **7/7 verified**;
- `026–032` — **7/7 verified**;
- `033–039` — **7/7 verified**.

## Non-negotiable translation rule — retain Kalaignar's language

Use `semantic-poetic-source-faithful` English, not a singable adaptation.

Preserve repetition/refrains, political and social force, concrete imagery, rhetorical questions, colloquial energy, culture-bearing terms, exact source turn/performance labels, and source anomalies as documented pressure points rather than hidden Tamil corrections.

The `033–039` batch adds important precedents:

- `033`: keep triple cheek/bowl/colour/sign repetition, the forceful bird, burning moon and the paired two-fish/two-honeys/two-deer/two-skies image chain; do not decode those images into body-part prose;
- `034`: keep the three-person paper boat and shared sinking, social abandonment, no place for the poor, no god in any temple, literal **death at six, death at a hundred**, and final Amma/mother call;
- `035`: keep `வட்டி / அசல்` as **interest / principal**, source-joined `கனியேமலரே` as conservative **fruit-flower**, cheek/fruit-lip/marriage wordplay, love putting forth shoots and throbbing `பருவம்`;
- `036`: preserve **justice for the heart / sword for the shoulder**, Bharathi/Buddha/Gandhi/Arignar Anna rhetoric, direct caste/religion challenge, duty/rights/humanity, `anne / appa`, and corruption/mirror/blame/pillar warning; preserve PDF 86–87 as one record;
- `037`: preserve **people / sceptre**, people cooking in burning fire, kings on the road, `sirukodindha`, bungalow/sour-kaadi street-life satire, pearl/mucus and gem reversals, `kuthuk-kallu`, and **survive by dying**; preserve PDF 90–91 as one record;
- `038`: retain direct **O Tamil**, thousand crescents, sun procession, Podhigai breeze, literature/youth/old-age chain and source-pressure `Ponni nadiyaan` without normalization;
- `039`: retain `kurinji`, honey-waist, rock-candy/milk/sugarcane-plough imagery, `iyal / isai / koothu / Muthamizh`, three fruits, `mukti`, pearl-rain, two-lamps embrace/extinguish pressure and **Tamil Mother**.

Do not revise verified 001–039 English into smoother generic lyric English merely for fluency.

## Exact next activity

Translate and verify **songs 040–046**.

For each song:

1. fetch the current verified Tamil song file;
2. preserve anthology number, film provenance and source PDF page(s);
3. create one source-linked English record under `translations/records/`;
4. map every Tamil lyric line/cue to English;
5. retain Kalaignar's language according to the approved guide and 001–039 precedents;
6. document difficult cultural/colloquial/source-specific terms rather than smoothing them away;
7. preserve any multi-page provenance exactly as the verified Tamil song record carries it;
8. update `translations/index.json` and create the next batch review only after all songs pass.

Do not alter verified Tamil files merely to make English smoother.

## Repository boundary

Work only inside `pugazg/kalaignar-cinema-works` unless explicitly instructed otherwise.
