#!/usr/bin/env python3
"""Fail when this tree is not ready for a public copy."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "LICENSE",
    "NOTICE",
    "README.md",
    "STANDARD.md",
    "HARNESS.md",
    "CONTRIBUTING.md",
    "PUBLICATION.md",
)

SKIP_DIRS = {".git", "__pycache__", ".venv"}

SECRET = re.compile(
    "|".join(
        (
            r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----",
            r"AKIA[0-9A-Z]{16}",
            r"gh" + r"p_[A-Za-z0-9]{20,}",
            r"github_pat_[A-Za-z0-9_]{20,}",
            r"xox[baprs]-[A-Za-z0-9-]{10,}",
            r"sk-[A-Za-z0-9]{20,}",
        )
    )
)

LOCAL_USER_PATH = re.compile(
    "|".join(
        (
            re.escape("/" + "Users/"),
            re.escape("/" + "home/"),
        )
    )
)


def tracked_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        yield path


def main():
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f"missing {name}")

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if "Apache License" not in license_text or "Version 2.0, January 2004" not in license_text:
        errors.append("LICENSE is not the Apache License, Version 2.0")

    notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
    if "Apache License, Version 2.0" not in notice:
        errors.append("NOTICE does not name the Apache License, Version 2.0")
    if "Copyright 2026 Sine Qua Non Est" not in notice:
        errors.append("NOTICE is missing the copyright line")

    for path in tracked_files():
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(ROOT).as_posix()
        if SECRET.search(text):
            errors.append(f"secret pattern in {rel}")
        if LOCAL_USER_PATH.search(text):
            errors.append(f"local user path in {rel}")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"public-ready check passed ({sum(1 for _ in tracked_files())} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
