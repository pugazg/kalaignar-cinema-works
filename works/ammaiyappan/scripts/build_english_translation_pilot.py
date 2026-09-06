#!/usr/bin/env python3
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIALOGUES = ROOT / "dialogues"
SCENES = ROOT / "scenes"
SONGS = ROOT / "songs"
OUT = ROOT / "translations"

TRANSLATIONS = {
    "d001": ("Hey—Mutha! What picture is this?", []),
    "d002": ("Nothing...", []),
    "d003": ("Hey!... Just show me; let me see...", []),
    "d004": ("Oh!... Mutha! I remember seeing a picture like this somewhere two or three weeks ago!...", []),
    "d005": ("What you are about to see... this picture is my dream of an ideal... the dawn-star of joy... The picture you saw a week or two ago was another copy of this picture—an unfinished drawing...", ["The source's `லட்சியக் கனவு / இன்ப விடிவெள்ளி` image sequence is preserved rather than compressed into a plain description of the portrait."]),
    "d006": ("Oh-ho! Was that yours too?", []),
    "d007": ("Yes. The earlier one slipped from my hand and was stolen....! I drew another one. That... this...", []),
    "d008": ("All right; all right, Mutha. If there were a woman in this world like the one in this picture, I would be the one to marry her.", []),
    "d009": ("Hm; why talk about something that does not exist.", []),
    "d010": ("True enough—what people talk about in this world is what does not exist... All right, aren't you coming to the monastery?", []),
    "d011": ("Village meeting.", ["The source is an abrupt two-word fragment, `ஊர் கூடம்.`; the English remains equally elliptical."]),
    "d012": ("What, Muthanna, all well?", ["`முத்தண்ணா` is retained as `Muthanna`; `சுகந்தானா?` is rendered as the colloquial `all well?`."]),
    "d013": ("What, is this some land of freedom for us to live in comfort? The man of comfort is right inside this monastery—Maykainatha Swami.", ["The verified Tamil prints `சுந்திர பூமி`; the English carries the evident freedom/comfort wordplay without altering that Tamil reading.", "The second `சுக` image is retained as `man of comfort`, keeping the satirical wordplay before Maykainatha Swami is named."]),
    "d014": ("May Ammaiyappan's grace reach the entire universe... O servants of the servants! O devotees filled with love!....... If you have questions of doubt, ask and gain clarity........", ["The devotional proclamation and extended pauses are preserved; `அய்ய வினைகள்` is translated by sense as questions of doubt without repairing the Tamil source."]),
    "d015": ("Swami, what does `Ammaiyappan` mean.........", ["The title-name `Ammaiyappan` is retained because the following exchange turns on its Tamil `Amma/Appa` wordplay."]),
    "d016": ("Goodness, don't you understand even this, Prince? This palaiyakkarar Baladevar here is your...", ["`பாளையக்கார` is retained as `palaiyakkarar`, a source-specific political/feudal title, rather than flattened to a generic `lord`."]),
    "d017": ("Father!......", []),
    "d018": ("Right, and she.......?", []),
    "d019": ("Mother!.......", []),
    "d020": ("Amma...... Appa...... Ammaiyappa.", ["The Tamil mother/father wordplay is preserved by transliteration; replacing it with a fully English compound would erase the title's sound-play."]),
    "d021": ("Oh! Then is it my mother and father whose hides you are wearing!", ["The source's satirical `தோலத் தரிப்பது` image is translated literally rather than doctrinally softened."]),
    "d022": ("Listen: just as you have an Ammaiyappan, the people of the world too have an Ammaiyappan.", []),
    "d023": ("Where are they, I wonder?—", []),
    "d024": ("They cannot be seen by the eye!—", []),
    "d025": ("When we, their children, can be seen by the eye, shouldn't the parents be visible too?", []),
    "d026": ("Wrong!... Those divine parents cannot be seen—they are formless—possessed of the power to create and destroy all the cosmic spheres... bearers of a thousand names... praised in many an invocatory verse... this world and the next, pleasure and pain... pillar and speck... there... here... shining everywhere... What, Sukhadev... has your confusion ended?...", ["The source's accumulating devotional catalogue and paired fragments are preserved rather than reorganized into systematic theology.", "`பாயிரம்` is rendered as `invocatory verse` for readability while retaining its literary function."]),
    "d027": ("It is only now beginning.", []),
    "d028": ("Oh, Ammaiyappa—", []),
    "d029": ("Sukhadev, don't ask mischievous questions like this; trying to trip up holy men in this way is a great sin......", []),
    "d030": ("No, Father, I only asked because I did not know. I take it back.......", []),
    "d031": ("Good.", []),
}

