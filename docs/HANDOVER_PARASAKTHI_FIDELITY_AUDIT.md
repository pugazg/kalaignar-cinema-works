# Parasakthi — project handover for fidelity audit

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover prepared: 2026-08-12

This document is the controlling handover for continuing the **Parasakthi Tamil visual-fidelity audit and canonical correction**. Always fetch the current `main` versions of the controlling files before making changes.

## 1. Source identity

Work: `பராசக்தி`  
Source booklet: `பராசக்தி — முழு வசனம் + பாடல்கள்`  
Source filename: `TVA_BOK_0062968_பராசக்தி.pdf`  
SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`

Verified source facts:

- Actual PDF pages: **58**.
- Image-only scan; the scan controls the canonical Tamil text.
- PDF 1: front cover.
- PDF 2: title page.
- PDF 3: cast/creative credits.
- PDF 4–57: printed dialogue/song pp. **3–56** (`printed page = PDF page - 1`).
- PDF 58: rear advertisement/back matter, not canonical film dialogue.
- The booklet credits Kalaignar M. Karunanidhi for screenplay/dialogue but lists multiple lyric contributors. Do not infer per-song authorship.

Some file parsers have incorrectly reported only 20 pages. Do not trust that count; the backing source is verified as 58 pages.

## 2. Non-negotiable archival rules

- Preserve source spelling, punctuation, speaker labels, stage directions, scene numbering, and source order.
- Do not modernize or silently repair the source.
- Do not use film audio, subtitles, web copies, later editions, or memory to fill damaged text.
- Use `⟦?⟧` or `⟦reading?⟧` when the scan does not support a confident reading.
- A page may be `verified` only after visual comparison and only if no unresolved reading remains.
- English translation remains blocked until the corresponding Tamil unit is verified.

## 3. Controlling files

Before continuing, fetch the current `main` versions of:

1. `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md`
2. `docs/TRANSCRIPTION_GUIDE.md`
3. `works/parasakthi/notes/fidelity-audit.md`
4. `works/parasakthi/metadata.yaml`
5. `works/parasakthi/mapping.md`
6. `works/parasakthi/transcription/full-text.md`
7. `works/parasakthi/transcription/parts/part-01-pdf-4-35.md`
8. `works/parasakthi/transcription/parts/part-02-pdf-36-57.md`
9. `data/works.json`
10. `works/parasakthi/README.md`
11. root `README.md`

The detailed page-by-page correction wording in `works/parasakthi/notes/fidelity-audit.md` is authoritative. Do not recreate corrections from memory.

## 4. Structural state

The complete first-pass Tamil transcription exists for **PDF 4–57 / printed pp. 3–56**:

- `part-01-pdf-4-35.md` — PDF 4–35 / printed pp. 3–34.
- `part-02-pdf-36-57.md` — PDF 36–57 / printed pp. 35–56, followed by the PDF 58 provenance note.

The corrected structural map contains **46 visible scene headings**. Preserve these source anomalies exactly:

- `காட்சி-23` not observed.
- `காட்சி-34` not observed.
- `காட்சி-48` occurs on PDF 49 / printed p.48, after `காட்சி-42` and before `காட்சி-44`.
- `காட்சி-43` occurs on PDF 57 / printed p.56, after scenes 46 and 47.

## 5. Fidelity-audit state

The part-01 visual audit is now **complete**.

Completed batches:

- Batch 1: PDF 4–11 / printed pp. 3–10.
- Batch 2: PDF 12–19 / printed pp. 11–18.
- Batch 3: PDF 20–27 / printed pp. 19–26.
- Batch 4: PDF 28–35 / printed pp. 27–34.

Cumulative audited range: **PDF 4–35 / printed pp. 3–34 = 32 pages**.

The latest batch, PDF 28–35, found ordinary source-form corrections but **no new unresolved source reading and no additional uncertainty-marker resolution**.

### Substantive omissions that must be restored

1. **PDF 7 / printed p.6** — missing printed `காட்சி—3` heading and opening block. The block begins with கல்யாணி in wedding dress crying before a mirror and continues through replies from பார்வதி / மாணிக்கம் before the continuation on PDF 8.
2. **PDF 12 / printed p.11** — missing full lyric stanza continuing the PDF 11 song, beginning `கற்றிலும் சித்திரமும் கண்டு—அதன்` and ending `அளிக்கும் கலைகள் அறிவோம்`.

### Ten uncertainty markers resolved from the scan

Replace these during the consolidated part-01 rewrite:

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

### Two genuinely unresolved part-01 readings

Retain explicit uncertainty notation for:

- **PDF 5 / printed p.4** — the damaged short span in `கல்யாணிக்குக் கல்யாணம் ⟦?⟧ தெரியுமா?`.
- **PDF 16 / printed p.15** — the marked word immediately before `தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`.

Do not infer either from external versions.

## 6. Latest Batch 4 highlights

The complete wording is in the audit ledger. Important examples:

- PDF 28: `மறுநாள் காலை`, `கடை ஒன்றின்`, `ஆளையே காணும்`, `நம் பயல்`, `(மைனர்களை அடித்து)`, `சொல்லிவிடுகிறேன்`.
- PDF 29: `சமுதாயம் அவள் வாழவிடவில்லை`; `அவர்களை வரச்சொன்னேன்`.
- PDF 30: `நீ ப்ளாக் மார்க்கெட்டை கேவலமா பேசறே`.
- PDF 31: `சிலர் அவனைத் துரத்தவே`; `அண்ணுவே நீங்கள் அழகான வாயால்`.
- PDF 32: `கள்ள மார்க்கெட்-காரன்`; `கந்த புராணத்திலிருந்து`.
- PDF 33: `அட போடா மடையா!`; `அந்தத் தண்ணுடையைக் கொஞ்சம் எடேன்`.
- PDF 34: `அந்தத் தலையணையைக் கொஞ்சமெடேன்`; `என் உப்பை தின்னுட்டு எனக்கே துரோகமா?`; `இங்கே நாராயண லீலாவா`.
- PDF 35: `ஏதாவது நாய்க்கும் வந்து நுழையும்!`.

## 7. Exact next work — consolidated part-01 rewrite

**Do not start PDF 36 yet.** The next required action is to rewrite `works/parasakthi/transcription/parts/part-01-pdf-4-35.md` once, applying the entire audit ledger for PDF 4–35.

The rewrite must:

1. apply every recorded correction for PDF 4–35;
2. restore the complete missing PDF 7 `காட்சி—3` opening block directly from the scan;
3. restore the complete missing PDF 12 lyric stanza directly from the scan;
4. replace the ten resolved uncertainty markers listed above;
5. retain explicit uncertainty notation on PDF 5 and PDF 16;
6. change every page anchor in PDF 4–35 from `draft` to:
   - `review` for PDF 5 and PDF 16;
   - `verified` for all other pages, provided no additional uncertainty emerges while applying corrections;
7. update/remove the old `Draft coverage` wording at the end of the part so it accurately records the completed visual audit and correction state;
8. verify after writing that all 32 source anchors remain present and in order.

After the part-01 rewrite, update:

- `works/parasakthi/notes/fidelity-audit.md`
- `works/parasakthi/metadata.yaml`
- `data/works.json`
- `works/parasakthi/transcription/full-text.md`
- `works/parasakthi/README.md`
- root `README.md`
- this handover document

At that point the next audit page becomes **PDF 36 / printed p.35**.

## 8. After part 01 is corrected

Audit **PDF 36–57 / printed pp. 35–56** against `part-02-pdf-36-57.md`, using the same scan-first rules. Preserve `காட்சி-48` and final `காட்சி-43` exactly as printed. Apply part-02 corrections only after its audit range is complete or in another explicitly controlled rewrite checkpoint.

PDF 58 remains back matter and is not part of the film-dialogue fidelity audit.

## 9. Durable checkpoint

At the time this handover is updated, the part-01 audit ledger, metadata, machine-readable state, README summaries, and canonical manifest have been advanced to show **audit complete through PDF 35 / printed p.34**. The canonical `part-01-pdf-4-35.md` itself still contains the first-pass text and has **not yet received the consolidated corrections**.
