# Project handover — கலைஞர் திரை இசைப் பாடல்கள்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup

Read current `README.md`, `metadata.yaml`, `PROGRESS.md`, `AUDIT.md`, `notes/FULL_PDF_SONG_PAGE_SCAN.md`, `notes/FINAL_DRAFT_001_003_REVIEW.md`, `songs/page-map.json`, `songs/index.json`, `translations/README.md`, `translations/index.json`, `translations/PILOT_REVIEW.md`, all scaled batch reviews through `translations/BATCH_047_054_REVIEW.md`, and `docs/SONG_TRANSLATION_GUIDE.md` before changing this work. Current GitHub `main` is authoritative.

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

- verified `001–054`: **54/54**;
- draft/review/not-started: **0/0/0**;
- Tamil song transcription: **complete-verified**;
- Tamil fidelity audit: **complete**;
- unresolved Tamil song readings: **0**.

Cross-page verified Tamil records are `009`, `019`, `023`, `024`, `036`, `037`, `051`, and `052`.

## English translation checkpoint

English translation is **complete-verified**.

Authoritative English-layer files:

- `docs/SONG_TRANSLATION_GUIDE.md`;
- `translations/schema.json`;
- `translations/index.json`;
- `translations/README.md`;
- `translations/PILOT_REVIEW.md`;
- all seven scaled batch reviews through `translations/BATCH_047_054_REVIEW.md`;
- `translations/records/song-001.json` through `song-054.json`.

Counts:

- source songs: **54/54 Tamil verified**;
- English translated total: **54/54**;
- English pilot-verified: **3** (`001–003`);
- English verified: **51** (`004–054`);
- English draft/review/not-started: **0/0/0**.

The final batch `047–054` is **8/8 PASS**. Multi-page provenance is preserved for `051` = PDF **121–122** and `052` = PDF **123–124**.

## Non-negotiable translation rule — retain Kalaignar's language

Use `semantic-poetic-source-faithful` English, not a singable adaptation.

Preserve repetition/refrains, political and social force, concrete imagery, rhetorical questions, colloquial energy, culture-bearing terms, exact source turn/performance labels, and source anomalies as documented pressure points rather than hidden Tamil corrections.

Final-batch precedents include:

- `047`: **sons of the soil**, eye/eyelid duty image, **hand for kinship / voice for rights**, `naam / naan` lip-wordplay, and conservative handling of `பிரிவாது`;
- `048`: `kalaignan`, `udanpirappe`, caste/religion division, sledgehammer rhetoric, Valluvar and `inba-pagai`;
- `049`: mother-warrior grief/pride, young-deer bride, tusker/steed imagery and womb-bearing motherhood;
- `050`: `mullai`, Tamil `mandram`, `bhava`, `jathi`, `veena`, `Nasika Poosani`, source-pressure `nyaayirene`, and the abrupt final source line;
- `051`: colloquial `machaan` erotic/comic register, `aandi`, `thaali`, `saivam / asaivam`, anti-subordination lines and pressure-point source phrases; preserve PDF 121–122 as one record;
- `052`: affection-parrot, `kurinji`, Kannagi, Classical Tamil, sibling/mother imagery and eyes-as-ponds; preserve PDF 123–124 as one record;
- `053`: preserve the printed clipped short-line structure rather than recomposing it into prose;
- `054`: preserve musical/place vocabulary, `Kodumudi kokilam`, honey/milk and `aanpaal` wordplay, `paayiram`, and the classical red-earth/water image.

Do not revise the verified 001–054 English corpus into smoother generic lyric English merely for fluency.

## Exact next activity

Run a **whole-corpus English reader/export preflight** across all 54 source-linked translation records.

The preflight should verify at minimum:

1. exactly 54 translation records, in anthology order `001–054`;
2. each record links to the correct verified Tamil song file and PDF page provenance;
3. the 3 `pilot-verified` and 51 `verified` statuses remain distinct and complete;
4. all eight cross-page song records preserve their full source-page arrays;
5. no missing/duplicate anthology song number, translation ID, song ID or record path;
6. `anthology-attributed` remains distinct from original-film primary-source verification;
7. reader/export generation does not alter the complete-verified Tamil or English source-linked records.

## Repository boundary

Work only inside `pugazg/kalaignar-cinema-works` unless explicitly instructed otherwise.
