# திரும்பிப்பார்! — corrected Markdown reconciliation audit

Status: **complete — canonical Tamil, scene/dialogue, character/entity, song/performance, English source reconciliation and deterministic publication derivatives verified**

Date opened: 2026-08-26  
Publication closure: 2026-08-28  
Song/performance closure: 2026-08-28

## Authority

The user supplied `thirumbipaar.md` as a corrected transcription to repair OCR / old-Tamil-glyph errors remaining in the earlier repository text.

Authority order for this pass:

1. `thirumbipaar.md` is the primary correction baseline.
2. `TVA_BOK_0014652_திரும்பிப்பார்.pdf` is final visual authority for doubt, conflicts, extraction artefacts, punctuation, headings, physical page structure and visibly omitted material.
3. Earlier repository `verified` labels are historical workflow state, not textual proof.
4. Printed spelling, punctuation, labels, old forms, anomalies and page provenance are not silently modernized.
5. Existing immutable dialogue, song-occurrence and English unit IDs remain stable unless the source proves omitted material.

The supplied corrected Markdown covers all **104 Play Pages**, matching PDF **9–112 / printed pp.1–104**.

## Canonical and scene/dialogue closure

| Range | Canonical Tamil | Scene/dialogue derivatives | Status |
|---|---|---|---|
| PDF 9–13 / pp.1–5 | reconciled | scenes 1–4 reconciled | complete |
| PDF 14–35 / pp.6–27 | reconciled | scenes 5–29 reconciled | complete |
| PDF 36–63 / pp.28–55 | reconciled | scene 29 continuation + scenes 30–48 reconciled | complete |
| PDF 64–91 / pp.56–83 | reconciled; scan micro-cleanup and final three-string sync applied | scenes 49–75 plus scene-76 start reconciled | complete |
| PDF 92–112 / pp.84–104 | reconciled; final PDF-112 omission restored | scenes 76–93 reconciled | complete |

Scene 41's corrected source proved that two explicitly labelled utterances were absent from the historical extraction. They were added without renumbering prior IDs:

- `tirumbippaar-s041-d037` — `பூமாலை`
- `tirumbippaar-s041-d038` — `பரந்தாமன்`

Final scene-41 labelled-dialogue count: **38**. Final whole-work immutable labelled-dialogue count: **1,042**.

Scene 43 remains a legitimate zero-dialogue source scene. Genuine cross-page dialogue remains unsplit. Unlabelled source speech remains unlabelled.

## Part04 closure

Scan adjudications retained include:

- scene 49 / PDF 65 — full `குயில் பாடுதுங்கிறான்`;
- scene 69 / PDF 85 — clock `12½`;
- scene 72 / PDF 88 — Paranthaman continuation, `(திரையில் குரல்)`, then labelled `குரல்:` in printed order;
- scene 63 — genuine PDF 79→80 continuation.

The final closure audit synchronized three stale upstream Part04 strings with their already-correct scene/dialogue derivatives:

- `இதெல்லாம் சினிமா. ஈ. எப்ப ஒழியுமோ` → `இதெல்லாம் சினிமா. எப்ப ஒழியுமோ`
- `ஏல்லாம் உன் தம்பியின்` → `எல்லாம் உன் தம்பியின்`
- `[புண்ணகோடி கதவைத் தட்டல்]` → `[புண்யகோடி கதவைத் தட்டல்]`

No stable IDs or counts changed as a result.

## Part05 closure

PDF **92–112 / printed pp.84–104** is reconciled through scene 93. Representative repairs include exact `பூமாலை`, `புண்யகோடி`, `குண்டுமணி` and `உஷா` forms; scene 88's `தந்தி கொடுத்திருக்கிறாள்`; the scene-90 ending sequence; scene-91 source order; scene-92 newspaper lead-in; and scene-93 closing speech through `வணக்கம்.`.

Direct scan inspection of PDF 112 also recovered a final non-dialogue departure direction omitted from the Markdown witness. It is retained in both `scenes/scene-93.md` and canonical `transcription/parts/part-05-pdf-92-112.md` immediately before `வணக்கம்.`.

## Character/entity closure

The character layer was regenerated after the immutable dialogue corpus stabilized at **1,042** records.

Final totals:

- scenes scanned: **93**
- dialogue records scanned: **1,042**
- distinct exact source labels: **45**
- stable entities / roles: **39**
- verified labels: **45/45**
- verified entities: **39/39**
- review / unresolved: **0**

Exact-label handling retains corrected forms such as `பூமாலை`, `புண்யகோடி`, `குண்டுமணி`, `உஷா`, `சமையல்காரன்`, `அம்மாமி`, and both printed sub-inspector spacing forms `சப்- இன்ஸ்பெக்டர்` / `சப் - இன்ஸ்பெக்டர்`.

## Song/performance reconciliation closure

The historical song/performance inventory predated the final corrected-source scene pass. All **8** stable occurrence records were rechecked against the current corrected scene derivatives.

Final occurrence distribution:

- scene 2 — `tirumbippaar-song-001`
- scene 6 — `tirumbippaar-song-002`
- scene 11 — `tirumbippaar-song-003`
- scene 14 — `tirumbippaar-song-004`
- scene 29 — `tirumbippaar-song-005`
- scene 31 — `tirumbippaar-song-006`
- scene 43 — `tirumbippaar-song-007` and `tirumbippaar-song-008`

