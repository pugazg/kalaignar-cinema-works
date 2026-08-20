# Project handover — TVA_BOK_0065773 source witness

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Parent work: `works/kalaignar-thirai-isai-paadalgal/`  
Active source path: `works/kalaignar-thirai-isai-paadalgal/sources/tva-bok-0065773/`

## Mandatory startup

Treat live GitHub `main` and the rendered supplied scan as authoritative over stale summaries.

Before changing this witness, read completely:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/SONG_ANTHOLOGY_PROCESSING_GUIDE.md`
3. `docs/ARCHIVAL_WORKFLOW.md`
4. `docs/SOURCE_POLICY.md`
5. `docs/TRANSCRIPTION_GUIDE.md`
6. parent work `README.md`, `metadata.yaml`, `mapping.md`, `AUDIT.md`
7. parent song layer `songs/README.md` and `songs/SOURCE_WITNESS_0065773_DEDUP.md`
8. this witness `README.md`, `metadata.yaml`, `mapping.md`, `PROGRESS.md`, `notes/INTAKE_AUDIT.md`

Do not reopen or overwrite the completed 2024 `TVA_BOK_0065867` Tamil/English corpus merely because this earlier source has the same title.

## Controlling source for this witness

`TVA_BOK_0065773_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`

- 62 physical PDF pages;
- 10,419,528 bytes;
- SHA-256 `56d414a65a61a73b990632eadc17a3b1efdc764d47f64b851060c161a3f98e3b`;
- image-only scan;
- rendered page images control Tamil readings.

Printed identity:

- title: `கலைஞர் திரை இசைப் பாடல்கள்`;
- compiler: `சிலோன் விஜயேந்திரன்`;
- publisher/imprint: `காந்தளகம்`;
- first-edition/date line: `முதற்பதிப்பு:` / `வைகாசி 21, திருவள்ளுவர் 2020 (03.06.89)`.

## Completed structural gate

Source intake and structural mapping are complete:

- front matter PDF 1–9;
- contents PDF 8–9;
- numbered body PDF 10–62 / printed pp.1–53;
- PDF→printed formula throughout body: `printed = pdf - 9`;
- 40 numbered song sections, consecutive 1–40;
- four body thematic divisions;
- no scene system;
- no missing/duplicate physical page observed;
- source discrepancies preserved for contents songs 30–31 and the song-33 film assignment.

## Completed song-presence deduplication gate

Current user instruction supersedes the earlier plan to create a separate full duplicate song corpus:

> Use the existing parent `songs/` folder. If a song is already in that folder, do not include it again.

The 40 source sections were therefore compared against the existing verified parent song layer before any song file was created.

Result:

- **40/40** source sections already represented;
- **39** distinct current song records matched;
- **0** genuinely new songs;
- **0** new parent lyric files;
- **0** existing verified lyric files modified;
- **0** `songs/index.json` additions.

Sections **4** (`ஊற்றெடுக்கும் அறிவினாலே...`) and **13** (`புதியதோர் பாதை வகுத்தோம்!`) both resolve to existing `songs/song-009.md`, because this witness splits material the 2024 witness preserves together.

Non-obvious lyric-level matches were also checked for sections 6, 7, 14, 24, 29 and 39. See `../../songs/SOURCE_WITNESS_0065773_DEDUP.md` for the complete 40-row map.

## Attribution boundary

This anthology witness can support `anthology-attributed` item status for what it prints. It must not be treated as automatic original-film primary-source authorship proof. Do not import absent or damaged lyrics from recordings, web lyrics, subtitles, the 2024 anthology or memory.

## Source-variant boundary

A deduplication match means **same underlying song**, not identical witness text. The 1989 witness has source-supported differences in segmentation, role labels, omissions and wording. Do not merge those differences into the verified 2024 song files unless a future explicit source-variant project establishes a separate editorial policy.

## Exact next activity

No required song import remains for `TVA_BOK_0065773`.

If the user later explicitly asks to continue this witness itself, the next archival activity is:

> **Transcribe and compare the 1989 witness as a separate textual witness for variant study, without creating duplicate parent song records or overwriting verified 2024 song text.**

The completed 2024 source track remains the active verified song corpus for translation/reader derivatives.
