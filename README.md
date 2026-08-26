# Kalaignar Cinema Works

A source-led archive of screenplay, dialogue, song, and related cinema writing credited to **Kalaignar M. Karunanidhi**.

The repository preserves source provenance, canonical transcription and derivative representations separately.

## Archival principles

1. **Primary source first.** The scanned publication controls canonical transcription.
2. **No silent correction.** Source anomalies stay documented.
3. **Page provenance is mandatory.** Transcribed, indexed and translated units remain traceable to PDF/printed pages.
4. **Uncertainty stays visible.** Interpretive pressure points are reviewed rather than guessed away.
5. **Source and derivatives are separate.** English translation never overwrites Tamil.
6. **Authorship is not inferred.** Mixed-credit material requires item-level evidence.
7. **Rights are not assumed.** No repository-wide public-domain/open-license claim is made.

## Reusable onboarding for new cinema works

For every newly supplied Kalaignar cinema source, use these project-level documents before work begins:

- `docs/CINEMA_WORKS_PROCESSING_GUIDE.md` — the detailed mature workflow from source intake through Reading Room integration;
- `docs/SONG_ANTHOLOGY_PROCESSING_GUIDE.md` — additional rules for compiled film-song/lyric anthologies;
- `docs/SONG_TRANSLATION_GUIDE.md` — source-faithful English rules for retaining Kalaignar's language in song translation;
- `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md` — project-level handover, reference implementations and lessons learned;
- `docs/START_NEW_CINEMA_WORK_PROMPT.md` — copy-paste prompt for starting a new work safely;
- `docs/ARCHIVAL_WORKFLOW.md`, `docs/SOURCE_POLICY.md`, and `docs/TRANSCRIPTION_GUIDE.md` — baseline source/transcription rules.

The preferred public reading destination for completed works is the **Kalaignar Digital Library / Reading Room at `https://nenjukkuneethi.org/read`**. Cinema works should normally be presented there by **scene**, using verified structured repository data. Standalone publication packages are secondary and should be created only when explicitly requested or independently useful. A source that is not actually scene-structured, such as a film story/song booklet, should retain its natural source structure rather than being forced into screenplay scenes.

## ராஜா ராணி status

The source `TVA_BOK_0017188_ராஜா_ராணி.pdf` is archived under `works/raja-rani/` and has completed source intake, structural mapping, canonical Tamil first pass, the full rendered-scan fidelity audit, source-supported scene segmentation, every scene-text derivative currently eligible from verified Tamil, the complete eligible immutable dialogue layer, the complete verified character/entity derivative, and the source-visible song/performance authorship gate. The source-linked English translation layer is now **pilot-verified**.

