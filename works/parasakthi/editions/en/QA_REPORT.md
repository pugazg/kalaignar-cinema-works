# Parasakthi English Reader Edition — Whole-work QA

**Status:** PASS  
**English authority:** `works/parasakthi/translations/records/`  
**Source scan SHA-256:** `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`

## Verified checks

- observed canonical scenes: **46/46** (`1–22, 24–33, 35–48`);
- absent canonical scenes: **23, 34** — no phantom reader sections created;
- English units: **769/769 unique, sequential and verified**;
- status counts: **769 verified / 0 review / 0 draft**;
- kind counts: **641 dialogue / 114 stage direction / 13 song / 1 quoted verse**;
- cross-page units: **16**, exactly matching `translations/index.json`;
- immutable dialogue-record links cross-checked: **634**;
- verified song/verse occurrence links cross-checked: **14**;
- distinct source paths existence-checked: **97**;
- direct source-linked labelled dialogue units without invented record IDs: **2**;
- direct source-linked unlabelled dialogue/performance units retained without invented speaker labels: **5**;
- additional indexed direct source-linked non-dialogue units retained: **2**;
- every provenance page lies inside PDF **4–57** / printed **3–56**, with the verified printed-page mapping;
- unit order is non-regressing in source-page order within every scene;
- scene order is non-regressing across the canonical sequence;
- both prose (`english_text`) and semantic-poetic/performance (`english_lines`) translation payloads are preserved according to the verified record rather than coerced by unit kind;
- reader Markdown contains every verified unit exactly once;
- reader HTML contains every verified unit exactly once;
- no `TODO`, `TBD`, `FIXME`, or template-placeholder token appears in reader text.

## Reader-edition policy

The reader export does **not** rewrite translation text. Dialogue displays an exact Tamil source `speaker_label` only when that verified metadata exists; source-unlabelled dialogue/performance remains unlabelled. Semantic-poetic `english_lines` remain line-structured even when the archival unit kind is dialogue. Songs and quoted verse preserve verified English line order. Stage directions remain separate. Source-numbering corrections for canonical scenes **43** and **48** are stated explicitly rather than silently normalized.

## Generated derivatives

- `reader-edition.md` — continuous Markdown reader edition with invisible unit/page provenance comments;
- `reader-edition.html` — standalone responsive/print-friendly HTML reader edition;
- `reader-edition.json` — concatenated machine-readable edition retaining full source-linked unit metadata;
- `manifest.json` — deterministic input/output integrity manifest.

The generator writes only inside `works/parasakthi/editions/en/`; it does not modify canonical Tamil, scene derivatives, dialogue records, character mappings, song inventory, Tamil song derivatives, or transcription files.
