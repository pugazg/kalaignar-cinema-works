# வண்டிக்காரன் மகன் — dialogue-index preflight

Status: **SUPERSEDED / HISTORICAL**

The original preflight counted **744** explicit dialogue candidates. A later structural-collision audit established that the parser had skipped **29** genuine source-labelled spoken utterances whose lines ended with parenthetical action, while correctly excluding **2** source-labelled action-only lines.

Current immutable dialogue authority: **773 records / 38 exact labels / QA PASS-RECONCILED**. Existing 744 IDs were preserved and 29 repair IDs were added append-only.

See `dialogue-structural-collision-audit.json`, `dialogue-index-qa.json`, and `../dialogues/index.json`.
