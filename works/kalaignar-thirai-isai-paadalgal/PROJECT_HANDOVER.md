# Project handover — கலைஞர் திரை இசைப் பாடல்கள்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup

Read current `README.md`, `metadata.yaml`, `PROGRESS.md`, `AUDIT.md`, `notes/FULL_PDF_SONG_PAGE_SCAN.md`, `notes/FINAL_DRAFT_001_003_REVIEW.md`, `songs/page-map.json`, and `songs/index.json` before changing this work. Current GitHub `main` is authoritative.

## Controlling source

`TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`

- 194 physical PDF pages;
- SHA-256 `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- image-only source;
- rendered scan controls.

## Critical rule — this PDF only

Process only actual numbered lyric pages/direct continuations. Ignore every non-song page for lyric-file creation. Multi-page lyrics remain one song file. Never import absent lyrics from elsewhere.

The full PDF is classified at **62 song-bearing / 132 ignored pages / 54 numbered songs**. Use `songs/page-map.json`; do not revert to film-section batching for Tamil lyric-file work.

## Current checkpoint

- verified: `001–054` — **54/54**;
- draft: **0**;
- review: **0**;
- not started: **0**;
- Tamil song transcription: **complete-verified**;
- Tamil fidelity audit: **complete**;
- unresolved Tamil song readings: **0**;
- English translation: **not started**.

Final Tamil gate review: `notes/FINAL_DRAFT_001_003_REVIEW.md`.

The final pilot recheck inspected only PDF 26, 29 and 30:

- song `001`: corrected pilot `அறியாண்டி` to source-visible `அறியான்டி`; confirmed `வேணசெல்வம்`, `பெண்ணி`, `ஏழைக்கிக்`;
- song `002`: passed without lyric correction; printed turn labels remain exact;
- song `003`: resolved the pilot uncertainty readings directly as `வந்தேன் தவழ்ந்தாய்?` and `பாழான எந்தன் வயிற்றில் பிறந்தாய் ராஜா!`.

Cross-page verified records are `009`, `019`, `023`, `024`, `036`, `037`, `051`, and `052`.

Music/voice lines were taken only when printed. Source speaker labels, refrain cues, colloquial spellings, unusual compounds, punctuation and lineation were preserved. No external lyrics were imported.

## Exact next activity

The Tamil gate is closed. Before scaling English translation:

1. inspect existing translation conventions in this repository;
2. define a song-translation schema/index that preserves song ID and Tamil source-file provenance;
3. create a small English pilot from verified Tamil song files;
4. review voice, cultural terms, refrains, speaker labels and source-specific wordplay before batch translation.

Do not alter the verified Tamil files merely to make English smoother.

## Repository boundary

Work only inside `pugazg/kalaignar-cinema-works` unless explicitly instructed otherwise.
