# ராஜா ராணி — Structural Mapping

## Source

`TVA_BOK_0017188_ராஜா_ராணி.pdf`

- PDF pages: **80**
- byte size: **31,600,388**
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`

## Source classification

**Full dialogue/screenplay publication with songs**

This is processed using the Parasakthi / Manohara workflow, not the limited story-and-song booklet workflow used for sources such as Manthiri Kumari.

## Verified whole-source boundaries

| PDF page(s) | Section | Status / treatment |
|---|---|---|
| 1 | Front cover | verified paratext |
| 2 | Book/title/publication details | verified paratext / metadata |
| 3 | `கதைச் சுருக்கம்` | verified narrative summary; do not convert into scenes |
| 4–9 (first part of p.9) | Film songs / performance text | verified source-position song section |
| 9 (second part) | Cast / performers / song-credit roster | verified credits / metadata |
| 10–79 | Main dialogue/screenplay | verified canonical screenplay range |
| 80 | Back cover | verified back-cover paratext |

## Printed pagination

- PDF 10 = printed p.9.
- PDF 79 = printed p.78.
- Canonical screenplay range: **PDF 10–79 / printed pp.9–78**.
- PDF 4 is the opening song page and does not show a visible printed page number in the rendered scan; do not invent one in canonical page anchors.

## Verified embedded dramatic sections

| Section | Boundary | Notes |
|---|---|---|
| `சேரன் செங்குட்டுவன்` | PDF **13–19**, printed pp. **12–18** | PDF 20 returns to film-level post-performance context |
| `அகல்யா நாடக ஒத்திகை` | PDF **40–first part of 41**, printed pp. **39–40** | rehearsal ends within PDF 41; film dialogue resumes on same page |
| `சாக்ரடீஸ் (நாடகம்)` | PDF **66–72**, printed pp. **65–71** | PDF 73 returns to film-level action |

See:

- `notes/embedded-drama-boundaries.md`
- `notes/full-source-structure-audit.md`

## Scene-separator finding

The screenplay uses **source-visible star ornamentation as recurring scene-boundary evidence**, but not in one completely uniform typography.

Verified examples include:

- PDF 10: a centered row of four stars between dramatic blocks;
- PDF 25: a centered rule–star–rule ornament (`—★—`); 
- later pages: the same divider family, often corrupted by OCR;
- PDF 79: star-flanked location heading `★ தோட்டம் ★` and a final rule–star–rule ornament.

Therefore:

- use the rendered scan, not OCR, to identify separators;
- preserve the exact printed ornament in canonical Tamil;
- do not normalize every separator to a single literal form;
- page breaks alone are not scene boundaries;
- star-flanked headings are heading evidence and must be distinguished from standalone divider ornaments.

## Scene/dialogue preparation rules

- Do not create scenes from the story summary.
- Scene boundaries must come from printed source structure and verified dramatic transitions.
- Preserve printed speaker labels exactly.
- Preserve stage directions and parentheticals.
- Do not invent speakers for unlabelled speech.
- Cross-page utterances remain single dialogue records.
- Embedded dramas remain inside `ராஜா ராணி` source order; they are not separate works.

## Song handling rules

- Keep songs as source structures until attribution and witness comparison gates are complete.
- Printed film-wide song-credit lists do not automatically assign every song without item-level mapping.
- Existing Kalaignar song corpus must be checked before creating duplicate song records.

## Gate status

- Source intake: **complete**
- Structural mapping: **complete**
- Whole-source boundary audit: **complete**
- Embedded dramatic-section boundary audit: **complete**
- Scene-separator policy: **verified**
- Canonical Tamil transcription: **not started**
- Visual fidelity audit: **not started**
- Structured derivatives: **blocked**

## Next activity

Begin canonical Tamil first-pass transcription in source order for **PDF 10–79 / printed pp.9–78**, preserving all source-visible stage directions, exact speaker labels, star ornaments, songs/performance blocks and embedded dramatic material.