- title leaf: **`ராஜா ராணி`**;
- cover form: **`ராஜாராணி`**;
- cover directly prints **`மு. கருணாநிதி`**, but no role label is printed beside that name;
- scan: **80 PDF pages**;
- source SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`;
- canonical screenplay/dialogue: PDF **10–79 / printed pp.9–78 — 70 pages**;
- source-numbered screenplay scenes: **none**;
- rendered-scan audit: **79/79 canonical source pages inspected**;
- verified/review source pages: **75 / 4**;
- verified/review screenplay pages: **66 / 4**;
- review pages: **PDF 27, 48, 57, 74**;
- PDF 74 remains review because a later `K. N. சங்கரன்` ownership/address overprint physically obscures original source text; hidden wording is not reconstructed;
- archival scene segmentation: **58 source-supported navigation segments**;
- verified scene-text eligibility: **50 segments**;
- verified scene-text derivatives: **50/50 eligible complete**;
- blocked scene segments: **8** — `s011`, `s012`, `s013`, `s033`, `s039`, `s053`, `s054`, `s055`;
- dialogue index: **complete for verified eligible scenes — 892 immutable records / 50 of 50 eligible scenes processed**;
- dialogue zero-record scenes: **`s008`, `s010`, `s014`, `s019`, `s020`, `s022`, `s027`, `s029`, `s030`, `s032`, `s037`, `s038`, `s042`, `s043`, `s048`**;
- dialogue cross-page records / tracked non-colon source-label delimiter anomalies: **11 / 3**;
- character exact-label inventory: **74/74 exact non-empty `speaker_label` strings inventoried**;
- character/entity index: **complete-verified — 74/74 labels dispositioned into 42 verified entities / role categories / collectives; 0 review / 0 unresolved**;
- numbered source songs: **11 `பாட்டு` blocks; 11/11 complete-verified Tamil song derivatives**;
- screenplay singing references: **4**;
- total song/singing occurrences inventoried: **15**;
- numbered-song authorship: **5 later-anthology Kalaignar attributions / 6 unresolved / 0 original-booklet item-level lyricist credits**;
- English translation: **pilot-verified — scene 1 / 50 eligible verified scenes**;
- English pilot units: **11 verified — 9 dialogue / 2 stage direction**;
- English pilot immutable dialogue links: **9/9 exactly once**.

The archive IDs `raja-rani-s001`–`raja-rani-s058` are navigation-only and are not presented as source scene numbers. Both the scene-text and dialogue phases deliberately remain complete **with review exclusions** rather than reconstructing uncertain or physically obscured text.

Dialogue Batches 001–006 cover every eligible verified scene range: `s001`–`s010`, `s014`–`s032`, `s034`–`s038`, `s040`–`s052`, and `s056`–`s058`. Only explicitly speaker-labelled utterances become immutable records; source-unlabelled material, written matter, performance cues and final printer matter remain outside the dialogue inventory. Exact source-visible speaker-label variation and delimiter irregularities remain unnormalized in this layer.

Character normalization is downstream only. Non-obvious mappings were resolved from verified context rather than spelling: scene 45 establishes `ரா` as **Rani**, not Raja; scene 52 explicitly introduces **Geetha's mother / Thayammal** before `தாய்:`; and scene 57 explicitly introduces **Sangaran** before `சங்:`. Context-reused `வேலை` remains a worker/servant role category rather than being forced into one physical person. Embedded `சேரன் செங்குட்டுவன்`, `அகல்யா`, and `சாக்ரடீஸ்` dramatic identities remain distinct from outer-film identities. No dialogue record was rewritten by character mapping.

The song gate keeps the PDF-9 six-name `பாடல்கள்:` roster film-wide rather than forcing it onto individual songs. The later verified `கலைஞர் திரை இசைப் பாடல்கள்` archive establishes item correspondence for numbered songs **3, 5, 6, 7 and 8**, which are recorded at **`anthology-attributed`** tier to `மு. கருணாநிதி`; songs **1, 2, 4, 9, 10 and 11** remain unresolved. Later-witness wording never overwrites this booklet: for example, Raja Rani song 8 retains `சீலா!...லாலீ!...அது போலீ!...` despite a different opening in the later anthology.

The screenplay singing cues are separately retained: scene 4 securely links to song 3, scene 16 to song 5, and scene 40 to song 8. Scene 58's `(இருவரும் பாடுகிறார்கள்)` has only a review-level contextual link to song 11 because no title or lyric is printed at the cue. During this gate the already verified PDF-30 separator and Rani singing stage direction were restored to `scene-016.md`; canonical Tamil, fidelity totals and immutable dialogue records did not change.

The English pilot is `raja-rani-s001` / PDF 10 / printed p.9. Its **11 verified units** link all **9/9** immutable dialogue records exactly once and preserve both source-visible stage directions. Exact `டாக்டர்` / `டாக்` speaker labels remain metadata rather than being normalized. The pilot retains `Amma` / `amma` and `Appa` where literal English would over-specify kinship/register, and preserves the broken `அப்படின்னு... அவங்கண்...?` as `Then... his eyes...?` rather than silently completing the source. No Tamil or completed source derivative was changed by translation.

**Next:** translate verified **`raja-rani-s002`–`raja-rani-s005`** in source order using the pilot rules. Preserve immutable dialogue links and source-visible stage/performance material, keep source-unlabelled speech unlabelled, and do not invent absent lyrics, scene endings or unresolved song authorship.

## மந்திரி குமாரி status

The source `TVA_BOK_0026144_மந்திரி_குமாரி.pdf` has completed source intake and whole-scan structural mapping under `works/manthiri-kumari/`.

- source classification: **film story-and-song booklet**, not a full screenplay/dialogue book;
- cover title: **`மந்திரி குமாரி`** under `மாடர்ன் தியேட்டர்ஸ்`;
- direct printed Kalaignar credit: **`கதை, வசனம் : மு. கருணாநிதி`**;
- scan: **14 PDF pages**, **579,782 bytes**;
- source SHA-256: `a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee`;
- PDF 2: cast/music/production credits;
- PDF 3–5: **`"மந்திரி குமாரி"—கதைச்சுருக்கம்`**;
- PDF 6–13: **`மந்திரி குமாரி—பாடல்கள்`**, **15** separately headed song/performance blocks;
- PDF 14: unrelated **`அமரகவி`** back-cover advertisement / paratext;
- source scene-numbering system: **none**;
- canonical Tamil first pass: **not-started**;
- visual fidelity audit: **not-started**;
- credits/story/song derivatives: **blocked until verified Tamil**;
- scene/dialogue derivatives: **not applicable as a full-work model from this source**.

The booklet's story/dialogue credit is primary-source evidence for that authorship role but is **not** automatically item-level lyric authorship. After this source is independently transcribed and visually verified, its song/performance material can be compared against the existing later `கலைஞர் திரை இசைப் பாடல்கள்` corpus without creating duplicate song records.

**Next:** canonical Tamil first-pass transcription of PDF 2–13 in source order with stable page anchors, followed by a separate full visual fidelity audit before structured derivatives.

## கலைஞர் திரை இசைப் பாடல்கள் status

The dedicated film-song anthology work under `works/kalaignar-thirai-isai-paadalgal/` is being processed from the supplied source `TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`.

- printed title: **`கலைஞர் திரை இசைப் பாடல்கள்`**;
- compiler: **`நெல்லை ஜெயந்தா`**;
- First Edition: **June 2024**;
- publisher: **தமிழ்நாடு இயல் இசை நாடக மன்றம்**;
- ISBN: **978-81-961205-2-8**;
- physical source binary: **194 PDF pages**, 130,427,193 bytes;
- source SHA-256: `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- printed colophon statement: **`No of pages : 192`**;
- structural mapping: **verified**;
- full PDF song-page scan: **complete — 62 song-bearing / 132 ignored pages**;
- numbered Tamil lyric corpus: PDF **24–130**;
- film sections: **23/23 mapped**;
- numbered songs: **54/54 inventoried (`001–054`)**;
- Tamil song transcription: **54/54 complete-verified**;
- Tamil fidelity audit: **complete — 0 draft / 0 review / 0 unresolved Tamil readings**;
- default attribution status: **`anthology-attributed`** — this 2024 anthology's attribution is not silently promoted to original-film primary-source verification;
- English translation: **54/54 complete-verified**;
- English pilot-verified: **3 (`001–003`)**;
- English verified: **51 (`004–054`)**;
- English draft/review/not-started: **0/0/0**;
- English mode: **`semantic-poetic-source-faithful`**, retaining Kalaignar's language rather than producing a singable rewrite;
- final English review: `works/kalaignar-thirai-isai-paadalgal/translations/BATCH_047_054_REVIEW.md`;
- English reader/export: **complete-verified, QA PASS** — 54/54 songs, 1,105/1,105 English lines-cues, 8 cross-page records, deterministic Markdown/HTML/JSON + manifest;

