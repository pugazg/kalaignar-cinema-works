# Reading Room title/film metadata reconciliation — archival decision record

This is a **hand-written archival decision record**. It is not generated, and
`integrations/reading-room/sync_status.py` does not write anywhere under
`notes/`.

It exists because the reconciliation history below was originally appended to
`AUDIT.md` and `PROGRESS.md`, inside the ranges those files hand to the status
generator. The post-merge automation regenerated those ranges and correctly
removed the hand-written prose. That behaviour is by design; the record simply
belonged somewhere the generator does not own.

Read this note before any downstream import, Reading Room application, or
authorship-inclusion work.

---

## 1. What failed

The downstream Reading Room payload builder
(`integrations/reading-room/build.py`) halted at the then-current source pin
with:

```
status= FAIL
error= film title drift at 001
```

## 2. Why an earlier PASS and a later FAIL are both correct

The English reader/export preflight compared the **translation records** against
their **verified Tamil song files**. Within that comparison surface its
zero-mismatch results were accurate, and they remain accurate.

The Reading Room builder added a **stricter cross-layer invariant** that no
earlier gate enforced:

```
songs/index.json  ↔  editions/en/reader-edition.json
```

Five metadata divergences sat precisely in that previously uncovered gap. The
builder halts on the first failure, so only `001` was named; the remaining four
were found by running its later gates independently.

This reconciliation is therefore an **extension of QA coverage**. It is **not**
evidence that the earlier QA PASS was fraudulent or meaningless.

---

## 3. The five source adjudications

Each was decided by direct inspection of the controlling 2024 scan
`TVA_BOK_0065867`. None was inferred from grammar, spelling convention or
outside knowledge of the films.

### 001 — film grouping label

Both forms genuinely occur in the controlling source:

| Surface | Prints |
|---|---|
| film section heading, PDF 24 | `மந்திரிகுமாரி` |
| numbered lyric page, PDF 26 | `மந்திரி குமாரி` |

- canonical film-grouping metadata: **`மந்திரிகுமாரி`**
- preserved page-local source variant: **`மந்திரி குமாரி`**

**Neither form is a typo.** The variant is recorded explicitly in the `001`
inventory `notes` and on the song page, not normalised away. The 1989 witness
`TVA_BOK_0065773` also prints the spaced form; that is secondary evidence only
and does not override the 2024 controlling source.

### 004 — title

Canonical: **`மாரி மகமாயி மாரி மகமாயி`**

Authority: the film-specific printed song list (PDF 32). The previously stored
shortened form was not a printed title.

### 007 — title

Canonical: **`பேசும் யாழே பெண் மானே`**

The `(சோகம்)` appearing on the lyric page belongs to the **voice credit**
`ஜிக்கி (சோகம்)`. It is not title text, and the voice credit itself is
unchanged. Song `005` carries the identical Tamil title, consistent with the
printed list showing that title twice for this film.

### 008 — title

Canonical: **`வருவாய் வருவாய்...`**

The following lyric line begins `வைபோக சுந்தரியே...`. That continuation must not
be synthesised into the title; the previously stored value had joined the first
lyric line to the opening word of the second.

### 015 — title

Canonical: **`காதல் துறையே புதுமைக் கனவே (சோகம்)`**

The printed list (PDF 43) carries `(சோகம்)` as the disambiguator distinguishing
this item from `014`, whose base title is identical. The separate page/context
text `முத்தாயி சோக கீதம்` (PDF 47) is **not** part of the canonical title and
remains in the lyric body and in the translation section layer.

**Song `014` is unchanged.** Because `014` and `015` share the same base title,
any future edit keyed by string match rather than song id will corrupt one of
them.

---

## 4. Title-authority rule for this work

1. The film-specific `இப்படத்தில் இடம் பெற்ற பாடல்கள்` list controls canonical
   **song-title** metadata where present.
2. Numbered lyric pages control the **lyric body**, role/performance labels,
   context labels and page-local wording.
3. The film section heading / contents control the corpus **film-grouping**
   label.
4. Genuine source-internal variants are **preserved explicitly**, never
   normalised into agreement.
5. A canonical title is **never** synthesised from a lyric first line, a voice
   credit, a context label or other neighbouring text.
6. Do **not** generalise this policy to other works without separate evidence
   from their own controlling sources.

---

## 5. The three project-created English-title repairs

Correcting a canonical Tamil title does not by itself correct English derived
from the superseded one. Independent review caught three derivatives still
carrying the old semantics.

| # | Old | Final | Reason |
|---|---|---|---|
| 007 | `O speaking yaazh, O doe — lament` | `O speaking yaazh, O doe` | the suffix rendered the voice-credit `(சோகம்)`, not title text |
| 008 | `Come, come... Vaibhoga Sundariye...` | `Come, come...` | the continuation came from the following lyric line |
| 015 | `O realm of love, O new dream — song of sorrow` | `O realm of love, O new dream (sorrow)` | `song of sorrow` rendered the separate `சோக கீதம்` context label |

