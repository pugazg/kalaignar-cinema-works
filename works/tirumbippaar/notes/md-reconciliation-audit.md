# திரும்பிப்பார்! — corrected Markdown reconciliation audit

Status: **canonical, scene/dialogue, character/entity and English source reconciliation complete; publication derivatives pending deterministic rebuild/revalidation**

Date opened: 2026-08-26

## Correction witness and authority

The user supplied `thirumbipaar.md` as a corrected transcription specifically to repair OCR / old-Tamil-glyph errors remaining in the repository transcription.

For this reconciliation pass:

1. `thirumbipaar.md` is the **primary correction baseline**.
2. `TVA_BOK_0014652_திரும்பிப்பார்.pdf` is the **final visual authority** when the Markdown is doubtful, appears to contain an extraction artefact, or visibly omits printed material.
3. Earlier repository `verified` labels are historical workflow state, not proof that the Tamil reading was correct.
4. Printed spelling, punctuation, labels, old forms, anomalies and physical page provenance are not silently modernized.
5. Existing immutable dialogue IDs are preserved unless the source proves an omitted labelled utterance.

The systematic error that triggered this pass included forms such as repository `பூமால்` where the corrected/source reading is `பூமாலை`, and repository `இல்ல` where the corrected/source reading is `இல்லை`.

## Input coverage

The supplied corrected Markdown contains all **104 Play Pages**, matching PDF **9–112 / printed pp.1–104**. Extraction-review commentary embedded between its batches is not edition text and was excluded.

## Completion table

| Range | Canonical Tamil | Scene/dialogue derivatives | Status |
|---|---|---|---|
| PDF 9–13 / pp.1–5 | reconciled | scenes 1–4 reconciled | complete |
| PDF 14–35 / pp.6–27 | reconciled | scenes 5–29 reconciled | complete |
| PDF 36–63 / pp.28–55 | reconciled | scene 29 continuation + scenes 30–48 reconciled | complete |
| PDF 64–91 / pp.56–83 | reconciled, scan micro-cleanup applied, final three-string canonical sync complete | scenes 49–75 reconciled; scene 76 begins on p.83 and crosses into Part 05 | complete |
| PDF 92–112 / pp.84–104 | reconciled and final PDF-112 scan omission restored | scenes 76–93 and all dialogue shards reconciled | complete |

## Scene 41 recovered records

The corrected source proved that the old dialogue extraction omitted two explicitly labelled utterances. They were added without renumbering any prior ID:

- `tirumbippaar-s041-d037` — `பூமாலை`
- `tirumbippaar-s041-d038` — `பரந்தாமன்`

Existing `tirumbippaar-s041-d034` retained its ID and genuine PDF 56→57 / printed 48→49 cross-page provenance.

Therefore:

- scene 41 dialogue count = **38**
- whole-work immutable labelled-dialogue total = **1,042**
- no existing dialogue IDs were renumbered.

## Structural findings retained

- Scene 42 and scene 43 remain separate source-supported segments.
- Scene 43 is legitimately **zero-dialogue**; its `கலப்படம்` performance/non-dialogue material remains in scene 43.
- Unlabelled source speech in scenes such as 34 and 44 was not assigned an invented speaker.
- Genuine cross-page dialogue records retain page provenance instead of being split or silently flattened.

## Part 04 scan adjudications and canonical synchronization

Part 04 / PDF 64–91 / printed pp.56–83 is closed at canonical and scene/dialogue layers. Scan-adjudicated cleanup includes:

- scene 49 / PDF 65: full `குயில் பாடுதுங்கிறான்` reading;
- scene 69 / PDF 85: clock preserved as `12½`;
- scene 72 / PDF 88: Paranthaman continuation, `(திரையில் குரல்)`, and the labelled `குரல்:` performance restored in printed order.

Scenes 49–75 were propagated with stable IDs and page provenance. Scene 63 retains the genuine PDF 79→80 cross-page `கொஞ்சங்-` / `கொஞ்சமா` record.

The final whole-layer closure audit also rechecked three previously flagged micro-regressions. Their scene/dialogue derivatives were already correct, but the upstream Part04 canonical batch had retained stale forms. `transcription/parts/part-04-pdf-64-91.md` has now been synchronized exactly as follows:

- `இதெல்லாம் சினிமா. ஈ. எப்ப ஒழியுமோ` → `இதெல்லாம் சினிமா. எப்ப ஒழியுமோ`
- `ஏல்லாம் உன் தம்பியின்` → `எல்லாம் உன் தம்பியின்`
- `[புண்ணகோடி கதவைத் தட்டல்]` → `[புண்யகோடி கதவைத் தட்டல்]`

These are source-layer synchronization fixes only. They do **not** alter scene numbering, dialogue IDs, dialogue counts, character mappings or English unit IDs.