The PDF-specific workflow processes only actual numbered lyric pages or their direct continuations. All **54** numbered Tamil song files are visually verified. Cross-page verified records are `009`, `019`, `023`, `024`, `036`, `037`, `051`, and `052`. No missing lyric was imported from soundtrack memory, websites or alternate editions.

The complete English corpus follows the same source discipline. Across all 54 songs it preserves Kalaignar's political and social rhetoric, repetition, concrete image chains, colloquial and folk speech, Tamil cultural vocabulary, performance terminology and difficult verified source forms instead of smoothing them into generic lyric English.

The final `047–054` batch preserves **sons of the soil** and `naam / naan` wordplay; `kalaignan` and `udanpirappe`; mother-warrior grief/pride; `mullai / bhava / jathi / veena`; the two-page colloquial `machaan` duet with `saivam / asaivam` wordplay and anti-subordination language; the two-page family song with Kannagi and Classical-Tamil imagery; the deliberately segmented performance-poem form of `053`; and `aanpaal / paayiram / water upon red earth` in `054`. Full two-page provenance is retained for `051` (PDF 121–122) and `052` (PDF 123–124).

Difficult verified Tamil forms remain documented rather than silently repaired through English. No verified Tamil song file was changed by the English translation layer.

The anthology's `மந்திரிகுமாரி` editorial note also mentions the censored/prohibited `ஆளப்பிறந்தவன் தமிழன் அவன்தானே`. Because its lyric is not printed as a numbered item, it remains an editorial note and is not inserted into the `001–054` corpus.