STAGES = {
    "stage1": {
        "pdf_page": 5, "printed_page": 3,
        "source_text": "ஒரு கோச் வந்து நிற்கிறது. பலதேவர், ராணி, எல்லோரும் இறங்கி உள்ளே செல்கின்றனர். கோச்சை ஓட்டிவந்த முத்தனும் இறங்குகிறான். அவன் குதிரையை எடுக்கிறான். அதிலிருந்து படம் ஒன்று விழுகிறது. சுகதேவ் கண்டு விடுகிறான்.",
        "english": "A coach arrives and stops. Baladevar, the queen and the others get down and go inside. Muthan, who drove the coach, also gets down. He takes the horse. A picture falls from it. Sukhadev notices.",
        "description": "Opening action prose before the first labelled utterance.",
        "notes": ["`அவன் குதிரையை எடுக்கிறான்` is kept conservatively as `He takes the horse`; no extra action such as tying or leading it away is added."],
    },
    "stage2": {
        "pdf_page": 5, "printed_page": 3,
        "source_text": "[காட்டுகிறான்.]",
        "english": "[He shows it.]",
        "description": "Bracketed action immediately after Sukhadev asks to see the picture.",
        "notes": [],
    },
    "stage3": {
        "pdf_page": 6, "printed_page": 4,
        "source_text": "[முத்தன் நண்பர்கள் வருகிறார்கள்]",
        "english": "[Muthan's friends arrive.]",
        "description": "Bracketed entrance cue after Muthan's `ஊர் கூடம்.` reply.",
        "notes": [],
    },
}

EVENTS = [
    "stage1", "d001", "d002", "d003", "stage2", "d004", "d005", "d006", "d007",
    "d008", "d009", "d010", "d011", "stage3", "d012", "d013", "d014", "d015",
    "d016", "d017", "d018", "d019", "d020", "d021", "d022", "d023", "d024",
    "d025", "d026", "d027", "d028", "d029", "d030", "d031",
]

README = """# அம்மையப்பன் — English translation layer

**Canonical authority:** 105/105 dual-gate verified Tamil, 63/63 verified scene derivatives, final dialogue/source-role layer, reconciled character/entity layer, and the closed source-only song/performance gate  
**Target language:** English (`en`)  
**Status:** **pilot verified — archival scene 1 / 63; 34/34 pilot units verified**

This layer is a source-linked English derivative. It does not repair, normalize, expand or overwrite the verified Tamil.

The booklet prints **no scene numbers**. Translation IDs such as `ammaiyappan-en-s001-u001` use the archive's 63-scene navigation segmentation only and must never be presented as source scene numbering.

## Translation principles

1. Tamil remains authoritative; English fluency is never evidence for changing a verified Tamil reading.
2. Preserve rhetoric, satire, repetition, wordplay, abrupt fragments, devotional accumulation and theatrical pauses.
3. Preserve exact Tamil speaker labels as metadata. Character/entity mappings may aid identity but never rewrite the Tamil labels.
4. Preserve source-role provenance for context-attributed dialogue supplements; do not turn a derivative attribution into a printed label.
5. Stage directions stay source-bounded; no action, identity or motivation is added for smoothness.
6. Cross-page source units remain one translation unit with page provenance/segments.
7. Decorative `★` remains structural and does not become invented prose.
8. The closed song/performance gate controls English: translate only the five source-visible occurrences when encountered, and never reconstruct absent lyrics.
9. The booklet's `கதை வசனம் / மு. கருணாநிதி` credit is not upgraded into lyric authorship.
10. Cultural/register terms may remain transliterated when substitution would erase source force; consequential choices go in unit notes.

## Pilot checkpoint

Scene 1 (`மடாலய வெளிப்புறம்`) covers PDF 5–7 / logical printed pp.3–5.

- translation units: **34**
- immutable explicit dialogue records: **31/31 linked exactly once**
- stage-direction/action units: **3**
- source-role supplement units: **0**
- song/performance occurrence links: **0**
- cross-page translation units: **0**
- canonical Tamil changes: **0**
- dialogue/character/song evidence changes: **0**

**Next:** translate and source-review archival scenes **2–5** using this pilot as the initial voice template.
"""