## Part 05 closure

Canonical Part 05 / PDF 92–112 / printed pp.84–104 was rebuilt from the corrected Markdown witness and reconciled through scene 93.

Important repairs include:

- exact labels corrected from old derivative forms such as `பூமால்` / `ஊஷா` to `பூமாலை` / `உஷா`;
- scene 87 retains the explicitly labelled `குண்டுமணி : ...` utterance under its existing stable record ID;
- scene 88 restores `தந்தி கொடுத்திருக்கிறாள்` and keeps its following labelled Paranthaman continuation together;
- scene 90 restores the corrected Bama/Paranthaman/Poomalai ending sequence across PDF 106–109 without changing IDs;
- scene 91 restores source order around `முதலாளி: பாண்டியன்!` and `(பாண்டியன் பிரவேசம்)`;
- scene 92 preserves its newspaper lead-in before the court material;
- scene 93 restores corrected `பூமாலை` text through `வணக்கம்.`.

Direct inspection of PDF 112 / printed p.104 also showed a final non-dialogue departure direction omitted by the Markdown witness. That scan-visible line is now retained in both `scenes/scene-93.md` and canonical `transcription/parts/part-05-pdf-92-112.md` immediately before `வணக்கம்.`.

## Character/entity regeneration

The historical character layer had been built against the pre-correction **1,040-record** dialogue set. After the Tamil layer stabilized at **1,042 records**, the character layer was regenerated without rewriting dialogue text or changing stable entity IDs where identity continuity remained valid.

Reconciled character-layer totals:

- dialogue records scanned: **1,042**
- scenes scanned: **93**
- distinct exact speaker labels: **45**
- stable entities / role categories: **39**
- verified labels: **45 / 45**
- verified entities: **39 / 39**
- review / unresolved labels or entities: **0**

Exact-label changes reflected in the regenerated inventory include `பூமாலை`, `புண்யகோடி`, `குண்டுமணி`, `உஷா`, `சமையல்காரன்`, `அம்மாமி`, and the two printed spacing variants `சப்- இன்ஸ்பெக்டர்` / `சப் - இன்ஸ்பெக்டர்`.

The former `குணமணி` inventory form is no longer retained as a valid exact source label; corrected dialogue evidence resolves it to `குண்டுமணி`. The two sub-inspector spacing forms remain separate exact source labels but map to one unnamed sub-inspector role.

## English source-reconciliation closure

The English translation layer has now been reconciled against the corrected Tamil source for **all 93 scenes**.

Current English totals:

- verified translation units: **1,330**
- dialogue-kind units: **1,049** = 1,042 labelled dialogue links + 7 deliberately unlabelled source-spoken units
- stage-direction units: **262**
- song-reference units: **7**
- chant units: **2**
- written-text units: **10**
- reconstructed full-song units: **0**
- source-labelled dialogue IDs linked: **1,042 / 1,042**

Historical surviving English unit IDs were preserved. New IDs were introduced only for source-proven omitted units, including recovered settings/actions; unsupported historical units were removed only where the corrected source proved that they did not belong. The scene 91→92 newspaper-heading boundary and the source-visible Court/Jail settings in scenes 92–93 are now represented at their correct source locations.

## Current synchronization boundary

- **Corrected canonical coverage:** PDF **9–112 / printed pp.1–104** — all five parts.
- **Canonical source layer:** **scan-closed and Part04 micro-sync complete**.
- **Scene/dialogue corrected reconciliation:** **complete through scene 93 / end of work**.
- **Immutable labelled-dialogue total:** **1,042**.
- **Character/entity layer:** **complete-verified-reconciled — 45 labels / 39 entities**.
- **English source-linked translation layer:** **complete — 93 / 93 scenes, 1,330 verified units, 1,042 / 1,042 labelled links**.
- **Existing stable dialogue IDs:** preserved throughout, apart from the two source-proven omitted scene-41 additions described above.

## Remaining downstream work

The source-linked layers are now synchronized. The historical publication derivatives under `editions/en/` — Markdown reader, standalone HTML, machine-readable JSON, QA reports, manifests and EPUB package — must now be regenerated deterministically from the corrected English layer and revalidated. Until that workflow passes, those generated files should not be treated as the current publication release.

## Next execution order

1. Run the deterministic Tirumbippaar English publication workflow.
2. Require reader QA to pass against all **93 scenes / 1,330 verified units / 1,042 labelled links**.
3. Rebuild and validate the deterministic EPUB package.
4. Synchronize work metadata from the validated publication outputs.
5. Restore final archive-wide publication status only after the generated artifacts and manifests reproduce successfully.

The old `104 verified / 0 review` statement remains historical audit status only; the corrected source, regenerated character layer and fully reconciled English layer supersede it for current textual correctness.