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

The visual audit for **PDF 4–35 / printed pp. 3–34** is complete and corrections are applied.

- **30 verified pages**
- **2 review pages: PDF 5 and PDF 16**

Those two source uncertainties remain unresolved and must not be inferred from external versions.

## Part 02 — visual audit complete, corrections pending

Completed audit batches:

- Batch 5: **PDF 36–43 / printed pp. 35–42**
- Batch 6: **PDF 44–51 / printed pp. 43–50**
- Batch 7: **PDF 52–57 / printed pp. 51–56**

Therefore the complete canonical range **PDF 4–57 / printed pp. 3–56 has now been visually compared against the scan**.

Part 02 canonical corrections have **not** yet been applied. The next operation is one consolidated source-led rewrite of `works/parasakthi/transcription/parts/part-02-pdf-36-57.md`.

### Part 02 uncertainty markers resolved from the scan, pending application

Six existing markers are securely resolved:

- PDF 36: `சேர்மையா`
- PDF 37: `ஒரு அரையணா`
- PDF 40: `பாலைவனத்தை பூஞ்சோலையாக்க`
- PDF 41: `சுட்டுக் கொல்லப்பட்டிருப்போம்`
- PDF 50: `சூறையாட`
- PDF 50: `அணைப்பிலே`

No new genuinely unreadable source span was found anywhere in Part 02.

### Part 02 blocks requiring direct source-led retranscription

The first-pass text is materially corrupted on these readable source pages and must be retranscribed directly from the scan during consolidation:

- **PDF 42 / printed p.41** — Gnanasekaran refugee/beggar-conference speech
- **PDF 44 / printed p.43** — Kalyani after being driven from Sekar's house
- **PDF 45 / printed p.44** — priest/Kalyani temple scene
- **PDF 46 / printed p.45** — river-side suicide monologue and aftermath
- **PDF 48 / printed p.47** — Kalyani courtroom/family-history passage
- **PDF 49 / printed p.48** — street-preacher speech
- **PDF 52 / printed p.51** — continuation of Gunasekaran's courtroom defence
- **PDF 53 / printed p.52** — defence concerning Kalyani, priest, suicide, Gandhi/calf analogy and `பகட்டு / பணம் / பக்தி` sequence
- **PDF 54 / printed p.53** — responsibility-for-crime argument, judge reply and recognition exchange

All other Part 02 pages still require the recorded source-form corrections from `works/parasakthi/notes/fidelity-audit.md`.

## Exact next work

Perform the **single consolidated Part 02 rewrite**:

1. fetch current `main` versions of this handover, `docs/TRANSCRIPTION_GUIDE.md`, `works/parasakthi/notes/fidelity-audit.md`, `works/parasakthi/transcription/parts/part-02-pdf-36-57.md`, metadata and machine state;
2. use the attached scan as the only textual authority;
3. apply every Batch 5–7 source-form correction;
4. directly retranscribe the nine pages/blocks listed above rather than trying to repair their corrupted first-pass wording piecemeal;
5. replace all six resolved uncertainty markers;
6. preserve `காட்சி—48` on PDF 49 and final `காட்சி—43` on PDF 57 exactly in source order;
7. promote Part 02 page anchors to `verified` unless a source uncertainty is actually discovered during application; do not manufacture `review` status merely because the first pass was poor;
8. perform a post-rewrite visual spot-check of every direct-retranscription page and all scene/page boundaries;
9. update ledger, metadata, `data/works.json`, READMEs/manifest as required, and this handover.

Do not begin English translation in the same operation. Finish the corrected Tamil canonical state and its verification first.

## Translation gate

English translation remains blocked for any unit that is not `verified`. Part 02 remains blocked until the consolidated rewrite and post-rewrite verification are complete.

## Durable continuation state

- Part 01 audit: **complete and applied — 30 verified / 2 review**
- Full canonical visual audit: **complete through PDF 57 / printed p.56**
- Part 02 audit: **complete — PDF 36–57 / printed pp.35–56**
- Part 02 corrections applied: **no**
- Part 02 resolved markers pending apply: **6**
- Part 02 direct retranscription pages: **42, 44, 45, 46, 48, 49, 52, 53, 54**
- Next activity: **consolidated Part 02 rewrite and post-rewrite verification**
