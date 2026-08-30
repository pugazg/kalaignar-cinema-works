# Kalaignar-authorship inclusion evidence — கலைஞர் திரை இசைப் பாடல்கள்

Durable, hand-written archival record. Lives under `notes/`, outside all
status-generator control. Nothing here is regenerated; edit it by hand.

This note explains the complete 54-song Kalaignar-authorship evidence gate and
the proposed public inclusion set it produces. The machine-readable outputs are:

- `authorship/inclusion-evidence.json` — the song-level evidence register, 001–054;
- `authorship/public-inclusion.json` — the derived inclusion manifest;
- `authorship/validate.py` — the fail-closed validator over both.

> **Revision note.** The first pass of this gate adjudicated the controlling
> 2024 source only. Independent review found that the project's **known 1989
> witness had not been adjudicated at all**. It has now been read and mapped in
> full, the evidence model has been rebuilt to hold structured evidence items
> from every witness rather than one flattened statement per song, and the
> inclusion set has been recomputed from the evidence. Any earlier statement
> that this gate rested on the 2024 source alone is superseded by this note.

## 1. Why this gate exists

`metadata.yaml` records `default_song_attribution_state: anthology-attributed`
and `primary_source_verification_requires_separate_evidence: true`. All 54
numbered lyrics carry that default. "Anthology-attributed" states only that a
lyric was printed in a volume titled
கலைஞர் திரை இசைப் பாடல்கள். It is a fact about the book,
not a song-level finding about who wrote the words.

Publishing the corpus as Kalaignar's lyrics requires the stronger, song-level
claim. This gate supplies it song by song, or declines to.

## 2. The two witnesses

### 2.1 Controlling 2024 source

`TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`,
SHA-256 `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`,
130,427,193 bytes, 194 PDF pages, compiler நெல்லை ஜெயந்தா, June 2024.
Byte-exact against `metadata.yaml` and `songs/index.json`.

Its decisive apparatus is the per-film box headed
இப்படத்தில் இடம் பெற்ற பாடல்கள், which lists that film's
songs with a **per-song lyricist column**. That column names கலைஞர்
for some songs and other writers (பாரதிதாசன், மருதகாசி,
வாலி, வைரமுத்து, கண்ணதாசன், ஆலங்குடி சோமு,
எஸ்.ஏ.ராஜ்குமார், இளையபாரதி and others) for the rest.

| Apparatus present | Film sections |
| --- | --- |
| Per-song lyricist column | 21 |
| Collective credit only, no per-song mapping | 1 (அம்மையப்பன்) |
| No song list printed at all | 1 (நெஞ்சுக்கு நீதி) |
| **Total** | **23** |

All 23 song-list pages were read: PDF 25, 28, 32, 43, 52, 61, 69, 72, 76, 79,
82, 89, 96, 99, 102, 105, 108, 112, 115, 119, 126, 129, plus PDF 85, which
prints no list.

### 2.2 Earlier 1989 witness

`TVA_BOK_0065773_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`,
SHA-256 `56d414a65a61a73b990632eadc17a3b1efdc764d47f64b851060c161a3f98e3b`,
10,419,528 bytes, 62 PDF pages. Compiler சிலோன் விஜயேந்திரன்,
imprint காந்தளகம், first edition
வைகாசி 21, திருவள்ளுவர் 2020 (03.06.89). This matches the
source package already committed at `sources/tva-bok-0065773/`.

**This volume prints no lyricist credit anywhere.** Its contents table gives
song, film and page only; its body sections give
ஆண்டு / படம் / இசை / பாடியவர் only. Its authorship
evidence is therefore of a different kind, and had to be read rather than
assumed.

Everything below was read from rendered page images. **OCR was not used as
textual authority** for either witness.

## 3. What the 1989 compiler actually claims

The compiler's preface, தொகுப்பாசிரியர் உரை, PDF 4, prints:

> விரிஞாலத் தமிழர்தம் நெஞ்சமெல்லாம் வீற்றிருக்கும்
> அருங்குணத் தலைவர் **கலைஞர் யாத்த** இன்னமுதத் திரைப்
> பாடல்களை மனோ விழைவோடு தொகுத்துச் செந்தமிழர்
> பார்வைக்குத் தந்துள்ளேன். **தமது திரைப் பாடல்களைத்
> தொகுப்பதற்கு அனுமதி வழங்கியதோடு** அமையாது பல்லாற்றானும்
> ஒத்துழைப்பு நல்கிய மாண்புமிகு தமிழக முதல்வர் **கலைஞர்**
> அவர்கட்கு யான் என்றும் கடப்பாடுடையேன்.

