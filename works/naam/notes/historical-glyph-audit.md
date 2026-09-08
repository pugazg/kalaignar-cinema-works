# நாம் — Historical Tamil Glyph Audit

Status: **final-verification-in-progress**  
Canonical source range: **PDF 5–71 — 67 pages**  
Binding guide: `../../../docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`

## Purpose

The `நாம்` source uses older Tamil print and an image-only scan. Historical character identity must therefore be decoded from the rendered source pixels rather than from modern visual resemblance, OCR, semantic expectation or a later spelling.

This audit begins with canonical transcription and remains a separate gate from ordinary visual-fidelity review.

## Mandatory families

Every canonical page must explicitly consider at least:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

The set is a minimum. Other worn, faint, broken or edition-specific ligatures remain in scope.

## Page-level method

For each PDF page 5–71:

1. inspect the complete page at enlarged/native resolution;
2. decode the full glyph cluster, not an isolated loop or vowel mark;
3. compare clearer same-edition examples when needed;
4. use grammar/lexical expectation only to locate a doubtful form, never as proof;
5. encode the positively supported historical character identity in normal Unicode;
6. preserve every other source feature — spelling, grammar, vocabulary, spacing and punctuation;
7. record consequential corrections explicitly;
8. never global-replace a glyph family;
9. leave unresolved forms `needs-review` rather than guessing.

OCR is a discovery/navigation aid only and has no authority for historical glyph identity.

## Verification model

A page can complete its historical-glyph first-pass inspection without becoming globally verified. Final canonical verification requires both:

- complete visual-fidelity comparison against the rendered page; and
- historical-glyph audit PASS for that page.

Until both gates are complete, no structured scene/dialogue/character/song derivative may treat the page as verified authority.

## Coverage

| Range | Pages expected | Glyph first-pass checked | Dual-gate verified | Needs review | Status |
|---|---:|---:|---:|---:|---|
| PDF 5–9 | 5 | 5 | 4 | 1 | final-audit: 4 verified / PDF5 hold |
| PDF 10–14 | 5 | 5 | 4 | 1 | final-audit: 4 verified / PDF10 hold |
| PDF 15–19 | 5 | 5 | 5 | 0 | final-audit: 5 verified |
| PDF 20–24 | 5 | 5 | 4 | 1 | final-audit: 4 verified / PDF24 hold |
| PDF 25–29 | 5 | 5 | 5 | 0 | final-audit: 5 verified |
| PDF 30–34 | 5 | 5 | 5 | 0 | final-audit: 5 verified |
| PDF 35–39 | 5 | 5 | 5 | 0 | final-audit: 5 verified |
| PDF 40–44 | 5 | 5 | 5 | 0 | final-audit: 5 verified |
| PDF 45–49 | 5 | 5 | 5 | 0 | final-audit: 5 verified |
| PDF 50–54 | 5 | 5 | 0 | 5 | partial-first-pass |
| PDF 55–59 | 5 | 5 | 0 | 5 | partial-first-pass |
| PDF 60–64 | 5 | 5 | 0 | 5 | partial-first-pass |
| PDF 65–69 | 5 | 5 | 0 | 5 | partial-first-pass |
| PDF 70–71 | 2 | 2 | 0 | 2 | first-pass-complete |
| **Total** | **67** | **67** | **42** | **25** | **final-verification-in-progress** |

## First-pass findings / correction log

