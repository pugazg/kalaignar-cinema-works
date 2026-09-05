# Historical Tamil Glyph Transcription Guide

## Purpose

This is a reusable source-first guide for transcribing older Tamil print into modern Unicode without silently changing the source text.

It was created from two kinds of evidence:

1. the user-supplied Periyar எழுத்துச் சீர்திருத்தம் reference chart; and
2. transcription failures and corrections encountered during direct scan review in this archive, especially `பெரிய இடத்துப் பெண்` (1953) and the earlier `புதையல்` work.

Use this document for future novels, stories, speeches, essays, poems, letters, newspapers and other older Tamil printed sources whenever historical typeforms may occur.

---

# 1. Core principle

> **Read character identity, not modern visual resemblance.**

Older Tamil type can use glyph shapes that look like a different modern Tamil sequence. A transcription must determine what character the historical type represents and then encode that character in normal modern Unicode.

This is **glyph decoding**, not modernization of the text.

Therefore:

- preserve the source's word, spelling, grammar, vocabulary and punctuation;
- convert only the proven historical glyph identity into its correct modern Unicode representation;
- do not reproduce an old glyph according to the modern character it merely resembles;
- do not use a historical-glyph finding as permission to rewrite the word into expected modern Tamil.

Example from direct source review:

- apparent modern-shape reading `நன்றுக` was wrong;
- the historical glyph was `றா`;
- correct Unicode transcription: **`நன்றாக`**.

The source wording remains the source wording; only the character identity is decoded correctly.

---

# 2. Known Periyar-reform-sensitive forms

The user-supplied reference chart establishes the following minimum set that must be checked explicitly in older print:

| Modern Unicode identity | Example shown in the supplied chart | Audit family |
|---|---|---|
| `ணா` | `அண்ணா` | `ணா` |
| `ணை` | `அணை` | `ணை` |
| `ணொ` | `மண்ணொடு` | `ணொ` |
| `ணோ` | `கண்ணோடு` | `ணோ` |
| `லை` | `தலை` | `லை` |
| `ளை` | `களை` | `ளை` |
| `றா` | `சிறார்` | `றா` |
| `றொ` | `மற்றொரு` | `றொ` |
| `றோ` | `காற்றோடு` | `றோ` |
| `னா` | `மன்னா` | `னா` |
| `னை` | `வினை` | `னை` |
| `னொ` | `என்னொடு` | `னொ` |
| `னோ` | `என்னோடு` | `னோ` |

This is a **minimum known reference set**, not a claim that every historical Tamil typeface has only these ambiguities. Remain alert for other old ligatures, faint vowel marks, worn type, broken ink and edition-specific forms.

---

# 3. Why visual resemblance is dangerous

A modern reader, OCR system or language model may see an old glyph and map it to the closest-looking current glyph. That can create a plausible-looking but false transcription.

Confirmed examples from this archive:

| Source / scan | Incorrect visual reading | Correct reading | Cause |
|---|---|---|---|
| `பெரிய இடத்துப் பெண்`, scan 14 | `ஆவிலைக்` | `ஆவலைக்` | historical `லை` identity |
| `பெரிய இடத்துப் பெண்`, scan 14 | `நின்றூர்` | `நின்றார்` | historical `றா` identity |
| `பெரிய இடத்துப் பெண்`, scan 16 | `போகிறயே` | `போகிறாயே` | historical `றா` identity |
| `பெரிய இடத்துப் பெண்`, scan 20 | `நன்றுகத்` | `நன்றாகத்` | historical `றா` identity |
| `பெரிய இடத்துப் பெண்`, scan 21 | `நன்றுகத்தான்` | `நன்றாகத்தான்` | historical `றா` identity |
| `பெரிய இடத்துப் பெண்`, scan 24 | `நன்றுக` | `நன்றாக` | historical `றா` identity |
| `பெரிய இடத்துப் பெண்`, scan 24 | `விழுவேன் என்றுனா?` | `விழுவேன் என்றானா?` | historical `றா` identity |
| `பெரிய இடத்துப் பெண்`, scan 25 | `வேலை மட்டுந்தானு?` | `வேலை மட்டுந்தானா?` | historical `னா` identity |

A different but related failure occurred in `புதையல்`: a faint/old `லை` could look like bare `ல்`, which tempted shortening such as `தெரியவில்லை` → `தெரியவில்ல`. High-resolution review showed that such apparent shortening could be an old/faint glyph effect rather than actual wording.

The lesson is broader than any one letter:

> **Never infer character identity from ordinary-zoom appearance alone.**

---

# 4. Mandatory page-level workflow

For every page from a potentially historical Tamil edition:

1. **Inspect the whole page first.** Understand the typeface, ink quality, damage, bleed-through and repeated glyph behaviour.
2. **Use enlarged/native pixels.** Do not decide a difficult glyph from a thumbnail or OCR text.
3. **Check all 13 known reform-sensitive forms.** Do this even when the page appears easy.
4. **Read the complete glyph cluster.** Do not isolate only the final curl, loop or vowel mark.
5. **Compare same-edition evidence.** If a form is unclear, find a clearer occurrence of the same letter family in the same source edition.
6. **Separate glyph identity from lexical expectation.** Grammar and expected wording can suggest where to look, but they are not proof.
7. **Encode the proven identity in modern Unicode.** The canonical Markdown should contain the correct character identity, not a visual imitation of the old metal-type shape.
8. **Preserve everything else.** Do not modernize spelling, sandhi, punctuation, vocabulary or grammar.
9. **If still ambiguous, do not guess.** Keep the page `needs-review` and record the unresolved cluster.
10. **Never global-replace.** Every occurrence must be checked on its own source pixels.

