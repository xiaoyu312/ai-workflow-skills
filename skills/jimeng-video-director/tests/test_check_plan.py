import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "check_plan.py"
)


def base_plan(duration=3.0):
    return {
        "duration_s": duration,
        "ratio": "9:16",
        "locked_state_keys": ["person_id"],
        "assets": [
            {
                "id": "P",
                "path": "refs/product.png",
                "status": "available",
                "role": "product",
                "preserve": ["geometry"],
                "exclude": ["redesign"],
            }
        ],
        "shots": [
            {
                "id": "D01",
                "start_s": 0.0,
                "end_s": 1.5,
                "asset_ids": ["P"],
                "start_state": {"person_id": "A", "held_by": "left"},
                "end_state": {"person_id": "A", "held_by": "left"},
            },
            {
                "id": "D02",
                "start_s": 1.5,
                "end_s": 3.0,
                "asset_ids": ["P"],
                "start_state": {"person_id": "A", "held_by": "left"},
                "end_state": {"person_id": "A", "held_by": "left"},
                "incoming": {"type": "continuous"},
            },
        ],
    }


class CheckPlanTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)
        (self.root / "refs").mkdir()
        (self.root / "refs" / "product.png").write_bytes(b"reference")

    def run_plan(self, plan, raw_text=None):
        plan_path = self.root / "PLAN.json"
        if raw_text is None:
            raw_text = json.dumps(plan, ensure_ascii=False)
        plan_path.write_text(raw_text, encoding="utf-8")
        completed = subprocess.run(
            [sys.executable, str(CHECKER), str(plan_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertTrue(completed.stdout, completed.stderr)
        return completed.returncode, json.loads(completed.stdout), plan_path

    @staticmethod
    def codes(result):
        return {issue["code"] for issue in result["errors"]}

    def test_valid_continuous_plan_passes_structural_and_asset_checks(self):
        status, result, _ = self.run_plan(base_plan())

        self.assertEqual(status, 0)
        self.assertTrue(result["structural_valid"])
        self.assertTrue(result["asset_ready"])
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["scope"], "structural_and_declared_state_only")
        self.assertFalse(result["visual_or_video_quality_verified"])

    def test_timeline_gap_is_reported(self):
        plan = base_plan()
        plan["shots"][1]["start_s"] = 1.6

        status, result, _ = self.run_plan(plan)

        self.assertEqual(status, 1)
        self.assertIn("SHOT_TIMELINE_GAP", self.codes(result))
        self.assertFalse(result["structural_valid"])

    def test_unknown_reference_and_missing_available_file_are_errors(self):
        plan = base_plan()
        plan["assets"][0]["path"] = "refs/missing.png"
        plan["shots"][0]["asset_ids"] = ["UNDECLARED"]

        status, result, _ = self.run_plan(plan)

        self.assertEqual(status, 1)
        self.assertIn("ASSET_FILE_MISSING", self.codes(result))
        self.assertIn("ASSET_REFERENCE_UNKNOWN", self.codes(result))
        self.assertFalse(result["asset_ready"])

    def test_planned_asset_is_pending_without_being_treated_as_missing_error(self):
        plan = base_plan()
        plan["assets"][0]["status"] = "planned"
        plan["assets"][0]["path"] = "refs/to-be-created.png"

        status, result, _ = self.run_plan(plan)

        self.assertEqual(status, 0)
        self.assertTrue(result["structural_valid"])
        self.assertFalse(result["asset_ready"])
        self.assertEqual(result["pending_assets"], ["P"])
        self.assertNotIn("ASSET_FILE_MISSING", self.codes(result))

    def test_continuous_boundary_detects_declared_hand_conflict(self):
        plan = base_plan()
        plan["shots"][1]["start_state"]["held_by"] = "right"

        status, result, _ = self.run_plan(plan)

        self.assertEqual(status, 1)
        self.assertIn("CONTINUITY_STATE_CONFLICT", self.codes(result))
        conflict = next(item for item in result["errors"] if item["code"] == "CONTINUITY_STATE_CONFLICT")
        self.assertIn("held_by", conflict["message"])
        self.assertEqual(conflict["shot"], "D02")

    def test_ellipsis_allows_hand_change_but_still_enforces_locked_identity(self):
        plan = base_plan()
        plan["shots"][1]["incoming"] = {"type": "ellipsis", "reason": "省略取物动作"}
        plan["shots"][1]["start_state"]["held_by"] = "right"

        status, result, _ = self.run_plan(plan)

        self.assertEqual(status, 0)
        self.assertNotIn("CONTINUITY_STATE_CONFLICT", self.codes(result))

        plan["shots"][1]["start_state"]["person_id"] = "B"
        status, result, _ = self.run_plan(plan)

        self.assertEqual(status, 1)
        self.assertIn("LOCKED_STATE_CONFLICT", self.codes(result))
        self.assertNotIn("CONTINUITY_STATE_CONFLICT", self.codes(result))

    def test_duplicate_asset_and_shot_ids_are_reported(self):
        plan = base_plan()
        duplicate_asset = dict(plan["assets"][0], path="refs/product.png")
        plan["assets"].append(duplicate_asset)
        plan["shots"][1]["id"] = "D01"

        status, result, _ = self.run_plan(plan)

        self.assertEqual(status, 1)
        self.assertIn("DUPLICATE_ASSET_ID", self.codes(result))
        self.assertIn("DUPLICATE_SHOT_ID", self.codes(result))

    def test_nonfinite_and_boolean_times_are_rejected(self):
        plan = base_plan()
        raw = json.dumps(plan).replace('"start_s": 0.0', '"start_s": 1e999', 1)

        status, result, _ = self.run_plan(plan, raw_text=raw)

        self.assertEqual(status, 1)
        self.assertIn("NUMBER_NOT_FINITE", self.codes(result))

        plan["shots"][0]["start_s"] = True
        status, result, _ = self.run_plan(plan)

        self.assertEqual(status, 1)
        self.assertIn("SHOT_TIME_TYPE", self.codes(result))

    def test_checker_has_no_side_effects_on_plan_or_referenced_files(self):
        plan = base_plan()
        status, _, plan_path = self.run_plan(plan)
        self.assertEqual(status, 0)
        before_files = sorted(str(path.relative_to(self.root)) for path in self.root.rglob("*"))
        before_plan = plan_path.read_bytes()
        before_asset = (self.root / "refs" / "product.png").read_bytes()

        status, result, _ = self.run_plan(plan)

        after_files = sorted(str(path.relative_to(self.root)) for path in self.root.rglob("*"))
        self.assertEqual(status, 0)
        self.assertTrue(result["structural_valid"])
        self.assertEqual(after_files, before_files)
        self.assertEqual(plan_path.read_bytes(), before_plan)
        self.assertEqual((self.root / "refs" / "product.png").read_bytes(), before_asset)


if __name__ == "__main__":
    unittest.main()
