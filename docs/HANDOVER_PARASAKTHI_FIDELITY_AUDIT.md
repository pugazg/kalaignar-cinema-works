# Parasakthi — project handover for fidelity audit

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

This is the controlling continuation note for the **Parasakthi Tamil visual-fidelity audit**.

## Source

- Work: `பராசக்தி`
- Source booklet: `பராசக்தி — முழு வசனம் + பாடல்கள்`
- File: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- Actual PDF pages: **58**
- PDF 4–57 = printed pp. **3–56**
- PDF 58 = rear advertisement/back matter
- Image-only scan; the scan is the canonical source.

Do not repair text from film audio, subtitles, web copies, later editions, memory, or familiar quotations. Preserve spelling, punctuation, scene numbering, source anomalies, and uncertainty transparently.

Uncertainty notation follows `docs/TRANSCRIPTION_GUIDE.md`:

- `⟦?⟧` — unreadable short span
- `⟦reading?⟧` — probable but unverified reading

## Files to read before continuing

Fetch current `main` versions of:

1. `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md`
2. `docs/TRANSCRIPTION_GUIDE.md`
3. `works/parasakthi/notes/fidelity-audit.md`
4. `works/parasakthi/metadata.yaml`
5. `works/parasakthi/mapping.md`
6. `works/parasakthi/transcription/full-text.md`
7. `works/parasakthi/transcription/parts/part-01-pdf-4-35.md`
8. `works/parasakthi/transcription/parts/part-02-pdf-36-57.md`
9. `data/works.json`
10. relevant READMEs

## Structural facts

The first-pass Tamil transcription is complete for **PDF 4–57 / printed pp. 3–56**.

Two canonical parts:

- Part 01: PDF 4–35 / printed pp. 3–34
- Part 02: PDF 36–57 / printed pp. 35–56

The scan has **46 visible scene headings**. Preserve source anomalies exactly:

- `காட்சி-23` not observed
- `காட்சி-34` not observed
- `காட்சி-48` appears on PDF 49 / printed p.48, after scene 42 and before scene 44
- `காட்சி-43` appears at the end on PDF 57 / printed p.56, after scenes 46 and 47

## Part 01 — completed

The visual audit for **PDF 4–35 / printed pp. 3–34** is complete, and the accumulated corrections have been applied in one consolidated rewrite of `part-01-pdf-4-35.md`.

Applied:

- all Batch 1–4 source-form corrections;
- restoration of the omitted PDF 7 `காட்சி—3` opening block directly from the scan;
- restoration of the omitted PDF 12 lyric stanza directly from the scan; its source opening is `கற்சிலையும் சித்திரமும் கண்டு—அதன்`;
- replacement of all ten uncertainty markers that were securely resolved during the audit;
- preservation of the two genuinely unresolved readings.

Part 01 page status is now:

- **30 verified pages**
- **2 review pages: PDF 5 and PDF 16**

The remaining Part 01 uncertainties are:

- PDF 5 / printed p.4: short damaged span in `கல்யாணிக்குக் கல்யாணம் ⟦?⟧ தெரியுமா?`
- PDF 16 / printed p.15: marked word before `தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

Do not infer either from external versions.

The canonical files now contain **9 explicit uncertainty markers across both parts**: 2 in Part 01 and 7 in unaudited Part 02.

## Exact next work

Start the Part 02 fidelity audit at **PDF 36 / printed page 35**.

Recommended next batch: **PDF 36–43 / printed pp. 35–42**.

For each page:

- compare the complete canonical page text against the rendered scan;
- inspect headings, speaker labels, directions, dialogue, punctuation, verse lineation, and page continuity;
- identify omissions as well as wrong words;
- resolve an existing uncertainty marker only when the scan supports a confident reading;
- record every finding in `works/parasakthi/notes/fidelity-audit.md`;
- do not normalize scene numbering or source language.

Use the same controlled workflow as Part 01: accumulate findings for Part 02, then perform a consolidated rewrite after its audit range is complete unless the ledger explicitly changes that rule.

## Translation gate

English translation remains blocked for any unit that is not `verified`. Part 01 pages marked `verified` are eligible individually under the repository rule, but PDF 5 and PDF 16 are not. Part 02 remains blocked until audited and promoted.

## Durable continuation state

- Part 01 audit: **complete and applied**
- Part 01: **30 verified / 2 review**
- Fidelity audit through: **PDF 35 / printed p.34**
- Next fidelity page: **PDF 36 / printed p.35**
- Part 02: **first-pass draft; audit not started**