**Next:** repository-internal anthology work is complete; downstream Kalaignar Digital Library / Reading Room integration may proceed from the verified reader/export package.

## மனோகரா status

The source `TVA_BOK_0010102_மனோகரா.pdf` has completed source intake, structural mapping, canonical Tamil verification, visual fidelity audit, scene derivation, immutable dialogue indexing, character/entity disposition, the song/performance authorship gate, and the complete source-linked English translation.

- source title: **`மனோகரா`**;
- printed credit: **`திரைக்கதை வசனம்` / `மு. கருணாநிதி`**;
- explicit edition statement: **`முதற்பதிப்பு : பிப்ரவரி 1954.`**;
- scan: **90 PDF pages**;
- source SHA-256: `87518fd8c290d7880aa2ddd9f2b5999c9d421d48fe1f02d61cf8e254393236a9`;
- main screenplay/dialogue: PDF **7–88 / logical printed pp.6–87** — **82 canonical pages**;
- source-numbered scene headings: **none printed**;
- canonical Tamil: **82/82 pages complete-verified**;
- visual fidelity audit: **complete — 82/82 pages, 0 unresolved source readings**;
- archival scene index / scene-text derivatives: **57/57 complete-verified**;
- dialogue index: **57/57 scenes, 983 immutable labelled-dialogue records, complete-verified**;
- dialogue cross-page records / label anomalies: **13 / 8**;
- sole zero-record dialogue scene: **`manohara-s024`**;
- character/entity index: **complete-verified — 111/111 labels dispositioned into 37 entities/role categories; `வர்மா` remains the sole unresolved label**;
- song/performance inventory: **6 source-visible occurrences; 1 verified / 1 review / 4 unresolved authorship**;
- verified song authorship: **`பொழுது புலர்ந்தது` — சுரபி**;
- Tamil song lyric derivative files: **0 — no complete lyric body is printed in this booklet**;
- English translation: **complete-verified — 57/57 archival scenes, 1,190/1,190 verified source-linked units**;
- English unit mix: **1,009 dialogue-kind / 173 stage direction / 6 song-reference / 1 chant / 1 written-text**;
- immutable dialogue links in English: **983/983 exactly once**;
- direct source-unlabelled spoken English units: **27**;
- genuine cross-page English units: **17**;
- translated source-visible song/performance occurrences: **6/6**.

The final requested English pass covered **`manohara-s046`–`manohara-s057`** and was checked directly against PDF **71–88 / logical printed pp.70–87**. It adds **267 verified units** and links all **216/216** immutable labelled dialogue records in those twelve scenes.

The finale remains source-shaped rather than compressed. Scene 48 preserves the exposure/arrest rhetoric and two new physical page crossings. Scenes 50–52 preserve source-empty speaker fields without inference, including the `thambi` vocative and `death-abhishekam`; scene 52 remains one utterance across PDF 79→80. Scene 54 keeps the hen/hawk motherhood image and `living portrait`. Scene 55 retains the complete Padmavathi/Manoharan rhetorical climax—including **Tamil Mother**, tears-versus-sword, motherland/Chola Mother, victory-garland, blood-tilak, slavery-fetters and repeated dust invocation—with four genuine page crossings through PDF 83→87. `சந்து புனை சிந்து பாடும்` remains conservatively `compose sandhu and sing sindhu`, Vasanthan's dying `தம்பி` remains `thambi`, and Kesari's `little... by little` threat is not softened.

Scene 56 leaves all four colon-only continuations null-speaker. Scene 57 preserves the unlabelled `பத்மா! என் இதயராணி...` continuation inside the king's preceding immutable record and closes with `கடமை, கண்ணியம், கட்டுப்பாடு` as **Duty, dignity, discipline**.

No canonical Tamil, scene, dialogue, character or song-inventory record was changed by the English translation.