That is an **explicit authorship claim**, not mere collection placement: the
volume collects *the film songs Kalaignar composed*, and Kalaignar himself
granted permission for *his* film songs to be compiled and cooperated in the
work. The preface also thanks the film historian
'பிலிம் நியூஸ்' ஆனந்தன் and Kalaignar's secretary
சண்முகநாதன்.

The independent foreword, தும்பியுரை (PDF 5–7), by
டாக்டர் சிலம்பொலி சு. செல்லப்பன், describes the book the
same way — கலைஞரின் திரையிசைப் பாடல்களை … தொகுத்தளிக்கிறார் —
and says the volume stands as evidence that Kalaignar is peerless
இசைப் பாடல்களை இயற்றுவதிலும், in composing songs too.

**Scope of the claim, stated exactly.** It is explicit, it is authorised by the
author, and it is enumerated by the contents — but it is made at **collection
scope**, not song by song. It is not a contemporary original-film credit and is
never recorded as one.

## 4. The complete 1989 → current mapping

The repository already held a verified structural map and deduplication audit
for this witness. Both were revalidated here rather than replaced.

- 1989 numbered sections: **40**
- sections mapped to current records: **40**
- distinct current song records: **39**
- unmapped sections: **0**
- multiple sections to one record: sections **4** and **13** both map to
  `song-009` — the 1989 witness splits material the 2024 witness keeps in one
  numbered song
- current songs absent from the 1989 witness: **15** — 014, 015, 017, 040,
  044–054

Source of the mapping: `songs/SOURCE_WITNESS_0065773_DEDUP.md`, revalidated
against the contents pages (PDF 8–9) and all 40 body sections in this activity.
The validator re-parses that file and requires the register to agree with it.

**Absence from the 1989 witness is recorded as a source fact only.** It is never
treated as evidence that a song is not Kalaignar's: the 1989 volume is a
forty-song selection, not a catalogue, and it predates several films in this
corpus.

## 5. Evidence model

Every one of the 54 records carries an `evidence_items` array. Each item
records:

`source_identifier`, `source_year_or_edition`, `source_kind`,
`source_path_or_filename`, `pdf_page_or_location`, `printed_page_if_known`,
`attribution_scope`, `attribution_as_printed_or_source_claim`,
`identity_basis`, `evidence_level`, `evidence_effect`, `basis`.

`attribution_scope` ∈ {`song-specific`, `collection-scoped-listed-song`,
`film-collective`, `film-writing-credit`, `implicit-collection-placement`,
`not-present-in-witness`}.

`evidence_effect` ∈ {`supports-kalaignar`, `supports-other`,
`limits-song-level-attribution`, `neutral-provenance`}.

Evidence levels are unchanged: **A** primary contemporary documentary,
**B** independent authoritative secondary, **C** explicit and song-specific,
**D** implicit or non-song-specific — never sufficient.

174 evidence items in total: **108** from the 2024 source, **66** from the 1989
witness.

## 6. How the 1989 evidence is levelled — one rule, applied uniformly

The reviewer's question was whether the 1989 source is merely collection
placement or makes an explicit scoped authorship claim. It makes an explicit
scoped claim. But *explicit* and *song-specific* are different things, and the
project's hierarchy turns on the latter. The same test is therefore applied to
both witnesses:

> **Level C requires an attribution to this song. Anything that covers the
> volume rather than the song is level D, however explicit it is.**

Applied to the 1989 witness this gives exactly two kinds of item, and every
mapped song gets the first:

- **`collection-scoped-listed-song`, level D, `supports-kalaignar`** — the
  preface and foreword claim, plus this song's presence in the enumerated
  contents. Recorded for all **39** mapped records. Positive evidence, but never
  sufficient on its own.
- **`song-specific`, level C, `supports-kalaignar`** — this song's *own* body
  section prints an editorial note naming கலைஞர் in connection with
  this song, its composition or its content as his expression. Recorded for the
  **12** sections that carry such a note: 1, 2, 5, 7, 8, 9, 10, 11, 12, 15, 21,
  34 → songs 031, 024, 037, 011, 012, 004, 042, 036, 043, 001, 038, 028.

