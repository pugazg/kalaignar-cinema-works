# Project handover — கலைஞர் திரை இசைப் பாடல்கள்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup

Read current `README.md`, `metadata.yaml`, `PROGRESS.md`, `AUDIT.md`, `notes/FULL_PDF_SONG_PAGE_SCAN.md`, `notes/FINAL_DRAFT_001_003_REVIEW.md`, `songs/page-map.json`, `songs/index.json`, `translations/README.md`, `translations/index.json`, `translations/PILOT_REVIEW.md`, `translations/BATCH_004_011_REVIEW.md`, `translations/BATCH_012_018_REVIEW.md`, `translations/BATCH_019_025_REVIEW.md`, `translations/BATCH_026_032_REVIEW.md`, `translations/BATCH_033_039_REVIEW.md`, `translations/BATCH_040_046_REVIEW.md`, and `docs/SONG_TRANSLATION_GUIDE.md` before changing this work. Current GitHub `main` is authoritative.

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
- `translations/BATCH_040_046_REVIEW.md`;
- `translations/records/song-001.json` through `song-046.json`.

Counts:

- source songs: **54/54 Tamil verified**;
- English translated total: **46/54**;
- English pilot-verified: **3** (`001–003`);
- English verified: **43** (`004–046`);
- English draft/review: **0/0**;
- English not started: **8** (`047–054`).

Completed scaled batches:

- `004–011` — `நாம்` — **8/8 verified**;
- `012–018` — `அம்மையப்பன்` — **7/7 verified**;
- `019–025` — **7/7 verified**;
- `026–032` — **7/7 verified**;
- `033–039` — **7/7 verified**;
- `040–046` — **7/7 verified**.

## Non-negotiable translation rule — retain Kalaignar's language

Use `semantic-poetic-source-faithful` English, not a singable adaptation.

Preserve repetition/refrains, political and social force, concrete imagery, rhetorical questions, colloquial energy, culture-bearing terms, exact source turn/performance labels, and source anomalies as documented pressure points rather than hidden Tamil corrections.

The `040–046` batch adds important precedents:

- `040`: keep **Kuramullai**, the one-day embrace/Raja refrain, little-flower eyes, source-pressure `சொல்லுக்கு செய்தாயே`, `பாட்டுப்பட்ட` as **song-struck**, `vallal`, and `rammai / jinnai / naatti`; do not repair these through soundtrack familiarity;
- `041`: keep the worker/rest elegy, mother's-lap / ground-sleep reversal, **little lion**, caste-division weapons, principle/martyrdom, Jesus/Buddha/Prophets/Gandhi/Periyar/Anna/Ambedkar chain, **speaking storm**, lineage-lamp and rough `da`;
- `042`: keep folk `di`, sun-fire/conspiracy burning, verified `ஏறிமலையில்` as source-pressure **eeri-malai**, clan-deity/golden-clan lion/earthquake-stage images, `kummi / kulavai`, `thambi`, explicit **private ownership / common ownership**, and `thumbi`;
- `043`: keep the campaign quotation, paired **calmly / at ease**, rise/fall/weights metaphor, worker/town-cheater contrast, vote-buying wretches, **bribe-demons**, rice-price politics, **hand for kinship / voice for rights**, `thambi`, Thenpandi lion and Kalaignar's `udanpirappe` address;
- `044`: keep **khaki-shirt man**, do-what-we-said / say-only-what-we-did ethics, `mamool`, the fence-grazing-crop proverb, goat/`vengai`, illicit-liquor `support` code-mixing and cotton-fluff tearing imagery;
- `045`: keep tears bathing the father's feet, **fingers made into eyes**, **ocean of compassion / Himalaya of patience**, and the source's hearts-as-flowers / garland / neck-of-fame-summit mixed metaphor;
- `046`: keep tilted court balance, repeated innocent-death question, **sin with one / blame with another**, `amavasai`, predator/goat and fence/crop images, **Mother Tamilagam**, and the verified closing `வாழுக்குவேலை / வாழுக்கு வேலை` as **vaazhukku-velai / vaazhukku velai** rather than silently emending it to a familiar alternate phrase.

Do not revise verified 001–046 English into smoother generic lyric English merely for fluency.

## Exact next activity

Translate and verify the **final songs 047–054**.

For each song:

1. fetch the current verified Tamil song file;
2. preserve anthology number, film provenance and source PDF page(s);
3. create one source-linked English record under `translations/records/`;
4. map every Tamil lyric line/cue to English;
5. retain Kalaignar's language according to the approved guide and 001–046 precedents;
6. document difficult cultural/colloquial/source-specific terms rather than smoothing them away;
7. preserve `051` as one English record across PDF **121–122** and `052` as one English record across PDF **123–124**;
8. update `translations/index.json` and create the final batch review only after all eight songs pass.

Do not alter verified Tamil files merely to make English smoother.

## Repository boundary

Work only inside `pugazg/kalaignar-cinema-works` unless explicitly instructed otherwise.
