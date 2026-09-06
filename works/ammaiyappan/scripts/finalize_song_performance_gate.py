#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SONGS = ROOT / "songs"

MATERIAL_CANDIDATES = {
    "ammaiyappan-perf-cand-002": "source-performance-occurrence",
    "ammaiyappan-perf-cand-004": "source-literary-verse-occurrence",
    "ammaiyappan-perf-cand-011": "source-performance-occurrence",
    "ammaiyappan-perf-cand-051": "source-performance-occurrence",
    "ammaiyappan-perf-cand-062": "source-performance-lead-in",
    "ammaiyappan-perf-cand-063": "source-performance-occurrence",
}

OCCURRENCES = [
    {
        "id": "ammaiyappan-song-001",
        "archive_scene_id": "ammaiyappan-s007",
        "archive_scene_ordinal": 7,
        "source_scene_file": "scene-007.md",
        "page_provenance": [{"pdf_page": 18, "printed_page": 16}],
        "occurrence_kind": "song-performance-reference",
        "performers_source_visible": ["முத்தன்", "முத்தாயி"],
        "source_visible_text": "[முத்தன்-முத்தாயி காதல் கீதம் பாட்டு முடியும் தருவாயில் சுமதி தன் இடையில் இருபுறங்களிலும் இரண்டு குடம் தண்ணீருடன் வருகிறாள். குடங்களை தூரத்தில் வைத்துவிட்டு முத்தன், முத்தாயி இருவரையும் பார்த்து தன் இரு கண்களையும் பொத்திக் கொண்டு அவர்களிடம் வந்து]",
        "source_visible_title": None,
        "printed_lyric_body": False,
        "authorship_status": "unresolved-source-does-not-attribute",
        "attributed_author_ta": None,
        "standalone_tamil_lyric_derivative_authorized": False,
        "notes": "The source says the Muthan–Muthayi love song is ending, but prints neither a title nor lyric lines. Do not import soundtrack lyrics or infer lyricist from story/dialogue credit.",
    },
    {
        "id": "ammaiyappan-song-002",
        "archive_scene_id": "ammaiyappan-s010",
        "archive_scene_ordinal": 10,
        "source_scene_file": "scene-010.md",
        "page_provenance": [{"pdf_page": 23, "printed_page": 21}],
        "occurrence_kind": "quoted-literary-verse-fragment",
        "performers_source_visible": [],
        "source_visible_lead_in": "சுகதேவ் : அய்யய்யோ! முக்கால் வாசி ராமாயணமே அது தான், ஆஹா! கவிச்சக்கரவர்த்தி கம்பர் காதலைப் பற்றி எப்படி வாணித்திருக்கிறார் தெரியுமா... ஒரு பாட்டு கேளு திரிசங்கு...",
        "source_visible_text": "கோமுனியுடன் வரு கொண்டல் என்றபின் தாமரைக் கண்ணினன் என்ற தன்மையால்...ஆம்...அவனே கொல் என்று ஐய நீங்கினள்...வாமமேகலையி வளர்ந்தது...",
        "source_visible_title": None,
        "printed_lyric_body": False,
        "authorship_status": "source-attributed-literary-quotation",
        "attributed_author_ta": "கம்பர்",
        "standalone_tamil_lyric_derivative_authorized": False,
        "notes": "Immediate source dialogue attributes the quotation to Kambar. It is retained as a partial literary verse quotation, not upgraded into a soundtrack-song credit or reconstructed full verse.",
    },
    {
        "id": "ammaiyappan-song-003",
        "archive_scene_id": "ammaiyappan-s019",
        "archive_scene_ordinal": 19,
        "source_scene_file": "scene-019.md",
        "page_provenance": [{"pdf_page": 39, "printed_page": 37}],
        "occurrence_kind": "singing-performance-cue",
        "performers_source_visible": ["முத்தன்"],
        "source_visible_text": "[முத்தன் பாடிக் கொண்டிருக்கும்போது அஞ்ச\nலோடி ஏதோ பைகளைக் தூக்கிக் கொண்டு\nவெளியே போகிறான் திரிசங்கு வருகிறான்.]",
        "source_visible_title": None,
        "printed_lyric_body": False,
        "authorship_status": "unresolved-source-does-not-attribute",
        "attributed_author_ta": None,
        "standalone_tamil_lyric_derivative_authorized": False,
        "notes": "The stage direction establishes that Muthan is singing, but the booklet prints no song title or lyric body at this occurrence.",
    },
    {
        "id": "ammaiyappan-song-004",
        "archive_scene_id": "ammaiyappan-s040",
        "archive_scene_ordinal": 40,
        "source_scene_file": "scene-040.md",
        "page_provenance": [{"pdf_page": 84, "printed_page": 82}],
        "occurrence_kind": "japa-performance-cue",
        "performers_source_visible": ["சுகதேவ்"],
        "source_visible_text": "[இளந்துறவி சுகதேவ், \"முத்தாயி\" ஜபத்துடன் நிஷ்டை இருக்கிறான். அப்போது துறவி வேடத்துடன் வேதாளம் வருகிறான்]",
        "source_visible_spoken_token": "முத்தாயி...முத்தாயி...",
        "source_visible_title": None,
        "printed_lyric_body": False,
        "authorship_status": "not-applicable-character-japa",
        "attributed_author_ta": None,
        "standalone_tamil_lyric_derivative_authorized": False,
        "notes": "This is a source-visible character japa/performance cue, not a soundtrack-song authorship claim. The spoken `முத்தாயி` remains linked through the dialogue layer where labelled.",
    },
    {
        "id": "ammaiyappan-song-005",
        "archive_scene_id": "ammaiyappan-s059",
        "archive_scene_ordinal": 59,
        "source_scene_file": "scene-059.md",
        "page_provenance": [{"pdf_page": 106, "printed_page": 104}],
        "occurrence_kind": "song-request-and-performance-cue",
        "performers_source_visible": ["முத்தாயி"],
        "source_visible_lead_in": "கடைசியாக ஒன்று கேட்கிறேன் முத்தாயி; கடைசியாக ஒன்று கேட்கிறேன்! நாம் இருவரும் சேர்ந்து பாடுவோமே அந்தக் காதல் பாட்டு, அதை இனிமேல் எங்கு கேட்கப்போகிறேன்; எங்கே அதை ஒரு தடவை பாடு!... கண்ணே பாடு! நீ பாடாவிட்டால் உன் காதலன் நிம்மதியாக சாகமாட்டான்...பாடு கண்ணே, பாடு!",
        "source_visible_text": "[அவள் பாடுகிறாள் அழுது கொண்டே. அவன் நடந்து கொண்டே இருக்கிறான் தூக்குமேடை நோக்கி]",
        "source_visible_title": None,
        "printed_lyric_body": False,
        "authorship_status": "unresolved-source-does-not-attribute",
        "attributed_author_ta": None,
        "standalone_tamil_lyric_derivative_authorized": False,
        "notes": "The source refers to `that love song we used to sing together` and shows Muthayi singing, but prints no title or lyric body. It may refer back to the recurring Muthan–Muthayi love-song performance, but the archive does not merge unnamed song identities without stronger source evidence.",
    },
]


