# Raja Rani English Translation — Batch 024–034 Review

## Scope

- Work: `raja-rani`
- User-requested batch size: **10 eligible verified scenes per iteration**.
- Scenes translated in this batch: `raja-rani-s024` through `raja-rani-s032`, then `raja-rani-s034`.
- `raja-rani-s033` remains excluded because it intersects review-limited PDF 48; no hidden or insecure Tamil was reconstructed.
- Source span represented: verified portions of PDF 40–46 and PDF 49–52.
- Translation authority: verified scene derivatives plus immutable dialogue shards.

## Batch counts

| Scene | Verified units | Immutable dialogue links | Source-unlabelled spoken | Stage directions |
|---|---:|---:|---:|---:|
| s024 | 34 | 32 | 0 | 2 |
| s025 | 38 | 33 | 0 | 5 |
| s026 | 3 | 1 | 0 | 2 |
| s027 | 1 | 0 | 0 | 1 |
| s028 | 70 | 64 | 1 | 5 |
| s029 | 1 | 0 | 0 | 1 |
| s030 | 1 | 0 | 0 | 1 |
| s031 | 6 | 3 | 0 | 3 |
| s032 | 1 | 0 | 0 | 1 |
| s034 | 77 | 65 | 2 | 10 |
| **Batch total** | **232** | **198** | **3** | **31** |

Dialogue-kind units total **201**: 198 immutable dialogue links plus three source-unlabelled spoken units. There are no new performance-cue, song, written-text or cross-page translation units in this batch.

## Source-fidelity decisions

### Scene 024 — `அகல்யா` rehearsal

The embedded-drama speaker labels are retained exactly (`இந்திரன்`, `இந்தி`, `அகல்யா`, `அகல்`, `முனிவர்`, `முனி`, etc.) rather than normalized to character names. The source quotes only the fragment `தேவரனையர் கயவர்`; English does not supply the rest of the Kural. The unusual `உன் சொத்தைக் காரணத்தை` phrase and the incomplete curse after `உன் உடம்பெல்லாம்` are rendered conservatively without using English fluency to repair Tamil.

### Scene 025

The comic English-derived `மென்ஷன்...நோமென்ஷன்` is retained as source texture. The odd source form `உடி புடாதே` remains unchanged upstream; English renders only the immediate action sense. Samarasam's repeated peace-versus-killing contradiction is preserved as comedy rather than harmonized.

### Scene 028

The source-unlabelled `இந்தா! அது வச்சு இருந்தேனே. அது எங்கே?` is a dialogue-kind unit with null `speaker_label` and null `source_record_id`; contextual ownership is not promoted into metadata. The `கண்ணு` cattle/eye misunderstanding is translated with a limited `kannu` retention and explanatory notes. Source-exact irregular forms such as `கொலைக்கும்`, `ஆதி`, and `அவ கிவன்னு` are not used as grounds for Tamil normalization.

### Scene 031

The source has only three labelled utterances amid stage-level chaos. The fight and the final river escape remain separate stage directions. No additional crowd dialogue is invented.

### Scene 034

Two source-unlabelled spoken spans remain deliberately unlabelled:

- `மெள்ள, மெள்ள, அந்தக் கையை பிடி...`
- `ஆ...பூச்சி, பூச்சி...`

Inline actions inside immutable dialogue records remain inside those linked units (`முகத்தில் ஊற்றிக் கொள்கிறான்`, `[தலைமுடியைக் காட்டுகிறான்.]`). Most importantly, corrected record `raja-rani-s034-d060` retains exact source speaker label **`ராணி`** in English metadata; it is not reassigned from contextual expectation.

## Integrity result — PASS

- expected immutable dialogue records in the 10 translated scenes: **198**;
- linked immutable dialogue records: **198/198**;
- source-unlabelled spoken units: **3**;
- stage-direction units: **31**;
- new cross-page units: **0**;
- invented speakers: **0**;
- blocked review-source scenes translated: **0**;
- canonical Tamil / dialogue / character / song layers modified by translation: **no**.

## Cumulative translation status

After this batch:

- verified eligible scenes translated: **30 / 50**;
- verified translation units: **715**;
- immutable dialogue records linked: **622 / 622 expected in translated scenes**;
- source-unlabelled spoken units: **11**;
- cross-page translation units: **6**;
- translated screenplay song/performance occurrences: **2**;
- unit-kind totals:
  - dialogue: **633**;
  - stage-direction: **78**;
  - performance-cue: **2**;
  - written-text: **2**;
  - song / song-reference / chant: **0**.

## Next 10-scene iteration

Continue with the next **10 eligible verified scenes**, skipping blocked `s039`:

`raja-rani-s035`, `s036`, `s037`, `s038`, `s040`, `s041`, `s042`, `s043`, `s044`, `s045`.

Use the same source-linked rules. Do not translate blocked review-source scene `s039`, invent speakers, supply absent lyrics, or normalize exact Tamil labels.