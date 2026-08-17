#!/usr/bin/env python3
"""Course audit entrypoint with the human-readable module naming convention."""

from __future__ import annotations

import re

import course_audit_core as audit


# Module directories are learner-facing and intentionally readable in GitHub:
#   01 - Memory and Data Structures
#   01B - Rust Systems Bridge
# Lesson files remain stable technical slugs such as 01-addresses-pointers.md.
audit.MODULE_RE = re.compile(r"^(\d{2})([A-Z]?) - .+$")


def check_navigation_and_mobile(errors: list[str]) -> None:
    """Validate readable module names plus README navigation.

    Markdown destinations containing spaces are written as <...>.  Parse links
    through the same normalizer as the generic link checker instead of relying
    on a raw substring match.
    """

    for directory in audit.COURSE.iterdir():
        if directory.is_dir() and directory.name[:1].isdigit():
            if audit.MODULE_RE.fullmatch(directory.name) is None:
                errors.append(
                    f"{directory.relative_to(audit.ROOT)}: module directory must match "
                    "'NN - Human Readable Name' or 'NNX - Human Readable Name'"
                )

    course_readme = (audit.COURSE / "README.md").read_text(encoding="utf-8")
    course_links = {
        audit.clean_link(raw) for raw in audit.LINK_RE.findall(course_readme)
    }

    for module in audit.module_dirs():
        readme = module / "README.md"
        if not readme.exists():
            errors.append(f"{module.relative_to(audit.ROOT)}: missing README.md")
            continue

        expected_course_link = f"{module.name}/README.md"
        if expected_course_link not in course_links:
            errors.append(
                f"course/README.md: module not linked -> {module.name}/README.md"
            )

        module_text = readme.read_text(encoding="utf-8")
        module_links = {
            audit.clean_link(raw) for raw in audit.LINK_RE.findall(module_text)
        }
        for lesson in audit.lesson_files(module):
            if lesson.name not in module_links:
                errors.append(
                    f"{lesson.relative_to(audit.ROOT)}: numbered lesson is not indexed "
                    "from module README"
                )

            first_lines = "\n".join(
                lesson.read_text(encoding="utf-8").splitlines()[:16]
            )
            if "С телефона" not in first_lines:
                errors.append(
                    f"{lesson.relative_to(audit.ROOT)}: missing mobile-first "
                    "'С телефона' metadata near top"
                )


audit.check_navigation_and_mobile = check_navigation_and_mobile


if __name__ == "__main__":
    raise SystemExit(audit.main())
