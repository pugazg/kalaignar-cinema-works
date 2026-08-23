# ராஜா ராணி

## Source status

Source: `TVA_BOK_0017188_ராஜா_ராணி.pdf`

Source/archive identifier used by the archive: `TVA_BOK_0017188` (from the supplied/archive filename; not observed as a printed identifier in the scan).

Classification: full dialogue/screenplay publication with songs.

Physical scan:

- PDF pages: **80**
- byte size: **31,600,388**
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`
- embedded OCR text layer: **present**, navigation aid only; rendered scan remains canonical

The title leaf prints **`ராஜா ராணி`**. The cover presents the title without a clearly visible word gap as **`ராஜாராணி`** and directly prints **`மு. கருணாநிதி`** beneath it. The cover does not print a role label next to that name.

The title/publication page visibly gives:

- `மலர் மன்றம்`
- `விருதுநகர்,`
- `விலை அணா 0-8-0`

No explicit edition statement or publication year has been identified in the scan. The final screenplay page has the printer line `அன்பு அச்சகம், மதுரை:-- 56`; the terminal `56` is preserved as printed and is **not** promoted to a publication year without a source label.

This work follows the Parasakthi / Manohara archival model because the source contains screenplay-style material:

- speaker-labelled dialogue;
- stage directions;
- dramatic sequences;
- embedded songs and performances.

## Printed Kalaignar / song credits

The cover directly prints `மு. கருணாநிதி`.

PDF 9 also contains a film-wide `பாடல்கள்:` credit roster:

- `மு. கருணாநிதி`
- `ஏ. மருதகாசி`
- `கே. பி. காமாக்ஷி`
- `எம். கே. ஆத்மநாதன்`
- `வில்லிபுத்தன்`
- `விவேகன்`

This roster does **not** establish item-level authorship for each numbered song. Song authorship remains gated until item-level evidence is available.

## Verified source structure

- PDF 1: front cover
- PDF 2: book/title/publication details
- PDF 3: `கதைச் சுருக்கம்`
- PDF 4–first part of PDF 9: songs/performance text — **11** numbered `பாட்டு` blocks, 1–11
- second part of PDF 9: cast / performers / song-credit roster
- PDF 10–79: canonical screenplay/dialogue range (printed pp.9–78)
- PDF 80: unnumbered back cover

Printed-page mapping for the screenplay is `printed page = PDF page - 1`: PDF 10 → printed p.9 and PDF 79 → printed p.78. PDF 4, the opening song page, does not show a visible printed page number and must not be assigned one by inference.

Embedded dramatic sections:

- `சேரன் செங்குட்டுவன்`: PDF 13–19 / printed pp.12–18
- `அகல்யா நாடக ஒத்திகை`: PDF 40–first part of 41 / printed pp.39–40
- `சாக்ரடீஸ் (நாடகம்)`: PDF 66–72 / printed pp.65–71

The source does **not** present a numbered screenplay-scene sequence. Therefore no artificial scene count, gap list, repeat list or reordered number sequence is assigned at intake. Later scene records must be derived only from verified source-supported boundaries.

## Scene-separator finding

The source uses recurring star ornamentation as scene-boundary evidence, but not one uniform glyph sequence throughout.

Examples include:

- centered rows of stars;
- rule–star–rule ornaments (`—★—`);
- star-flanked headings such as `★ தோட்டம் ★`.

Canonical transcription must preserve the exact printed ornament visible on each page. OCR must not normalize or decide scene separators. Page breaks alone are not scene boundaries.

## Scan-condition findings

No missing or duplicated complete PDF page was identified in the whole-scan intake overview.

Source-condition issues requiring explicit handling include:

- PDF 1: cover wear and a later pencil/handwritten numeric annotation below the printed Kalaignar name; the annotation is not canonical source text;
- PDF 27 / printed p.26: a faint/washed part of Rani's internal-monologue block leaves one short first-pass reading explicitly uncertain as `⟦நீ?⟧`;
- PDF 74 / printed p.73: a later ownership/address stamp or overprint beginning `K. N. சங்கரன்` covers part of the upper-right printed source text; any source reading hidden by it must remain unresolved unless the scan supports a reading elsewhere;
- PDF 80: stained/damaged back cover with edge wear; no back-matter text was identified there.

## Canonical Tamil first-pass progress

The work already existed when this intake was resumed, so no duplicate work directory was created. At that time, `works/raja-rani/pages/` contained **44 pre-existing draft files (`001.md`–`044.md`)**. Several were summary placeholders or partial transcriptions and could not be treated as canonical completion merely because the files existed.

Those drafts are being reconciled directly against the rendered scan in source order.

Current continuous first-pass coverage is now:

- source PDF **1–30**: reconciled as draft first-pass material;
- front matter / story / song / credits: PDF **1–9**;
- screenplay: PDF **10–30 / printed pp.9–29**;
- screenplay progress: **21/70 pages**;
- embedded `சேரன் செங்குட்டுவன்`: complete in first-pass source order through PDF 19;
- PDF 22→23: the printed letter remains a genuine cross-page written-text structure;
- PDF 25 and later structural ornaments are retained from the scan instead of normalized;
- PDF 27 retains explicit uncertainty where the scan is not yet secure enough for a definitive reading.

All reconciled pages remain **draft**. No page is promoted to `verified` during this first-pass activity.

The pre-existing files PDF **31–44** remain untrusted working drafts until each is reconciled against its rendered source page.

## Current gate

- Source intake: **complete**
- Structural mapping: **complete**
- Whole-source boundary audit: **complete**
- Scene-separator policy: **verified**
- Canonical Tamil first pass: **in progress — PDF 1–30 continuous**
- Screenplay first pass: **PDF 10–30 / printed pp.9–29 — 21/70 pages**
- Verified Tamil pages: **0 claimed**
- Visual fidelity audit: **not started**
- Dialogue / scene / character / translation derivatives: **blocked until verified Tamil**

## Authoritative mapping / progress notes

- `mapping.md`
- `notes/full-source-structure-audit.md`
- `notes/embedded-drama-boundaries.md`
- `notes/scene-heading-inventory.md`
- `notes/transcription-state-reconciliation.md`
- `notes/canonical-first-pass-batch-001.md`
- `notes/canonical-first-pass-batch-002.md`

## Source rules

- The scan is the controlling source.
- OCR is navigation assistance only.
- No silent correction or modernization.
- No invented speakers.
- Song authorship requires item-level evidence.
- First-pass uncertainty remains explicit instead of being repaired from memory or external sources.

## Next activity

Continue **canonical Tamil first-pass transcription from PDF 31 onward**, in source order, with stable page anchors. Reconcile the pre-existing PDF 31–44 drafts against the rendered scan rather than trusting them as complete. After the whole first pass reaches PDF 79, perform a **separate visual fidelity audit** before any structured derivatives.
