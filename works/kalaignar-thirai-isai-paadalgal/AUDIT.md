# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Scope

This audit covers the complete PDF-specific song-presence scan and line-level Tamil lyric verification for all **54 numbered songs** in the supplied anthology.

The rendered scan is authoritative. A song is verified only after its song-bearing page(s) are visually checked. No external recording, lyric website, subtitle, alternate edition, or soundtrack-memory reconstruction is used to repair the anthology text.

## Full-PDF page classification

**PASS — 194/194 pages scanned.**

- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs located: **54/54**;
- final song-bearing page: **130**.

Authoritative ledger: `notes/FULL_PDF_SONG_PAGE_SCAN.md`  
Machine map: `songs/page-map.json`

## Final lyric fidelity status

- draft: **0**;
- verified: **54** (`001–054`);
- review: **0**;
- not started: **0**;
- unresolved Tamil song readings: **0**.

The Tamil song corpus is therefore **complete-verified**.

Final draft-gate review: `notes/FINAL_DRAFT_001_003_REVIEW.md`.  
Final formerly not-started batch review: `notes/FINAL_PAGE_BATCH_065_130_REVIEW.md`.

## Final pilot-draft disposition

The last three draft pages were reinspected directly:

- PDF 26 → song `001`;
- PDF 29 → song `002`;
- PDF 30 → song `003`.

Results:

- `001`: corrected pilot `அறியாண்டி` to source-visible `அறியான்டி`; confirmed `வேணசெல்வம்`, `பெண்ணி`, and `ஏழைக்கிக்` exactly as printed;
- `002`: pilot transcription passed without lyric correction; printed `தங்`, `கல்`, and `தங்,கல்` labels remain exact;
- `003`: resolved the two pilot uncertainty markers directly from the scan as `வந்தேன் தவழ்ந்தாய்?` and `பாழான எந்தன் வயிற்றில் பிறந்தாய் ராஜா!`.

## Cross-page records

The following verified songs span more than one song-bearing page and remain one file each:

- `009` — PDF 38–39;
- `019` — PDF 53–54;
- `023` — PDF 58–59;
- `024` — PDF 62–63;
- `036` — PDF 86–87;
- `037` — PDF 90–91;
- `051` — PDF 121–122;
- `052` — PDF 123–124.

## PDF-specific processing rule

For this PDF only, process actual numbered lyric pages/direct continuations and ignore every other page for lyric-file creation. Do not import missing lyrics from elsewhere.

## Gate result

**PASS — Tamil transcription complete-verified; Tamil fidelity audit complete.**

English translation is now unblocked but remains a separate derivative layer and has not yet started.
