# அம்மையப்பன் — English batch review: scenes 36–40

**Batch:** archival scenes `ammaiyappan-s036`–`ammaiyappan-s040`  
**Status:** **verified**  
**Source basis:** frozen 105/105 verified Tamil + 63/63 verified scene derivatives + closed dialogue/source-role/character/song evidence

## Batch result

Archival scenes **36–40** are translated and source-reconciled without changing canonical Tamil, scene text, dialogue evidence, character/entity evidence or the closed song/performance inventory.

- scenes verified: **5/5**
- translation units: **90/90 verified**
- dialogue-kind units: **80**
  - immutable explicit dialogue records linked: **80/80**
  - source-role supplement records linked: **0**
- stage/action units: **9**
- japa units: **1** — scene 40 source-visible `ammaiyappan-song-004` cue
- song-reference / literary-verse / written-text units: **0**
- cross-page units: **1** — `ammaiyappan-en-s037-u003`
- retained source-visible song/performance occurrences encountered: **1/1** — `ammaiyappan-song-004`
- duplicate source-span ownership introduced: **0**
- source-visible structural stars translated as prose: **0**

## Scene reconciliation

| Scene | Explicit dialogue links | Source-role supplements | Stage/action | Japa | Total units | Result |
|---|---:|---:|---:|---:|---:|---|
| 36 | 23 | 0 | 5 | 0 | 28 | PASS |
| 37 | 16 | 0 | 0 | 0 | 16 | PASS |
| 38 | 8 | 0 | 1 | 0 | 9 | PASS |
| 39 | 16 | 0 | 2 | 0 | 18 | PASS |
| 40 | 17 | 0 | 1 | 1 | 19 | PASS |
| **Total** | **80** | **0** | **9** | **1** | **90** | **PASS** |

## Source-role provenance

Direct inspection of the closed `dialogues/source-role-resolved-records.json` shows **no source-role supplement in archival scenes 36–40**. The closed sequence moves from `ammaiyappan-s035-r001` to `ammaiyappan-s050-r001`; therefore every spoken unit in this batch is either one of the 80 immutable explicit dialogue records or, in scene 40, the separately source-visible japa cue.

No printed speaker label is invented, expanded or normalized.

## Cross-page continuity

Exactly one immutable dialogue record crosses a page boundary in this batch:

- scene 37 `ammaiyappan-s037-d003` → English `ammaiyappan-en-s037-u003`: PDF **80 → 81** / printed **78 → 79**.

It remains one logical English unit with `english_page_segments`; no page-boundary duplication is introduced.

## Scene 36 — mistaken abduction, proclamation and disguised household

The scene preserves the rapid change from Velazhagan's mistaken capture of the woman-disguised Sukhadev to the public proclamation and the disguised Muthan–Muthayi couple seeking work.

- Five source-bounded actions remain stage/action units; the source `* * *` separator is structural and is not translated as prose.
- Exact source label `தன` is preserved wherever printed. The closed record-aware character layer may distinguish Thanapathi from the merchant, but English metadata does not rewrite the label.
- The merchant's baby-talk record `ammaiyappan-s036-d008` retains its embedded `[குழந்தை அழுகிறது.]` action inside the immutable dialogue unit.
- The source-visible `ஆராரோ...` vocable in that same record remains there. The closed song/performance inventory does **not** retain it as a separate occurrence, so no song unit, title, lyric body or authorship claim is manufactured.
- Frozen spacing/wording around `வாழைக்குல ைமாதிரி` is handled conservatively and not repaired upstream.
- The disguise names `பொன்னி` / `பொன்னன்` remain source-visible role-play names rather than new character aliases.

## Scene 37 — cross-page extortion exchange

Vedalam's reward/extortion exchange with Tirisangu preserves the source's comic turns around love-song/plight, funeral-pyre inheritance and the Palayakkarar relationship.

`ammaiyappan-s037-d003` stays whole across PDF 80→81. Exact shortened labels `வேதா` / `திரி` remain source metadata. The source phrase `பொல்லாம் கட்டப்பட்டு` is interpreted only from immediate context and is not silently normalized in Tamil.

## Scene 38 — embedded actions and predatory food-chain rhetoric

The source-owned servant arrival inside `ammaiyappan-s038-d003` and Baladevar's return inside `ammaiyappan-s038-d007` remain inside those immutable dialogue records; only the separate `(பலதேவர் போகிறார்)` cue becomes its own stage unit.

Vedalam's chain — fly → spider → lizard → cat → `குறவன்` → Yama — is translated without sanitizing or replacing the source social/community label. `குறவன்` is retained as **Kuravan** in English notes/register, and the culminating ambition to become Pazhuthar Palayakkarar remains intact.

## Scene 39 — liberation rhetoric and private family turn

The opening political discussion preserves the source's liberation/independence rhetoric, exact friend labels including `தோழ 2`, and the transition into Muthan and Muthayi's private exchange.

- `புறநானூறு` is a rhetorical literary reference only; no external poem or passage is imported.
- Muthayi's `இன்னும் எட்டு, ஒன்பது மாதங்கள் பொறுத்திருங்கள்...` is translated directly. English does not add explanatory pregnancy prose beyond what the source itself says.

## Scene 40 — source-only japa occurrence

The closed song/performance inventory identifies exactly one retained occurrence in this batch:

`ammaiyappan-song-004` — **japa-performance-cue**, PDF 84 / printed 82, performer source-visible as Sukhadev, authorship status `not-applicable-character-japa`.

The source has two distinct printed spans tied to that occurrence, and English preserves both without duplicating one span:

1. `ammaiyappan-en-s040-u001` (`kind: japa`) owns only the opening stage cue that Sukhadev is in **nishta** performing `முத்தாயி` japa when Vedalam enters in ascetic disguise;
2. `ammaiyappan-en-s040-u004` remains the immutable explicit dialogue record `ammaiyappan-s040-d002`, translating only the separately printed spoken token `முத்தாயி...முத்தாயி...` and linking the same occurrence ID.

This is one **unique occurrence** represented across its two distinct source spans, not duplicate source ownership. It is not a soundtrack song; no title, lyric body or lyricist is inferred.

Vedalam's goddess-name invocation remains dialogue-owned. Frozen/uncertain forms such as `சுக வார்த்தியினைக்`, `இஞ்ஞானி`, `தன் பயனை`, `தச்சு...தச்சு...` and `செய்யவேண்டிய அகமெல்லாம்` are handled by bounded transliteration/contextual notes rather than upstream Tamil repair. Viswamitra–Menaka and Murugan–Valli–Narada references are translated only to the extent printed.

## Integrity result

**PASS.** All **80** eligible explicit dialogue records in scenes 36–40 are linked exactly once; the closed source-role layer contributes **0** supplements; all nine separate stage/action spans are owned once; the one cross-page dialogue stays whole; `ammaiyappan-song-004` is represented only from its source-visible japa cue and labelled spoken token; no frozen Tamil/dialogue/character/song file was modified.

**Next batch:** archival scenes **41–45**. The closed source-role layer has no supplement in that range, and the closed song/performance inventory has no retained occurrence there. Reconfirm live `main` before writing, preserve exact speaker/page provenance, and keep frozen source evidence unchanged.