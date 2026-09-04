# மந்திரி குமாரி — English translation layer

Source: `TVA_BOK_0026144_மந்திரி_குமாரி.pdf`  
Target language: English  
Status: **complete-verified**

This layer translates only the **verified source-linked Tamil derivatives** of the Manthiri Kumari story-and-song booklet. It does not convert the booklet into a screenplay, infer absent lyric authorship, import external lyrics, or repair canonical Tamil through English interpretation.

## Source structure translated

### Story summary

Source: verified continuous PDF **3–5** `கதைச்சுருக்கம்` derivative.

- translation record: `story-summary.json`;
- schema: `story-summary.schema.json`;
- source-linked logical prose units: **13**;
- cross-page prose units: **1** — the paragraph that crosses PDF 3→4;
- synthetic screenplay scene IDs: **0**;
- immutable dialogue IDs manufactured from synopsis speech: **0**;
- mode: **`semantic-source-faithful-prose`**.

### Songs / performances

Source: the **15/15 complete-verified** PDF **6–13** performance records.

- translation records: `performances/001.json` through `performances/015.json`;
- schema: `performance.schema.json`;
- performance records translated: **15/15**;
- translation sections: **52**;
- Tamil source lines/cues mapped: **234**;
- English lines/cues mapped: **234**;
- line-count mapping mismatches: **0**;
- cross-page performance records: **7** — blocks `002`, `004`, `006`, `007`, `009`, `011`, `013`;
- mode: **`semantic-poetic-source-faithful`**.

The English layer preserves source-visible `தொகையறா` / `பாட்டு` subdivisions, `(வசனம்)` and other performance/refrain cues such as `(வாழ்)`, `(இசை)`, `(பெண்)`, `(கண்)`, `(என்)`, `(மனம்)` and `(பெற)` where present. Exact Tamil source/turn labels remain metadata; English display labels do not replace them.

## Authorship and cross-witness boundary

Translation does not change evidence status.

- booklet item-level lyric authorship verified: **0/15**;
- item-level lyric authorship unresolved: **15/15**;
- confirmed current-anthology witness: **1/15**, block 11 `மாட்டுக்கார பையன்` ↔ `kalaignar-song-001`;
- source-only relative to the current anthology corpus: **14/15**;
- authorship upgrades caused by translation: **0**.

For block 11, the later anthology translation is only a comparison/style precedent. The corrected booklet witness controls this translation and is not repaired from the anthology.

## Preserved source irregularities

Translation notes explicitly retain or document difficult source forms instead of silently correcting them. Important examples include:

- story-summary irregular forms and punctuation such as `வெள்ளத்திலகப்பட்ட`, `சாகசம் பேசி`, and `தேடி.`;
- performance 5's anomalously positioned `[போடுதே.]`;
- performance 6's unusual comic forms such as `இருச்சவாய்` and `பாலைவனைத்`;
- performance 13's **printed heading `பார்த்திபன்—மந்திரிகுமாரி` while its source turn labels are `பார்த்திபன்` / `அமுதவல்லி`** — both are preserved without normalization.

## QA

Whole-layer QA: **PASS**.

See `FINAL_TRANSLATION_QA.md` and `index.json`.

- missing translation records: **0**;
- duplicate translation IDs: **0**;
- performance line/cue mapping mismatches: **0**;
- canonical Tamil changed by translation: **no**;
- synthetic screenplay scene IDs created: **0**;
- external/unprinted lyric lines imported: **0**.

## Exact next activity

> **Build and QA a deterministic bilingual reader/export layer from the complete-verified story-summary and 15 performance translations. Preserve the booklet's natural `கதைச்சுருக்கம்` + performance navigation, Tamil/English source pairing, page provenance, source-visible cues and unresolved lyric-authorship state. Do not invent screenplay scenes.**
