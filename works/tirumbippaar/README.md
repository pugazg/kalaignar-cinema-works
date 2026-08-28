# திரும்பிப்பார்!

Archival record for the scanned first-edition screenplay/dialogue booklet **`திரும்பிப்பார்!`**, credited on the cover as `கதை - வசனம் — கலைஞர் மு. கருணாநிதி`.

## Source checkpoint

- Source: `TVA_BOK_0014652_திரும்பிப்பார்.pdf`
- Identifier: `TVA_BOK_0014652`
- PDF pages: **112**
- Main screenplay: PDF **9–112** / printed pp. **1–104**
- File size: **173,960,052 bytes**
- SHA-256: `973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682`
- Edition statement: **`முதல் பதிப்பு: 1953`**
- Cover imprint: `திராவிடப் பண்ணை`, `தெப்பக்குளம் :: திருச்சி`
- Source type: image scan; embedded OCR is navigation assistance only

PDF 2 prints `உரிமையுடையது.` and `விலை ரூ. 0-10-0`. The lower printer-imprint line is physically cropped; the archive retains only the visible partial reading `சிட்டி பிரஸ், மதுரை ரோ…` and does not reconstruct the missing continuation.

## Textual authority

The user-supplied corrected `thirumbipaar.md` is the correction baseline for the 104 screenplay pages because it repairs systematic OCR / old-Tamil-glyph loss in the earlier repository transcription. The rendered scan remains the final authority whenever that Markdown is doubtful, conflicts with the printed page, or omits visible printed material.

Printed spelling, punctuation, labels, old forms, English text, scene structure and physical page boundaries are preserved. Unlabelled speech is not assigned an invented speaker. Stable dialogue, song-occurrence and English unit IDs are not renumbered merely to make later source-order repairs look sequential.

## Final reconciliation status

The corrected source-critical pass and all source-authorized structured/publication derivatives are **complete**:

- canonical Tamil: **PDF 9–112 / printed pp.1–104 — scan-closed**;
- canonical batches: **5/5 reconciled**;
- scenes: **93/93 reconciled**;
- immutable labelled-dialogue records: **1,042**;
- scene 41: **38** labelled records after two source-proven omissions were added as `tirumbippaar-s041-d037` and `tirumbippaar-s041-d038`;
- scene 43: legitimate **zero-dialogue** scene;
- character/entity layer: **45 exact source labels / 39 verified entities or roles / 0 unresolved**;
- song/performance inventory: **8/8 source-reconciled occurrences / 3 verified authorship / 5 evidence-limited unresolved**;
- Tamil song-lyric derivative gate: **closed with 0 files because the booklet prints no complete lyric body for either named song**;
- English source reconciliation: **93/93 scenes / 1,330 verified units / 1,042 of 1,042 labelled dialogue links**;
- English reader QA: **PASS**;
- deterministic EPUB 3 QA: **PASS**.

The final English unit composition is **1,049 dialogue-kind / 262 stage-direction / 7 song-reference / 2 chant / 10 written-text / 0 reconstructed full-song**. Seven source-visible spoken units intentionally remain unlabelled, and 12 genuine cross-page English units remain intact.

## Important source-critical findings

The reconciliation retained rather than normalized several source-sensitive structures:

- scene 41's recovered labelled dialogue without renumbering existing IDs;
- scene 42 and scene 43 as separate source-supported segments;
- song occurrence `tirumbippaar-song-007` belongs to scene **43**, where `கலப்படம் கலப்படம்` is printed; scene 42 is the spoken lead-in only;
- scene 49's full `குயில் பாடுதுங்கிறான்` reading;
- scene 69's printed `12½` clock;
- scene 72's Paranthaman / `(திரையில் குரல்)` / `குரல்:` order;
- scene 63's genuine PDF 79→80 dialogue continuation and stable d020/d021 split;
- scene 76's genuine PDF 91→92 continuation;
- scene 92's newspaper lead-in followed by the Court setting;
- scene 93's Jail setting, final children/warders departure direction, and `வணக்கம்.` without turning the closing `★` into invented prose.

The final closure audit also synchronized three stale Part04 canonical strings with their already-correct derivatives: the stray `ஈ.` after `இதெல்லாம் சினிமா.` was removed, `ஏல்லாம்` was corrected to `எல்லாம்`, and `[புண்ணகோடி கதவைத் தட்டல்]` was corrected to `[புண்யகோடி கதவைத் தட்டல்]`.

The song/performance reconciliation additionally synchronized stale source text in occurrences 001, 002 and 005, and moved occurrence 007 from the old scene-42 attribution to corrected scene 43 without changing its stable ID. No external catalog evidence was used to alter canonical Tamil or scene boundaries.

## Song/performance gate

The booklet contains eight inventoried song, singing or chant occurrences. Three named-song occurrences have item-level authorship evidence: `பாண்டியன் என் சொல்லை` is mapped to **பாரதிதாசன்**, while the `கலப்படம்` occurrence and its reprise are mapped to **கண்ணதாசன்**. Five occurrences remain unresolved because the booklet does not print enough identifying text or item-level credit to establish authorship safely.

No complete lyric body for either named soundtrack song is printed in this booklet. Therefore **zero Tamil lyric-derivative files is the correct completed state**. Lyrics are not imported from catalog metadata, recordings, websites, streaming services, later editions or another song booklet. Reopen this track only if a new controlling source supplies printed lyrics or explicit item-level credits.

## Publication package

The current English publication package was regenerated from the corrected source-linked translation layer and committed by the deterministic workflow in commit **`55bb983eb2959190f025250099793ab5efce2b9f`**.

Reader outputs under `editions/en/`:

- `reader-edition.md`
- `reader-edition.html`
- `reader-edition.json`
- `QA_REPORT.md`
- `manifest.json`

EPUB outputs:

- `tirumbippaar-en.epub`
- `EPUB_QA_REPORT.md`
- `package-manifest.json`

Current EPUB checkpoint:

- scenes: **93**
- English units: **1,330**
- ZIP members: **99**
- size: **370,218 bytes**
- SHA-256: `88bf02ac345926d02a3b6e25ea262c3f6aafe59383a620b2bb160cdd3fabbb31`

See `editions/en/QA_REPORT.md` and `editions/en/EPUB_QA_REPORT.md` for the generated release gates.

## Repository layout

- `transcription/` — canonical Tamil page-order transcription
- `scenes/` — scene derivatives
- `dialogues/` — immutable labelled-dialogue records
- `characters/` — exact-label inventory and entity mapping
- `songs/` — corrected-source song/performance occurrence inventory and authorship evidence
- `translations/` — corrected source-linked English records
- `editions/en/` — deterministic reader and EPUB derivatives
- `notes/md-reconciliation-audit.md` — source-critical reconciliation and closure ledger
- `metadata.yaml` — machine-readable work status

## Closure

There is no remaining source-authorized Tirumbippaar derivative work in the current repository plan. The five unresolved song/chant authorship occurrences are **evidence-limited unresolved states, not pending guesses**. A future activity should reopen this work only when a new controlling source or explicit new publication/integration requirement is supplied.

Future Reading Room or website integration should consume the verified structured repository data and must not alter canonical Tamil, exact speaker labels, stable IDs, page provenance or verified English text.