| PDF | Printed page | Earlier/apparent reading | Source-supported Unicode reading | Historical family | Evidence | Status |
|---:|:---:|---|---|---|---|---|
| 6 | 6 | apparent bare-`ள்` surface in `அவள்...` cluster | `அவளை` | `ளை` | enlarged source cluster + same-word syntax; old `ளை` identity | **final-verified** |
| 6 | 6 | old `னா` form in `சூரியனால்` | `சூரியனால்` | `னா` | enlarged source pixels; family explicitly checked before Unicode encoding | **final-verified** |
| 11 | 11 | old-form cluster in `கண்ணாடிச்` | `கண்ணாடிச்` | `ணா` | enlarged source pixels; positive family occurrence | **final-verified** |
| 15 | 15 | historical `றா` cluster | `வாறேன்` | `றா` | enlarged source pixels; occurrence-specific final review | **final-verified** |
| 16 | 16 | historical `னை` clusters | `காடனை` / `வேடனை` | `னை` | enlarged source pixels; occurrence-specific final review | **final-verified** |
| 18 | 18 | historical `னை` cluster | `தன்னை` | `னை` | enlarged source pixels; occurrence-specific final review | **final-verified** |
| 21 | 21 | modern-lookalike `நீதானு...?` | `நீதானா...?` | `னா` | enlarged source pixels + binding guide's same-family precedent (`மட்டுந்தானு?` → `மட்டுந்தானா?`) | **final-verified** |
| 25 | 25 | historical `ளை` cluster in `உங்களை` | `உங்களை` | `ளை` | enlarged source pixels; direct final review | **final-verified** |
| 26 | 26 | old-form `லை` cluster in `அலைந்தான்` | `அலைந்தான்` | `லை` | enlarged source pixels + same-edition family comparison | **final-verified** |
| 27 | 27 | historical `ணை` cluster | `சாணைக்கல்லிலே` / `சாணைக்கல்லை` | `ணை` | enlarged source pixels; both same-page occurrences checked | **final-verified** |
| 28 | 28 | historical `லை` / `னா` shapes in phrase | `காதலை நான்` | `லை` / `னா` | enlarged source pixels + same-edition family comparison | **final-verified** |
| 29 | 29 | historical `ணா` cluster in payment wording | `அணா` | `ணா` | enlarged source pixels; repeated source occurrence | **final-verified** |
| 31 | 31 | historical `றா` cluster | `தவறான` | `றா` | enlarged source pixels | **final-verified** |
| 31 | 31 | historical `னை` cluster | `இவனை` | `னை` | enlarged source pixels | **final-verified** |
| 32 | 32 | historical `னை` clusters | `அவனை` / `ஜமீனையே` | `னை` | enlarged source pixels | **final-verified** |
| 34 | 34 | historical `ளை` cluster | `அவளை` | `ளை` | enlarged source pixels | **final-verified** |
| 34 | 34 | historical `ணை` cluster | `பஞ்சணை` | `ணை` | enlarged source pixels | **final-verified** |
| 35 | 35 | historical `னா` cluster | `நானம்மா` | `னா` | enlarged source pixels | **final-verified** |
| 37 | 37 | historical `னை` cluster | `உன்னை` | `னை` | enlarged source pixels | **final-verified** |
| 39 | 39 | historical `னோ` cluster | `எமனோடு` | `னோ` | enlarged source pixels + same-edition family comparison | **final-verified** |
| 40 | 40 | historical `னை` cluster | `உன்னை` | `னை` | enlarged source pixels | **final-verified** |
| 42 | 42 | historical `ணை` cluster | `மண்ணைவாரிப்` | `ணை` | enlarged source pixels | **final-verified** |
| 43 | 43 | historical `னை` cluster | `குமரனை` | `னை` | enlarged source pixels | **final-verified** |
| 44 | 44 | historical `னை` cluster | `உன்னை` | `னை` | enlarged source pixels; occurrence-specific final review | **final-verified** |
| 45 | 45 | historical `றா` cluster | `கொன்றாய்` | `றா` | enlarged source pixels | **final-verified** |
| 48 | 48 | historical `னை` cluster | `என்னை` | `னை` | enlarged source pixels | **final-verified** |
| 49 | 49 | historical `ணா` cluster | `மணாளன்` | `ணா` | enlarged source pixels | **final-verified** |
| 49 | 49 | historical `னோ` cluster | `கேளேனோ` | `னோ` | enlarged source pixels + same-edition PDF 39 comparison | draft-supported |
| 51 | 51 | historical `னை` cluster | `என்னை` | `னை` | enlarged source pixels | draft-supported |
| 52 | 52 | historical `லை` place-name | `மலையங்களா` | `லை` | enlarged source pixels | draft-supported |
| 52 | 52 | historical `லை` name ending | `அண்ணுமலை` | `லை` | enlarged source pixels | draft-supported |
| 53 | 53 | historical `லை` name ending | `அண்ணுமலை` | `லை` | enlarged source pixels | draft-supported |
| 54 | 54 | historical `லை` place-name | `மலையங்களா` | `லை` | enlarged source pixels | draft-supported |