The **Manohara English reader/export preflight now passes** across all 57 scene records and 1,190 verified units: 983/983 immutable dialogue links exactly once, 27 null-speaker spoken units, 17 cross-page units and all 6 song/performance links, with zero missing/extra/duplicate dialogue links, synthetic scene-end units, direct structural-star units, page-order regressions, unit-ID errors or provenance/scene-metadata errors.

The deterministic **Manohara English reader/export package now passes generated-output QA**: Markdown, standalone HTML and machine-readable JSON each contain all 1,190 verified units exactly once, with an integrity manifest recording reproducible input/output hashes. No canonical Tamil or structured source derivative was changed.

**Next:** integrate the verified Manohara English reader into the Kalaignar Digital Library / Reading Room, preserving the 57 scene IDs strictly as archival navigation rather than source numbering.

## Parasakthi status

The canonical Tamil covers PDF **4–57 / printed pp.3–56** and is fully verified at **54/54 pages**. PDF 58 is back matter.

Completed source/Tamil derivatives:

- scene layer: **46/46**;
- dialogue index: **642 records, complete-verified**;
- character index: **69/69 source labels disposed**;
- song/verse occurrences: **14**;
- song authorship: **14/14 verified**;
- Tamil soundtrack files: **11/11 complete-verified**;
- separate quoted verse: **1**.

The source-linked English translation is **complete-verified for all 46 observed canonical scenes**: scenes **1–22, 24–33 and 35–48**. Canonical scenes **23 and 34 are absent** and correctly have no translation records.

Final English totals are **769/769 verified units**: **641 dialogue / 114 stage direction / 13 song / 1 quoted verse**. A whole-work reader QA now also passes across all 769 units: **634 immutable dialogue-record links**, **14 song/verse occurrence links**, **16 cross-page units**, and **97 distinct source paths** were checked. Source-unlabelled dialogue/performance remains unlabelled rather than receiving invented speaker metadata.

Publication-facing, provenance-safe English derivatives are generated under `works/parasakthi/editions/en/` as Markdown, standalone HTML and machine-readable JSON, with a generated QA report and deterministic integrity manifest. The active GitHub Actions workflow reruns the QA/build when its authoritative inputs change.

No canonical Tamil, scene, dialogue, character, song or transcription derivative was modified by the English translation or reader-export work.

**Next:** no required Parasakthi English translation or QA/export activity remains. For public access, future downstream work should prioritize integration into `https://nenjukkuneethi.org/read`; standalone packaging should be done only when separately requested or useful.

## திரும்பிப்பார்! status

The second screenplay is archived from `TVA_BOK_0014652_திரும்பிப்பார்.pdf`.

- explicit source edition statement: **`முதல் பதிப்பு: 1953`**;
- scan: **112 PDF pages**;
- main screenplay: PDF **9–112 / printed pp.1–104**;
- scene-number pass: **93 scene starts, consecutively 1–93**;
- source intake: **complete**;
- structural mapping: **verified**;
- scene-heading / structural-label audit: **93/93 dispositioned**;
- canonical Tamil: **104 verified / 0 draft / 0 review**;
- fidelity audit: **complete**;
- scene index / scene-text derivatives: **93/93 complete**;
- dialogue index: **1,040 records across 93 scene shards, complete**;
- character index: **45/45 exact speaker labels dispositioned into 39 verified entities/role categories**;
- song/performance inventory: **8 source-visible occurrences dispositioned**;
- song authorship mapping: **3 verified occurrences / 5 unresolved occurrences**;
- source-named songs with verified item-level authorship: **`பாண்டியன் என் சொல்லை` — பாரதிதாசன்; `கலப்படம்` — கண்ணதாசன்**;
- Tamil song-lyric derivative files: **0**, because this booklet prints no complete lyric body for either source-named song;
- English translation: **complete-verified — scenes 1–93, 1,321 verified source-linked units**;
- English reader/export edition: **complete-verified — Markdown / HTML / JSON + QA report + integrity manifest**;
- English EPUB 3 package: **complete-verified — deterministic package QA PASS**.

Earlier audit work found and repaired a first-pass storage gap at PDF **61–63** and a missing explicit page anchor at PDF **80**; both are fidelity-verified. The final audit corrected the scene-72 structural label at PDF **87 / printed p.79** to the scan-visible `[தாசி வீடு`.

