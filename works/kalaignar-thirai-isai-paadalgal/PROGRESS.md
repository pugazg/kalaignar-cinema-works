# Progress — கலைஞர் திரை இசைப் பாடல்கள்

## Current phase

**Tamil song transcription — in progress.**

Source intake and the full anthology structural map are complete. The complete numbered-song inventory is established before further transcription.

## Counts

| Item | Status |
|---|---:|
| Physical PDF pages | 194 |
| Tamil film sections in numbered corpus | 23/23 mapped |
| Numbered songs | 54/54 inventoried |
| Draft song files | 3 |
| Verified song files | 0 |
| Review song files | 0 |
| Not-started song files | 51 |
| English translations | 0 |

## Completed activity

### Intake / map

- source identity, file size, SHA-256 and physical page count recorded;
- title/compiler/publisher/edition/ISBN recorded from the scan;
- front matter, filmography, contents, numbered corpus and back matter mapped;
- all 23 numbered-film sections mapped;
- all 54 printed song numbers inventoried in source order;
- separate song-anthology processing rules established at `docs/SONG_ANTHOLOGY_PROCESSING_GUIDE.md`.

### Initial song batch

Created draft source-led records for:

1. `001` — `ஊருக்கு உழைப்பவண்டி` — `மந்திரிகுமாரி` — PDF 26;
2. `002` — `இல் வாழ்வினிலே ஒளி ஏற்றும் தீபம்` — `பராசக்தி` — PDF 29;
3. `003` — `பூமாலை நீயே...` — `பராசக்தி` — PDF 30.

These records are **draft, not verified**. Song 001 and song 003 contain source forms that deserve a dedicated visual recheck before promotion to verified.

## Attribution checkpoint

The anthology presents the numbered corpus as Kalaignar film songs. Repository status therefore begins at `anthology-attributed`.

This status means: **the 2024 anthology makes the attribution**. It does not by itself mean an original film-era primary source has been checked for every item.

## Special note

The `மந்திரிகுமாரி` prose on PDF 25 mentions `ஆளப்பிறந்தவன் தமிழன் அவன்தானே` as another Kalaignar-written song and says it was censored/prohibited. Because the lyric is not printed as a numbered record, it is documented in `notes/anthology-notes.md` but is not inserted into `001–054`.

## Next activity

Process **songs 004–011** from **`நாம்`**, PDF **31–41**:

1. inspect the film metadata / song-list context page(s);
2. transcribe each numbered lyric from the rendered scan;
3. preserve composer, voice, turn labels, refrains and lineation;
4. recheck the batch visually;
5. update `songs/index.json`, this progress file, `AUDIT.md`, `metadata.yaml` and the work README.

Do not begin English translation before Tamil verification.
