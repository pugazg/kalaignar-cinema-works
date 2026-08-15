# திரும்பிப்பார்! — song / performance authorship gate

**Stage:** structured derivatives  
**Canonical authority:** verified Tamil transcription / scene derivatives  
**Authorship gate:** **complete-with-unresolved-authorship**  
**Candidate occurrences:** **8**  
**Verified authorship:** **3** occurrences / **2** distinct named songs  
**Unresolved authorship:** **5** occurrences  
**Tamil song derivative files:** **0**

This directory inventories every source-visible song, singing, chant or named-song structure identified by the verified structural audit. It separates **what the booklet actually prints** from external item-level authorship metadata. Nothing in this layer may rewrite or expand the canonical Tamil.

## Files

- `schema.json` — song/performance inventory schema.
- `credits.json` — result of the booklet-credit gate.
- `tracklist-evidence.json` — separately documented item-level public music-catalog evidence.
- `inventory.json` — eight canonical song/performance occurrence records.
- `index.json` — completion checkpoint and unresolved-authorship ledger.

## Booklet credit gate

PDF **1–8** were visually inspected. The cover credits **`கதை - வசனம் — கலைஞர் மு. கருணாநிதி`**, but the front matter contains no `பாடல்கள்` heading, lyricist list or item-level song attribution. The story-dialogue credit is therefore **not** treated as a lyric credit.

The rule is strict: an occurrence remains `unresolved` unless the canonical booklet itself attributes it or separately documented item-level evidence establishes authorship.

## Source-visible inventory

Eight occurrences are dispositioned:

1. scene 2 / PDF 10 — Poomaal teaches children through song; no title or lyrics printed — **unresolved**.
2. scene 6 / PDF 15 — Bama's song has just ended; no title or lyrics printed — **unresolved**.
3. scene 11 / PDF 19 — Paranthaman and another woman sing in a boat; no title or lyrics printed — **unresolved**.
4. scene 14 / PDF 22 — stage song; no title or lyrics printed — **unresolved**.
5. scene 29 / PDF 35 — standalone `கோஷம்` labour chant — **unresolved authorship** and not asserted to be a soundtrack song.
6. scene 31 / PDF 38 — named song `பாண்டியன் என் சொல்லை` — **பாரதிதாசன்**, verified from item-level external catalog evidence.
7. scene 42 / PDF 57 — `கலப்படம் கலப்படம்` — **கண்ணதாசன்**, verified from item-level external catalog evidence.
8. scene 43 / PDF 57 — office-boy reprise/reference to the same `கலப்படம்` song — **கண்ணதாசன்**.

The public soundtrack catalog contains nine tracks, but this archive maps only the two titles that the booklet itself names and that have an exact title correspondence. The other soundtrack rows are **not** guessed onto the unnamed performance references.

## Late source correction discovered at this gate

Reinspection of the rendered scan at **PDF 38 / printed p.30** showed that scene 31 prints **`பாண்டியன் என் சொல்லை`**, not the earlier transcription `பாண்டியன் என் செல்வம்`. The correction was made from the scan itself in both the canonical part-03 transcription and `scenes/scene-31.md` before item-level authorship was mapped.

The external catalog independently contains `Pandiyan En Sollai`, but it was not used to decide the canonical Tamil reading. The scan remains the text authority.

## Why there are no Tamil song files

Neither source-named soundtrack song has a complete lyric body printed in this booklet:

- scene 31 gives a song title/performance reference only;
- scene 42 prints only `கலப்படம் கலப்படம்`, and scene 43 names the reprise.

Accordingly, this activity creates **no reconstructed song-lyric file**. Lyrics are not imported from audio, websites, streaming services, later editions or another song booklet. The canonical scene files already preserve every song-related word that this source supplies.

## Next structured derivative

Begin **English translation as a separate derivative layer**, starting with a source-linked schema and a small verified pilot. Song/performance references may be translated only to the extent that they occur in the canonical Tamil; absent lyrics must remain absent.
