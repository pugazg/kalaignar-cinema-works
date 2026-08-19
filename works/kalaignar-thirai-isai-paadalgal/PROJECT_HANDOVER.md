# Project handover — கலைஞர் திரை இசைப் பாடல்கள்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup

Read current `README.md`, `metadata.yaml`, `PROGRESS.md`, `AUDIT.md`, `notes/FULL_PDF_SONG_PAGE_SCAN.md`, `notes/FINAL_DRAFT_001_003_REVIEW.md`, `songs/page-map.json`, `songs/index.json`, `translations/README.md`, `translations/index.json`, `translations/PILOT_REVIEW.md`, and `docs/SONG_TRANSLATION_GUIDE.md` before changing this work. Current GitHub `main` is authoritative.

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

Final Tamil gate review: `notes/FINAL_DRAFT_001_003_REVIEW.md`.

Cross-page verified Tamil records are `009`, `019`, `023`, `024`, `036`, `037`, `051`, and `052`.

## English translation checkpoint

English translation is now **pilot-verified** for songs `001–003`.

Authoritative English-layer files:

- `docs/SONG_TRANSLATION_GUIDE.md`;
- `translations/schema.json`;
- `translations/index.json`;
- `translations/README.md`;
- `translations/PILOT_REVIEW.md`;
- `translations/records/song-001.json`;
- `translations/records/song-002.json`;
- `translations/records/song-003.json`.

Counts:

- source songs: **54/54 Tamil verified**;
- English pilot-verified: **3**;
- English draft/review: **0/0**;
- English not started: **51**.

## Non-negotiable translation rule — retain Kalaignar's language

Use `semantic-poetic-source-faithful` English, not a singable adaptation.

Preserve:

- repetition and refrain architecture;
- political/social satire and class language without euphemism;
- concrete imagery before stylistic smoothing;
- rhetorical questions and accumulations;
- colloquial energy and culture-bearing words;
- exact source turn/performance labels in provenance;
- source anomalies as documented pressure points rather than hidden Tamil corrections.

The approved pilot intentionally keeps images/phrases such as **buffalo calf**, **sugarcane-Tamil**, **flower where dew sleeps**, **magnetic statue**, **live like honey**, repeated **Why were you born?**, and the poor-versus-grandee contrast.

The verified Tamil `வந்தேன் தவழ்ந்தாய்?` in song `003` is not silently emended through English. Likewise, unusual source forms in song `001` remain immutable Tamil even when the English must interpret their contextual force conservatively.

## Exact next activity

Translate and verify **songs 004–011**, the complete `நாம்` group.

For each song:

1. fetch the current verified Tamil song file;
2. preserve the anthology number, film provenance and source PDF page;
3. create one source-linked English record under `translations/records/`;
4. map every Tamil lyric line/cue to English;
5. retain Kalaignar's language according to the pilot rules;
6. document difficult cultural/colloquial/source-specific terms instead of smoothing them away;
7. update `translations/index.json` and batch review only after all eight songs pass.

Do not alter verified Tamil files merely to make English smoother.

## Repository boundary

Work only inside `pugazg/kalaignar-cinema-works` unless explicitly instructed otherwise.
