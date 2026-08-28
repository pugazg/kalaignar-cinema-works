# Tirumbippaar English Reader Edition — Whole-work QA

**Status:** PASS  
**English authority:** `works/tirumbippaar/translations/records/`  
**Source scan SHA-256:** `973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682`

## Verified checks

- canonical scenes: **93/93** in corrected source order;
- English units: **1,330/1,330 unique and verified**;
- status counts: **1,330 verified / 0 review / 0 draft**;
- kind counts: **1,049 dialogue / 262 stage direction / 7 song-reference / 2 chant / 10 written-text / 0 full-song**;
- immutable labelled dialogue records linked exactly once: **1042/1,042**;
- source-visible unlabelled spoken units retained without invented speaker/dialogue IDs: **7**;
- verified song/performance occurrence links cross-checked: **7**;
- cross-page English units: **12**, exactly matching `translations/index.json`;
- all provenance lies inside PDF **9–112** / printed **1–104**, with `printed = PDF - 8`;
- stable historical English unit IDs are preserved even when recovered units make numeric IDs non-sequential in source order;
- source-only structural stars do not survive as synthetic `(Scene ends.)` units;
- reader Markdown and HTML contain every verified English unit exactly once;
- no editorial placeholder token appears in reader text.

## Source-sensitive structures retained

Scene 41 retains its recovered dialogue links; scene 63 retains the stable split required by the immutable dialogue corpus; scene 80 retains its genuine cross-page units; scene 92 begins with its newspaper heading and Court setting before the judgment; scene 93 begins with its Jail setting and retains the final children/warders departure, `Vanakkam.`, and no synthetic star-end prose.

The generator writes only inside `works/tirumbippaar/editions/en/` and does not modify canonical Tamil or structured source layers.