A later derivative-stage scan recheck also corrected scene 31 at PDF **38 / printed p.30** from the earlier transcription `பாண்டியன் என் செல்வம்` to the source-visible song title **`பாண்டியன் என் சொல்லை`**. The canonical Part 03 transcription and scene derivative were corrected from the scan, and the change is recorded in `works/tirumbippaar/notes/post-fidelity-corrections.md`.

The PDF-2 lower imprint remains a documented source crop. Reinspection supports only the visible partial `சிட்டி பிரஸ், மதுரை ரோ…`; the missing continuation is not reconstructed.

The song gate visually checked PDF **1–8** and found no lyricist/song-credit section. The cover `கதை - வசனம்` credit is not treated as song authorship. Item-level external music-catalog evidence is used only for the two exact source-named title matches; unnamed singing references and the scene-29 labour chant remain explicitly unresolved rather than being guessed onto other soundtrack rows.

The completed English derivative is stored under `works/tirumbippaar/translations/`. Final totals are **1,321/1,321 verified units: 1,047 dialogue / 254 stage direction / 7 song-reference / 2 chant / 11 written-text / 0 full-song units**. All **1,040 immutable labelled dialogue records** are linked exactly once; seven additional source-visible spoken units remain deliberately unlabelled in metadata.

The translation contains **12 genuine cross-page units** and preserves all six zero-dialogue source scenes (**10, 11, 25, 26, 43, 54**) through their source-visible narrative, performance or written material. Scene 31 links exactly to song occurrence `tirumbippaar-song-006`; scenes 42–43 preserve only source-visible `கலப்படம்` material, with absent lyrics remaining absent.

The publication-reader preflight performed a final derivative-only reconciliation. Residual synthetic `(Scene ends.)` units created solely from structural `★` separators were removed from scenes **21, 26, 27, 29, 30 and 34**; scene 29's `கோஷம்` heading and scene 30's location heading were restored to source order; and scene 47's three duplicated stage-action units were removed. Final diagnostics report **0 synthetic star-end units, 0 page-order regressions, 0 unit-ID errors, 0 missing dialogue links and 0 extra dialogue links**.

Scene 57 retains all **50** labelled dialogue records individually. Scene 90 retains the source direction `[மரணமூச்சுவிடும் பரந்தாமன்]`; scene 91 preserves `பத்திரிகை News` as written newspaper content; scene 93 preserves final `வணக்கம்.` and leaves the following `★` structural.

The provenance-safe reader/export layer under `works/tirumbippaar/editions/en/` passes whole-work QA across **93 scenes / 1,321 units / 1,040 immutable dialogue links / 12 cross-page units**. It generates `reader-edition.md`, standalone `reader-edition.html`, machine-readable `reader-edition.json`, `QA_REPORT.md` and `manifest.json`.

The same automated publication workflow now builds `tirumbippaar-en.epub` as a deterministic **EPUB 3** package. EPUB QA confirms **93 scene XHTML documents**, every one of the **1,321 verified unit IDs exactly once**, **99 ZIP members**, complete TOC/OPF/spine coverage, and first/uncompressed exact `mimetype`. The package is **370,615 bytes** with SHA-256 `17b9422cf2bf9cd30c90829a2dbd18115e20b8bd1cf7e5bb9da2cc0cdcc23c7f`; `EPUB_QA_REPORT.md` and `package-manifest.json` record the package checkpoint.

The active GitHub Actions workflow reruns reader preflight, whole-work reader QA, deterministic EPUB packaging and metadata synchronization when authoritative inputs change, and commits reproducible outputs only after all gates pass.

No canonical Tamil, scene, dialogue, character or song-inventory layer was changed by the English translation, final reader reconciliation, reader export or EPUB packaging.

**Next:** no required Tirumbippaar English translation, reader-export or EPUB-packaging activity remains. Its intended primary public destination is the scene-based Reading Room at `https://nenjukkuneethi.org/read`, using the verified Tamil/English structured data. Additional standalone packages are optional only when explicitly requested.

## Status vocabulary

`not-started` · `draft` · `draft-complete` · `review` · `verified` · `pilot-verified` · `complete-verified` · `unresolved`

Translation status is independent of source-transcription verification status.