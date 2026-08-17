#!/usr/bin/env python3
"""Static integrity and curriculum dependency checks for the learner path."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "course"
MANIFEST = COURSE / "CONCEPT_DEPENDENCIES.json"

ALLOWED_EXTERNAL_FILES = {
    COURSE / "OPTIONAL_READING.md",
    COURSE / "SOURCE_MATRIX.md",
    COURSE / "ENVIRONMENT.md",
}
PLACEHOLDER_EXEMPT_FILES = {COURSE / "AUTHORING_STANDARD.md"}
REQUIRED_PROJECT_DOCS = {"README.md", "SPEC.md", "ACCEPTANCE.md", "TESTS.md", "HINTS.md"}
MARKERS = ("cite", "filecite", "memcite", "sandbox:/")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://", re.IGNORECASE)
MODULE_RE = re.compile(r"^(\d+)([a-z]?)")
LESSON_RE = re.compile(r"^(\d{2})([a-z]?)-.+\.md$")
ASCII_TOKEN_RE = re.compile(r"^[a-z0-9_-]+$")


def markdown_files() -> list[Path]:
    return sorted(COURSE.rglob("*.md"))


def suffix_rank(value: str) -> int:
    return 0 if not value else ord(value.lower()) - ord("a") + 1


def module_sort_key(path: Path) -> tuple[int, int, str]:
    match = MODULE_RE.match(path.name)
    if not match:
        return (10_000, 0, path.name)
    return (int(match.group(1)), suffix_rank(match.group(2)), path.name)


def lesson_sort_key(path: Path) -> tuple[int, int, str]:
    match = LESSON_RE.match(path.name)
    if not match:
        return (10_000, 0, path.name)
    return (int(match.group(1)), suffix_rank(match.group(2)), path.name)


def module_dirs() -> list[Path]:
    return sorted(
        [p for p in COURSE.iterdir() if p.is_dir() and MODULE_RE.match(p.name)],
        key=module_sort_key,
    )


def lesson_files(module: Path) -> list[Path]:
    return sorted(
        [
            p
            for p in module.glob("*.md")
            if LESSON_RE.match(p.name) and not p.name.endswith(".solution.md")
        ],
        key=lesson_sort_key,
    )


def course_position(path: Path) -> tuple[int, int, int, int, str]:
    rel = path.relative_to(COURSE)
    if len(rel.parts) < 2:
        raise ValueError(f"not a module lesson: {rel}")
    module_name, lesson_name = rel.parts[0], rel.parts[-1]
    mm = MODULE_RE.match(module_name)
    lm = LESSON_RE.match(lesson_name)
    if not mm or not lm:
        raise ValueError(f"not an ordered lesson: {rel}")
    return (
        int(mm.group(1)),
        suffix_rank(mm.group(2)),
        int(lm.group(1)),
        suffix_rank(lm.group(2)),
        lesson_name,
    )


def check_text(path: Path, text: str, errors: list[str]) -> None:
    for marker in MARKERS:
        if marker in text:
            errors.append(f"{path.relative_to(ROOT)}: internal marker {marker!r}")

    in_fence = False
    if path not in PLACEHOLDER_EXEMPT_FILES:
        for lineno, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("```"):
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
            errors.append(
                f"{directory.relative_to(ROOT)}: missing project docs {', '.join(missing)}"
            )


def check_duplicate_lesson_prefixes(errors: list[str]) -> None:
    for module in module_dirs():
        seen: dict[str, Path] = {}
        for path in lesson_files(module):
            match = re.match(r"^(\d{2}[a-z]?)-", path.name)
            assert match is not None
            prefix = match.group(1)
            if prefix in seen:
                errors.append(
                    f"{module.relative_to(ROOT)}: duplicate lesson prefix {prefix}: "
                    f"{seen[prefix].name}, {path.name}"
                )
            seen[prefix] = path


def check_orphan_solutions(errors: list[str]) -> None:
    for solution in COURSE.rglob("*.solution.md"):
        lesson_name = solution.name.removesuffix(".solution.md") + ".md"
        lesson = solution.with_name(lesson_name)
        if not lesson.exists():
            errors.append(
                f"{solution.relative_to(ROOT)}: orphan solution; missing lesson {lesson.name}"
            )


def check_navigation_and_mobile(errors: list[str]) -> None:
    course_readme = (COURSE / "README.md").read_text(encoding="utf-8")

    for module in module_dirs():
        readme = module / "README.md"
        if not readme.exists():
            errors.append(f"{module.relative_to(ROOT)}: missing README.md")
            continue

        expected_course_link = f"({module.name}/README.md)"
        if expected_course_link not in course_readme:
            errors.append(f"course/README.md: module not linked -> {module.name}/README.md")

        module_text = readme.read_text(encoding="utf-8")
        for lesson in lesson_files(module):
            if f"]({lesson.name})" not in module_text:
                errors.append(
                    f"{lesson.relative_to(ROOT)}: numbered lesson is not indexed from module README"
                )

            first_lines = "\n".join(lesson.read_text(encoding="utf-8").splitlines()[:16])
            if "С телефона" not in first_lines:
                errors.append(
                    f"{lesson.relative_to(ROOT)}: missing mobile-first 'С телефона' metadata near top"
                )


def semantic_lines(path: Path) -> list[tuple[int, str]]:
    result: list[tuple[int, str]] = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith(("←", "→", "↑")):
            continue
        # Link destinations are navigation paths, not learner-facing teaching prose.
        visible = re.sub(r"\]\([^)]+\)", "]", line)
        result.append((lineno, visible.casefold()))
    return result


def guard_matches(term: str, line: str) -> bool:
    """Match manifest guard terms conservatively to avoid noisy semantic lint.

    ASCII identifiers such as ELF/TLB/SLO/socket use token boundaries so `elf`
    does not match `self` and `slo` does not match `slow`. Multi-word phrases
    and deliberate Russian stems use substring matching.
    """
    folded = term.casefold()
    if ASCII_TOKEN_RE.fullmatch(folded):
        return re.search(
            rf"(?<![a-z0-9_]){re.escape(folded)}(?![a-z0-9_])", line
        ) is not None
    return folded in line


def check_concept_manifest(errors: list[str]) -> None:
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"course/CONCEPT_DEPENDENCIES.json: cannot load: {exc}")
        return

    if data.get("schema_version") != 2:
        errors.append("course/CONCEPT_DEPENDENCIES.json: schema_version must be 2")

    concepts = data.get("concepts")
    if not isinstance(concepts, list):
        errors.append("course/CONCEPT_DEPENDENCIES.json: concepts must be a list")
        return

    by_name: dict[str, dict[str, object]] = {}
    for raw in concepts:
        if not isinstance(raw, dict) or not isinstance(raw.get("name"), str):
            errors.append("course/CONCEPT_DEPENDENCIES.json: every concept needs string name")
            continue
        name = raw["name"]
        if name in by_name:
            errors.append(f"course/CONCEPT_DEPENDENCIES.json: duplicate concept {name}")
            continue
        by_name[name] = raw

    positions: dict[str, tuple[int, int, int, int, str]] = {}
    for name, raw in by_name.items():
        first = raw.get("first_introduced_in")
        if not isinstance(first, str):
            errors.append(f"concept {name}: missing first_introduced_in")
            continue
        path = ROOT / first
        if not path.exists():
            errors.append(f"concept {name}: first introduction does not exist -> {first}")
            continue
        try:
            positions[name] = course_position(path)
        except ValueError as exc:
            errors.append(f"concept {name}: {exc}")

        requires = raw.get("requires", [])
        if not isinstance(requires, list) or not all(isinstance(x, str) for x in requires):
            errors.append(f"concept {name}: requires must be list[str]")

        guard_terms = raw.get("guard_terms", [])
        if not isinstance(guard_terms, list) or not all(isinstance(x, str) for x in guard_terms):
            errors.append(f"concept {name}: guard_terms must be list[str]")

    for name, raw in by_name.items():
        if name not in positions:
            continue
        for dependency in raw.get("requires", []):
            if dependency not in by_name:
                errors.append(f"concept {name}: unknown prerequisite {dependency}")
                continue
            if dependency in positions and positions[dependency] > positions[name]:
                errors.append(
                    f"concept {name}: prerequisite {dependency} is introduced later"
                )

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(name: str, trail: list[str]) -> None:
        if name in visited:
            return
        if name in visiting:
            errors.append(
                "course/CONCEPT_DEPENDENCIES.json: dependency cycle -> "
                + " -> ".join(trail + [name])
            )
            return
        visiting.add(name)
        for dependency in by_name.get(name, {}).get("requires", []):
            if dependency in by_name:
                visit(dependency, trail + [name])
        visiting.remove(name)
        visited.add(name)

    for name in by_name:
        visit(name, [])

    ordered_lessons = [lesson for module in module_dirs() for lesson in lesson_files(module)]
    lesson_positions = {lesson: course_position(lesson) for lesson in ordered_lessons}

    for name, raw in by_name.items():
        if name not in positions:
            continue
        first_position = positions[name]
        guard_terms = [term for term in raw.get("guard_terms", []) if term]
        if not guard_terms:
            continue
        for lesson, position in lesson_positions.items():
            if position >= first_position:
                continue
            for lineno, line in semantic_lines(lesson):
                matched = next((term for term in guard_terms if guard_matches(term, line)), None)
                if matched is not None:
                    errors.append(
                        f"{lesson.relative_to(ROOT)}:{lineno}: guarded term {matched!r} "
                        f"appears before concept {name!r} is introduced"
                    )
                    break


def gha_escape(text: str) -> str:
    return text.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def main() -> int:
    errors: list[str] = []
    files = markdown_files()
    for path in files:
        text = path.read_text(encoding="utf-8")
        check_text(path, text, errors)
        check_links(path, text, errors)

    check_projects(errors)
    check_duplicate_lesson_prefixes(errors)
    check_orphan_solutions(errors)
    check_navigation_and_mobile(errors)
    check_concept_manifest(errors)

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
