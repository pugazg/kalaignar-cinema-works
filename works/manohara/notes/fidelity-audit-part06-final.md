# மனோகரா — Part 06 final fidelity record

Source: `TVA_BOK_0010102_மனோகரா.pdf`  
SHA-256: `87518fd8c290d7880aa2ddd9f2b5999c9d421d48fe1f02d61cf8e254393236a9`

This note records the final source-led disposition of Part 06, PDF **79–88** / printed pp. **78–87**.

## Initial visual audit

Batch 13 audited the complete ten-page range and recorded **63** scan-supported correction groups with **0 unresolved source readings**. The detailed initial ledger is `fidelity-audit-part06-batch13.md`.

## Controlled correction application

The exact pre-application Part 06 blob was:

`a8cf810464c4f574e4bb3e8e374be27267b96156`

The initial reviewed corrections were applied while all ten page anchors remained `draft`. The correction sequence was intentionally source-led and mechanically checked against expected Git blobs:

- first correction-application commit: `a70009a170aefbbf59e3e2b4dfa3a1cadce1da6f`;
- completion of the initially reviewed correction set: `5d2002de0852930453b89153afe68e70a8d54eab`;
- initial corrected-draft blob after that pass: `6edba1c8abec2b918ad0267550091454766268aa`.

## Post-application full visual recheck

The complete PDF **79–88** range was then reopened and compared again against the rendered scan, not merely against the correction ledger. That second full-range comparison found **five additional source-supported corrections** that the first audit had missed:

1. PDF 84 / printed p.83: `சுந்தர வாழ்வை குறையிட்டவளே` → `சுந்தர வாழ்வை சூறையிட்டவளே`.
2. PDF 87 / printed p.86: `பச்சிளங் குழந்தை—பட்டத்திளவரசன்!` → source hyphen form `பச்சிளங் குழந்தை - பட்டத்திளவரசன்!`.
3. PDF 87 / printed p.86: remove the inserted sentence break in `(மனோகரனின் பலத்தால் தூண் நொறுங்கி விழுகிறது அதற்குத் தாய்மைக் குரலும் உதவியாகிறது.)`.
4. PDF 87 / printed p.86: source punctuation is `[உக்ரசேனன் மனோகரனால் கொல்லப் படுகிறான், பாண்டியன் படையும் வருகிறது...` with a comma after `படுகிறான்`.
5. PDF 88 / printed p.87: restore the comma in `இறுதி மூச்சுவரையில், கொஞ்சம்...`.

The recheck also caught an application-level speaker-label issue in the already-recorded final-page correction: `பத்மா! என் இதயராணி. என்னை மன்னித்துவிடு.` is an **unlabelled continuation of the king's speech**, not a new `அரசர் :` label and not a `பத்மாவதி :` label.

Those recheck findings were applied in commit:

`2f5b88fba7329c53e53025e190fa2da2e0a78b4e`

The final corrected-draft Git blob was:

`fdd2a499784cfb6a9717d83955020be84aa9f5f5`

The full ten-page source comparison was repeated after those fixes. Result:

- additional correction required: **0**;
- unresolved source readings: **0**;
- post-application visual recheck: **passed**.

Part 06 therefore contains **68 final source-supported correction groups** in total: **63** from the initial audit plus **5** additional corrections found by the mandatory post-application full-range recheck.

## Verification promotion

All ten PDF 79–88 page anchors were promoted from `draft` to `verified` only after the final recheck passed.

Verification commit:

`0c491d98448c62300a76c5735a52416ca1204182`

Verified Part 06 blob:

`6b3f1fcae181b0cc22110540044b05a5c1505783`

## Final Part 06 result

- canonical range: **PDF 79–88 / printed pp.78–87**;
- pages: **10 verified / 0 review / 0 draft within Part 06**;
- final correction groups: **68**;
- unresolved source readings: **0**;
- post-application visual recheck: **passed**.

## Whole-work Tamil fidelity result

With Part 06 verified, the complete canonical screenplay/dialogue layer is now:

- **82/82 canonical pages verified**;
- verified range: **PDF 7–88 / logical printed pp.6–87**;
- draft pages: **0**;
- review pages: **0**;
- visual fidelity audit: **complete**;
- Parts 01–06: **complete-verified**.

No structured scene/dialogue/character/song/translation derivative should be treated as source-authoritative until it is generated from this verified Tamil layer under the repository workflow.
