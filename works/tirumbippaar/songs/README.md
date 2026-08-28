# திரும்பிப்பார்! — song / performance authorship gate

**Stage:** structured derivatives  
**Canonical authority:** corrected/scan-closed Tamil transcription and reconciled scene derivatives  
**Authorship gate:** **complete-verified-reconciled with 5 evidence-limited unresolved occurrences**  
**Candidate occurrences:** **8**  
**Verified authorship:** **3** occurrences / **2** distinct named songs  
**Unresolved authorship:** **5** occurrences  
**Tamil song derivative status:** **closed-no-source-full-lyrics**  
**Tamil song derivative files:** **0 by source rule**

This directory inventories every source-visible song, singing, chant or named-song structure identified by the corrected source. It separates **what the booklet actually prints** from external item-level authorship metadata. Nothing in this layer may rewrite, expand or normalize the canonical Tamil.

## Files

- `schema.json` — song/performance inventory schema.
- `credits.json` — result of the booklet-credit gate.
- `tracklist-evidence.json` — separately documented item-level public music-catalog evidence.
- `inventory.json` — eight stable song/performance occurrence records.
- `index.json` — reconciled completion checkpoint, unresolved-authorship ledger and Tamil-derivative gate.

## Corrected-source reconciliation

The historical song inventory predated the final corrected-source scene pass. Reconciliation against the current scene derivatives found four source-metadata drifts while preserving all eight stable occurrence IDs:

- `tirumbippaar-song-001` now carries exact corrected `பூமாலை`, not stale `பூமால்`;
- `tirumbippaar-song-002` now carries corrected `பாமா பாடிமுடிந்ததும் குடத்தை எடுத்துக்கொண்டு போகிறாள்`;
- `tirumbippaar-song-005` now preserves the corrected scene-29 chant punctuation exactly;
- `tirumbippaar-song-007` belongs to **scene 43**, not scene 42. Corrected scene 42 ends after Kumudha asks to hear the song; corrected scene 43 begins with Pandiyan singing what he wrote and prints `கலப்படம் கலப்படம்`. `tirumbippaar-song-008` remains the office-boy reprise later in the same scene 43.

The eight occurrences therefore lie in scenes **2, 6, 11, 14, 29, 31 and 43**, with two distinct occurrences in scene 43. Scene 42 is the spoken lead-in to the song performance but contains no separate inventory occurrence.

## Booklet credit gate

PDF **1–8** were visually inspected. The cover credits **`கதை - வசனம் — கலைஞர் மு. கருணாநிதி`**, but the front matter contains no `பாடல்கள்` heading, lyricist list or item-level song attribution. The story-dialogue credit is therefore **not** treated as a lyric credit.

The rule remains strict: an occurrence stays `unresolved` unless the canonical booklet itself attributes it or separately documented item-level evidence establishes authorship.

## Source-visible inventory

Eight occurrences are dispositioned:

1. scene 2 / PDF 10 — Poomaalai teaches children through song; no title or lyrics printed — **unresolved**.
2. scene 6 / PDF 15 — Bama's song has just ended; no title or lyrics printed — **unresolved**.
3. scene 11 / PDF 19 — Paranthaman and another woman sing in a boat; no title or lyrics printed — **unresolved**.
4. scene 14 / PDF 22 — stage song; no title or lyrics printed — **unresolved**.
5. scene 29 / PDF 35 — standalone `கோஷம்` labour chant — **unresolved authorship** and not asserted to be a soundtrack song.
6. scene 31 / PDF 38 — named song `பாண்டியன் என் சொல்லை` — **பாரதிதாசன்**, verified from item-level external catalog evidence.
7. scene 43 / PDF 57 — Pandiyan sings what he wrote and the booklet prints only `கலப்படம் கலப்படம்` — **கண்ணதாசன்**, verified from item-level external catalog evidence.
8. scene 43 / PDF 57 — office-boy reprise/reference to the same `கலப்படம்` song — **கண்ணதாசன்**.

The public soundtrack catalog contains nine tracks, but this archive maps only the two titles that the booklet itself names and that have an exact title correspondence. The other soundtrack rows are **not** guessed onto the unnamed performance references.

## Source correction discovered during authorship work

Direct reinspection of the rendered scan at **PDF 38 / printed p.30** established that scene 31 prints **`பாண்டியன் என் சொல்லை`**, not the earlier `பாண்டியன் என் செல்வம்` reading. The correction was made from the scan itself before item-level authorship was mapped.

The external catalog independently contains `Pandiyan En Sollai`, but it was not used to decide the canonical Tamil reading. The scan remains the text authority.

## Why the Tamil song-derivative track is closed with zero files

Neither source-named soundtrack song has a complete lyric body printed in this booklet:

- scene 31 gives the title/performance reference `பாண்டியன் என் சொல்லை` but no lyric body;
- scene 43 prints only `கலப்படம் கலப்படம்`, followed by the office-boy reprise reference, but no additional lyric lines.

The other singing occurrences likewise contain only performance context, and scene 29 contains a source-visible labour chant rather than a verified soundtrack-song lyric block.

Accordingly, **zero reconstructed Tamil song-lyric files is the correct completed state**, not unfinished work. Lyrics are not imported from audio, catalog metadata, websites, streaming services, later editions or another song booklet. The canonical scene files already preserve every song-related Tamil word supplied by this controlling source.

## Final gate

- occurrence inventory: **8/8 source-reconciled**;
- stable occurrence IDs: **preserved**;
- verified authorship: **3**;
- unresolved authorship: **5**, retained because the controlling evidence does not resolve them;
- full named-song lyric blocks printed in source: **0**;
- Tamil lyric-derivative files authorized: **0**;
- external evidence changed canonical Tamil: **no**.

No further Tamil song-text derivative is authorized from this booklet. Reopen this track only if a new controlling source supplies printed lyric bodies or explicit item-level credits.
