# Kalaignar-authorship inclusion evidence — கலைஞர் திரை இசைப் பாடல்கள்

Durable, hand-written archival record. Lives under `notes/`, outside all
status-generator control. Nothing here is regenerated; edit it by hand.

This note explains the complete 54-song Kalaignar-authorship evidence gate and
the proposed public inclusion set it produces. The machine-readable outputs are:

- `authorship/inclusion-evidence.json` — the song-level evidence register, 001–054;
- `authorship/public-inclusion.json` — the derived inclusion manifest;
- `authorship/validate.py` — the fail-closed validator over both.

## 1. Why this gate exists

`metadata.yaml` records `default_song_attribution_state: anthology-attributed`
and `primary_source_verification_requires_separate_evidence: true`. Every one of
the 54 numbered lyrics carries that same default. "Anthology-attributed" states
only that the lyric was printed in a volume titled
கலைஞர் திரை இசைப் பாடல்கள். It is a fact about the
book, not a song-level finding about who wrote the words.

Publishing the corpus as Kalaignar's lyrics requires a stronger, song-level
claim. This gate supplies exactly that claim, song by song, or declines to.

## 2. The evidence apparatus in the controlling scan

The controlling source is
`TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`,
SHA-256 `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`,
130,427,193 bytes — byte-exact against `metadata.yaml` and `songs/index.json`.
Pages were rendered as images and read directly. OCR was not used as textual
authority.

The decisive apparatus is internal to the source. Each film section prints a box
headed இப்படத்தில் இடம் பெற்ற பாடல்கள்
listing that film's songs, and — for most films — a **per-song lyricist column**
beside each title. That column names கலைஞர் for some songs and
other writers (பாரதிதாசன், மருதகாசி, வாலி, வைரமுத்து,
கண்ணதாசன், ஆலங்குடி சோமு, எஸ்.ஏ.ராஜ்குமார்,
இளையபாரதி and others) for the rest. It is a song-level, explicit,
source-internal attribution.

Across the 23 film sections:

| Apparatus present | Film sections |
| --- | --- |
| Per-song lyricist column | 21 |
| Collective credit only, no per-song mapping | 1 (அம்மையப்பன்) |
| No song list printed at all | 1 (நெஞ்சுக்கு நீதி) |

Every one of the 23 song-list pages was read for this gate: PDF pages 25, 28,
32, 43, 52, 61, 69, 72, 76, 79, 82, 89, 96, 99, 102, 105, 108, 112, 115, 119,
126 and 129, plus PDF page 85, which prints no list.

## 3. Evidence levels and decision vocabulary

Evidence levels:

- **A** — primary contemporary documentary evidence;
- **B** — independent authoritative secondary evidence;
- **C** — anthology-internal, explicit and song-specific attribution;
- **D** — implicit or non-song-specific evidence. Never sufficient.

Decisions:

- **established-kalaignar** — song-specific source evidence attributes the lyric to Kalaignar;
- **established-other** — song-specific source evidence attributes it to a named writer who is not Kalaignar;
- **unresolved** — the source leaves this song's lyricist undetermined;
- **insufficient-evidence** — no song-specific authorship evidence is present in the controlling source.

**Inclusion rule.** A song enters the proposed public inclusion set if and only
if its decision is `established-kalaignar` at evidence level A, B or C. Level D
never qualifies. `validate.py` enforces this rule against every record rather
than trusting the stored flag.

**`unresolved` and `insufficient-evidence` are never converted into "not
Kalaignar".** They are different findings. Both mean the source does not say.
The validator additionally rejects any withheld record whose written basis reads
as a positive finding of non-authorship.

## 4. Outcome

| Decision | Songs | Count |
| --- | --- | --- |
| established-kalaignar | 001–011, 019–035, 037–054 | 46 |
| unresolved | 012–018 | 7 |
| insufficient-evidence | 036 | 1 |
| established-other | — | 0 |

Proposed public inclusion set: **46 of 54**.

No song in this corpus was adjudicated `established-other`. That is expected:
the anthology prints numbered lyrics only for the songs its own per-film lists
attribute to கலைஞர், and it lists the other writers' songs without
reproducing them.

## 5. The two withheld groups

### 012–018 — அம்மையப்பன், unresolved

PDF page 43 prints one collective credit for the whole film —
பாடலாசிரியர்கள் : கலைஞர், சுரதா,
எம்.கே. ஆத்மநாதன், முத்துக்கூத்தன் — with no
per-song mapping. The compiler's own note on the same page, headed
இசைத்தட்டே இல்லை, records that neither the film nor
a gramophone record survives, that all of the film's songs are reproduced here,
and states in terms that it could not be confirmed which of them Kalaignar
wrote.

The source therefore names Kalaignar as one of four possible writers for seven
songs and declines to say which. These seven remain `unresolved`. Kalaignar may
well have written some or all of them; the source does not license the claim
song by song.

### 036 — நெஞ்சுக்கு நீதி, insufficient-evidence

