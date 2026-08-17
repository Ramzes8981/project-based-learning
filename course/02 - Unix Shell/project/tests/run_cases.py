#!/usr/bin/env python3
"""Small black-box smoke harness for the course shell.

Usage:
    python3 project/tests/run_cases.py ./path/to/shell

This does not encode the shell implementation. It only exercises external stdin/stdout behavior.
"""

from __future__ import annotations

import pathlib
import subprocess
import sys
import tempfile


def run(shell: str, script: str, cwd: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [shell],
        input=script,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd,
        timeout=5,
        check=False,
    )


def require(condition: bool, message: str, result: subprocess.CompletedProcess[str] | None = None) -> None:
    if condition:
        return
    if result is not None:
        print("stdout:\n" + result.stdout)
        print("stderr:\n" + result.stderr, file=sys.stderr)
    raise SystemExit("FAIL: " + message)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: run_cases.py /absolute/or/relative/path/to/shell")

    shell = str(pathlib.Path(sys.argv[1]).resolve())

    r = run(shell, "printf COURSE_MARKER\\n\nexit\n")
    require("COURSE_MARKER" in r.stdout, "external command output missing", r)

    r = run(shell, "definitely_missing_course_command\nprintf AFTER_FAIL\\n\nexit\n")
    require("AFTER_FAIL" in r.stdout, "shell did not continue after exec failure", r)

    with tempfile.TemporaryDirectory() as td:
        r = run(shell, "pwd\ncd /\npwd\nexit\n", cwd=td)
        lines = [line.strip() for line in r.stdout.splitlines()]
        require("/" in lines or any(line.endswith(" /") for line in lines), "cd/pwd behavior not observed", r)

        out = pathlib.Path(td) / "out.txt"
        r = run(shell, f"printf REDIR > {out}\nexit\n", cwd=td)
        require(out.exists() and "REDIR" in out.read_text(), "output redirection failed", r)

    r = run(shell, "printf abc | wc -c\nexit\n")
    require(any(token == "3" for token in r.stdout.split()), "pipeline smoke case failed", r)

    print("black-box smoke cases: PASS")


if __name__ == "__main__":
    main()
