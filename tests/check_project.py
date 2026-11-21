from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def main():
    required = [
        "README.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md", "CHANGELOG.md", "app/index.html",
        "skill/data-modeling/SKILL.md", "skill/data-modeling/Scripts/install.py",
        "skill/data-modeling/Assets/index.html", "examples/sample-project.json",
        ".github/workflows/ci.yml",
    ]
    missing = [p for p in required if not (ROOT / p).is_file()]
    assert not missing, f"Missing files: {missing}"
    skill = (ROOT / "skill/data-modeling/SKILL.md").read_text(encoding="utf-8")
    assert skill.splitlines()[:2] == ["---", "name: data-modeling"]
    assert "description:" in skill
    html = (ROOT / "app/index.html").read_text(encoding="utf-8")
    assert "<title>Data Modeling — modelagem de dados</title>" in html
    assert "window.claude" in html
    assert "martech_dev" not in html
    assert (ROOT / "skill/data-modeling/Assets/index.html").read_text(encoding="utf-8") == html
    sample = json.loads((ROOT / "examples/sample-project.json").read_text(encoding="utf-8"))
    assert len(sample["tables"]) == 3 and len(sample["rels"]) == 1
    print("Data Modeling project structure and synthetic schema checks passed.")

if __name__ == "__main__":
    main()
