# திரும்பிப்பார்! — corrected Markdown reconciliation audit

Status: **source/dialogue reconciliation complete through scene 93; character/entity and publication layers pending regeneration/revalidation**

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
| PDF 64–91 / pp.56–83 | reconciled and scan micro-cleanup applied | scenes 49–75 reconciled; scene 76 begins on p.83 and crosses into Part 05 | complete |
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

## Part 04 scan adjudications

Part 04 / PDF 64–91 / printed pp.56–83 is closed at canonical and scene/dialogue layers. Scan-adjudicated cleanup includes:

- scene 49 / PDF 65: full `குயில் பாடுதுங்கிறான்` reading;
- scene 69 / PDF 85: clock preserved as `12½`;
- scene 72 / PDF 88: Paranthaman continuation, `(திரையில் குரல்)`, and the labelled `குரல்:` performance restored in printed order.

Scenes 49–75 were propagated with stable IDs and page provenance. Scene 63 retains the genuine PDF 79→80 cross-page `கொஞ்சங்-` / `கொஞ்சமா` record.

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

## Current synchronization boundary

- **Corrected canonical coverage:** PDF **9–112 / printed pp.1–104** — all five parts.
- **Canonical source layer:** **scan-closed**.
- **Scene/dialogue corrected reconciliation:** **complete through scene 93 / end of work**.
- **Immutable labelled-dialogue total:** **1,042**.
- **Existing stable IDs:** preserved throughout, apart from the two source-proven omitted scene-41 additions described above.

## Downstream reconciliation

The character/entity inventory was built against the historical 1,040-record dialogue corpus and is now being regenerated from the stable corrected 1,042-record corpus. Exact source labels changed during reconciliation, including `பூமாலை`, `புண்யகோடி`, `குண்டுமணி`, `சமையல்காரன்`, `அம்மாமி`, `உஷா`, and the two printed spacing variants `சப்- இன்ஸ்பெக்டர்` / `சப் - இன்ஸ்பெக்டர்`.

English translations, reader/export derivatives and EPUB outputs remain potentially stale wherever corrected Tamil changes meaning, wording, or source linkage. Their historical verification state is not a current synchronization claim.

## Next execution order

1. Regenerate/reconcile `characters/labels-inventory.json`, `characters/entities-pilot.json`, `characters/entities.json`, `characters/index.json`, and `characters/README.md` against the 1,042-record corpus.
2. Update Tirumbippaar README/metadata/checkpoints to reflect the regenerated character layer.
3. Reconcile English translation and reader/export/EPUB derivatives where Tamil changes are semantically material.
4. Restore final archive status only when all affected layers agree.

The old `104 verified / 0 review` statement remains historical audit status only; the corrected source layer now supersedes it for textual correctness.
