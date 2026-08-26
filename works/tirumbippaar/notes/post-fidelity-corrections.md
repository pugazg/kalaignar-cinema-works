# திரும்பிப்பார்! — post-fidelity source corrections

The earlier canonical page audit had been recorded as **104 verified / 0 draft / 0 review**. On 2026-08-26 the user supplied a corrected full-volume `thirumbipaar.md` and identified a systematic old-Tamil-glyph reading failure in the prior repository transcription. The full-volume text is therefore reopened under `notes/md-reconciliation-audit.md`; the corrected Markdown is the primary correction baseline and the rendered PDF is the final authority for any doubtful conflict.

## PDF 9–13 / printed pp.1–5 — corrected Markdown reconciliation batch 1

**Date:** 2026-08-26  
**Correction witness:** user-supplied `thirumbipaar.md`  
**Final authority for doubt:** rendered `TVA_BOK_0014652_திரும்பிப்பார்.pdf`

This batch confirms that earlier `verified` text had dropped or misread old-print Tamil glyphs and also contained ordinary OCR drift. Representative corrections include:

- `பூமால்` / `பூமால்தான்` → `பூமாலை` / `பூமாலைதான்`;
- `இல்ல.` / `இல்ல இல்ல.` → `இல்லை.` / `இல்லை இல்லை.`;
- `சம்பந்தமே` → `சம்மந்தமே`;
- `ஆதாரமாக` → `ஆதரவாக`;
- `கோயமுத்தார்` → `கோயமுத்தூர்`;
- `சோர்ப்புடன்` → `சோம்பலுடன்`;
- `மனுஷன் தூங்கவிடாமல்` → `மனுஷனை தூங்கவிடாமல்`;
- `பிடிக்கலே` → `பிடிக்கிலே`;
- `தாம்ப் பள்ளிக்கூடத்துக்குப்` → `தர்மப் பள்ளிக்கூடத்துக்குப்`;
- `வழியில்ல` → `வழியில்லை`;
- `லேடிஸ்` → `லேடீஸ்`;
- `படுக்க வராதே தப்பு` → `படுக்க வர்ரதே தப்பு`;
- `தேவைத்தான்` → `தேவைதான்`;
- `முணுமுணுத்தபடி` → `முணுமுணுத்தப்படி`;
- `Nightdress கள்` → `Nightdress களை`;
- scene 4 `நான் எதா` / `எனக்கு நான் நக்ஷத்திரத்திலே` → `நாள் எதா` / `எனக்கு நாள் நக்ஷத்திரத்திலே`;
- `அதுல என்ன` → `அதனால் என்ன`;
- `ஏம்மா...லக்ஷ்மி` → `ஏம்பா...லக்ஷிமி`;
- scene 5 `உள்ளே வாங்க` → `உள்ளே வாருங்க`, `பார்த்தமாதிரி` → `பாத்தமாதிரி`, `வியர்வையாகி` → `வியர்வையாக்கி`, `பாடு பட்டு` → `பாடுபட்டு`, `எழுதிய தென்று` → `எழுதியதென்று`.

The canonical `part-01-pdf-9-13.md` and scene derivatives 1–4 were updated in this batch. Dialogue records for scenes 1, 2 and 4 were reconciled while preserving their stable record IDs. Scene 3's dialogue text required no change; only its stage-direction text changed.

Character/entity and English/publication derivatives are intentionally not declared synchronized yet because the full 104-page correction pass is still in progress.

## PDF 14–35 / printed pp.6–27 — corrected Markdown canonical merge / batch 2

**Date:** 2026-08-26  
**Correction witness:** user-supplied `thirumbipaar.md`  
**Final authority for doubt:** rendered `TVA_BOK_0014652_திரும்பிப்பார்.pdf`

`transcription/parts/part-02-pdf-14-35.md` has now been rebuilt in source order from the user's corrected Markdown baseline. This is a canonical-layer correction pass, not a modernization pass.

The opening PDF 14–18 segment contains a dense cluster of earlier OCR/glyph errors. Representative corrections include:

- `குரு: பக்தா!` → `குரல் : பக்தா!`;
- `தம்பி எண்ணனும்` → `கம்பி எண்ணனும்`;
- `கூடா ஒரு கப் காபி` → `சூடா ஒரு கப் காபி`;
- `மண்டையின் வில்லே` → `மன்மதனின் வில்லே`;
- `இன்பமான ஜோதியை` → `இன்பமான ஜோடியை`;
- `பாட்டுமுடிந்ததும்` → `பாடிமுடிந்ததும்`;
- `பூமால்` → `பூமாலை` throughout the corrected range;
- scene 7 source speaker form `குண்டுமணி` restored from the earlier `குணமணி` reading;
- the corrected Markdown's accidental non-Tamil extraction token `అది` is **not** imported; the source-language form is `அது`.

Scene derivatives 5–10 and their affected dialogue records had already been partially reconciled during the opening Batch-2 work. The canonical Part-02 merge now establishes the corrected text through PDF 35; however, **scene/dialogue derivatives beginning on PDF 19 are still pending synchronization**. This temporary difference is explicitly tracked in `md-reconciliation-audit.md` and must not be mistaken for a closed archival state.

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