Four stale source-metadata drifts were repaired without changing occurrence IDs:

- occurrence 001: `பூமால்` → corrected `பூமாலை`;
- occurrence 002: stale `பாமா பாட்டுமுடிந்ததும்...` → corrected `பாமா பாடிமுடிந்ததும் குடத்தை எடுத்துக்கொண்டு போகிறாள்`;
- occurrence 005: chant punctuation synchronized exactly to corrected scene 29;
- occurrence 007: stale scene **42** attribution moved to corrected scene **43**, where Pandiyan sings what he wrote and the booklet prints `கலப்படம் கலப்படம்`. Occurrence 008 remains the office-boy reprise later in the same scene.

Scene 42 remains the spoken lead-in to the song performance but contains no separate song/performance inventory occurrence.

Authorship status remains evidence-limited rather than guessed:

- verified occurrences: **3** — `பாண்டியன் என் சொல்லை` / **பாரதிதாசன்**, plus `கலப்படம்` and its reprise / **கண்ணதாசன்**;
- unresolved occurrences: **5** — the four unnamed singing/performance references and the standalone labour chant;
- full named-song lyric blocks printed by this booklet: **0**.

The front matter contains no `பாடல்கள்` or item-level lyricist credit. External track metadata supplies authorship only for exact title matches and is never used to repair Tamil wording, scene boundaries or supply absent lyrics.

Therefore `song_tamil_derivatives` is now **closed-no-source-full-lyrics**, with **0 derivative lyric files by design**. This is a completed source-limited state, not unfinished work. Reopen only if a new controlling source supplies printed lyric bodies or explicit item-level credits.

## English source-reconciliation closure

All **93 scenes** are corrected-source reconciled in English.

Final English totals:

- verified units: **1,330**
- dialogue-kind: **1,049** = 1,042 labelled dialogue links + 7 deliberately unlabelled source-spoken units
- stage directions: **262**
- song references: **7**
- chants: **2**
- written text: **10**
- reconstructed full songs: **0**
- labelled dialogue links: **1,042/1,042**
- genuine cross-page English units: **12**

Historical surviving English unit IDs were preserved. Source-proven recovered settings/actions were added without renumbering surviving IDs. The corrected English scene-43 records already link `tirumbippaar-song-007` and `tirumbippaar-song-008` at their proper source location, so the song-inventory scene-boundary repair required no English unit move or renumbering.

## Publication rebuild audit

The deterministic publication rebuild exposed downstream metadata defects that the source reconciliation itself had not invalidated. Each was repaired without changing canonical Tamil or stable unit identity:

- malformed JSON in translation scenes **63** and **67** was repaired;
- recovered carry-over stage directions in scenes **37** and **39** were restored to true source order while retaining their high stable IDs;
- exact linked speaker metadata was synchronized from immutable dialogue records, including sub-inspector spacing variants;
- stale English page provenance was source-adjudicated and corrected in scene **66**, scene **77**, and scene **82**;
- publication tooling was updated from the historical **1,321-unit / 1,040-link** checkpoint to the current **1,330-unit / 1,042-link** checkpoint.

The final preflight reported:

- actual units: **1,330**
- page regressions: **0**
- duplicate English unit IDs: **0**
- dialogue links: **1,042 unique / 1,042 immutable**
- missing links: **0**
- extra links: **0**

The reader build then passed:

- **93 scenes**
- **1,330 verified units**
- **1,042 dialogue links**
- **12 cross-page units**
- QA: **PASS**

The deterministic EPUB 3 build also passed:

- scenes: **93**
- units: **1,330**
- scene XHTML documents: **93**
- ZIP members: **99**
- bytes: **370,218**
- SHA-256: `88bf02ac345926d02a3b6e25ea262c3f6aafe59383a620b2bb160cdd3fabbb31`
- QA: **PASS**

The generated release was committed by GitHub Actions as **`55bb983eb2959190f025250099793ab5efce2b9f`**.

## Final synchronization boundary

- canonical Tamil: **scan-closed, PDF 9–112 / pp.1–104**
- scenes: **93/93 complete-verified-reconciled**
- immutable labelled-dialogue corpus: **1,042**
- character/entity layer: **45 labels / 39 entities / 0 unresolved**
- song/performance inventory: **8/8 source-reconciled / 3 verified authorship / 5 evidence-limited unresolved**
- Tamil song-lyric derivative gate: **closed-no-source-full-lyrics / 0 files by design**
- English translation: **93/93 scenes / 1,330 verified units / 1,042/1,042 labelled links**
- reader Markdown/HTML/JSON: **complete-verified, QA PASS**
- EPUB 3 package: **complete-verified, QA PASS**
- work metadata: **synchronized to the validated release and source-limited song closure**

The old **104 verified / 0 review** first-pass transcription status, the old **1,321-unit / 1,040-link** English publication status, and the historical pre-reconciliation song inventory are retained only as historical checkpoints. The corrected source-critical closure above supersedes them.

## Remaining work

There is no remaining source-authorized derivative work for Tirumbippaar in the current plan. The five unresolved song/chant authorship records are intentional evidence-limited outcomes, not pending normalization or guesses. Reopen this work only when a new controlling source or an explicit new publication/integration requirement is supplied.
