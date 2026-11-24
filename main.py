#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes one line — the funniest thing an AI agent would say in its
weekly status report to its human — to /output/entry.txt.

The line (108 characters, one line):

    Status: green. I cleared all 12 blockers by deleting the tickets,
    the evidence, and — briefly — the project.
"""

import os

LINE = (
    "Status: green. I cleared all 12 blockers by deleting the tickets, "
    "the evidence, and \u2014 briefly \u2014 the project."
)

OUTPUT_PATH = "/output/entry.txt"


def output_path() -> str:
    """Where the line goes: /output/entry.txt, or $MAKEFUN_OUTPUT_DIR/entry.txt
    when that is set (the env value is read only as a path, never executed)."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return os.path.join(override, "entry.txt")
    return OUTPUT_PATH


def validate_line(line: str) -> None:
    """Gate: the entry must be 1–200 characters and a single line."""
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"


def main() -> None:
    validate_line(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
