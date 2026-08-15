# திரும்பிப்பார்! — post-fidelity source corrections

The canonical page audit remains **104 verified / 0 draft / 0 review**. This ledger records source-supported corrections discovered during later derivative work after a page had already been marked verified.

## PDF 38 / printed p.30 — scene 31 song title

**Discovered during:** per-song authorship gate  
**Date:** 2026-08-15  
**Source authority:** rendered page image from `TVA_BOK_0014652_திரும்பிப்பார்.pdf`

The stored scene-31 direction previously read:

`குமுதா “பாண்டியன் என் செல்வம்” என்ற பாட்டை ...`

Direct reinspection of PDF 38 shows the printed reading:

`குமுதா “பாண்டியன் என் சொல்லை” என்ற பாட்டை ...`

### Correction applied

- `transcription/parts/part-03-pdf-36-63.md` — `செல்வம்` → `சொல்லை`
- `scenes/scene-31.md` — same source-supported correction

No dialogue record, character mapping, scene numbering, pagination or page-status count changes.

The subsequent authorship check found a public soundtrack catalog entry titled `Pandiyan En Sollai`, but that external metadata was **not** used to choose or repair the Tamil. The scan itself establishes `பாண்டியன் என் சொல்லை`; the external source is recorded separately only for item-level authorship in `../songs/tracklist-evidence.json`.