def main():
    preflight = json.loads((SONGS / "performance-preflight.json").read_text(encoding="utf-8"))
    assert preflight["scene_files_scanned"] == 63
    assert preflight["candidate_count"] == 64
    candidates = preflight["candidates"]
    assert len(candidates) == 64
    candidate_ids = {x["candidate_id"] for x in candidates}
    assert set(MATERIAL_CANDIDATES).issubset(candidate_ids)

    dispositions = []
    for c in candidates:
        cid = c["candidate_id"]
        if cid in MATERIAL_CANDIDATES:
            disposition = MATERIAL_CANDIDATES[cid]
            if cid == "ammaiyappan-perf-cand-062":
                note = "Lead-in to ammaiyappan-song-005; the following stage direction is the actual performance cue."
            else:
                note = "Retained in the source-visible song/performance inventory."
        else:
            disposition = "not-separate-performance-occurrence"
            note = "Keyword occurs in ordinary dialogue, metaphor/reference, ritual discussion, or as a lexical substring; no separately bounded song/verse/performance body is established at this candidate line."
        dispositions.append({
            "candidate_id": cid,
            "archive_scene_ordinal": c["archive_scene_ordinal"],
            "pdf_page": c["pdf_page"],
            "source_text": c["source_text"],
            "disposition": disposition,
            "note": note,
        })

    retained = [x for x in dispositions if x["candidate_id"] in MATERIAL_CANDIDATES]
    assert len(retained) == 6
    assert len(OCCURRENCES) == 5
    assert sum(1 for x in OCCURRENCES if x["authorship_status"] == "unresolved-source-does-not-attribute") == 3
    assert sum(1 for x in OCCURRENCES if x["authorship_status"] == "source-attributed-literary-quotation") == 1
    assert sum(1 for x in OCCURRENCES if x["authorship_status"] == "not-applicable-character-japa") == 1
    assert all(x["printed_lyric_body"] is False for x in OCCURRENCES)
    assert all(x["standalone_tamil_lyric_derivative_authorized"] is False for x in OCCURRENCES)

    credits = {
        "work_id": "ammaiyappan",
        "status": "complete-source-credit-gate",
        "booklet_work_credit": "கதை வசனம் / மு. கருணாநிதி",
        "lyric_credit_present_in_controlling_booklet": False,
        "policy": "The story/dialogue credit is not a lyric credit. Unnamed song performances remain unresolved unless the controlling source or exact item-level evidence establishes authorship.",
        "external_item_level_evidence_used": False,
        "canonical_tamil_changed_by_authorship_work": False,
    }

    inventory = {
        "work_id": "ammaiyappan",
        "status": "complete-source-reconciled",
        "canonical_authority": "verified 105/105 Tamil and 63/63 scene derivatives",
        "occurrence_count": 5,
        "occurrences": OCCURRENCES,
    }

    candidate_doc = {
        "work_id": "ammaiyappan",
        "status": "complete-dispositioned",
        "preflight_candidate_count": 64,
        "retained_candidate_hits": 6,
        "retained_occurrence_count": 5,
        "non_occurrence_candidate_hits": 58,
        "dispositions": dispositions,
    }

    index = {
        "work_id": "ammaiyappan",
        "status": "complete-verified-source-only",
        "authorship_gate": "closed-with-evidence-limited-unresolved-occurrences",
        "candidate_hits_reviewed": 64,
        "source_visible_occurrences": 5,
        "unresolved_authorship_occurrences": 3,
        "source_attributed_literary_quotation_occurrences": 1,
        "authorship_not_applicable_occurrences": 1,
        "full_named_song_lyric_blocks_printed": 0,
        "standalone_tamil_lyric_files_authorized": 0,
        "standalone_tamil_lyric_files_created": 0,
        "external_item_level_evidence_used": False,
        "canonical_tamil_changed": False,
        "english_translation_gate": "ready",
        "source_rule": "Translate only the performance references, visible fragment, japa token and cues actually printed. Do not reconstruct absent lyrics.",
        "next_activity": "Begin source-linked English translation using the verified Tamil/dialogue/character layers and this closed song/performance gate.",
    }

    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "ammaiyappan-song-performance-schema",
        "title": "Ammayappan song/performance occurrence inventory",
        "type": "object",
        "required": ["work_id", "status", "occurrence_count", "occurrences"],
        "properties": {
            "work_id": {"const": "ammaiyappan"},
            "status": {"type": "string"},
            "occurrence_count": {"type": "integer", "minimum": 0},
            "occurrences": {"type": "array"},
        },
        "additionalProperties": True,
    }

    readme = """# அம்மையப்பன் — song / verse / performance authorship gate

**Canonical authority:** verified 105/105 Tamil and 63/63 scene derivatives  
**Gate status:** **COMPLETE — source-only, with evidence-limited unresolved authorship**  
**Preflight candidates reviewed:** **64/64**  
**Source-visible retained occurrences:** **5**  
**Full song lyric bodies printed by the booklet:** **0**  
**Standalone Tamil lyric files authorized:** **0**

The controlling booklet contains performance/song references, one Kambar-attributed literary verse fragment, and one japa cue, but it does **not** print a complete soundtrack lyric body or a lyricist credit. The printed `கதை வசனம் / மு. கருணாநிதி` credit is therefore not promoted into lyric authorship.

## Source-visible occurrences

1. **Scene 7 / PDF 18** — Muthan–Muthayi love-song performance is ending. No title or lyric lines are printed. **Authorship unresolved.**
2. **Scene 10 / PDF 23** — Sukhadev introduces a partial verse by referring explicitly to **Kambar** and recites a visible fragment. This is retained as a **source-attributed literary quotation**, not a soundtrack lyric.
3. **Scene 19 / PDF 39** — stage direction shows **Muthan singing**. No title or lyric body is printed. **Authorship unresolved.**
4. **Scene 40 / PDF 84** — Sukhadev is in `முத்தாயி` japa; the source-visible spoken token is `முத்தாயி...முத்தாயி...`. This is a **character japa**, so lyric authorship is not applicable.
5. **Scene 59 / PDF 106** — Muthan asks Muthayi to sing “that love song we used to sing together”; the stage direction shows her singing while he walks toward the gallows. No title or lyric body is printed. **Authorship unresolved.**

The scene-59 reference may point back to the recurring Muthan–Muthayi love song seen in scene 7, but the archive does not merge unnamed song identities without stronger source evidence.

## Candidate disposition

The keyword preflight produced 64 navigation hits. Six hits support the five retained occurrences; the remaining 58 are ordinary dialogue, metaphor/reference, ritual discussion, or lexical matches such as `ஏற்பாடு`, `பாடுபட`, `பாட்டி`, and `வானம்பாடி`. They are not separate song/performance bodies.

See `candidate-disposition.json` for all 64 decisions.

## Tamil lyric derivative gate

Zero Tamil lyric files is the correct completed state for this booklet. No lyrics may be imported from film audio, streaming catalogs, websites, subtitles, later editions or memory. The scene files already preserve every source-visible song/performance word supplied by the controlling source.

## English gate

English translation may now proceed. Translate only the source-visible reference/cue/fragment actually printed; do not reconstruct the absent love-song or singing lyrics.
"""

    SONGS.mkdir(exist_ok=True)
    (SONGS / "credits.json").write_text(json.dumps(credits, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (SONGS / "inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (SONGS / "candidate-disposition.json").write_text(json.dumps(candidate_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (SONGS / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (SONGS / "schema.json").write_text(json.dumps(schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (SONGS / "README.md").write_text(readme, encoding="utf-8")

    print(json.dumps({
        "candidates_reviewed": 64,
        "occurrences": 5,
        "unresolved_authorship": 3,
        "full_lyric_blocks": 0,
        "tamil_lyric_files_authorized": 0,
        "english_gate": "ready",
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
