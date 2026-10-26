import copy
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("validator", Path(__file__).parents[1] / "tools" / "validate_episode.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def passed():
    return {"status": "pass", "observation": "Observed in test fixture only", "evidence": "fixture://not-production"}


def fixture():
    r = {"run_id": "unit-test", "workflow_commit": "test", "style_lock_version": 1,
         "style_reference": v.REFERENCE, "story_locked": True, "target_seconds": 35,
         "reference_inspection": passed(), "actual_seconds": 35, "shots": [],
         "film_checks": {k: passed() for k in v.FILM_CHECKS},
         "owner_final_approval": {"approved": False, "statement": "", "recorded_at": ""}}
    for i in range(5):
        r["shots"].append({"id": str(i), "planned_seconds": 7, "measured_seconds": 7,
            "dialogue": "Hello.", "dialogue_characters": 6, "speaker": "sister", "voice": "Ana",
            "causal_action": True, "story_event": "event", "location_id": "garden",
            "composition": str(i), "start_state": "start", "action": "action", "end_state": "end",
            "action_timing": "0-7", "cut_reason": "next event", "converted_asset": "private-fixture",
            "checks": {k: passed() for k in v.SHOT_CHECKS}})
    r["joins"] = [{"from": str(i), "to": str(i+1), **passed()} for i in range(4)]
    return r


class FactoryGates(unittest.TestCase):
    def test_valid_record(self):
        self.assertEqual(v.validate(fixture(), "review"), [])

    def test_hard_limits(self):
        for key, value in (("planned_seconds", 10.01), ("measured_seconds", 10.01),
                           ("dialogue", "x" * 101), ("voice", "Other")):
            r = fixture()
            r["shots"][0][key] = value
            self.assertTrue(v.validate(r, "review"), key)

    def test_wrong_style_and_static_story(self):
        r = fixture()
        r["style_reference"] = "The Leaf Boat - Continuity Revision"
        self.assertTrue(v.validate(r))
        r = fixture()
        for shot in r["shots"]:
            shot["composition"] = "same"
            shot["causal_action"] = False
        self.assertEqual(len(v.validate(r)), 2)

    def test_unverified_media_cannot_pass_review(self):
        r = fixture()
        r["shots"][1]["checks"]["audio"] = {"status": "pass"}
        self.assertTrue(v.validate(r, "review"))
        r = fixture()
        r["reference_inspection"] = {"status": "pending"}
        self.assertTrue(v.validate(r, "generation"))

    def test_missing_or_wrong_joins(self):
        r = fixture()
        r["joins"] = []
        self.assertTrue(v.validate(r, "review"))
        r = fixture()
        r["joins"][0]["to"] = "wrong"
        self.assertTrue(v.validate(r, "review"))

    def test_download_requires_final_approval(self):
        r = fixture()
        self.assertTrue(v.validate(r, "download"))
        r["owner_final_approval"] = {"approved": True, "statement": "Final 100% go ahead",
                                    "recorded_at": "2026-10-26"}
        self.assertEqual(v.validate(r, "download"), [])

    def test_bad_data_blocks_without_crashing(self):
        for replacement in (None, [], [None], [{}]):
            r = fixture()
            r["shots"] = replacement
            self.assertTrue(v.validate(r, "review"))


if __name__ == "__main__":
    unittest.main()
