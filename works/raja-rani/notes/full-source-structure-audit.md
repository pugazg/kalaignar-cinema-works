# ராஜா ராணி — Full Source Structure Audit

## Source

- filename: `TVA_BOK_0017188_ராஜா_ராணி.pdf`
- source/archive identifier: `TVA_BOK_0017188` — from the archive filename, not observed as a printed identifier
- PDF pages: **80**
- byte size: **31,600,388**
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`
- PDF form: scanned publication with an embedded OCR text layer

The rendered scan remains the controlling source. OCR is used only for navigation and cannot control punctuation, ornamentation, page numbers, speaker labels, spelling, scene boundaries or obscured readings.

## Verified source identity

- title leaf: **`ராஜா ராணி`**
- cover title form: **`ராஜாராணி`**
- cover directly prints: **`மு. கருணாநிதி`**
- the cover does not print a role label beside the name
- PDF 2 visible imprint: **`மலர் மன்றம்` / `விருதுநகர்,`**
- PDF 2 visible price: **`விலை அணா 0-8-0`**
- explicit edition statement: **none identified**
- explicit publication year: **none identified**
- PDF 79 final printer line: **`அன்பு அச்சகம், மதுரை:-- 56`**; `56` is retained as printed and is not interpreted as a year without source evidence

## Verified whole-source structure

| PDF page(s) | Source function | Archival treatment |
|---|---|---|
| 1 | Front cover | Paratext; preserve separately from canonical screenplay text |
| 2 | Book/title/publication details | Paratext / publication metadata |
| 3 | `கதைச் சுருக்கம்` | Narrative summary; do **not** convert into screenplay scenes |
| 4–9 (first part of p.9) | Film songs / performance text | Source-position song layer; **11 numbered `பாட்டு` blocks (1–11)**; authorship handled separately |
| 9 (second part) | Cast / performers / song-credit roster | Credits / metadata; not screenplay dialogue |
| 10–79 | Main screenplay/dialogue | Canonical Tamil screenplay transcription range |
| 80 | Back cover | Back-cover paratext; outside canonical screenplay |

## Printed pagination

- PDF 10 visibly carries printed page **9**.
- PDF 79 visibly carries printed page **78**.
- The screenplay maps **PDF 10–79 → printed pp.9–78**, with `printed = PDF - 1` throughout that range.
- Within the song section, PDF 5 visibly carries printed p.4 and subsequent numbered pages continue consistently.
- The opening song page (PDF 4) does not show a visible printed page number in the rendered scan, so no printed-page value is invented for it.
- Front cover, publication/title pages and back cover are unnumbered paratext for archival purposes.

## Song / performance credit gate

PDF 9 prints this film-wide `பாடல்கள்:` roster:

- `மு. கருணாநிதி`
- `ஏ. மருதகாசி`
- `கே. பி. காமாக்ஷி`
- `எம். கே. ஆத்மநாதன்`
- `வில்லிபுத்தன்`
- `விவேகன்`

The source supports the existence of this roster, but **does not by itself map each of the 11 numbered song blocks to one lyricist**. Item-level authorship remains unresolved at intake.

## Embedded dramatic/performance sections inside the screenplay

These remain inside `ராஜா ராணி` source order and are not separate repository works.

| Embedded section | Verified PDF range | Printed range / note |
|---|---:|---|
| `சேரன் செங்குட்டுவன்` | **13–19** | printed pp.12–18; PDF 20 returns to film-level post-performance context |
| `அகல்யா நாடக ஒத்திகை` | **40–first part of 41** | printed pp.39–40; main film dialogue resumes within PDF 41 |
| `சாக்ரடீஸ் (நாடகம்)` | **66–72** | printed pp.65–71; PDF 73 returns to film-level action |

## Scene / section numbering finding

No source-numbered screenplay scene sequence is printed. The work instead uses headings, dramatic transitions and recurring decorative star separators.

Consequently:

- no source scene count is claimed at intake;
- scene-number gaps, repeats and out-of-order numbers are not applicable;
- later archival scene segmentation must remain a derivative built only after verified Tamil.

## Scene-separator verification

### Finding

The recurring star-divider family is source-supported, but its typography is not uniform throughout the book.

Direct rendered-scan inspection shows multiple forms:

1. **PDF 10 / printed p.9** — after the opening hospital sequence, a centered row of **four star ornaments** appears before the next dramatic block.
2. **PDF 25 / printed p.24** — a clear centered **rule–star–rule** ornament (`—★—`) separates blocks.
3. Later screenplay pages include the same separator family; OCR variably corrupts the ornaments.
4. **PDF 79 / printed p.78** — a location/scene heading appears as **`★ தோட்டம் ★`**, and a final centered rule–star–rule ornament closes the text.
5. Embedded drama subsections can use decorated headings rather than one universal separator form.

### Archival rule

- Treat a source-visible centered star ornament / star-divider between dramatic blocks as strong scene-boundary evidence.
- Treat star-flanked location or dramatic headings as heading evidence, not as ordinary dialogue.
- Do **not** normalize every ornament to the literal string `—★—` in canonical Tamil; preserve the exact printed ornament seen on each page.
- Do **not** use OCR output to decide the ornament form.
- Do not create a new scene merely because a PDF page changes.
- During later scene-derivative construction, reconcile the ornament with the surrounding stage direction / heading / action.

## Scan-condition audit

Whole-scan inspection did **not** identify a missing or duplicated complete PDF page in this intake pass.

Documented source-condition issues:

- **PDF 1:** cover wear and a later pencil/handwritten numeric annotation below the printed `மு. கருணாநிதி`. The later mark is not source text.
- **PDF 74 / printed p.73:** a later ownership/address stamp or overprint beginning **`K. N. சங்கரன்`** obscures part of the upper-right printed source text. The obscured reading must not be reconstructed from film audio, memory, OCR or later editions.
- **PDF 80:** unnumbered back cover with staining, edge wear and physical damage; no back-matter/catalogue/advertisement text is identified on the page.
- General wear, contrast variation and edge damage occur across the physical scan and must remain source-condition evidence rather than be silently repaired in transcription.

## Existing repository-state reconciliation

The `raja-rani` work predates this completed intake checkpoint. `works/raja-rani/pages/` already contains **44 draft files (`001.md`–`044.md`)**.

Those files are not accepted as a complete canonical first pass:

- the batch is draft/unverified;
- page metadata and status formatting are inconsistent;
- `pages/012.md` contains an explicit continuation placeholder rather than a full page transcription;
- no full visual fidelity audit has verified the batch.

The drafts are therefore retained as working material only. The next canonical pass must revisit the rendered scan in source order and reconcile these files before treating any page as complete.

## Mapping disposition

The whole-source structural boundary gate is now **complete**:

- source identity: verified to the extent visibly printed
- front matter boundary: verified
- story-summary boundary: verified
- song section boundary: verified
- song block count: 11
- cast/credits boundary: verified
- screenplay start: PDF 10 / printed p.9
- screenplay end: PDF 79 / printed p.78
- back cover: PDF 80
- embedded drama boundaries: verified
- scene-separator policy: verified from rendered scan
- missing/duplicate full-page check: no issue identified in intake overview
- source-condition exception at PDF 74: documented

## Current gate

- Source intake: **complete**
- Structural mapping: **complete**
- Existing draft page files: **001–044, incomplete/unverified**
- Canonical Tamil first pass: **not complete**
- Verified Tamil pages: **0 claimed at this checkpoint**
- Visual fidelity audit: **not started**
- Structured derivatives: **blocked**

## Next activity

**Canonical Tamil first-pass transcription from the rendered scan, in source order, with stable page anchors — followed later by a separate visual fidelity audit before any structured derivatives.**
