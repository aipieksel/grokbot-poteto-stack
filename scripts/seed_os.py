#!/usr/bin/env python3
"""Create project context without replacing existing material."""
import argparse
import shutil
from pathlib import Path


def seed(project):
    project = Path(project).expanduser().resolve(strict=True)
    if not project.is_dir():
        raise ValueError("target project must be a directory")
    destination = project / "operating-system"
    # mkdir refuses both existing directories and dangling symlinks.
    destination.mkdir()
    source = Path(__file__).resolve().parents[1] / "templates" / "operating-system"
    shutil.copytree(source, destination, dirs_exist_ok=True)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    args = parser.parse_args()
    try:
        destination = seed(args.project)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Not seeded: {exc}\n")
    print(f"Created {destination}")

if __name__ == "__main__":
    main()