For `015` the title's own `(சோகம்)` is rendered as the parenthetical
**`(sorrow)`**, without importing `கீதம்`. The base matches `014`, whose Tamil
base title is identical. `song of sorrow` remains correct where it actually
belongs — the translation section label for `முத்தாயி சோக கீதம்`.

---

## 6. Zero lyric-text drift

The reconciliation changed **metadata only**. Verified against the pre-PR source
main `6a8c59c445890e568dfe65cc36c2900dd2a8a0b3`:

| Measure | Result |
|---|---|
| Tamil lyric-body files changed | **0 / 54** |
| English lyric lines changed | **0 / 1105** |
| Paired inline-Tamil lines changed | **0 / 1105** |
| Line IDs changed | **0** |

Aggregate SHA-256 values, identical before and after:

- Tamil lyric bodies of all 54 song files:
  `9178702195f80f98fe9ded9dd32924bd2156adbce02c3333d8b271be904448e1`
- all 1,105 stored English lines:
  `a8975d7088bd3e9036f21b3d371af69448505c45da6e66a8f3bb8d041f6e00c5`
- their paired Tamil:
  `8635ba48d1e5e94421a13ba11af2b237f80d2f27af55e50f5c7167ff81c8aa74`

Scope of semantic change: **5** source/title metadata findings plus **3**
project-created English-title derivatives. No lyric text was rewritten.

---

## 7. Builder state after reconciliation

**English publication builder** — PASS · 54 songs · 1,105 line-cues · 0 warnings
· 0 errors.

**Reading Room payload builder** — PASS · 23 film groups · 54 songs · 1,105
line-cues · 8 cross-page songs · 0 warnings · 0 errors ·
`site_application_status: not-applied`.

Archival census: 54/54 Tamil `verified`, 0 unresolved Tamil song readings;
English 3 `pilot-verified` + 51 `verified`; **54 `anthology-attributed`**.

Generated payload SHA-256:
`8ec0e25f7fc1f1a9750d370ccbef5dd07caa66629a3dfacb8425bbeebd08fcce`

`not-applied` means the public Digital Library has **not** consumed this payload.
A verified payload is not a deployment.

---

## 8. Source checkpoints

| Checkpoint | Meaning |
|---|---|
| `18a35e32d0e4bab85e01569f336ab9a7603c9c2f` | PR #5 head as independently reviewed |
| `4dae107d61da02ceb65c8a8b460c03c1c55ac4c2` | **human-reviewed reconciliation squash merge** — its commit message carries the full adjudication |
| `fdf55fdf7c80f4769f870f2ba2ae6a72f1804461` | **subsequent automated** status/payload synchronisation (`github-actions[bot]`, direct parent `4dae107d`) |

The two are different in kind: `4dae107d` is the reviewed source decision;
`fdf55fdf` is generated bookkeeping that followed it.

---

## 9. What remains intentionally unresolved — authorship inclusion

**This reconciliation does not establish that all 54 archival songs are
Kalaignar-authored, and it must not be read as doing so.**

- The archival corpus remains **54 songs**, all **`anthology-attributed`**.
- `anthology-attributed` records how the 2024 compilation presents an item. It
  is **not** original-film primary-source verification of authorship, and it is
  not a public-inclusion decision.
- The owner's publication policy is that only lyrics **established as written by
  Kalaignar** will appear in the Digital Library.
- The controlling source itself carries at least one relevant caution: the
  அம்மையப்பன் film section (PDF 43) prints an editorial note stating that all the
  film's songs were included but that the compiler could not confirm which of
  them Kalaignar wrote.

Determining the Kalaignar-authored inclusion set is a **separate pre-E1 gate**.
It was deliberately not attempted here: no song was removed, no attribution
status promoted or downgraded, and no public inclusion count is asserted by this
record.

---

## 10. Standing cautions for future work

- `sync_status.py` owns exactly the regions it delimits with
  `BEGIN GENERATED: reading-room-status` / `END GENERATED: reading-room-status`
  marker comments, in `AUDIT.md`, `PROGRESS.md`, the work `README.md` and
  `PROJECT_HANDOVER.md`. Everything outside those marker pairs is human-authored
  and is never rewritten.
- Keep hand-written prose outside the marker pairs. Do not duplicate, relocate or
  nest the markers, and do not hand-edit content between them — change the
  generator instead and let it regenerate.
- `notes/` is outside generator control entirely and remains the durable home for
  archival decision records such as this one.
- The `PROJECT_HANDOVER.md` pointer to this note must stay above that file's
  marker block.
- *(Historical, for context only: before the markers existed the generator located
  its regions by heading text, so prose that repeated a boundary heading could
  capture the replacement. That failure mode is retired and is not the current
  operating rule.)*
- Keep `014` and `015` distinct in any title-related edit.
- The lyric body, the voice credit and the context label are three separate
  source surfaces. Do not merge them to produce a more descriptive title.
