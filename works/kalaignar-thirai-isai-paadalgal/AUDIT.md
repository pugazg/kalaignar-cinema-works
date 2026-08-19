# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Scope

This checkpoint covers the **complete 194-page song-presence scan** and line-level Tamil lyric verification through numbered song **023**.

The rendered scan is authoritative. The full-PDF scan classifies pages; a song is marked verified only after its own song-bearing page(s) are visually checked.

## Full-PDF page classification

**PASS — 194/194 pages scanned.**

- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs located: **54/54**;
- final song-bearing page: **130**.

Authoritative ledger: `notes/FULL_PDF_SONG_PAGE_SCAN.md`  
Machine map: `songs/page-map.json`

## Lyric fidelity status

- draft: **3** (`001–003`);
- verified: **20** (`004–023`);
- review: **0**;
- not started: **31** (`024–054`).

Verified page runs:

- PDF 33–41 → songs 004–011;
- PDF 44–50 → songs 012–018;
- PDF 53–59 → songs 019–023.

Latest detailed review: `notes/PAGE_BATCH_053_059_REVIEW.md`.

### Latest fidelity dispositions

- PDF 51–52 were skipped as non-song pages.
- Song 019 remains one record across PDF 53–54 and preserves speaker labels, ticket-price wordplay, colloquial source forms and repeated cues.
- Song 020 retains `வேலை யில்லாத` and `எனமனம்போலவே` as printed.
- Song 021 retains `ஆழிசூழ்`, `வந்திங்கு`, repetitions and source lineation.
- Song 022 retains `மணிப் புறா`, `பூமானே`, `ரோஜாக் கொல்லை`, `முகந்தானே`, and `சுகந்தானே`.
- Song 023 remains one source record across PDF 58–59. Its printed `வசனம்` / `பாட்டு` alternation is preserved, including card-suit forms `கிளாவர்`, `டைமன்`, and `இஸ்பேட்`.

## PDF-specific processing rule

For this PDF only, process actual numbered lyric pages/direct continuations and ignore every other page for lyric-file creation. Do not import missing lyrics from elsewhere.

## Next

Skip PDF **60–61**. Resume at **PDF 62–63 / song 024** and continue only through the whitelist.

Songs 001–003 still require their dedicated fidelity recheck before the Tamil corpus can become contiguous-complete.
