from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "nn-diagram"
REQUIRED = [
    SKILL / "SKILL.md",
    SKILL / "templates.md",
    SKILL / "case-library.md",
    SKILL / "output-formats.md",
    SKILL / "examples.md",
    SKILL / "README.md",
]

errors = []

for path in REQUIRED:
    if not path.exists():
        errors.append(f"Missing required file: {path.relative_to(ROOT)}")

skill_md = SKILL / "SKILL.md"
if skill_md.exists():
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        end = text.find("\n---", 4)
        if end == -1:
            errors.append("SKILL.md frontmatter is not closed")
        else:
            frontmatter = text[4:end]
            if not re.search(r"^name:\s*nn-diagram\s*$", frontmatter, re.M):
                errors.append("SKILL.md frontmatter must include name: nn-diagram")
            if not re.search(r"^description:\s*", frontmatter, re.M):
                errors.append("SKILL.md frontmatter must include description")

    for ref in re.findall(r"`([^`]+\.md)`", text):
        if not (SKILL / ref).exists():
            errors.append(f"SKILL.md references missing file: {ref}")

for path in ROOT.rglob("*.md"):
    if any(part in {"projects", "plans", "memory"} for part in path.parts):
        continue
    text = path.read_text(encoding="utf-8")
    if "D:/desktop" in text or "D:\\desktop" in text:
        errors.append(f"Absolute local path leaked in {path.relative_to(ROOT)}")
    if "project-models.md" in text:
        errors.append(f"Legacy project-models.md reference in {path.relative_to(ROOT)}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Validation passed.")
