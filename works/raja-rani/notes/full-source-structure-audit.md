# ராஜா ராணி — Full Source Structure Audit

## Source

- filename: `TVA_BOK_0017188_ராஜா_ராணி.pdf`
- PDF pages: **80**
- byte size: **31,600,388**
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`

The rendered scan remains the controlling source. OCR is used only for navigation and cannot control punctuation, ornamentation, page numbers, speaker labels, or scene boundaries.

## Verified whole-source structure

| PDF page(s) | Source function | Archival treatment |
|---|---|---|
| 1 | Front cover | Paratext; preserve separately from canonical screenplay text |
| 2 | Book/title/publication details | Paratext / publication metadata |
| 3 | `கதைச் சுருக்கம்` | Narrative summary; do **not** convert into screenplay scenes |
| 4–9 (first part of p.9) | Film songs / performance text | Source-position song layer; authorship handled separately |
| 9 (second part) | Cast / performers / song-credit roster | Credits / metadata; not screenplay dialogue |
| 10–79 | Main screenplay/dialogue | Canonical Tamil screenplay transcription range |
| 80 | Back cover | Back-cover paratext; outside canonical screenplay |

## Printed pagination

- PDF 10 visibly carries printed page **9**.
- PDF 79 visibly carries printed page **78**.
- The screenplay therefore maps **PDF 10–79 → printed pp.9–78**.
- Within the song section, PDF 5 visibly carries printed p.4 and subsequent pages continue consistently; the opening song page (PDF 4) does not show a visible printed page number in the rendered scan, so no printed-page value should be invented for that page in canonical anchors.
- Front cover, publication/title pages and back cover are unnumbered paratext for archival purposes.

## Embedded dramatic/performance sections inside the screenplay

These remain inside `ராஜா ராணி` source order and are not separate repository works.

| Embedded section | Verified PDF range | Printed range / note |
|---|---:|---|
| `சேரன் செங்குட்டுவன்` | **13–19** | printed pp.12–18; PDF 20 returns to film-level post-performance context |
| `அகல்யா நாடக ஒத்திகை` | **40–first part of 41** | printed pp.39–40; main film dialogue resumes within PDF 41 |
| `சாக்ரடீஸ் (நாடகம்)` | **66–72** | printed pp.65–71; PDF 73 returns to film-level action |

## Scene-separator verification

### Finding

The user's proposed `——★——` separator is **substantially correct as the source's recurring scene-boundary ornament, but the typography is not uniform throughout the book**.

Direct rendered-scan inspection shows multiple source-visible forms:

1. **PDF 10 / printed p.9** — after the opening hospital sequence, the source uses a centered row of **four star ornaments** before the next dramatic block.
2. **PDF 25 / printed p.24** — the source uses a clear centered **rule–star–rule** ornament (`—★—`) before the next dramatic block.
3. Later screenplay pages include the same star-divider family; OCR variably corrupts these as `——`, `—*—`, `———-—`, `%`, letters, or other garbage.
4. **PDF 79 / printed p.78** — a location/scene heading appears as **`★ தோட்டம் ★`**, and the page also ends with a centered rule–star–rule ornament.
5. Embedded drama subsections can have decorated headings such as court/prison/location headings rather than relying only on one exact separator glyph arrangement.

### Archival rule

Therefore:

- Treat a **source-visible centered star ornament / star-divider between dramatic blocks** as strong scene-boundary evidence.
- Treat **star-flanked location or dramatic headings** as heading evidence, not as ordinary dialogue.
- Do **not** normalize every ornament to the literal string `—★—` in canonical Tamil; preserve the exact printed ornament seen on each page.
- Do **not** use OCR output to decide the ornament form.
- Do not create a new scene merely because a PDF page changes.
- During scene-derivative construction, reconcile the ornament with the surrounding stage direction / heading / action so that decorative stars used as headings are not mistaken for standalone scenes.

## Mapping disposition

The whole-source structural boundary gate is now **complete**:

- front matter boundary: verified
- story-summary boundary: verified
- song section boundary: verified
- cast/credits boundary: verified
- screenplay start: PDF 10 / printed p.9
- screenplay end: PDF 79 / printed p.78
- back cover: PDF 80
- embedded drama boundaries: verified
- scene-separator policy: verified from rendered scan

## Next gate

Begin canonical Tamil first-pass transcription in **source order**, using PDF 10–79 as the screenplay range and preserving all source-visible star ornaments, headings, stage directions, songs, speaker labels and embedded dramatic material exactly where they occur.

Structured scene/dialogue/character derivatives remain blocked until the corresponding Tamil is visually verified.
