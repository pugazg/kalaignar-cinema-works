# வண்டிக்காரன் மகன் — dialogue source review

Status: **PASS / CLOSED / LATE RECONCILIATION APPLIED**

This note records the source-sensitive adjudications that were required between dialogue preflight and immutable record generation. The controlling authority remains the rendered image-only scan `TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf`; no PDF binary is committed.

## Non-colon anomaly review

All **16/16** preflight non-colon candidates were checked against the controlling scan and retained as non-dialogue source text. They occur on PDF **18, 36, 46–47, 60 and 73** and are punctuation/verse/performance fragments, not explicit speaker labels. **Promoted to dialogue: 0.**

## Cross-page review

All **3/3** candidate cross-page labelled utterances were checked as continuous source turns and remain one immutable dialogue record each:

- `vandikkaran-magan-s035-d006` — source scene `25`, `சடையன்`, PDF **48→49**;
- `vandikkaran-magan-s055-d004` — source scene `42-எ`, `சடையன்`, PDF **68→69**;
- `vandikkaran-magan-s070-d005` — source scene `54`, `விங்கன்`, PDF **85→86**.

Each record preserves both PDF/printed-page provenance entries and `page_segments`; no repeated speaker label was invented at the page break.

## Unlabelled-source rule

The preflight inventoried **148** unlabelled ordinary blocks. They were reviewed under the source rule rather than assigned inferred identities: **source-unlabelled blocks assigned a speaker = 0**. Stage directions, source captions, songs/performance matter, written/narrative matter and unlabelled speech remain outside immutable dialogue starts unless an explicit source speaker label exists.

## Closure

A later structural-collision audit reopened this gate on direct canonical evidence: 31 explicit-label lines had been hidden from the legacy parser by line-ending parenthetical syntax. **29** are spoken utterances and were restored with append-only IDs; **2** are source-labelled action-only lines and remain outside dialogue. The reconciled immutable dialogue layer therefore contains **773 records / 38 exact labels**, with **15** legitimate zero-dialogue scenes, **3** multi-page records, **0** duplicate dialogue IDs and **0** speaker-label normalizations. All original **744/744 IDs** remain unchanged. See `dialogue-index-qa.json` and `../dialogues/index.json`.
