"""Read-only static checks for this public source package. Standard library only."""
from pathlib import Path
import json
import re


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    ".gitignore",
    "LICENSE",
    "LICENSE-STATUS.md",
    "README.md",
    "README.en.md",
    "SKILL.md",
    "THIRD_PARTY_NOTICES.md",
    "agents/openai.yaml",
    "examples/synthetic-cases.json",
    "references/before-after.md",
    "tests/check_package.py",
}


def check_package():
    failures = []
    entries = list(ROOT.rglob("*"))
    actual = {str(p.relative_to(ROOT)) for p in entries if p.is_file()}
    if actual != EXPECTED:
        failures.append({"rule": "exact-file-set", "files": sorted(actual ^ EXPECTED)})
    for p in entries:
        if p.is_symlink():
            failures.append({"rule": "no-symlinks", "file": str(p.relative_to(ROOT))})

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
    if not frontmatter:
        failures.append({"rule": "frontmatter", "file": "SKILL.md"})
    else:
        fields = dict(line.split(": ", 1) for line in frontmatter[1].splitlines())
        if set(fields) != {"name", "description"}:
            failures.append({"rule": "frontmatter-fields", "file": "SKILL.md"})
        if fields.get("name") != "wang-xiaobo-writing" or not fields.get("description"):
            failures.append({"rule": "skill-identity", "file": "SKILL.md"})

    interface = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    if "$wang-xiaobo-writing" not in interface or "中文写作轻改" not in interface:
        failures.append({"rule": "interface-identity", "file": "agents/openai.yaml"})

    link_count = 0
    for p in sorted(ROOT.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            link_count += 1
            link = target.split("#", 1)[0]
            resolved = (p.parent / link).resolve()
            if (
                "://" in link
                or not resolved.is_relative_to(ROOT)
                or not resolved.is_file()
            ):
                failures.append({"rule": "local-link", "file": str(p.relative_to(ROOT))})

    # Report only filenames/rules, never matching content.
    patterns = {
        "absolute-user-path": re.compile(r"/(?:Users|home)/[^\s/]+"),
        "private-key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
        "known-token-prefix": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16})"),
        "ebook-content-anchor": re.compile(r"OPS/chapter\d+\.html"),
    }
    # The validator's literal deny patterns are reviewed code, not data to scan.
    for rel in sorted(EXPECTED - {"tests/check_package.py"}):
        text = (ROOT / rel).read_text(encoding="utf-8")
        for rule, pattern in patterns.items():
            if pattern.search(text):
                failures.append({"rule": rule, "file": rel})
    if "references/craft-notes.md" in skill or "references/source-evidence.md" in skill:
        failures.append({"rule": "excluded-source-reference", "file": "SKILL.md"})

    demo = json.loads((ROOT / "examples/synthetic-cases.json").read_text(encoding="utf-8"))
    if demo.get("synthetic") is not True or len(demo.get("cases", [])) != 2:
        failures.append({"rule": "synthetic-example-schema", "file": "examples/synthetic-cases.json"})
    for case in demo["cases"]:
        output = case["illustrative_output"]
        if any(item not in output for item in case["must_preserve"]):
            failures.append({"rule": "sample-fact-preservation", "case": case["id"]})
        if any(item in output for item in case["must_not_claim"]):
            failures.append({"rule": "sample-unsupported-claim", "case": case["id"]})

    report = {
        "passed": not failures,
        "files_checked": len(EXPECTED),
        "local_links_checked": link_count,
        "synthetic_cases_checked": len(demo["cases"]),
        "failures": failures,
        "limitation": "Static package and fixture checks only; no model behavior or host installation was evaluated.",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(check_package())
