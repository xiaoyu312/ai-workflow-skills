from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PackageChecks(unittest.TestCase):
    def test_local_markdown_references_resolve(self):
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\[[^]\n]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                target = target.split("#", 1)[0]
                if not target or re.match(r"[a-z]+://", target):
                    continue
                self.assertFalse(Path(target).is_absolute(), (path.name, "absolute link"))
                self.assertTrue((path.parent / target).resolve().is_relative_to(ROOT), (path.name, "outside package"))
                self.assertTrue((path.parent / target).exists(), (path.name, target))

    def test_generator_reproduces_examples(self):
        files = sorted((ROOT / "examples").glob("*"))
        before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.is_file()}
        subprocess.run([sys.executable, "-B", str(ROOT / "scripts/generate_demo.py")], check=True, capture_output=True)
        self.assertEqual(before, {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.is_file()})

    def test_skill_has_metadata_and_no_private_media(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\n"))
        self.assertRegex(skill, r"(?m)^name: [a-z0-9-]+$")
        self.assertRegex(skill, r"(?m)^description: .+")
        for path in ROOT.rglob("*"):
            self.assertFalse(path.is_symlink())
            self.assertNotIn(path.suffix.lower(), {".mp4", ".mp3", ".wav", ".jpg", ".png", ".sqlite", ".db", ".xlsx", ".pdf", ".pem", ".key"})

    def test_synthetic_data_is_explicit_and_coherent(self):
        data=json.loads((ROOT/"examples/demo.json").read_text())
        self.assertEqual(data["classification"],"synthetic_demo")
        self.assertEqual(data["label"],"模拟数据 DEMO")
        if "weeks" in data:
            for row in data["weeks"]:
                self.assertAlmostEqual(row["roi"],row["gmv"]/row["spend"])
                self.assertAlmostEqual(row["roi"],row["cvr"]*row["aov"]/row["cpc"])
            self.assertEqual(sum(x["spend"] for x in data["current_scenes"]),data["weeks"][-1]["spend"])
            self.assertEqual(sum(x["gmv"] for x in data["current_scenes"]),data["weeks"][-1]["gmv"])
        if "product" in data:
            self.assertTrue(data["product"]["unknown_facts"])
            self.assertEqual(data["final_status"],"补信息后可拍")
        css=ROOT/"tokens/colors_and_type.css"
        if css.exists():
            text=css.read_text()
            declared=set(re.findall(r"(--[a-z0-9-]+)\s*:",text))
            used=set(re.findall(r"var\((--[a-z0-9-]+)\)",text))
            self.assertTrue(used <= declared)

if __name__ == "__main__":
    unittest.main()
