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

The visual audit for **PDF 4–35 / printed pp. 3–34** is complete and the accumulated corrections have been applied.

Part 01 status:

- **30 verified pages**
- **2 review pages: PDF 5 and PDF 16**

The remaining Part 01 uncertainties are:

- PDF 5 / printed p.4: short damaged span in `கல்யாணிக்குக் கல்யாணம் ⟦?⟧ தெரியுமா?`
- PDF 16 / printed p.15: marked word before `தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

Do not infer either from external versions.

## Part 02 — audit in progress

Completed audit batches:

- Batch 5: **PDF 36–43 / printed pp. 35–42**
- Batch 6: **PDF 44–51 / printed pp. 43–50**
- Cumulative Part 02 audit: **PDF 36–51 / printed pp. 35–50**

Part 02 canonical corrections have **not** been applied yet. Continue accumulating findings until PDF 57 is audited, then perform one consolidated Part 02 rewrite.

### Part 02 uncertainty markers resolved from the scan, pending application

Six existing markers have been securely resolved:

- PDF 36: `சேர்மையா`
- PDF 37: `ஒரு அரையணா`
- PDF 40: `பாலைவனத்தை பூஞ்சோலையாக்க`
- PDF 41: `சுட்டுக் கொல்லப்பட்டிருப்போம்`
- PDF 50: `சூறையாட`
- PDF 50: `அணைப்பிலே`

No new genuinely unreadable source span has been found in the Part 02 audit through PDF 51.

### Part 02 blocks requiring direct source-led retranscription

The first-pass text is materially corrupted on these source-readable pages and must be retranscribed directly from the scan during the consolidated rewrite:

- **PDF 42 / printed p.41** — Gnanasekaran's long refugee/beggar-conference speech
- **PDF 44 / printed p.43** — portions of Kalyani's speech after being driven from Sekar's house
- **PDF 45 / printed p.44** — priest/Kalyani temple scene, especially the proposition and priest's internal monologue
- **PDF 46 / printed p.45** — Kalyani's river-side suicide monologue and immediate aftermath
- **PDF 48 / printed p.47** — Kalyani's courtroom answer and family-history passage
- **PDF 49 / printed p.48** — street-preacher speech before the printed `காட்சி—48`

Do not patch these blocks from memory or external Parasakthi versions.

## Exact next work

Audit the final Part 02 range: **PDF 52–57 / printed pp. 51–56**.

For every page:

- compare the complete canonical page text against the rendered scan;
- inspect headings, speaker labels, stage directions, dialogue, punctuation, verse lineation, and page continuity;
- identify omissions and materially corrupted passages as well as isolated word errors;
- resolve an existing uncertainty marker only when the scan supports a confident reading;
- record findings in `works/parasakthi/notes/fidelity-audit.md`;
- preserve the source-order anomalies, especially final `காட்சி—43` on PDF 57.

After PDF 52–57 are fully audited, the next activity is the **single consolidated rewrite of `part-02-pdf-36-57.md`**, including direct retranscription of the six blocks listed above plus any additional block discovered in the final batch. Only then promote Part 02 page anchors individually to `verified` / `review`.

## Translation gate

English translation remains blocked for any unit that is not `verified`. Part 02 remains blocked until its consolidated source correction and page-status promotion are complete.

## Durable continuation state

- Part 01 audit: **complete and applied — 30 verified / 2 review**
- Fidelity audit through: **PDF 51 / printed p.50**
- Part 02 audited: **PDF 36–51 / printed pp.35–50**
- Part 02 resolved markers pending apply: **6**
- Part 02 direct retranscription pages: **42, 44, 45, 46, 48, 49**
- Next fidelity page: **PDF 52 / printed p.51**
- Next batch: **PDF 52–57 / printed pp.51–56**