The test is mechanical — *does this song's section print a note naming
கலைஞர்?* — so it cannot be tuned to a desired outcome, and the operative
sentence of every one of the 12 notes is quoted verbatim in the register for
independent checking. Examples:

- section 15 → song 001: **கலைஞர் எழுதிய முதற் திரைப்படப் பாடலான இது** —
  *this, the first film song Kalaignar wrote*;
- section 9 → song 004: **கலைஞர் யாத்துள்ளார்** — *Kalaignar has composed it*;
- section 1 → song 031: **பாடலை இயற்றி உள்ளார் கலைஞர்**;
- section 11 → song 036: **மேற்காணும் பாடலில் நயமாகச் சாடுகிறார் கலைஞர்**.

The remaining 28 mapped sections print no note and stay at level D. That is not
a judgement against those songs; it is simply what the source prints.

## 7. Decision rule, separate from the evidence

A record's decision is a property of the record, never of any single item. A
record may hold positive and limiting items at once.

1. If a **material conflict** exists → `unresolved`, and never automatically included.
2. Else if any item supports Kalaignar at level A/B/C → `established-kalaignar`.
3. Else if any item supports a named other writer at level A/B/C → `established-other`.
4. Else if any item limits song-level attribution → `unresolved`.
5. Else → `insufficient-evidence`.

`public_inclusion` is true if and only if the decision is
`established-kalaignar` and no material conflict is declared.

**Material conflict is defined narrowly and deliberately:** two or more items
make *incompatible positive attributions* — one supports Kalaignar and another
supports a different named writer for the same song, both at level A/B/C. **A
source declaring its own inability to confirm authorship is not a material
conflict.** It is limiting evidence, not a competing attribution. This
distinction decides song 012, so it is stated before the outcome rather than
after it.

No song in this corpus has a material conflict, and no song is
`established-other`: nothing in either witness attributes any of these 54
lyrics to a named writer other than Kalaignar. The mechanism exists and is
exercised by the validator's mutation tests.

## 8. Outcome

| Decision | Songs | Count |
| --- | --- | --- |
| `established-kalaignar` | 001–012, 019–054 | **48** |
| `unresolved` | 013–018 | 6 |
| `insufficient-evidence` | — | 0 |
| `established-other` | — | 0 |

Proposed public inclusion set: **48 of 54**.

The previous pass returned 46. The count was **recomputed from the evidence,
not preserved**: songs 012 and 036 moved to `established-kalaignar` on 1989
song-specific evidence, and `insufficient-evidence` fell to zero.

## 9. Song 012 — அம்மையப்பா அருள்புரிவாய் எல்லாம் உன் செயல்

**Identity.** 1989 section 8, PDF 22–23, printed pp. 13–14. Its opening —
அம்மையப்பா அருள்புரிவாய் எல்லாம் / உன்செயல் அம்மையப்பா
— and its printed metadata,
ஆண்டு: 1954; படம்: 'அம்மை யப்பன்'; இசை: டி.ஆர். பாப்பா;
பாடியவர்: சீர்காழி கோவிந்தராஜன், match 2024 song 012. The printed
text of both witnesses was compared line by line. Same song.

**2024 evidence.** PDF 43 prints one collective credit for the whole film —
பாடலாசிரியர்கள் : கலைஞர், சுரதா, எம்.கே. ஆத்மநாதன்,
முத்துக்கூத்தன் — with no per-song mapping, and the compiler's note
headed இசைத்தட்டே இல்லை states that neither the film nor a
gramophone record survives, that all of the film's songs are reproduced, and
that it could not be confirmed which of them Kalaignar wrote. Scope
`film-collective`, level D, effect `limits-song-level-attribution`.

**1989 evidence.** The collection-scope item (level D), and — decisively — this
song's own section note on printed p. 13:

> மேற்காணும் அரிய பாடலிற் **கலைஞர்**, சமதிருஷ்டி உடையவன்
> எனப்படும் இறைவன் சிருஷ்டியிலே காணப்படும் வெறுக்கத்தக்க
> வேறுபாடுகளை மிக நளினமாகக் **கண்டிக்கிறார்**.

*In the above rare song, Kalaignar very elegantly condemns the repugnant
inequalities found in the creation of the god who is called even-eyed.* Scope
`song-specific`, level C, effect `supports-kalaignar`.