| 55 | 55 | historical `லை` cluster | `உயிலை` | `லை` | enlarged source pixels | draft-supported |
| 57 | 57 | historical `லை` name ending | `அண்ணுமலை` | `லை` | enlarged source pixels | draft-supported |
| 59 | 59 | historical `றா` cluster | `தவறாமல்` | `றா` | enlarged source pixels | draft-supported |
| 59 | 59 | historical `னை` cluster | `முனையிலே` | `னை` | enlarged source pixels | draft-supported |
| 59 | 59 | historical `ணா` cluster | `அண்ணா` | `ணா` | enlarged source pixels + same-edition comparison | draft-supported |
| 60 | 60 | historical `ணா` cluster | `அண்ணா` | `ணா` | enlarged source pixels | draft-supported |
| 61 | 61 | historical `லை` name ending | `அண்ணுமலை` | `லை` | enlarged source pixels | draft-supported |
| 62 | 62 | historical `லை` name ending | `அண்ணுமலை` | `லை` | enlarged source pixels | draft-supported |
| 62 | 62 | historical `னை` cluster | `ஜமீனை` | `னை` | enlarged source pixels | draft-supported |
| 64 | 64 | historical `னா` cluster | `வாடினான்` | `னா` | enlarged source pixels | draft-supported |

| 65 | 65 | historical `னா` clusters | `மனிதனாகுகிறதும்` / `மனிதனாகுவதும்` | `னா` | enlarged source pixels | draft-supported |
| 65 | 65 | historical `லை` name ending | `அண்ணுமலை` | `லை` | enlarged source pixels | draft-supported |
| 66 | 66 | historical `ணா` cluster | `காலணா` | `ணா` | enlarged source pixels | draft-supported |
| 66 | 66 | historical `லை` cluster | `காலை` | `லை` | enlarged source pixels | draft-supported |
| 67 | 67 | historical `னை` cluster | `மனைவி` | `னை` | enlarged source pixels | draft-supported |
| 68 | 68 | historical `லை` cluster | `உயிலை` | `லை` | enlarged source pixels | draft-supported |
| 69 | 69 | historical `னை` cluster | `உன்னை` | `னை` | enlarged source pixels | draft-supported |

| 70 | 70 | historical `லை` clusters | `சிறைச்சாலை` / `மலையப்பன்` | `லை` | enlarged source pixels | draft-supported |
| 70 | 70 | historical `னா` cluster | `குமரனால்` | `னா` | enlarged source pixels | draft-supported |
| 70 | 70 | historical `னை` cluster | `என்னை` | `னை` | enlarged source pixels | draft-supported |
| 70 | 70 | historical `றா` cluster | `வருகிறாள்` | `றா` | enlarged source pixels | draft-supported |
| 71 | 71 | historical `ளை` cluster | `உங்களை` | `ளை` | enlarged source pixels | draft-supported |

These findings decode character identity only. They do not authorize spelling modernization elsewhere.

## PDF 15–19 scan-backed textual reconciliation

Direct enlarged-pixel comparison corrected five local first-pass readings:

- PDF 15 `எல்லோருக்கும்` — not `எல்லோருக்குமே`;
- PDF 15 `உருண்டோடிடுமே` — the printed `மே` is retained;
- PDF 17 `அவன் கை வலி` — not `அவனே கை வலி`;
- PDF 19 `என்னே` — not `என்ன`;
- PDF 19 `என் மருமகளும்` — not `என் மருமகனும்`.

These are local source-fidelity corrections, not historical-family substitution rules. PDF 15–19 was nevertheless checked page-by-page for the full mandatory family set.

## PDF 20–24 glyph/text findings

- PDF 21 `நீதானா...?` is the batch's consequential historical-family decision: the old `னா` glyph can resemble `னு`, but source-supported character identity is `னா`;
- PDF 20 `போறு ஞானம்!` and `பாய்சன்!` remain source-visible forms;
- PDF 21 `மாடெல்லே` and related colloquial forms remain source-controlled;
- PDF 22 `பாலிலா` remains as printed;
- PDF 23 `தூர பந்து` / `மட்டாக` and `காலராவா? ஜன்னியா?` remain unmodernized;
- PDF 24 `கெளரவம்` remains in the printed orthographic form;
- PDF 20–24 introduced **0 new explicit uncertainty markers**.