---

# 5. Glyph decoding is not spelling correction

These two operations must remain separate.

## Allowed

If the source uses an old form representing `றா`, encode `றா` in Unicode.

Example:

- apparent shape: `நன்றுக`
- source character identity: `நன்றாக`
- canonical transcription: `நன்றாக`

## Not allowed

Do not change a source word merely because modern Tamil would normally be written differently.

Examples of things that must remain source-faithful unless the pixels prove otherwise:

- old spelling;
- unusual sandhi;
- colloquial forms;
- archaic vocabulary;
- odd grammar;
- repeated words;
- unusual punctuation;
- period-specific compounds and spacing.

A historical-glyph correction changes **character identity only**. A separate lexical/source-text correction requires its own positive scan evidence and should be recorded separately in the audit.

---

# 6. Same-edition comparison method

When a glyph is uncertain:

1. identify its consonant/vowel family;
2. locate a clearer instance of that family elsewhere in the same book or issue;
3. compare stroke direction, loop placement, vowel-mark attachment and surrounding spacing;
4. prefer same-font/same-edition evidence over a generic internet chart when resolving the actual scan;
5. use the reform chart to identify candidate families, not to force a reading.

A chart tells you **what old-form families can exist**. The scan tells you **which one is actually printed here**.

---

# 7. OCR policy

OCR may be used only as a discovery aid.

Do not trust OCR for historical Tamil glyph identity because OCR can:

- map an old glyph to the closest-looking modern character;
- drop faint vowel marks;
- merge neighboring characters;
- split one historical ligature into multiple modern characters;
- normalize a rare source form into a common word.

For any difficult or reform-sensitive cluster, the controlling authority is the source image.

---

# 8. Recommended canonical page note

Each page record may include a short audit block such as:

```markdown
## Historical-glyph first-pass notes

- complete page inspected at enlarged/high resolution;
- checked the full known set: `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- representative source occurrences: `<word>` (`<family>`), `<word>` (`<family>`);
- character identities were decoded before transcription;
- no global replacement or spelling modernization was used;
- page remains `needs-review` unless the project verification policy explicitly permits closure.
```

If a correction is made, record it explicitly:

```markdown
- apparent/earlier reading: `...`
- source-supported Unicode reading: `...`
- historical identity: `றா`
- evidence: direct enlarged source-pixel comparison
```

---

# 9. Recommended work-level audit table

```markdown
| Scan | Printed page | Earlier/apparent reading | Source-supported reading | Historical family | Evidence | Status |
|---:|:---:|---|---|---|---|---|
| 24 | 23 | `நன்றுக` | `நன்றாக` | `றா` | enlarged source scan | needs-review |
```

Keep historical-glyph corrections separate from ordinary transcription corrections. This makes later review much easier.

---

# 10. Decision tree for a doubtful cluster

```text
Difficult Tamil glyph
        |
        v
Inspect native/enlarged source pixels
        |
        v
Does it match one of the known 13 historical families?
       / \
      yes  no/unclear
       |       |
       v       v
Compare     Check same-edition
same-page   and same-font examples
examples       |
       \       /
        v     v
Is character identity positively supported?
       / \
      yes  no
       |    |
       v    v
Encode      Keep `needs-review`;
modern      do not guess from context
Unicode
identity
      |
      v
Preserve source wording unchanged
```

---

# 11. Page breaks and historical glyphs are separate problems

Do not mix these decisions.

A word may be physically split across lines or pages while also containing an old glyph. Resolve them independently:

- first determine the correct character identity from the printed glyph;
- separately record the physical page/line boundary;
- join cross-page fragments only in an assembled reading layer when the join is positively established and provenance remains reversible.

Do not use a likely cross-page word to force an uncertain glyph reading.

---

# 12. Verification policy

A historical-glyph pass can be complete without calling a page `verified`.

Recommended states:

- `not-started` — no canonical transcription yet;
- `partial` — transcription incomplete;
- `needs-review` — canonical text exists but project policy or unresolved questions prevent verification;
- `verified` — only when the project's explicit visual-verification gate has been satisfied;
- `blocked` — source evidence is unavailable or physically insufficient.

If a project discovers a systematic glyph error after pages were previously called verified, reopen the affected coverage to `needs-review` and perform a retrospective source-pixel audit.

---

# 13. Reusable startup checklist for future works

Before transcribing a new older Tamil source:

- [ ] identify publication/edition and scan condition;
- [ ] inspect several representative pages before bulk transcription;
- [ ] determine whether historical Tamil typeforms are present;
- [ ] keep this 13-form reference available;
- [ ] record a project-specific historical-glyph policy in the work README/audit;
- [ ] transcribe from source pixels, not OCR authority;
- [ ] inspect difficult clusters at enlarged/native resolution;
- [ ] compare same-edition examples when uncertain;
- [ ] encode correct modern Unicode identity only;
- [ ] preserve source spelling/grammar/punctuation;
- [ ] record each correction with scan provenance;
- [ ] avoid global replacements;
- [ ] leave unresolved pages `needs-review`;
- [ ] complete a work-level historical-glyph audit before release or translation.

---

# 14. Short rule to remember

> **Old shape ≠ modern look-alike. Identify the historical Tamil character first; then encode that identity in modern Unicode, while leaving the source wording untouched.**
