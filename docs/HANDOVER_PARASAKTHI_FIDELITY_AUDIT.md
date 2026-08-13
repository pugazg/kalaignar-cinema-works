# Parasakthi — project handover after Tamil fidelity audit

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

This is the controlling continuation note for the **Parasakthi canonical Tamil transcription after completion of the visual-fidelity audit**.

## Source

- Work: `பராசக்தி`
- Source booklet: `பராசக்தி — முழு வசனம் + பாடல்கள்`
- File: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- Actual PDF pages: **58**
- PDF 4–57 = printed pp. **3–56**
- PDF 58 = rear advertisement/back matter
- Image-only scan; the scan is the controlling textual source.

Do not repair unreadable text from film audio, subtitles, web copies, later editions, memory, or familiar quotations. Preserve genuine source uncertainty transparently.

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

## Canonical coverage and audit result

The canonical Tamil transcription covers **PDF 4–57 / printed pp. 3–56**.

Two canonical parts:

- Part 01: PDF 4–35 / printed pp. 3–34
- Part 02: PDF 36–57 / printed pp. 35–56

The full canonical range has completed page-by-page visual fidelity audit.

### Part 01

- **30 verified pages**
- **2 review pages: PDF 5 and PDF 16**

The two unresolved source readings are:

- PDF 5 / printed p.4: short damaged span in `கல்யாணிக்குக் கல்யாணம் ⟦?⟧ தெரியுமா?`
- PDF 16 / printed p.15: unclear word before `தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

Do not infer either from external versions. Leave them as `review` unless stronger source evidence becomes available.

### Part 02

Part 02 has been fully audited, consolidated, and post-rewrite verified:

- **22 verified pages**
- **0 review pages**
- **0 remaining uncertainty markers**

Six first-pass uncertainty markers were resolved directly from the scan:

- PDF 36: `சேர்மையா`
- PDF 37: `ஒரு அரையணா`
- PDF 40: `பாலைவனத்தை பூஞ்சோலையாக்க`
- PDF 41: `சுட்டுக் கொல்லப்பட்டிருப்போம்`
- PDF 50: `சூறையாட`
- PDF 50: `அணைப்பிலே`

Nine materially corrupted first-pass blocks were retranscribed directly from the scan:

- PDF **42, 44, 45, 46, 48, 49, 52, 53, 54**

After the first consolidated rewrite, an enlarged post-rewrite visual check identified additional source-form inaccuracies, especially on PDF 44–46 and PDF 52–54. Those were corrected in the final Part 02 corrective commit:

`ac4828c60f9a69590f1fc6b2da17114f62c16d22`

## Critical scene-number correction

The booklet itself contains a two-heading scene-number misprint/transposition near the end. **Do not revert the canonical correction.**

### PDF 49 / printed p.48

- Booklet prints: `காட்சி—48`
- Canonical visible heading: **`காட்சி—43`**
- Reason: this scene follows `காட்சி—42` and precedes `காட்சி—44`.

### PDF 57 / printed p.56

- Booklet prints: `காட்சி—43`
- Canonical visible heading: **`காட்சி—48`**
- Reason: this is the final scene after `காட்சி—46` and `காட்சி—47`.

The source readings are preserved as hidden HTML comments immediately before the two corrected headings in `part-02-pdf-36-57.md`, and both source and canonical values are recorded in `mapping.md` and `metadata.yaml`.

Therefore the canonical sequence near the end is:

`காட்சி—42` → **`காட்சி—43`** → `காட்சி—44` → `காட்சி—45` → `காட்சி—46` → `காட்சி—47` → **`காட்சி—48`**.

Headings 23 and 34 remain unobserved in the source; do not invent them.

## Durable final Tamil state

- Structural mapping: **verified**
- Canonical Tamil coverage: **complete — PDF 4–57 / printed pp. 3–56**
- Full visual fidelity audit: **complete**
- Total canonical page status: **52 verified / 2 review**
- Part 01: **30 verified / 2 review**
- Part 02: **22 verified / 0 review**
- Remaining source uncertainties: **PDF 5 and PDF 16 only**
- Part 02 post-rewrite corrective verification: **complete**
- Scene-number correction: **source PDF49 48 → canonical 43; source PDF57 43 → canonical 48**
- PDF 58: rear advertisement/back matter, recorded as `paratext`
- Per-song authorship mapping: **not-started**

## Translation gate

English translation may begin only for Tamil source units marked `verified`. PDF 5 and PDF 16 remain blocked unless their source uncertainties are resolved from stronger evidence.

Do **not** alter the canonical Tamil merely to make translation smoother. Translation is derivative and must remain separate from the source transcription.

## Next work

There is **no remaining page-by-page Tamil fidelity-audit work** for this scan.

For any future continuation:

- keep the two Part 01 uncertainties explicit unless stronger source evidence is obtained;
- preserve the documented scene-number correction described above;
- if moving to derivatives, work only from `verified` Tamil units;
- song-specific work should first resolve per-song authorship because the booklet credits multiple lyric contributors.

Do not silently reintroduce the booklet's swapped `காட்சி—48` / `காட்சி—43` headings into the visible canonical copy.
