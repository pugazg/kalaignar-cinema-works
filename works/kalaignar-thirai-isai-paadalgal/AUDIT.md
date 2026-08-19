# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Scope

This audit covers the complete PDF-specific song-presence scan, line-level Tamil lyric verification for all **54 numbered songs**, and the entire source-linked English translation corpus from pilot `001–003` through final batch `047–054`.

The rendered scan controls Tamil. Verified Tamil song files control the English derivative. No external recording, lyric website, subtitle, alternate edition, campaign text, commentary, or soundtrack-memory reconstruction is used to repair either layer.

## Full-PDF page classification

**PASS — 194/194 pages scanned.**

- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs located: **54/54**;
- final song-bearing page: **130**.

Authoritative ledger: `notes/FULL_PDF_SONG_PAGE_SCAN.md`  
Machine map: `songs/page-map.json`

## Final Tamil lyric fidelity status

- draft: **0**;
- verified: **54** (`001–054`);
- review: **0**;
- not started: **0**;
- unresolved Tamil song readings: **0**.

The Tamil song corpus is **complete-verified** and immutable translation input.

## Cross-page source records

The following songs span more than one song-bearing page and remain one record each in both Tamil and English where translated:

- `009` — PDF 38–39;
- `019` — PDF 53–54;
- `023` — PDF 58–59;
- `024` — PDF 62–63;
- `036` — PDF 86–87;
- `037` — PDF 90–91;
- `051` — PDF 121–122;
- `052` — PDF 123–124.

## English translation authority

- guide: `docs/SONG_TRANSLATION_GUIDE.md`;
- schema: `translations/schema.json`;
- index: `translations/index.json`;
- pilot review: `translations/PILOT_REVIEW.md`;
- scaled reviews: `translations/BATCH_004_011_REVIEW.md`, `translations/BATCH_012_018_REVIEW.md`, `translations/BATCH_019_025_REVIEW.md`, `translations/BATCH_026_032_REVIEW.md`, `translations/BATCH_033_039_REVIEW.md`, `translations/BATCH_040_046_REVIEW.md`, `translations/BATCH_047_054_REVIEW.md`.

The approved mode is **`semantic-poetic-source-faithful`**. English retains Kalaignar's language, rhetoric, repetition, political/social force, concrete imagery, colloquial energy, culture-bearing vocabulary and source-specific constructions. It is not a singable adaptation.

## Translation gates

- pilot `001–003`: **3/3 PASS — pilot-verified**;
- `004–011`: **8/8 PASS**;
- `012–018`: **7/7 PASS**;
- `019–025`: **7/7 PASS**;
- `026–032`: **7/7 PASS**;
- `033–039`: **7/7 PASS**;
- `040–046`: **7/7 PASS**;
- `047–054`: **8/8 PASS**.

## Final batch fidelity highlights — `047–054`

- `047`: **sons of the soil**, eye/eyelid duty imagery, repeated courage/wisdom lines, **hand for kinship / voice for rights**, and `naam / naan` lip-position wordplay remain source-shaped; `பிரிவாது` is documented rather than normalized.
- `048`: `kalaignan`, `udanpirappe`, direct caste/religion division and sledgehammer rhetoric, Valluvar and source-pressure `inba-pagai` remain explicit.
- `049`: mother-warrior pride/grief, sculpted-beauty casket, young-deer bride, tusker/steed violence, battlefield fame and womb-bearing motherhood remain unsoftened.
- `050`: `mullai`, Tamil `mandram`, `bhava`, `jathi`, `veena`, `Nasika Poosani`, jathi vocables, source-pressure `nyaayirene` and the abrupt final line remain visible.
- `051`: PDF **121–122** remains one record; the `machaan` duet preserves sexual/comic food imagery, `aandi`, `thaali`, `saivam / asaivam`, anti-subordination language and verified pressure-point phrases without outside repair.
- `052`: PDF **123–124** remains one record; affection-parrot, `kurinji`, repeated chorus responses, Kannagi, Classical Tamil, red jasmine, sibling/mother imagery and eyes becoming ponds remain intact.
- `053`: the printed clipped short-line architecture, `bhava`, Pearl-Tamil and Chola praise remain segmented rather than reconstructed into prose.
- `054`: musical/place vocabulary, `Kodumudi kokilam`, honey/milk and `aanpaal` wordplay, `paayiram`, and the classical **water upon red earth** image remain culturally and literarily audible.

Detailed review: `translations/BATCH_047_054_REVIEW.md`.

## Final gate result

- Tamil transcription: **complete-verified — 54/54**;
- Tamil fidelity audit: **complete**;
- English translation: **complete-verified — 54/54**;
- English pilot-verified: **3** (`001–003`);
- English verified: **51** (`004–054`);
- English draft/review/not-started: **0/0/0**;
- reader/export: **not started**.

**PASS — both the Tamil song corpus and the source-linked English translation corpus are complete-verified.**

## Next activity

Run a whole-corpus English **reader/export preflight** across all 54 translation records. Preserve anthology order, Tamil/source links, page provenance, `anthology-attributed` status, and the distinction between `pilot-verified` and `verified`. Do not alter the complete-verified Tamil or English source-linked layers merely for publication smoothness.
