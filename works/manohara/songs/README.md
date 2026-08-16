# மனோகரா — song / performance authorship gate

**Stage:** structured derivatives  
**Canonical authority:** verified Tamil transcription / scene derivatives  
**Authorship gate:** **complete-with-unresolved-authorship**  
**Candidate occurrences:** **6**  
**Verified authorship:** **1** occurrence  
**Review authorship:** **1** occurrence  
**Unresolved authorship:** **4** occurrences  
**Tamil song derivative files:** **0**

This directory inventories every source-visible song or singing structure identified in the verified Manohara booklet and separates **what the booklet actually prints** from external item-level authorship evidence. Nothing in this layer rewrites or expands canonical Tamil or the immutable dialogue records.

## Files

- `schema.json` — Manohara song/performance inventory schema.
- `credits.json` — booklet front-matter credit gate.
- `tracklist-evidence.json` — separately documented external title/authorship evidence.
- `inventory.json` — six source-visible occurrence records.
- `index.json` — completion checkpoint and authorship-status ledger.

## Booklet credit gate

PDF **1–6** were visually inspected. The title page prints **`திரைக்கதை வசனம் / மு. கருணாநிதி`**. The front matter contains no `பாடல்கள்` heading, lyricist list, contributor block or item-level song attribution. The screenplay-dialogue credit is therefore **not** treated as a lyric credit.

The rule remains strict: an occurrence is `verified` only when the booklet itself supplies an item-level credit or separately documented item-level external evidence establishes authorship. Performer identity, nearby dialogue, film-wide lyricist lists and soundtrack memory do not establish authorship.

## Source-visible inventory

Six occurrences were verified against the rendered scan and canonical scene files:

1. `manohara-s003` / PDF **9** — `(வசந்தன் ; விகடன் சந்தேகமில்லே பாட்டு)` — source-visible named song reference; **authorship unresolved**. The official Saregama Manohara page confirms a `Santhegam Illai` track title, but the retrieved official metadata does not establish an item-level lyricist.
2. `manohara-s008` / PDF **16** — nested-play காதல்பாட்டு `(நிலாவிலே ! சல்லாபமே!! பாடுகின்றனர்.)` — **authorship unresolved**. No safe item-level title/lyricist match is forced from broader soundtrack lists.
3. `manohara-s016` / PDF **30** — `“வாழ்வதே மாது நான்” பாட்டு` — **authorship unresolved**. Public discographies contain a similar Manohara title, but the evidence inspected does not securely assign a lyricist to this booklet occurrence.
4. `manohara-s019` / PDF **32** — `[“சிங்காரப் பைங்கிளியே... பேசு” — பாட்டு]` with the following boat-singing direction — **authorship review**. External sources conflict: a digitized publication associates the song with உடுமலை நாராயண கவி, while another Tamil-cinema retrospective attributes it to மு. கருணாநிதி. The booklet itself gives no lyricist, so the archive does not choose between them.
5. `manohara-s024` / PDF **37** — `“பொழுது புலர்ந்தது” பாட்டு` — **சுரபி, verified**. The title corresponds to Saregama's Manohara track `Pozhuthu Pularnthathey`, and Saregama's Surabi artist page identifies Surabi as a lyricist while listing that exact Manohara track.
6. `manohara-s030` / PDF **41** — `வசந்த விழாக் கொண்டாட்டம். பாட்டுகள்... மனோகரனும் விஜயாவும் பாடுகிறார்கள்` followed by source-labelled lines beginning `விஜயா : இந்த அன்பு மாறவே மாறாதே...` — **authorship unresolved**. These labelled lines are already preserved in the immutable dialogue layer. No soundtrack row is guessed onto this untitled booklet occurrence.

The PDF-wide text search also returned the ordinary word `குளிப்பாட்டு` at PDF 83. It is prose, not a song/performance structure, and is therefore excluded from this inventory.

## External evidence discipline

The official Saregama Manohara album page is useful for title correspondence but is not assumed to be an exhaustive representation of everything named or performed in this booklet. Only one item-level lyricist attribution met the archive's verification standard at this gate: **`பொழுது புலர்ந்தது` — சுரபி**.

`சிங்காரப் பைங்கிளியே... பேசு` remains deliberately in `review` because the external attribution record is contradictory. This preserves the disagreement rather than converting a disputed secondary claim into a source fact.

## Why there are no Tamil song files

The booklet prints song titles/refrain references and, in scene 30, a partial labelled singing sequence, but it does **not** print a complete standalone lyric body for any of the six occurrences.

Accordingly this activity creates **no reconstructed Tamil lyric file**. Lyrics are not imported from recordings, streaming services, record catalogs, websites, later editions or another song booklet. The canonical scene and dialogue files already preserve every song-related word supplied by this edition.

## Next structured derivative

Begin **English translation as a separate source-linked derivative layer**. Song/performance material may be translated only to the extent printed in the canonical Tamil. Absent lyrics must remain absent, and the `review` / `unresolved` authorship dispositions remain independent of translation.
