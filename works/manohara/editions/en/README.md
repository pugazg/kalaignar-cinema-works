# மனோகரா — English reader/export layer

This directory holds publication-facing English derivatives and the QA machinery that protects their provenance.

## Current status

**Reader/export preflight: PASS.**

The source-linked English translation remains authoritative for this derivative layer:

- **57/57** archival scene records;
- **1,190/1,190** verified English units;
- **983/983** immutable labelled dialogue records linked exactly once;
- **27** direct source-unlabelled spoken units;
- **17** genuine cross-page units;
- **6/6** source-visible song/performance occurrences linked;
- **0** synthetic scene-end units;
- **0** units derived directly from decorative/structural stars;
- **0** page-order, unit-ID, provenance or scene-metadata errors.

See `PREFLIGHT_QA_REPORT.md` for the completed gate and `audit_probe.py` for the reproducible diagnostic.

No publication-facing `reader-edition.md`, `reader-edition.html` or `reader-edition.json` has been generated yet. Those belong to the next activity and must be derived from the verified translation records without changing canonical Tamil, scene, dialogue, character or song layers.

## Next activity

Generate deterministic publication-facing English reader derivatives in Markdown, standalone HTML and machine-readable JSON; run generated-output QA against all **1,190** verified unit IDs and **983** immutable dialogue links; then write an integrity manifest before Reading Room integration.