**Adjudication.** The two sources do not contradict each other. The 2024
compiler records his own inability to confirm, at film level; he does not
attribute this song to anyone else. The 1989 compiler — writing 35 years
earlier, with Kalaignar's own permission and cooperation — attributes this
specific song's authorial act to Kalaignar. Neither witness names another
writer for it. A song-level attribution at level C is not displaced by a
film-level declaration of uncertainty at level D.

**Decision: `established-kalaignar`. Included.**

The steelman for leaving it unresolved was weighed and is recorded here: the
1989 statement is appreciation prose rather than a credit line, and the 2024
compiler was the later and better-resourced editor. It does not carry, because
the 1989 volume's stated premise is that its contents are Kalaignar's
compositions, because its note speaks about *this* song, and because the 2024
compiler's uncertainty is expressly about the whole அம்மையப்பன் set
rather than about this lyric.

## 10. Song 036 — நெஞ்சுக்கு நீதியும்

**Identity.** 1989 section 11, PDF 27–28, printed pp. 18–19. The printed text is
**verbatim identical** to 2024 song 036 across all its stanzas —
நெஞ்சுக்கு நீதியும் / தோளுக்கு வாளும் … through
கவி பாரதி பாடிய நீதி … and
மனிதராய் வாழ்ந்திடுவோம். Its metadata,
ஆண்டு: 1979; படம்: 'நெஞ்சுக்கு நீதி'; பாடியவர்: டி.எம்.எஸ்.;
இசை: சங்கர் கணேஷ், matches. Same song.

**2024 evidence.** PDF 85 prints no song list and therefore no lyricist column
at all; its only Kalaignar credit is
கதை, திரைக்கதை, வசனம் : கலைஞர் மு.கருணாநிதி — story,
screenplay and dialogue, a writing credit for the film and **not** a lyric
credit, which must not be read across into song authorship. The numbered lyric
page (PDF 86) prints only இசை and குரல். Both recorded as
level D, effect `neutral-provenance`. **The 2024 witness is silent; silence is
not an attribution to anyone else.**

**1989 evidence.** The collection-scope item (level D), and this song's own
section note on printed p. 19:

> எதிரிகளைக் கண்டு **கலைஞர்** எஞ்ஞான்றும் கலங்கியது கிடையாது.
> … வீண்பழி போடுவதை **மேற்காணும் பாடலில் நயமாகச் சாடுகிறார்
> கலைஞர்**.

*In the above song, Kalaignar elegantly rebukes …* Scope `song-specific`, level
C, effect `supports-kalaignar`.

**Adjudication.** One qualifying song-specific attribution, no contrary
attribution, no material conflict. The earlier reading of `insufficient-evidence`
was correct on the 2024 source alone and is wrong once the 1989 witness is
admitted.

**Decision: `established-kalaignar`. Included.**

## 11. The other six அம்மையப்பன் songs

They do not share one cross-witness result, and are not treated as a block.

| Song | 1989 presence | 1989 song-specific note | Decision |
| --- | --- | --- | --- |
| 012 | section 8 | **yes** | `established-kalaignar` |
| 013 நீலக்கடல் பாரு பாப்பா | section 36, printed p. 46 | no | `unresolved` |
| 014 காதல் துறையே புதுமைக் கனவே | absent | — | `unresolved` |
| 015 காதல் துறையே … (சோகம்) | absent | — | `unresolved` |
| 016 சின்னப் புது மலரே | section 35, printed p. 45 | no | `unresolved` |
| 017 சிதைந்ததே என் காதல் உயிரோவியம் | absent | — | `unresolved` |
| 018 காதல் புறா காதிலே பேசுவதென்னோ | section 23, printed p. 33 | no | `unresolved` |

013, 016 and 018 gain positive 1989 evidence — they sit inside the 1989
volume's explicit authorship claim — but only at collection scope, level D,
which never qualifies. 014, 015 and 017 are absent from that volume, which is
recorded as a source fact and is **not** negative evidence.

All six remain `unresolved`. **Unresolved is not a finding that these songs are
not Kalaignar's.** It is the absence of song-level evidence either way, and it
is the state a stronger witness would change.

## 12. Two title-match gaps, resolved on the lyric pages

Unchanged from the first pass, and now corroborated by a third witness.

