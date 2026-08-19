# கலைஞர் திரை இசைப் பாடல்கள்

Source-led archival work for the supplied anthology **`கலைஞர் திரை இசைப் பாடல்கள்`**, compiled by **நெல்லை ஜெயந்தா** and published by **தமிழ்நாடு இயல் இசை நாடக மன்றம்**.

This is a **song anthology work**, not a screenplay/dialogue-booklet work. Its numbered song corpus is stored under `songs/`.

## Source authority

The supplied scan controls what this **2024 anthology edition** prints: its lyric text, song numbering, film grouping, headings, music/voice labels and editorial attribution claims.

Because this is a later anthology, an anthology attribution is not silently promoted to an original-film primary-source attribution. The repository uses `anthology-attributed` unless stronger source-specific evidence has separately been established.

The source PDF itself is not committed to this repository.

## Source checkpoint

- archive identifier from supplied filename: `TVA_BOK_0065867`;
- source filename: `TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`;
- source SHA-256: `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- binary size: **130,427,193 bytes**;
- physical PDF pages in the supplied binary: **194**;
- printed title: **`கலைஞர் திரை இசைப் பாடல்கள்`**;
- compiler: **`நெல்லை ஜெயந்தா`**;
- edition statement: **First Edition — June 2024**;
- printed `No of pages` statement: **192**;
- ISBN: **978-81-961205-2-8**;
- publisher: **தமிழ்நாடு இயல் இசை நாடக மன்றம்**.

The PDF is image-only for archival purposes; OCR/text extraction is not authoritative.

## Structural checkpoint

The full source has been mapped before large-scale lyric transcription.

- front matter / essays / introductory filmographies: PDF 1–20;
- contents: PDF 21–23;
- numbered Tamil film-song corpus: PDF **24–130**;
- film sections in numbered corpus: **23**;
- printed numbered songs: **001–054**;
- other-language film details: PDF 131–139;
- `கலைஞரின் பட உலகப் பயணம்`: PDF 140–181;
- `கலைஞருக்குக் கலை உலகக் கதவைத் திறந்தவர்கள்`: PDF 182–188;
- bibliography: PDF 189;
- note/back-matter pages: PDF 190–194.

See `mapping.md` for the section-by-section map.

## Song work status

- complete song inventory: **54/54**;
- draft lyric records: **3/54** (`001`–`003`);
- verified lyric records: **8/54** (`004`–`011`);
- review lyric records: **0/54**;
- not-started lyric records: **43/54** (`012`–`054`);
- English translation: **not-started**;
- reader/export: **not-started**.

Songs 004–011 form the complete verified `நாம்` batch. The rendered scan was checked across PDF **31–41**; numbered lyric pages are PDF **33–41**, with song `009` continuing across PDF **38–39**.

Key fidelity dispositions from this batch:

- `004` uses scan-supported **`மாரி`**, not the initial `மாறி` typo;
- `005` retains source spacing `பெண் மானே` and its `குமரன்` / `மீனா` / `இருவரும்` turns;
- `006` prints no separate `குரல்` line, so no singer identity is inferred; source role `மீனா:` is retained;
- `007` retains printed `ஜிக்கி (சோகம்)`;
- `008` retains source forms such as `சைபோக`, `சைரந்திரியே`, `மம்முதா`;
- `009` is one source record across two pages;
- `010` keeps the scan-visible `பலியாக தருகின்ற இளமை` rather than silently changing it;
- `011` retains its `(எதையும்)` refrain cues and source political/philosophical wording.

See `notes/BATCH_004_011_REVIEW.md` for the complete batch audit.

The first three records remain **draft**. Their dedicated fidelity recheck has not yet been completed, so they are not promoted merely because their pages were inspected during intake.

## Attribution disposition

The anthology's film-level list for `நாம்` on PDF 32 places `கலைஞர்` beside the eight entries represented by songs 004–011. These remain **`anthology-attributed`**, because this 2024 compilation is evidence for the anthology's attribution and not automatically an original film-era authorship source.

The same PDF separately lists `ஆயிரம் தெய்வங்கள்` with `பாரதியார்`; that item is not inserted into the numbered Kalaignar-song batch.

## Important editorial disposition

The anthology's `மந்திரிகுமாரி` note says Kalaignar wrote two songs for the film, including **`ஆளப்பிறந்தவன் தமிழன் அவன்தானே`**, and states that this first song was censored/prohibited. The anthology does **not** print it as a numbered lyric record. It is therefore preserved only as an editorial/prose-mentioned song and is **not** inserted into the numbered `001–054` corpus.

## Documents

- `metadata.yaml` — source and progress metadata;
- `mapping.md` — full structural/film-section map;
- `PROGRESS.md` — live processing checkpoint;
- `AUDIT.md` — source, structural and fidelity audit;
- `PROJECT_HANDOVER.md` — continuation instructions;
- `notes/anthology-notes.md` — editorial/source notes;
- `notes/BATCH_004_011_REVIEW.md` — verified `நாம்` batch review;
- `songs/README.md` — song-layer policy;
- `songs/schema.json` — inventory/record schema;
- `songs/index.json` — all 54 numbered songs and current statuses;
- `docs/SONG_ANTHOLOGY_PROCESSING_GUIDE.md` — reusable repository-level anthology workflow.

## Next activity

Process and visually verify **songs 012–018**, the `அம்மையப்பன்` section at PDF **42–50**, preserving exact anthology lineation, labels, composer/voice metadata and source spelling. Do not begin English translation yet.