The film section (PDF page 85) prints no song list, and so no lyricist column at
all. Its only Kalaignar credit is
கதை, திரைக்கதை, வசனம் : கலைஞர் மு.கருணாநிதி
— story, screenplay and dialogue. That is a writing credit for the film, not a
lyric credit, and it must not be read across into song authorship. The numbered
lyric page (PDF page 86) prints only இசை and குரல்.

What remains is the implicit evidence that the song appears in a volume titled
கலைஞர் திரை இசைப் பாடல்கள். That is level D, and
level D does not qualify. This is not a finding that the song is not
Kalaignar's.

## 6. Two title-match gaps, resolved on the lyric pages

Two Kalaignar-attributed list entries do not match the opening line of the
numbered lyric they belong to. Both were resolved by reading the lyric pages
themselves, not by inference.

**Song 023 — ராஜா ராணி.** The p. 52 list has no entry
கண்ணற்ற தகப்பனுக்கு. Its fifth Kalaignar entry is
பூனை கண்ணை மூடிக்கொண்டால், which appears verbatim
as the fourth line of the printed lyric on PDF page 58:
பூனை கண்ணை மூடிக்கொண்டால் பூலோகம்
இருண்டு போகுமோ?. The list titles the song by an interior line.
The film's five Kalaignar-attributed list entries then correspond one-to-one,
without remainder, to the five numbered lyrics 019–023; the six entries credited
to other writers have no printed lyric in the anthology.

**Song 043 — மக்கள் ஆணையிட்டால்.** The p. 102 list credits
உங்கள் ஓட்டு கதிரவனுக்கா, to கலைஞர்.
The numbered lyric on PDF page 103 opens with that line as a quoted refrain
above the body: "உங்கள் ஓட்டு கதிரவனுக்கா, எங்கள்
ஓட்டு கதிரவனுக்கே…". The film's one
Kalaignar entry corresponds to the anthology's one printed lyric for the film;
the other four entries are credited to எஸ்.ஏ.ராஜ்குமார் and are
not reproduced.

Both are recorded in the register as `list_to_lyric_match: "internal-line"`.

## 7. Printed title variants, recorded not corrected

Where a list entry and its numbered lyric title differ, the difference is
recorded as a source variant and never used to correct either form. The register
classifies each match as `exact`, `prefix-variant`, `punctuation-variant`,
`spelling-variant`, `spacing-variant` or `internal-line`. Song 042 is a spelling
variant (சுருளு மீசைகாரனடி வேலுதம்பி on the list,
சுருளு மீசைக்காரனடி வேலுத்தம்பி on the lyric page);
song 053 is a spacing variant. Both forms are printed in the same controlling
scan. This follows the title-authority rule already recorded in
`notes/READING_ROOM_TITLE_RECONCILIATION.md`.

## 8. Song 001 — a second, explicit witness

PDF page 25 carries, beyond the list line, the compiler's own statement that 15
songs were prepared for மந்திரிகுமாரி, that Kalaignar wrote two of
them — ஆளப்பிறந்தவன் தமிழன் அவனிதனிலே and
ஊருக்கு உழைப்பவண்டி — that the first was refused by the
censor, that Kalaignar asked for his name to be kept off the titles so the film
credits and the record label name கா.மு.ஷெரீப் and
மருதகாசி instead, and that for the remaining thirteen songs it is
not known who wrote which. Song 001 is
ஊருக்கு உழைப்பவண்டி, named there explicitly.

This page is also why the absence of Kalaignar's name from a film's titles is
never treated here as evidence against his authorship.

## 9. What this gate did not do

- No authorship was inferred from theme, vocabulary, Dravidian ideological
  content, poetic style, known phrases, chronology, film memory, soundtrack
  memory, or from what sounds like Kalaignar.
- No date, venue, occasion, printed page number, song boundary, authorship or
  rights status was supplied that the source does not print.
- No external web source, encyclopaedia, blog, video description, social post or
  lyrics site was used as authorship evidence.
- OCR was not used as textual authority.
- The register makes **no rights or licensing determination**. Inclusion here
  concerns authorship evidence only.
- The controlling scan was not modified, and no song text, translation, edition,
  payload or existing status field was changed by this work.

## 10. Validator

`authorship/validate.py` is fail-closed and follows the repository validator
contract: exit **0** on success, **1** on data-integrity failure, **2** when it
cannot validate. It checks that the register pins the same controlling-scan
SHA-256 as `songs/index.json` and `metadata.yaml`; that it covers songs 001–054
exactly once each, in ascending order; that every record's identity, film, lyric
title and lyric pages agree with `songs/index.json`; that the inclusion rule
holds for every record independently of the stored flag; that every included
song names the printed list page, list entry and printed lyricist it rests on;
that every declared count matches the records; and that
`authorship/public-inclusion.json` is the byte-exact derivation of the register.

`python3 authorship/validate.py` verifies. `--write` regenerates the manifest.
The manifest is generated: change the register and regenerate, never hand-edit
it.

## 11. Status of this record

The evidence gate is complete for all 54 numbered songs of this work. The
proposed public inclusion set of 46 songs is a **proposal for independent
review**; it has not been applied to any downstream edition, payload or Reading
Room surface, and this work performs no such application.
