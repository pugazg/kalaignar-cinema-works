# Ammayappan — unlabelled source-role review

Status: **COMPLETE — 20/20 blocks resolved**

The 1009 explicit colon-labelled dialogue records are not rewritten by this review. Source-role-resolved dialogue that lacks an explicit colon label is emitted separately so that attribution basis remains visible.

## Resolution summary

- raw residual blocks: **20**
- raw source lines: **35**
- resolved dialogue supplements: **15**
- non-dialogue source units: **6** (the mixed scene-005 block splits into one action unit plus one semicolon-labelled dialogue unit)
- unresolved blocks: **0**
- source punctuation normalized: **0**
- speaker aliases expanded/normalized: **0**

## Source exception

Scene 005 preserves the exact source form `திரு; ...`. It is classified as dialogue because the verified scene context and later `திரு : ...` turns establish its role, but the semicolon is retained as the source delimiter and is not corrected to a colon.

## Decisions

- `ammaiyappan-s001-u001` — **non_dialogue_action_narrative**: source prose describes coach arrival and character actions; no speech turn
- `ammaiyappan-s005-u001` — **mixed_action_plus_semicolon_label_exception** — speaker `திரு`: block begins with source action prose, then exact source form “திரு; …”; the same scene later prints “திரு : …”; preserve semicolon and do not normalize it
- `ammaiyappan-s006-u001` — **contextual_dialogue_continuation** — speaker `சுக`: preceding explicit சுக turn continues around the parenthetical sword-fight cue; no intervening speaker is introduced
- `ammaiyappan-s006-u002` — **contextual_dialogue_continuation** — speaker `சுக`: continues the same sword-practice exchange after “(மீண்டும் சண்டை)”; no intervening speaker is introduced
- `ammaiyappan-s006-u003` — **contextual_dialogue_continuation** — speaker `சுக`: immediately follows explicit “சுக : டேய்...நீ போ,” and the cue “(முத்தனிடம்)”; the cue identifies the addressee, not a new speaker
- `ammaiyappan-s008-u001` — **contextual_dialogue_continuation** — speaker `திரி`: preceding explicit திரி turn is interrupted only by the source cue announcing the goat and சுகதேவ் arrival; the unlabelled line continues his invitation
- `ammaiyappan-s011-u001` — **contextual_dialogue_continuation** — speaker `முத்தன்`: preceding explicit முத்தன் turn is followed by “[சிரிக்கிறாள்]”; the unlabelled question responds directly to that laugh
- `ammaiyappan-s011-u002` — **contextual_dialogue_continuation** — speaker `திரிசங்கு`: preceding explicit திரிசங்கு turn sends முத்தாயி away; after “[முத்தாயி போகிறாள் கலங்கியபடி]” the prayer/address continues from him
- `ammaiyappan-s011-u003` — **non_dialogue_action_narrative**: source prose narrates the fight and embeds quoted words inside narration rather than as a standalone speaker-labelled turn
- `ammaiyappan-s014-u001` — **non_dialogue_action_narrative**: source prose describes முத்தன் checking the sword and பூங்காவனம் arriving
- `ammaiyappan-s017-u001` — **contextual_dialogue_continuation** — speaker `முத்தன்`: preceding explicit முத்தன் political speech is interrupted only by “[நண்பர்கள் சிரிக்கிறார்கள்...]”; the next lines directly address those friends
- `ammaiyappan-s017-u002` — **contextual_dialogue_continuation** — speaker `வேதாளம்`: preceding explicit வேதாளம் turn sends the others away; after “[போகிறார்கள்]” he immediately addresses முத்தன்
- `ammaiyappan-s018-u001` — **non_dialogue_stage_direction_continuation**: this is the second-page continuation of the square-bracket stage direction beginning on PDF 37 and ending with “]” on PDF 38
- `ammaiyappan-s027-u001` — **contextual_dialogue_continuation** — speaker `முத்தன்`: preceding explicit முத்தன் denunciation is followed by “[சிரிக்கிறார்கள்]”; the unlabelled lines sarcastically answer that laughter and continue his address
- `ammaiyappan-s027-u002` — **contextual_dialogue_stage_cue_attribution** — speaker `திரிசங்கு`: immediately preceding source cue is “[திரிசங்கு வருகிறான்.]”; the following insult is addressed to his daughter before her labelled response
- `ammaiyappan-s030-u001` — **contextual_dialogue_continuation** — speaker `வேல`: preceding explicit வேல threat continues after “[இழுத்து உள்ளே தள்ளுகிறான்.]”; the stage-direction subject remains வேலழகன் and no new speaker appears
- `ammaiyappan-s035-u001` — **contextual_dialogue_stage_cue_attribution** — speaker `திரிசங்கு`: source cue explicitly says திரிசங்கு sees சுகதேவ் arriving; the next unlabelled line is his face-saving remark, not a continuation of the preceding முத்தாயி label
- `ammaiyappan-s041-u001` — **non_dialogue_stage_direction_continuation**: this is the PDF 86 continuation of the square-bracket storm/action direction begun on PDF 85
- `ammaiyappan-s050-u001` — **contextual_dialogue_stage_cue_attribution** — speaker `சுகதேவ்`: immediately preceding source cue says arriving சுகதேவ் sees முத்தாயி leave with வேதாளம்; the following unlabelled monologue is his reaction
- `ammaiyappan-s059-u001` — **contextual_dialogue_continuation** — speaker `முத்தன்`: verified derivative explicitly records that the PDF 104 speech continues on PDF 105; no new speaker intervenes