**Song 023 — ராஜா ராணி.** The 2024 p. 52 list has no
கண்ணற்ற தகப்பனுக்கு entry; its fifth Kalaignar entry,
பூனை கண்ணை மூடிக்கொண்டால், appears verbatim as the fourth line
of the printed lyric on PDF 58. The five Kalaignar-attributed list entries map
one-to-one, without remainder, onto lyrics 019–023. The 1989 witness prints the
same song again under a *third* title — section 39, லீலா… — its own
opening word. Three printings, three different incipits, one song.

**Song 043 — மக்கள் ஆணையிட்டால்.** The 2024 p. 102 Kalaignar entry
உங்கள் ஓட்டு கதிரவனுக்கா, is the quoted refrain opening the
lyric on PDF 103. The 1989 witness prints the same song as section 12,
ஆற அமரக் கொஞ்சம்…, without that refrain.

Both are recorded as `list_to_lyric_match: "internal-line"`. Printed title
variants are recorded as source variants and never used to correct either form.

## 13. What this gate did not do

- No authorship was inferred from theme, vocabulary, Dravidian ideological
  content, poetic style, known phrases, chronology, film memory or soundtrack
  memory.
- No external web source, encyclopaedia, blog, video description, social post or
  lyrics site was used. **No external research was needed:** the repository and
  the two scans were sufficient.
- No date, venue, occasion, printed page number, song boundary, authorship or
  rights status was supplied that the sources do not print.
- OCR was not used as textual authority.
- The register makes **no rights or licensing determination**.
- Neither scan was modified, and no song text, translation, edition, payload or
  archival status field was changed. **All 54 records remain
  `anthology-attributed`;** the register sits alongside that field and does not
  promote, downgrade or replace it. The validator fails if that field moves.
- No new numbered song record was created. The 1989 witness adds evidence, not
  songs.

## 14. Validator

`authorship/validate.py` is fail-closed: exit **0** success, **1**
data-integrity failure, **2** cannot validate. It enforces rather than trusts:

- exactly 54 records, songs 001–054 once each, ascending;
- every record's id, film, lyric title and lyric pages agree with `songs/index.json`;
- every record has a non-empty `evidence_items` array, and every item carries all
  twelve provenance fields, a known scope, level and effect, and an auditable basis;
- every record cites the 2024 source, and every record cites the 1989 witness —
  as presence or as explicit absence;
- `witness_1989_sections` equals the mapping re-parsed from the committed
  `songs/SOURCE_WITNESS_0065773_DEDUP.md`;
- any item qualifying for inclusion is `song-specific` and records the printed
  attribution it rests on, so **D-only evidence cannot produce inclusion**;
- any `supports-other` item names the other writer;
- **decision, material conflict and inclusion are recomputed from the items** and
  must match the stored values — a record cannot be included while `unresolved`,
  `insufficient-evidence`, or in declared conflict;
- withheld records' prose may not read as a finding of non-authorship;
- the register pins the controlling-scan SHA-256 recorded in both
  `songs/index.json` and `metadata.yaml`, and every witness SHA-256 is well formed;
- `songs/index.json` still carries `anthology-attributed` for all 54;
- every declared count matches the records;
- `authorship/public-inclusion.json` is the **byte-exact** derivation of the
  register, including the register's own SHA-256 and the source-main SHA.

`python3 authorship/validate.py` verifies; `--write` regenerates the manifest
and is byte-stable across runs. The manifest is generated — change the register
and regenerate, never hand-edit it.

## 15. Manifest provenance

`authorship/public-inclusion.json` pins:

- `controlling_source_sha256` — the 2024 scan;
- `witness_sha256` — every witness, including the 1989 volume;
- `evidence_register_sha256` — the SHA-256 of the exact bytes of
  `authorship/inclusion-evidence.json`, so a manifest cannot silently outlive the
  register it was derived from;
- `source_main_sha` — `84bc974c76326fafc7224d7209a2c704e214d92c`, the source-repository
  `main` this branch was cut from and against which the gate was adjudicated.

The register does **not** contain its own hash; that would be circular. The
validator computes the hash from the file and requires the manifest to match.

## 16. Status of this record

The evidence gate is complete for all 54 numbered songs across both known
witnesses. The proposed public inclusion set of **48** songs is a **proposal for
independent review**; it has not been applied to any downstream edition,
payload or Reading Room surface, and this work performs no such application.

If a further witness is admitted later — a contemporary songbook, a film-era
credit, a gramophone label — it enters as additional evidence items and the
decisions are recomputed. The six `unresolved` songs are the ones such a witness
would most likely settle.
