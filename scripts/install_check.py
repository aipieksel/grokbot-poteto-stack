#!/usr/bin/env python3
import json
import re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
errors = []
for path in root.rglob("*.md"):
    for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        if ":" in link or link.startswith("#"):
            continue
        if not (path.parent / link.split("#")[0]).exists():
            errors.append(f"{path.relative_to(root)}: {link}")
for path in (root / "templates").rglob("*.json"):
    if json.loads(path.read_text()) != []:
        errors.append(f"nonempty starter state: {path.name}")
required = ["SKILL.md", "scripts/seed_os.py", "templates/operating-system/agents/operator.md"]
errors += [f"missing {name}" for name in required if not (root / name).is_file()]
if errors:
    raise SystemExit("\n".join(errors))
print("PASS: package links and starter templates")