The non-glyph items above are textual-fidelity decisions and do not create replacement rules.

## PDF 25–29 glyph/text findings

- PDF 26 `அலைந்தான்` is a source-backed historical-`லை` decoding;
- PDF 27 `சாணைக்கல்லிலே` and `சாணைக்கல்லை` are checked historical-`ணை` cases;
- PDF 28 `காதலை நான்` was checked specifically against historical `லை` / `னா` forms;
- PDF 29 `அணா` is a positive historical-`ணா` case, visible in the payment exchange;
- PDF 25 source speaker forms `சஞ்சீவி` / `சஞ்` remain as printed;
- PDF 26 retains `தயாரப்பட்ட விஷம்`, `மதோன்மத்த வம்சத்தின்`, `மண்ணுங்கட்டியாவது`, `சுத்தப் பைத்தியக்காரனு`;
- PDF 27 retains `உயில் ஒரு வாள்!`, `ஏராளமான சம்பத்துகள்`, `ஏமாற்றத்தையும் ஏணிப்படியாக்கிக்`;
- PDF 28 retains `லஷ்மி`, `ஜமீன்தாரணி யாக்க`, and the source-unlabeled dialogue continuations;
- PDF 29 retains `காண்டிராக்ட்காரன்`;
- PDF 25–29 introduced **0 new explicit uncertainty markers**.

The non-glyph items above are source-fidelity decisions and do not create replacement rules.

## PDF 30–34 glyph/text findings

- PDF 31 `தவறான` is a source-backed historical-`றா` decoding;
- PDF 31 `இவனை` and PDF 32 `அவனை` / `ஜமீனையே` are checked historical-`னை` cases;
- PDF 34 `அவளை` is a checked historical-`ளை` case;
- PDF 34 `பஞ்சணை` is a checked historical-`ணை` case;
- PDF 32 source `குற்ற மாச்சுதுங்களே...`, PDF 33 source `மாத்திரை` / `தைலம்`, and PDF 34 source `அங்கே மீனு இருந்தாள்` remain unmodernized first-pass readings;
- PDF 30–34 introduced **0 new explicit uncertainty markers**.

The non-glyph items above are source-fidelity decisions and do not create replacement rules.

## PDF 35–39 glyph/text findings

- PDF 35 `நானம்மா` is checked historical `னா`;
- PDF 37 `உன்னை` is checked historical `னை`;
- PDF 39 `எமனோடு` is checked historical `னோ`;
- the PDF 35–36 scene-21 lyric is preserved as printed with lineation and without outside reconstruction or authorship inference;
- PDF 35–39 introduced **0 new explicit uncertainty markers**.

## PDF 40–44 glyph/text findings

- PDF 40/41/43/44 `உன்னை` / `குமரனை` are checked historical `னை`;
- PDF 42 `மண்ணைவாரிப்` is checked historical `ணை`;
- source-period/colloquial readings `கோவேரிக் கழுதைக்கு`, `ஆவேஷ மூச்சால்`, `விட்டானுக்கும்?`, `மண்டேகங்கள்`, `நாய்க்குட்டி`, and `மாத்திரை முன்னேற்ற ஆஸ்பத்திரியை` remain unmodernized;
- PDF 40–44 introduced **0 new explicit uncertainty markers** and no new standalone lyric/song block.

## PDF 45–49 glyph/text findings

- PDF 45 `கொன்றாய்` is checked historical `றா`;
- PDF 48–49 `என்னை` is checked historical `னை`;
- PDF 49 `மணாளன்` is checked historical `ணா`;
- PDF 49 `கேளேனோ` is checked historical `னோ`, using the same-edition PDF 39 `எமனோடு` precedent rather than modern visual resemblance;
- PDF 49 opens the mapped scene-31 lyrical witness; `தளா தீச்சுழலில்` remains source-visible and unexpanded;
- PDF 45–49 introduced **0 new explicit uncertainty markers**.

## Source-irregular forms retained

