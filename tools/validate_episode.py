"""Validate private production records; does not inspect pixels or listen to audio."""
import argparse
import json
import math
import sys

REFERENCE = "The Leaf Boat - Animated Garden Test"
SHOT_CHECKS = ("style", "character_finish", "literal_action", "continuity", "pacing", "audio")
FILM_CHECKS = ("visual_story", "pacing", "audio", "timeline_reopened", "final_playback")


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def evidence(value):
    return isinstance(value, dict) and value.get("status") == "pass" and all(
        isinstance(value.get(k), str) and value[k].strip()
        for k in ("observation", "evidence")
    )


def validate(record, stage="plan"):
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    require(isinstance(record, dict), "Record must be an object")
    if not isinstance(record, dict):
        return errors
    require(bool(record.get("run_id")), "Missing run_id")
    require(bool(record.get("workflow_commit")), "Missing workflow_commit")
    require(record.get("style_lock_version") == 1, "Use approved style-lock version 1")
    require(record.get("style_reference") == REFERENCE, "Wrong approved style reference")
    require(record.get("story_locked") is True, "Story intent must be locked before advancing")
    target = record.get("target_seconds")
    require(number(target) and target > 0, "Invalid target_seconds")
    shots = record.get("shots", [])
    require(isinstance(shots, list) and len(shots) > 0, "Shots must be a nonempty list")
    if not isinstance(shots, list) or not shots:
        return errors
    ids, compositions = [], set()
    total, causal = 0, 0
    for index, shot in enumerate(shots):
        tag = f"Shot {index + 1}"
        require(isinstance(shot, dict), f"{tag}: must be an object")
        if not isinstance(shot, dict):
            continue
        sid = shot.get("id")
        require(isinstance(sid, str) and bool(sid.strip()) and sid not in ids, f"{tag}: missing/duplicate ID")
        ids.append(sid)
        seconds = shot.get("planned_seconds")
        require(number(seconds) and 0 < seconds <= 10, f"{tag}: planned duration must be >0 and <=10")
        if number(seconds):
            total += seconds
        line = shot.get("dialogue")
        require(isinstance(line, str) and bool(line.strip()) and len(line) <= 100,
                f"{tag}: exact dialogue must contain 1..100 characters")
        if isinstance(line, str):
            require(shot.get("dialogue_characters") == len(line), f"{tag}: dialogue character count is wrong")
        speaker = shot.get("speaker")
        require(speaker in ("sister", "brother"), f"{tag}: invalid speaker/narrator")
        require(shot.get("voice") == {"sister": "Ana", "brother": "Justin"}.get(speaker) and
                speaker in ("sister", "brother"), f"{tag}: wrong approved voice")
        for key in ("story_event", "location_id", "composition", "start_state", "action",
                    "end_state", "action_timing", "cut_reason"):
            value = shot.get(key)
            require(isinstance(value, str) and bool(value.strip()), f"{tag}: missing {key}")
        composition = shot.get("composition")
        if isinstance(composition, str) and composition.strip():
            compositions.add(composition)
        causal += shot.get("causal_action") is True
        if stage in ("review", "download"):
            measured = shot.get("measured_seconds")
            require(number(measured) and 0 < measured <= 10, f"{tag}: measured duration missing or >10")
            require(bool(shot.get("converted_asset")), f"{tag}: missing identified converted asset")
            checks = shot.get("checks", {})
            if not isinstance(checks, dict):
                checks = {}
            for key in SHOT_CHECKS:
                require(evidence(checks.get(key)), f"{tag}: {key} requires actual pass observation and evidence")
    if number(target):
        require(abs(total - target) < 0.001, f"Planned shots total {total:g}s, target is {target:g}s")
    if target == 35:
        require(len(compositions) >= 3, "35-second proof needs >=3 purposeful compositions")
        require(causal >= 2, "35-second proof needs >=2 visible cause-and-effect actions")
    if stage in ("generation", "review", "download"):
        require(evidence(record.get("reference_inspection")), "Approved reference inspection is unverified")
    if stage in ("review", "download"):
        joins = record.get("joins", [])
        require(isinstance(joins, list) and len(joins) == len(shots) - 1, "Missing per-join checks")
        if isinstance(joins, list):
            for i, join in enumerate(joins):
                require(isinstance(join, dict) and i + 1 < len(ids) and
                        join.get("from") == ids[i] and join.get("to") == ids[i + 1] and evidence(join),
                        f"Join {i + 1}: ordered continuity/pacing pass evidence required")
        checks = record.get("film_checks", {})
        if not isinstance(checks, dict):
            checks = {}
        for key in FILM_CHECKS:
            require(evidence(checks.get(key)), f"Film: {key} is unverified")
        actual = record.get("actual_seconds")
        require(number(actual) and actual > 0, "Missing measured film runtime")
        if number(actual) and number(target):
            tolerance = record.get("runtime_tolerance_seconds", 0.5)
            require(number(tolerance) and 0 <= tolerance <= 0.5, "Runtime tolerance must be 0..0.5s")
            if number(tolerance) and 0 <= tolerance <= 0.5:
                require(abs(actual - target) <= tolerance, "Film runtime is outside the declared tolerance")
    if stage == "download":
        approval = record.get("owner_final_approval", {})
        require(isinstance(approval, dict) and approval.get("approved") is True and
                isinstance(approval.get("statement"), str) and bool(approval["statement"].strip()) and
                isinstance(approval.get("recorded_at"), str) and bool(approval["recorded_at"].strip()),
                "PC download blocked: explicit final owner approval statement/time required")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record")
    parser.add_argument("--stage", choices=("plan", "generation", "review", "download"), default="plan")
    args = parser.parse_args()
    try:
        with open(args.record, encoding="utf-8") as handle:
            record = json.load(handle)
        errors = validate(record, args.stage)
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    for error in errors:
        print("BLOCKED: " + error)
    if errors:
        return 1
    print(f"Record checks passed for {args.stage}; this does not certify media quality.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
