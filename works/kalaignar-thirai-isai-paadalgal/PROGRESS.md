# Progress — கலைஞர் திரை இசைப் பாடல்கள்

## Current phase

**Tamil song transcription and fidelity verification — in progress.**

Source intake, full anthology structural mapping and the complete numbered-song inventory are established. Song transcription now advances in source order with each completed batch visually rechecked before verification.

## Counts

| Item | Status |
|---|---:|
| Physical PDF pages | 194 |
| Tamil film sections in numbered corpus | 23/23 mapped |
| Numbered songs | 54/54 inventoried |
| Draft song files | 3 |
| Verified song files | 8 |
| Review song files | 0 |
| Not-started song files | 43 |
| English translations | 0 |

## Completed activity

### Intake / map

- source identity, file size, SHA-256 and physical page count recorded;
- title/compiler/publisher/edition/ISBN recorded from the scan;
- front matter, filmography, contents, numbered corpus and back matter mapped;
- all 23 numbered-film sections mapped;
- all 54 printed song numbers inventoried in source order;
- separate song-anthology processing rules established at `docs/SONG_ANTHOLOGY_PROCESSING_GUIDE.md`.

### Initial draft batch — songs 001–003

Draft source-led records remain for:

1. `001` — `ஊருக்கு உழைப்பவண்டி` — `மந்திரிகுமாரி` — PDF 26;
2. `002` — `இல் வாழ்வினிலே ஒளி ஏற்றும் தீபம்` — `பராசக்தி` — PDF 29;
3. `003` — `பூமாலை நீயே...` — `பராசக்தி` — PDF 30.

These three remain **draft, not verified**. Songs 001 and 003 contain source forms that still require their dedicated line-by-line recheck.

### Verified batch — songs 004–011 / `நாம்`

The complete `நாம்` section at PDF **31–41** was inspected directly from the rendered scan. Eight song files were transcribed and visually rechecked:

- `004` — `மாரி மகமாயி மாரி` — PDF 33 — verified;
- `005` — `பேசும் யாழே பெண் மானே` — PDF 34 — verified;
- `006` — `மணமில்லா மலர் நானம்மா!` — PDF 35 — verified;
- `007` — `பேசும் யாழே பெண் மானே` (`ஜிக்கி (சோகம்)`) — PDF 36 — verified;
- `008` — `வருவாய் வருவாய்...` — PDF 37 — verified;
- `009` — `புதியதோர் பாதை வகுப்போம்` — PDF 38–39 — verified;
- `010` — `வாழ்க வாழ்க வாழ்க வாழ்கவே` — PDF 40 — verified;
- `011` — `எதையும் தாங்கும் இதயம் வேண்டும்` — PDF 41 — verified.

Batch review: `notes/BATCH_004_011_REVIEW.md`.

Important dispositions:

- song 004 was corrected to the scan-supported `மாரி`, not the first-pass typo `மாறி`;
- song 006 prints no separate `குரல்` line, so no singer was inferred; its source role `மீனா:` is retained;
- song 009 spans PDF 38→39 and remains one song record;
- source-colloquial/unusual forms and role/refrain labels were preserved rather than normalized.

## Attribution checkpoint

The anthology presents the numbered corpus as Kalaignar film songs. Repository status therefore remains `anthology-attributed` unless separately strengthened by original-film primary-source evidence.

For `நாம்`, PDF 32 explicitly places `கலைஞர்` beside the eight entries represented by songs 004–011. The separate `ஆயிரம் தெய்வங்கள்` entry is printed there with `பாரதியார்` and is not inserted into this numbered Kalaignar-song batch.

## Special note

The `மந்திரிகுமாரி` prose on PDF 25 mentions `ஆளப்பிறந்தவன் தமிழன் அவன்தானே` as another Kalaignar-written song and says it was censored/prohibited. Because the lyric is not printed as a numbered record, it is documented in `notes/anthology-notes.md` but is not inserted into `001–054`.

## Next activity

Process **songs 012–018** from **`அம்மையப்பன்`**, PDF **42–50**:

1. inspect the film metadata / song-list context page(s);
2. transcribe every numbered lyric in source order;
3. preserve exact composer, voice, character/turn and refrain labels;
4. recheck every lyric line against the rendered scan;
5. update the inventory and checkpoint documents;
6. do not begin English translation before Tamil verification.