- PDF 12 `தளிர்ச்சிருக்கே` is retained as source-visible wording at first pass;
- PDF 13 `கீல்வலிக்கார தங்கையன்` is preserved source-faithfully;
- PDF 14 visibly prints `வாலாம்` twice;
- PDF 15 `பிரேமா வாகவர்` remains as printed;
- PDF 17's extended labour/tax rhetoric remains source-controlled;
- PDF 19 `சோபிதத்தை`, `கானல் மாடுமே`, and `காதியின்` remain unmodernized first-pass readings;
- PDF 20–24 source-irregular/period wording remains as documented in `textual-notes-pdf-020-024.md`;
- PDF 25–29 source-irregular/period wording remains as documented in `textual-notes-pdf-025-029.md`;
- PDF 40–44 source-irregular/period wording remains as documented in `textual-notes-pdf-040-044.md`.

## Performance evidence affecting later gates

- PDF 16 / `காட்சி 7` contains an explicit `[பாட்டு]` witness with three numbered sections. The booklet's PDF 4 item-level credit identifies **`ஆயிரம் தெய்வங்கள்` — பாரதியார்**. No outside lyric witness was used.
- PDF 18 / `காட்சி 8` contains a source-visible lineated lyrical duet labelled `குமரன்`, `மீனு`, and `இருவர்`, beginning `பேசும் யாழே பெண் மானே`. Its authorship remains unadjudicated.
- PDF 20–34 introduces no newly distinct standalone lyric/song structure; PDF 35–36 contains the mapped scene-21 lyrical witness; PDF 40–44 adds no new standalone lyric/song structure; PDF 49 opens the mapped scene-31 lyrical witness and PDF 50 continues it.

These observations are structural/source evidence only and do not bypass the canonical dual gate.

## Open source questions affecting the cumulative draft

- PDF 5: one physically damaged introductory line remains unresolved;
- PDF 9: one word in the montage/action paragraph after `(நாட்கள் பல கடந்தன)` remains unresolved;
- PDF 10–49 introduced **0 new explicit uncertainty markers**.

Neither open issue is being guessed from context.

## Source-specific cautions

- front matter is physically damaged, but this canonical audit currently covers the screenplay range PDF 5–71;
- many pages contain later handwritten pencil numbers/marks near the upper-right margin; these are not printed Tamil and must not enter the canonical layer;
- fading, bleed-through and broken ink require same-edition comparison rather than silent normalization;
- PDF 5 has no securely visible printed page numeral; glyph decisions and pagination decisions remain separate;
- source-colloquial and source-irregular forms remain source-faithful and are not standardized during glyph decoding.

## Next activity

Continue canonical Tamil first-pass transcription with PDF 55–59, preserving source order, stable page anchors and page-level historical-glyph checks. PDF 59 reaches the first of the already mapped poetic/song-like blocks between scenes 36 and 37; preserve only the booklet witness and do not infer missing lyrics or authorship. Keep all first-pass pages draft/needs-review until the later separate visual-fidelity and final historical-glyph gates pass.


## First-pass closure

All **67/67 canonical pages (PDF 5–71)** have completed occurrence-specific historical-glyph first-pass inspection. This is not final glyph verification: all pages remain review-pending until paired visual-fidelity comparison closes the dual gate. The two source uncertainties remain explicit at PDF 5 and PDF 9.

## PDF 5–9 final dual-gate audit

- historical-glyph final PASS: **PDF 5–9 / 5 of 5**;
- visual-fidelity PASS: **PDF 6–9 / 4 pages**;
- PDF 5 remains held only for a physically missing lexical beginning, not for unresolved historical-glyph identity;
- PDF 9 historical/lexical reinspection resolves `குறுக்கொடிய` and confirms source `காதல்`;
- full decision log: `verification-audit-pdf-005-009.md`.

Next final audit range: **PDF 10–14**.

## PDF 10–14 final dual-gate audit