PILOT_REVIEW = """# அம்மையப்பன் — English pilot review

**Pilot:** `ammaiyappan-s001`  
**Source:** PDF 5–7 / logical printed pp.3–5  
**Status:** **verified**  
**Units:** **34** — 31 dialogue / 3 stage direction

## Review result

The scene-1 English pilot is linked to all **31/31** immutable explicit dialogue records in exact source order and preserves the three non-dialogue action/stage units supplied by the verified scene derivative. No source-role supplement or song/performance occurrence belongs to this scene.

No canonical Tamil, dialogue record, character/entity mapping or song/performance evidence was modified.

## Voice decisions established by the pilot

### 1. Preserve comedy and wordplay

The scene moves from the portrait exchange into Muthan's freedom/comfort satire and Sukhadev's questioning of Maykainatha. English must not flatten those shifts into neutral exposition. `Amma...... Appa...... Ammaiyappa.` remains transliterated because the title itself is produced through the mother/father sound-play.

### 2. Keep colloquial address visible

`முத்தா` and `முத்தண்ணா` are carried as `Mutha` and `Muthanna` where they function as address. Exact Tamil `speaker_label` metadata remains untouched.

### 3. Preserve devotional accumulation without doctrinal repair

Maykainatha's catalogue of the invisible divine parents remains cumulative: cosmic creation/destruction, thousand names, invocatory verses, this world/the next, pleasure/pain, pillar/speck, here/there. English does not reorganize it into smoother theology.

### 4. Preserve source irregularity rather than changing Tamil

The verified source form `சுந்திர பூமி` is not altered. English carries the evident freedom/comfort wordplay and records the decision in a note. Likewise `அய்ய வினைகள்` is translated by contextual sense without becoming a Tamil correction.

### 5. Stage directions remain minimal

The opening action is translated without inventing what Muthan does with the horse beyond the source. `[காட்டுகிறான்.]` and `[முத்தன் நண்பர்கள் வருகிறார்கள்]` remain discrete action units.

### 6. Do not import absent song material

Scene 1 has no retained song/performance occurrence. The closed source-only song gate remains authoritative; no film lyric, audio wording or remembered material is introduced.

## Integrity checks

- immutable explicit dialogue links: **31/31**
- missing dialogue links: **0**
- duplicate dialogue links: **0**
- stage-direction units: **3**
- source-role supplement units: **0**
- song/performance occurrence links: **0**
- cross-page units: **0**
- structural-star prose units: **0**
- canonical Tamil/dialogue/character/song changes: **0**

## Scaling instruction

Use this pilot as the initial voice template for the next bounded batch. Preserve source force before optimizing English smoothness. Where a cultural term, pun, satire, repetition or abrupt fragment resists elegant English, retain the source structure and document the choice instead of rewriting the Tamil.

**Next batch target:** archival scenes **2–5**.
"""


def adapt_schema() -> dict:
    p = ROOT.parent / "manohara" / "translations" / "schema.json"
    schema = json.loads(p.read_text(encoding="utf-8"))

    def walk(v):
        if isinstance(v, str):
            return v.replace("manohara", "ammaiyappan").replace("Manohara", "Ammayappan")
        if isinstance(v, list):
            return [walk(x) for x in v]
        if isinstance(v, dict):
            return {k: walk(x) for k, x in v.items()}
        return v

    schema = walk(schema)
    schema["properties"]["archival_scene_ordinal"]["maximum"] = 63
    schema["$defs"]["unit"]["properties"]["archival_scene_ordinal"]["maximum"] = 63
    schema["$defs"]["unit"]["properties"]["kind"]["enum"] = [
        "dialogue", "stage-direction", "song-reference", "literary-verse", "japa", "written-text"
    ]
    source = schema["$defs"]["source"]
    source["required"].append("speaker_label_origin")
    source["properties"]["speaker_label_origin"] = {
        "type": ["string", "null"],
        "enum": ["source-explicit-colon", "source-explicit-noncolon-delimiter", "source-context-attributed", None],
    }
    return schema


