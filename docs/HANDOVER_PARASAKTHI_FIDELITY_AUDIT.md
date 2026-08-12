# Parasakthi — project handover for fidelity audit

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover prepared: 2026-08-12  
Last verified project HEAD before this handover update: `1bc8192f0ddf31b2b570f770a376d1c94b9fcee7`

This document is the controlling handover for continuing the **Parasakthi Tamil visual-fidelity audit** in another chat window. Read it together with the current `main` versions of the files listed below before making any new transcription or audit changes.

## 1. Source and project identity

Work: `பராசக்தி`  
Source booklet: `பராசக்தி — முழு வசனம் + பாடல்கள்`  
Attached/source filename: `TVA_BOK_0062968_பராசக்தி.pdf`  
SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`

Verified source facts:

- Actual PDF page count: **58**.
- Image-only scan; do not trust OCR or parsed text as canonical source text.
- PDF 1: front cover.
- PDF 2: title page.
- PDF 3: cast/creative credits.
- PDF 4–57: printed dialogue/song pages **3–56** (`printed page = PDF page - 1`).
- PDF 58: rear advertisement / back matter, not canonical film dialogue.
- The title/credits pages credit Kalaignar M. Karunanidhi for screenplay/dialogue, but the credits page lists multiple lyric contributors. Do **not** automatically attribute every song to Kalaignar.

Important tooling caveat: in some file-tool responses the attachment parser has incorrectly reported only **20 pages**. The backing source has already been independently verified as **58 pages**. If a later chat sees the 20-page parser count, do not treat that as the actual PDF length. Read/render the backing PDF pages directly.

## 2. Non-negotiable archival rules

The scan controls the canonical Tamil text.

Do not:

- modernize spelling or punctuation;
- normalize scene numbering;
- silently repair apparent printing errors;
- substitute film audio, subtitles, web quotations, later editions, or memory;
- guess a damaged word simply because a familiar Parasakthi line is known elsewhere;
- mark a page `verified` while a source uncertainty on that page remains unresolved.

Use the uncertainty notation defined in `docs/TRANSCRIPTION_GUIDE.md`:

- `⟦?⟧` — unreadable short span;
- `⟦reading?⟧` — probable but not yet secure reading.

## 3. Files that control continuation

Before continuing, fetch and read the current `main` versions of:

1. `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md` — this document.
2. `docs/TRANSCRIPTION_GUIDE.md` — transcription/review rules.
3. `works/parasakthi/notes/fidelity-audit.md` — detailed page-by-page audit ledger.
4. `works/parasakthi/metadata.yaml` — source and progress metadata.
5. `works/parasakthi/mapping.md` — corrected source structure and scene-start map.
6. `works/parasakthi/transcription/full-text.md` — canonical manifest.
7. `works/parasakthi/transcription/parts/part-01-pdf-4-35.md` — first canonical part.
8. `works/parasakthi/transcription/parts/part-02-pdf-36-57.md` — second canonical part.
9. `data/works.json` — machine-readable progress state.
10. `works/parasakthi/README.md` and root `README.md` — public progress summaries.

Do not continue from an older cached copy of these files.

## 4. Structural state already established

The complete first-pass Tamil transcription is present for **PDF 4–57 / printed pp. 3–56**. It is split into two archival parts:

- `part-01-pdf-4-35.md` — PDF 4–35 / printed pp. 3–34.
- `part-02-pdf-36-57.md` — PDF 36–57 / printed pp. 35–56, followed by the PDF 58 back-matter provenance note.

The first-pass transcription status is `draft-complete`; it is **not** verified Tamil.

Corrected structural mapping confirms **46 visible `காட்சி-N` headings**. Preserve these source anomalies exactly:

- `காட்சி-23` was not observed.
- `காட்சி-34` was not observed.
- `காட்சி-48` occurs on PDF 49 / printed p.48, after `காட்சி-42` and before `காட்சி-44`.
- `காட்சி-43` occurs at the very end on PDF 57 / printed p.56, after scenes 46 and 47.

Earlier structural notes that had treated 33, 38, and 40 as absent were corrected: those headings are present.

## 5. Fidelity-audit state at handover

The second-pass visual audit is **in progress**.

Completed and committed:

- Batch 1: **PDF 4–11 / printed pp. 3–10**.
- Batch 2: **PDF 12–19 / printed pp. 11–18**.
- Batch 3: **PDF 20–27 / printed pp. 19–26**.
- Cumulative audited range: **PDF 4–27 / printed pp. 3–26** = **24 pages**.
- Next page that has not been committed as audited: **PDF 28 / printed p.27**.

The detailed findings are in `works/parasakthi/notes/fidelity-audit.md` and must be treated as the authoritative audit ledger.

### Two substantive first-pass omissions already found

1. **PDF 7 / printed p.6** — the draft omitted the printed `காட்சி—3` heading and its opening block. The missing block begins with கல்யாணி in wedding dress crying before a mirror and continues with her lament about the absent brothers and replies from பார்வதி / மாணிக்கம். It must be restored from the scan during the consolidated part-01 rewrite.

2. **PDF 12 / printed p.11** — the draft omitted a complete lyric stanza continuing the song from PDF 11. It begins `கற்றிலும் சித்திரமும் கண்டு—அதன்` and ends `அளிக்கும் கலைகள் அறிவோம்`. It must be restored in source position during the consolidated part-01 rewrite.

### Existing uncertainty markers resolved visually but not yet applied to canonical text

Ten readings have been resolved directly from the scan and are pending the consolidated rewrite of part 01:

- PDF 13: `பஞ்சையாய்`
- PDF 13: `பராரியாய்`
- PDF 16: `சோப்பு`
- PDF 17: `நல்லவன், நாதியற்றவனை`
- PDF 18: `கேளாமலேயே`
- PDF 19: `வித்தாத்தானே வீணுப்போனவனே?`
- PDF 20: `ஈசனார்`
- PDF 22: `லாண்டறியே`
- PDF 22: `டேபின்`
- PDF 23: `சஞ்சீவி நாம பர்வதம்`

Do not treat the old uncertainty markers in the canonical file as still unresolved merely because they have not yet been replaced there.

### Known genuinely unresolved readings within the audited range

Two readings remain genuinely unclear after enlarged visual inspection:

- **PDF 5 / printed p.4** — the short damaged span in `கல்யாணிக்குக் கல்யாணம் ⟦?⟧ தெரியுமா?`.
- **PDF 16 / printed p.15** — the marked word before `தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`.

Do not infer either from external versions.

The first-pass canonical files still contain **19 explicit uncertainty markers across both parts** because the consolidated audit rewrite has not yet happened. Ten of those markers have now been resolved in the audit ledger; the two readings above remain unresolved within PDF 4–27; markers on later unaudited pages still require visual review.

## 6. Important corrections already recorded

Do not recreate these from memory; use the audit ledger for exact wording. Examples already recorded include:

- PDF 4: `இந்த மண் மாதாவின் மடியிலே` rather than draft `மடியில்`.
- PDF 5: `விளையாண்டுகிட்டு` rather than draft `விண்ணியாண்டுகிட்டு`.
- PDF 7: `(ஞான சேகரன் வருந்துகிறான்)` rather than draft `வந்துகிறான்`, plus the omitted `காட்சி—3` opening block.
- PDF 11: feminine stage-direction forms `தவறியவள் ... வெளியேறுபவள் ... செய்கிறாள்`; `உம்...வேண்டாம்...தேங்க்ஸ்`; lyric `இனிக்கும் விதத்தில் சுகம்`.
- PDF 12: omitted lyric stanza, `ஆணவத்தினிலே`, `இனிக்கும் விதத்தில் சுகம்`, `தன் பணத்தை பூராவும் பறிகொடுக்கிறான்`.
- PDF 13–19: multiple colloquial/source-form corrections plus six uncertainty resolutions.
- PDF 20: `ஈசனார்`, `சாட்சி கோர்ட்டு ஏறாதடி`, `முட்டாபயலையெல்லாம்`, `பிச்சைக்காரனில்லை`.
- PDF 21: `அவுங்க`, `அவளையும்`, `அவளை சிசுவும்`, `துயரப்படுறியே`, `யானையும் வாகனமாய்—சின்ன`.
- PDF 22: `வெள்ளியினால்`, `உனை`, `லாண்டறியே`, `டேபின்`, `தான் ஆட்டத்துக்கு வர்லே`.
- PDF 23: `மந்திரி பிரதானீகளே`, `பரதேசிப் பசங்களா`, `சஞ்சீவி நாம பர்வதம்`.
- PDF 24–27: many source-form corrections in the mad/road and Venu-Kalyani scenes, recorded page by page in the ledger.

Again, `works/parasakthi/notes/fidelity-audit.md` is authoritative for the complete findings.

## 7. Do not rewrite part 01 yet

The deliberate workflow is to avoid repeated large-file rewrites.

`part-01-pdf-4-35.md` has **not** yet been rewritten with audit corrections. Its page anchors remain `draft`.

Continue accumulating audit findings until **PDF 35 / printed p.34** has been completely audited. Only then perform one consolidated rewrite of part 01 that:

1. applies every recorded correction for PDF 4–35;
2. restores the missing PDF 7 `காட்சி—3` opening block;
3. restores the missing PDF 12 lyric stanza;
4. replaces uncertainty markers whose readings were securely resolved from the scan;
5. retains explicit uncertainty notation wherever the source is still genuinely unclear;
6. changes each individual page anchor from `draft` to:
   - `verified` only if that page has no unresolved source reading after correction;
   - `review` if an unresolved source reading remains.

After the rewrite, update the audit ledger, metadata, `data/works.json`, relevant READMEs, and the handover state.

## 8. Exact next work

Start from **PDF 28 / printed page 27**.

Recommended next audit batch: **PDF 28–35 / printed pp. 27–34**, completing the audit range for part 01.

For every page in that batch:

- compare the full canonical page text against the rendered scan;
- inspect speaker labels, punctuation, directions, dialogue, headings, verse lineation, and page continuity;
- identify omissions as well as wrong words;
- resolve existing `⟦...⟧` markers only when the scan supports a confident reading;
- record findings in `works/parasakthi/notes/fidelity-audit.md`;
- update progress metadata/README/handover after the batch;
- **do not rewrite `part-01-pdf-4-35.md` until PDF 35 is completely audited**.

After PDF 28–35 are audited and committed, the next step should be the consolidated rewrite of `part-01-pdf-4-35.md`.

## 9. After part 01 is corrected

Once PDF 4–35 is fully audited and the consolidated part-01 rewrite is complete:

1. audit **PDF 36–57 / printed pp. 35–56** against `part-02-pdf-36-57.md`;
2. resolve or retain its remaining explicit uncertainty markers using the same rules;
3. apply part-02 corrections in a controlled rewrite;
4. promote page anchors individually to `review` / `verified`;
5. verify that source-order anomalies (`காட்சி-48`, final `காட்சி-43`) remain unchanged;
6. only after the Tamil text for a unit is `verified` may an English translation of that unit begin.

PDF 58 remains rear advertisement/back matter and is not part of the canonical film-dialogue audit, though its provenance note should remain intact.

## 10. Commit discipline

Continue working on `main` unless the user explicitly asks otherwise.

After each audit batch:

- commit the audit-ledger update;
- update `metadata.yaml` and `data/works.json` to the new audited-through page;
- update the Parasakthi README and root README if they expose progress;
- update this handover document so another chat can resume without relying on conversation memory.

Do not claim corrections have been applied to canonical Tamil until the corresponding transcription part has actually been rewritten and committed.

## 11. Suggested opening prompt for the next chat

Use this with the same source PDF attached:

> I am continuing `pugazg/kalaignar-cinema-works` Parasakthi fidelity audit. Read the current `main` versions of `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md`, `docs/TRANSCRIPTION_GUIDE.md`, `works/parasakthi/notes/fidelity-audit.md`, `works/parasakthi/metadata.yaml`, `works/parasakthi/mapping.md`, and both canonical transcription parts. Treat those repository files as controlling instructions. The attached source is `TVA_BOK_0062968_பராசக்தி.pdf`, SHA-256 `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`, actual 58 PDF pages. Continue the visual fidelity audit exactly from **PDF 28 / printed page 27**. Do not use subtitles, web copies, later editions, or memory to repair the text. Record findings first; do not rewrite part 01 until PDF 35 has been completely audited.

## 12. Durable checkpoint

At this handover update, the latest completed audit batch is:

`PDF 20–27 / printed pp. 19–26` — Batch 3, recorded in `works/parasakthi/notes/fidelity-audit.md`.

After this handover file is committed, treat the resulting newer `main` HEAD as the new durable checkpoint and fetch it fresh in the next chat.
