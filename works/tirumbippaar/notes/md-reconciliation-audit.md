# திரும்பிப்பார்! — corrected Markdown reconciliation audit

Status: **source/dialogue reconciliation complete through scene 93; downstream layers still pending**

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

The supplied corrected Markdown contains all **104 Play Pages**, matching PDF **9–112 / printed pp.1–104**. Extraction-review commentary embedded between its batches is not edition text and is excluded.

## Progress

| Range | Canonical Tamil | Scene/dialogue derivatives | Status |
|---|---|---|---|
| PDF 9–13 / pp.1–5 | reconciled | scenes 1–4 reconciled | complete |
| PDF 14–35 / pp.6–27 | reconciled | scenes 5–29 reconciled | complete |
| PDF 36–63 / pp.28–55 | reconciled | scene 29 continuation + scenes 30–48 reconciled | complete |
| PDF 64–91 / pp.56–83 | reconciled and scan micro-cleanup applied | scenes 49–75 reconciled; scene 76 begins on p.83 and crosses into Part 05 | complete |
| PDF 92–112 / pp.84–104 | corrected-Markdown canonical reconciliation complete | scenes 76–93 and all existing dialogue shards reconciled | **dialogue/scene pass complete** |

## Scene 41 recovered records

The corrected source proved that the old dialogue extraction omitted two explicitly labelled utterances. They were added without renumbering any prior ID:

- `tirumbippaar-s041-d037` — `பூமாலை`
- `tirumbippaar-s041-d038` — `பரந்தாமன்`

Existing `tirumbippaar-s041-d034` retained its ID and its genuine PDF 56→57 / printed 48→49 cross-page provenance.

Therefore:

- scene 41 dialogue count = **38**
- whole-work immutable labelled-dialogue total = **1,042**
- no existing dialogue IDs were renumbered.

## Part 03 structural findings retained

- Scene 42 and scene 43 remain separate source-supported segments.
- Scene 43 is legitimately **zero-dialogue**; its `கலப்படம்` performance/non-dialogue material remains in scene 43.
- Unlabelled source speech in scenes such as 34 and 44 was not assigned an invented speaker.

## Part 04 closure

Part 04 / PDF 64–91 / printed pp.56–83 is closed at canonical and scene/dialogue layers. The scan-adjudicated cleanup includes:

- scene 49 / PDF 65: full `குயில் பாடுதுங்கிறான்` reading;
- scene 69 / PDF 85: clock preserved as `12½`;
- scene 72 / PDF 88: Paranthaman continuation, `(திரையில் குரல்)`, and the labelled `குரல்:` performance restored in the printed order.

Scenes 49–75 were propagated with stable IDs and page provenance. Scene 63 retains the genuine PDF 79→80 cross-page `கொஞ்சங்-` / `கொஞ்சமா` record.

## Part 05 canonical and derivative reconciliation

Canonical Part 05 / PDF 92–112 / printed pp.84–104 was rebuilt from the corrected Markdown witness. Scene/dialogue propagation is now complete through **scene 93**, including the scene-76 PDF 91→92 cross-part continuation.

Important Part-05 repairs include:

- source labels corrected from old derivative forms such as `பூமால்` / `ஊஷா` to the corrected exact labels `பூமாலை` / `உஷா` where supplied by the correction witness;
- scene 87 retains the explicitly labelled `குண்டுமணி : ...` utterance under its existing stable record ID rather than replacing it with guessed speech;
- scene 88 restores `தந்தி கொடுத்திருக்கிறாள்` and keeps the following `சீரழிந்த குடும்பத்திலே மறுமலர்ச்சி உண்டாக்குவேன்` inside the same labelled Paranthaman utterance;
- scene 90 restores the corrected `குமுதாவுக்கு வலைவீச வந்திருக்கிறாய்`, the full Bama/Paranthaman/Poomalai ending sequence across PDF 106–109, and exact `பூமாலை` labels without changing IDs;
- scene 91 restores the source order in which `முதலாளி: பாண்டியன்!` precedes `(பாண்டியன் பிரவேசம்)`, and keeps the newspaper material with scene 92 rather than scene 91;
- scene 92 preserves its source-supported newspaper lead-in before the court material, while retaining the two existing stable dialogue IDs;
- scene 93 restores corrected `பூமாலை` text through the final `வணக்கம்.` and retains the scan-visible final non-dialogue departure direction in the scene derivative.

### One canonical scan-propagation cleanup remains

Direct inspection of PDF 112 / printed p.104 shows a final parenthetical departure direction after Poomalai's closing speech and before `வணக்கம்.`. The corrected Markdown omits this non-dialogue line. `scene-93.md` retains that scan-visible material, but the same line still needs to be inserted back into `transcription/parts/part-05-pdf-92-112.md` before the canonical full-volume layer is declared completely scan-closed.

This does **not** alter dialogue IDs or the 1,042-record total.

## Current synchronization boundary

- **Corrected Markdown canonical coverage:** PDF **9–112 / printed pp.1–104** — all five parts.
- **Canonical scan-closed boundary:** PDF **9–111**, plus PDF 112 dialogue/text; one final PDF-112 non-dialogue parenthetical remains to be propagated into canonical Part 05.
- **Scene/dialogue corrected reconciliation:** **complete through scene 93 / end of work**.
- **Immutable labelled-dialogue total:** **1,042**.
- **Existing stable IDs:** preserved throughout, apart from the two source-proven omitted scene-41 additions described above.

## Known-stale downstream layers

The character/entity inventory is intentionally stale because exact source labels changed during reconciliation, including `பூமாலை`, `புண்யகோடி`, `குரல்`, `குண்டுமணி`, `சமையல்காரன்`, `அம்மாமி`, `உஷா`, and source-spacing variants of police labels.

English translations, reader/export derivatives and EPUB outputs may also be stale wherever corrected Tamil changes meaning, wording, or source linkage. Their historical verification state is not a current synchronization claim.

## Next execution order

1. Insert the scan-visible final PDF-112 departure direction into canonical Part 05 and close the canonical source layer.
2. Update `transcription/full-text.md`, Tirumbippaar README/metadata/checkpoints and verify dialogue/index totals remain 1,042.
3. Regenerate/reconcile the character/entity layer from the now-stable corrected dialogue corpus.
4. Reconcile English translation and reader/export/EPUB derivatives where Tamil changes are semantically material.
5. Restore final archive status only when all affected layers agree.

The old `104 verified / 0 review` statement remains historical audit status only and is superseded for textual correctness by this reconciliation pass until downstream synchronization is complete.