def main() -> None:
    out_records = OUT / "records"
    out_records.mkdir(parents=True, exist_ok=True)

    scene_text = (SCENES / "scene-001.md").read_text(encoding="utf-8")
    for key, stage in STAGES.items():
        assert stage["source_text"] in scene_text, f"missing source stage cue: {key}"

    dialogue_rows = json.loads((DIALOGUES / "records/scene-001.json").read_text(encoding="utf-8"))
    assert len(dialogue_rows) == 31
    by_short = {r["id"].rsplit("-", 1)[-1]: r for r in dialogue_rows}
    assert set(by_short) == {f"d{i:03d}" for i in range(1, 32)}
    assert set(TRANSLATIONS) == set(by_short)

    supplements = json.loads((DIALOGUES / "source-role-resolved-records.json").read_text(encoding="utf-8"))
    assert not [r for r in supplements if r["archive_scene_id"] == "ammaiyappan-s001"]
    song_inventory = json.loads((SONGS / "inventory.json").read_text(encoding="utf-8"))
    assert not [o for o in song_inventory["occurrences"] if o["archive_scene_id"] == "ammaiyappan-s001"]

    units = []
    stage_ord = 0
    for i, event in enumerate(EVENTS, start=1):
        uid = f"ammaiyappan-en-s001-u{i:03d}"
        if event.startswith("stage"):
            stage_ord += 1
            s = STAGES[event]
            units.append({
                "id": uid,
                "kind": "stage-direction",
                "status": "verified",
                "target_language": "en",
                "scene_id": "ammaiyappan-s001",
                "archival_scene_ordinal": 1,
                "source": {
                    "source_path": "works/ammaiyappan/scenes/scene-001.md",
                    "canonical_scene_path": "works/ammaiyappan/scenes/scene-001.md",
                    "source_record_id": None,
                    "source_occurrence_id": None,
                    "source_locator": {"kind": "scene-stage-direction", "ordinal": stage_ord, "description": s["description"]},
                    "speaker_label": None,
                    "speaker_label_origin": None,
                    "page_provenance": [{"pdf_page": s["pdf_page"], "printed_page": s["printed_page"]}],
                },
                "translation": {"english_text": s["english"], "mode": "prose-faithful", "notes": s["notes"]},
            })
        else:
            r = by_short[event]
            english, notes = TRANSLATIONS[event]
            units.append({
                "id": uid,
                "kind": "dialogue",
                "status": "verified",
                "target_language": "en",
                "scene_id": "ammaiyappan-s001",
                "archival_scene_ordinal": 1,
                "source": {
                    "source_path": "works/ammaiyappan/dialogues/records/scene-001.json",
                    "canonical_scene_path": "works/ammaiyappan/scenes/scene-001.md",
                    "source_record_id": r["id"],
                    "source_occurrence_id": None,
                    "source_locator": None,
                    "speaker_label": r["speaker_label"],
                    "speaker_label_origin": "source-explicit-colon",
                    "page_provenance": deepcopy(r["page_provenance"]),
                },
                "translation": {"english_text": english, "mode": "prose-faithful", "notes": notes},
            })

    assert len(units) == 34
    dlinks = [u["source"]["source_record_id"] for u in units if u["kind"] == "dialogue"]
    assert dlinks == [r["id"] for r in dialogue_rows]
    assert len(set(dlinks)) == 31
    assert sum(u["kind"] == "stage-direction" for u in units) == 3
    assert all(len(u["source"]["page_provenance"]) == 1 for u in units)

    scene_record = {
        "work_id": "ammaiyappan", "target_language": "en", "scene_id": "ammaiyappan-s001",
        "archival_scene_ordinal": 1, "source_scene_number": None,
        "pilot_status": "verified", "scene_status": "verified",
        "unit_count": len(units), "units": units,
    }
    (out_records / "scene-001.json").write_text(json.dumps(scene_record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    schema = adapt_schema()
    (OUT / "schema.json").write_text(json.dumps(schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    preflight = {
        "work_id": "ammaiyappan", "target_language": "en", "status": "complete-pass-pilot-unblocked",
        "authority": {
            "canonical_tamil": "105/105-dual-gate-complete-verified",
            "scene_derivatives": "63/63-complete-verified",
            "dialogue_final_index": f"{json.loads((DIALOGUES / 'final-index.json').read_text(encoding='utf-8'))['total_dialogue_units_for_downstream_indexing']}-downstream-units-complete-source-role-resolved",
            "exact_source_speaker_labels": 62,
            "character_entity_index": "26-entities-complete-verified-reconciled",
            "song_performance_gate": "complete-verified-source-only",
            "source_visible_song_performance_occurrences": 5,
            "full_named_song_lyric_blocks_printed": 0,
        },
        "source_scene_numbering": "none-printed", "archive_scene_count": 63,
        "translation_policy": {
            "scene_sharded": True,
            "exact_tamil_speaker_labels_preserved_as_metadata": True,
            "immutable_dialogue_ids_linked": True,
            "source_role_origin_preserved": True,
            "source_unlabelled_speech_must_not_gain_invented_speaker": True,
            "cross_page_source_units_remain_single_translation_units": True,
            "decorative_stars_create_no_translation_units": True,
            "absent_song_lyrics_must_not_be_reconstructed": True,
            "canonical_tamil_may_not_be_changed_by_translation": True,
        },
        "pilot": {
            "scene_id": "ammaiyappan-s001", "archive_scene_ordinal": 1,
            "source_pdf_pages": [5, 6, 7], "logical_printed_pages": [3, 4, 5],
            "explicit_dialogue_records_expected": 31, "source_role_supplement_records_expected": 0,
            "stage_direction_units_expected": 3, "song_performance_occurrence_links_expected": 0,
            "total_translation_units_expected": 34, "cross_page_translation_units_expected": 0,
        },
        "next_action": "Translate and source-review archival scenes 2-5 using the verified pilot voice rules; preserve exact dialogue/source-role provenance and closed song/performance evidence.",
    }
    (OUT / "preflight.json").write_text(json.dumps(preflight, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    index = {
        "work_id": "ammaiyappan", "target_language": "en", "status": "pilot-verified",
        "schema": "schema.json", "readme": "README.md", "preflight": "preflight.json", "pilot_review": "PILOT_REVIEW.md",
        "record_directory": "records", "pilot_scene": "ammaiyappan-s001", "source_scene_numbering": "none-printed",
        "scenes_expected": 63, "scenes_started": [1], "scenes_verified": [1], "scenes_in_review": [],
        "translation_units": 34, "unit_status_counts": {"draft": 0, "review": 0, "verified": 34},
        "unit_kind_counts": {"dialogue": 31, "stage-direction": 3, "song-reference": 0, "literary-verse": 0, "japa": 0, "written-text": 0},
        "scene_records": [{"scene_id": "ammaiyappan-s001", "archival_scene_ordinal": 1, "path": "records/scene-001.json", "unit_count": 34, "status": "verified"}],
        "dialogue_source_records_expected_in_completed_scenes": 31, "dialogue_source_records_linked": 31,
        "source_role_supplement_records_linked": 0, "cross_page_translation_units": [],
        "translated_song_performance_occurrences": [], "source_visible_structural_stars_translated": 0,
        "completed_batches": ["pilot scene 1"], "next_scene_batch": "2-5",
        "next_activity": "Translate and source-review archival scenes 2-5 using the verified pilot voice rules; preserve exact dialogue/source-role provenance and closed song/performance evidence.",
        "canonical_tamil_modified": False, "scene_files_modified": False, "dialogue_records_modified": False,
        "character_index_modified": False, "song_inventory_modified": False,
    }
    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "README.md").write_text(README, encoding="utf-8")
    (OUT / "PILOT_REVIEW.md").write_text(PILOT_REVIEW, encoding="utf-8")

    print(json.dumps({
        "pilot_scene": 1, "units": 34, "dialogue_links": 31, "stage_directions": 3,
        "source_role_supplements": 0, "song_occurrence_links": 0, "next_batch": "2-5"
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
