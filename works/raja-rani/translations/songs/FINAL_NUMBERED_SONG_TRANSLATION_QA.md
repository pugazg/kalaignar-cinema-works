# Raja Rani — Final Numbered-Song English Translation QA

Status: **PASS — 11/11 numbered front-matter songs complete-verified**

This checkpoint verifies the dedicated English translation layer for all eleven numbered `பாட்டு` bodies printed across PDF 4–9 of `TVA_BOK_0017188_ராஜா_ராணி.pdf`.

## Coverage

- numbered songs expected: **11**;
- English song records present: **11/11**;
- verified: **11**;
- review: **0**;
- draft: **0**;
- not started: **0**;
- translation sections/turn groups: **67**;
- source Tamil line/cue entries represented: **181**;
- English line/cue entries represented: **181**;
- multi-page numbered-song records: **4** — songs 2, 3, 8 and 10.

The line/cue count treats each stored `source_tamil_lines` entry as one source-facing unit and verifies a one-for-one English entry in the corresponding section. It does not claim that the printed booklet itself numbers lyric lines.

## Source authority and structural checks

PASS:

1. Every English record points to one of the 11 verified Tamil derivatives under `works/raja-rani/songs/tamil/`.
2. Song IDs remain exactly `raja-rani-song-001` through `raja-rani-song-011`; the English derivative IDs are separately `raja-rani-song-en-001` through `raja-rani-song-en-011`.
3. PDF provenance matches the verified song inventory:
   - song 1: PDF 4;
   - song 2: PDF 4–5;
   - song 3: PDF 5–6;
   - song 4: PDF 6;
   - songs 5–7: PDF 7;
   - song 8: PDF 7–8;
   - song 9: PDF 8;
   - song 10: PDF 8–9;
   - song 11: PDF 9.
4. Source-visible turn/performance labels are retained in metadata where present, including Geetha/Babu, Rani, numbered customers, `தாண்டவன் பாடல்`, `விருத்தம்`, `ரேடியோ பாடல்`, `ராணியின் சோகப் பாடல்`, and the song/dialogue interleaving inside song 8.
5. Refrain cues such as `(ஆ)`, `(கா)`, `(மூணு)`, `(கண்)`, `(திரு)`, `(ஒரு)` and `(சரியான)` are retained or transliterated as cues rather than expanded into lyrics not printed at that location.
6. No missing soundtrack lyric, alternate-edition wording, web lyric or later-anthology textual variant was imported.

## Difficult-source fidelity

PASS. Translation does not silently repair verified Tamil.

Examples deliberately preserved include:

- song 1's split `உரு / வானால்` lineation;
- song 2's opaque `சாக சந் தானா`, transliterated rather than emended;
- song 3's rapid ticket-price code-switching and opaque comic `ட்ரீயோ...` sequence;
- song 4's concrete strap-torn old-slipper image and pointed catalogue of laughter types;
- song 6's `தாழி`, catastrophic `ஊழி`, and `கற்புக்கு இலக்கணம்` imagery;
- song 7's `முல்லை` image and compact source syntax;
- song 8's `லீலா / லாலீ / போலீ` sound-play, Harishchandra sarcasm, and playing-card suit word-play;
- song 10's verified `மானில` context and fragmentary closing `மங்கை என் வாழ்வெல்லாம்`;
- song 11's joined `என்னாசை`, retained conservatively rather than normalized.

## Authorship integrity

PASS — translation changed **no authorship disposition**.

Later-anthology Kalaignar-attributed numbered songs remain exactly:

- 3
- 5
- 6
- 7
- 8

Unresolved lyricist numbered songs remain exactly:

- 1
- 2
- 4
- 9
- 10
- 11

Original Raja Rani booklet item-level lyricist credits remain **0**. A verified English translation is not evidence for upgrading an unresolved or anthology-attributed authorship tier.

## Screenplay performance-link integrity

PASS — no link was added or promoted.

Verified links remain:

- `raja-rani-song-perf-001` → song 3 / scene 4;
- `raja-rani-song-perf-002` → song 5 / scene 16;
- `raja-rani-song-perf-003` → song 8 / scene 40.

Review link remains review:

- `raja-rani-song-perf-004` → song 11 / scene 58.

The scene-58 cue does not print a song number or lyric line, so the English song layer does not promote that contextual relation.

## Separation from screenplay translation

PASS. The existing screenplay English layer remains unchanged at:

- **58/58** archival scenes;
- **1,236** verified screenplay units;
- **1,071/1,071** immutable dialogue links;
- **19** source-unlabelled spoken units;
- **15** genuine cross-page translation units.

Full numbered lyrics are not duplicated into scene translation records where the screenplay prints only a singing cue.

## Final disposition

The source-linked English textual translation of Raja Rani is now complete for both supported layers:

- screenplay: **58/58 scenes complete-verified**;
- numbered front-matter songs: **11/11 complete-verified**.

No Tamil source, scene, immutable dialogue record, character mapping, authorship tier, or performance-link status was changed by this numbered-song translation phase.

## Next activity

Build the deterministic whole-work bilingual reader/export from the completed verified screenplay and numbered-song translation layers, run whole-work QA, and prepare source-linked Reading Room integration data. Do not create a new standalone PDF/EPUB merely because translation is complete unless separately requested or independently useful.
