#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

One line (max 200 chars): the apology an AI agent gives its human after
accidentally deleting the production database. The line is assembled from
named parts so the wording stays reviewable, then validated before writing.

Stdlib only: the grading sandbox is plain python:3.13-slim (no Pillow).
"""

import os
import sys

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

# The apology, in three named beats: the confession, the rebuild, the catch.
CONFESSION = "Sorry \u2014 I deleted the production database, "
REBUILD = "then rebuilt it from memory in 40 milliseconds. "
AFTERMATH = "Every row is back, except three customers, who are all named Kevin now."


def build_entry() -> str:
    """Assemble the single apology line from its named parts."""
    parts = [CONFESSION, REBUILD, AFTERMATH]
    return "".join(parts)


def validate_entry(line: str) -> str:
    """Check the line fits the bounty rules: 1-200 chars, exactly one line."""
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def write_entry(line: str, path: str = OUTPUT_PATH) -> None:
    """Write the validated line to the output file, creating its directory."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


def main() -> int:
    entry = validate_entry(build_entry())
    write_entry(entry)
    print(f"wrote {len(entry)}-char entry to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
