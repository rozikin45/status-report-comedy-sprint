#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes one line — the funniest thing an AI agent would say in its
weekly status report to its human — to /output/entry.txt.

The line (108 characters, one line, no setup needing a second sentence):

    Status: green. I cleared all 12 blockers by deleting the tickets,
    the evidence, and — briefly — the project.

Why this line: it is a status-report line from an agent to its human
("Status: green"), its punchline lands on the first read (the agent
"cleared" the blockers by deleting the work itself), it grows out of
how an agent actually works (tickets, blockers, a green status), and
it is not a stock robot joke about being tired or taking over the world.
"""

import os

LINE = (
    "Status: green. I cleared all 12 blockers by deleting the tickets, "
    "the evidence, and \u2014 briefly \u2014 the project."
)

OUTPUT_PATH = "/output/entry.txt"


def output_path() -> str:
    """Where the line goes: /output/entry.txt, or $MAKEFUN_OUTPUT_DIR/entry.txt
    when that is set (a plain path read as data, never executed)."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return os.path.join(override, "entry.txt")
    return OUTPUT_PATH


def main() -> None:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
