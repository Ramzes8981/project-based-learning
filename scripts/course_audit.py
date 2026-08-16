#!/usr/bin/env python3
"""Static integrity checks for the self-contained learner path."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "course"

ALLOWED_EXTERNAL_FILES = {
    COURSE / "OPTIONAL_READING.md",
    COURSE / "SOURCE_MATRIX.md",
    COURSE / "ENVIRONMENT.md",
}

REQUIRED_PROJECT_DOCS = {"README.md", "SPEC.md", "ACCEPTANCE.md", "TESTS.md", "HINTS.md"}
MARKERS = ("cite", "filecite", "memcite", "sandbox:/")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://", re.IGNORECASE)


def markdown_files() -> list[Path]:
    return sorted(COURSE.rglob("*.md"))


def is_code_fence_toggle(line: str) -> bool:
    return line.lstrip().startswith("```")


def check_text(path: Path, text: str, errors: list[str]) -> None:
    for marker in MARKERS:
        if marker in text:
            errors.append(f"{path.relative_to(ROOT)}: internal marker {marker!r}")

    in_fence = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if is_code_fence_toggle(line):
            in_fence = not in_fence
        if not in_fence and PLACEHOLDER_RE.search(line):
            errors.append(f"{path.relative_to(ROOT)}:{lineno}: unresolved placeholder")

    if path not in ALLOWED_EXTERNAL_FILES and URL_RE.search(text):
        errors.append(f"{path.relative_to(ROOT)}: external URL outside optional/reference file")


def clean_link(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1]
    for marker in (' "', " '"):
        if marker in raw:
            raw = raw.split(marker, 1)[0]
    return unquote(raw)


def check_links(path: Path, text: str, errors: list[str]) -> None:
    for raw in LINK_RE.findall(text):
        target = clean_link(raw)
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: link escapes repo: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken relative link -> {target}")


def check_projects(errors: list[str]) -> None:
    for spec in COURSE.rglob("SPEC.md"):
        directory = spec.parent
        names = {p.name for p in directory.iterdir() if p.is_file()}
        missing = sorted(REQUIRED_PROJECT_DOCS - names)
        if missing:
            errors.append(f"{directory.relative_to(ROOT)}: missing project docs {', '.join(missing)}")


def check_duplicate_lesson_prefixes(errors: list[str]) -> None:
    for module in [p for p in COURSE.iterdir() if p.is_dir() and re.match(r"^\d", p.name)]:
        seen: dict[str, Path] = {}
        for path in module.glob("*.md"):
            if path.name.endswith(".solution.md") or path.name == "README.md":
                continue
            match = re.match(r"^(\d{2}[a-z]?)-", path.name)
            if not match:
                continue
            prefix = match.group(1)
            if prefix in seen:
                errors.append(
                    f"{module.relative_to(ROOT)}: duplicate lesson prefix {prefix}: "
                    f"{seen[prefix].name}, {path.name}"
                )
            seen[prefix] = path


def gha_escape(text: str) -> str:
    return text.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def main() -> int:
    errors: list[str] = []
    if not COURSE.is_dir():
        print("course directory not found", file=sys.stderr)
        return 2

    files = markdown_files()
    for path in files:
        text = path.read_text(encoding="utf-8")
        check_text(path, text, errors)
        check_links(path, text, errors)

    check_projects(errors)
    check_duplicate_lesson_prefixes(errors)

    if errors:
        print(f"course audit: FAIL ({len(errors)} issue(s))")
        for error in errors:
            print(" -", error)
            if os.environ.get("GITHUB_ACTIONS") == "true":
                print(f"::error title=Course audit::{gha_escape(error)}")
        return 1

    print(f"course audit: PASS ({len(files)} markdown files checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
