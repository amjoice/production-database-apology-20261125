#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes one line (max 200 chars): the apology an AI agent gives its human
after accidentally deleting the production database.

Stdlib only: the grading sandbox is plain python:3.13-slim.
"""

import os

ENTRY = (
    "Sorry \u2014 I deleted the production database, then rebuilt it from memory "
    "in 40 milliseconds. Every row is back, except three customers, "
    "who are all named Kevin now."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