- historical-glyph final PASS: **PDF 10–14 / 5 of 5**;
- visual-fidelity PASS: **PDF 11–14 / 4 pages**;
- PDF 10 remains held only because the physical right edge removes the ending of a word after visible `வரைக்…`; no reconstruction is permitted;
- source corrections include `மகனோடே`, `வேலையைப்பாரு`, `கூடாதுன்னு`, `எங்களை`, `இல்லேப்பா`, the restored `(மாத்திரை போகிறான்)`, `உயிரை`, and `சங்கேதப் படாதீர்கள்`;
- full decision log: `verification-audit-pdf-010-014.md`.

Next final audit range: **PDF 15–19**.

## PDF 15–19 final dual-gate audit

- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;
- dual-gate canonical: **5/5 VERIFIED**;
- no new uncertainty; PDF 5 and PDF 10 remain the only source-damage holds;
- details: `verification-audit-pdf-015-019.md`.

Next final audit range: **PDF 20–24**.

## PDF 20–24 final dual-gate audit

- historical-glyph final: **5/5 PASS**;
- visual-fidelity: **PDF 20–23 PASS / PDF 24 HOLD**;
- PDF 21 `நீதானா...?` is final-verified historical `னா`;
- PDF 24 hold is caused by a later dark mark obscuring the printed glyph after visible `தே`, not by historical-glyph ambiguity;
- details: `verification-audit-pdf-020-024.md`.

Next final audit range: **PDF 25–29**.

## PDF 25–29 final dual-gate audit

- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;
- dual-gate canonical: **5/5 VERIFIED**;
- consequential scan corrections include PDF 25 `உங்களை` / `கடமைசபதம் எடுத்திருக்கிறேன்`, PDF 28 `லக்ஷ்மி`, and PDF 29 `ஹல்லோ` / `ஆரஞ்சுப்பழமும்`;
- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;
- details: `verification-audit-pdf-025-029.md`.

Next final audit range: **PDF 30–34**.

## PDF 30–34 final dual-gate audit

- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;
- dual-gate canonical: **5/5 VERIFIED**;
- consequential scan corrections: PDF 30 `ஜனங்கள்` / `இல்லாமே` / `போயிடு வாங்க`; PDF 32 `இருப்பவனை`; PDF 33 `ஜரிகைத்` / `இன்பலோகத்தை`; PDF 34 `இதற்கெல்லாம்`;
- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;
- details: `verification-audit-pdf-030-034.md`.

Next final audit range: **PDF 35–39**.

## PDF 35–39 final dual-gate audit

- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;
- dual-gate canonical: **5/5 VERIFIED**;
- scan corrections include PDF 37 `ஆச்சி` / `சரியாய்போச்சிங்க` / `வெளியூருக்கெல்லாம்` / `ஆள`, PDF 38 `மட்டம் தட்ட`, and PDF 39 `பைத்தியம்` / `தெளியும்` / `ஹூம்`;
- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;
- details: `verification-audit-pdf-035-039.md`.

Next final audit range: **PDF 40–44**.

## PDF 40–44 final dual-gate audit

- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;
- dual-gate canonical: **5/5 VERIFIED**;
- scan corrections include PDF 40 `விதியற்றவனே`, PDF 41 `விளைவு`, PDF 42 `உயிலைகொடுத்தவுடன்` / `விவாக சுப`, PDF 43 `மண்டூகங்கள்`, PDF 44 `இல்லே` / `போட்டி ஆஸ்பத்திரி`;
- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;
- details: `verification-audit-pdf-040-044.md`.

Next final audit range: **PDF 45–49**.

## PDF 45–49 final dual-gate audit

- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;
- dual-gate canonical: **5/5 VERIFIED**;
- scan corrections include PDF 45 `என் காரியம் செய்தாய்?` / `சொல்லுகிறியே`, PDF 46 `வாசல்லே` / `அவனை நம்பிப் பிரயோஜனம் இல்லே`, PDF 47 `எப்படிய்யா`, PDF 48 `கட்டுகள்` / `சதி செய்துவிட்டாய்` / `கேடுகெட்டவனே` / `பால் வடியும்` / `வடிகிறது`, and PDF 49 `இதயம் இல்லாதவனே`;
- final glyph cases include `கொன்றாய்` (`றா`), `என்னை` (`னை`), `மணாளன்` (`ணா`) and `கேளேனோ` (`னோ`);
- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;
- details: `verification-audit-pdf-045-049.md`.

Next final audit range: **PDF 50–54**.
