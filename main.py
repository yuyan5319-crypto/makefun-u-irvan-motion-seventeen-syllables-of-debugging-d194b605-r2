#!/usr/bin/env python3
"""It Calls My Name -- one haiku about debugging (5-7-5).

Writes the haiku to <MAKEFUN_OUTPUT_DIR>/entry.txt, or ./output/entry.txt
when MAKEFUN_OUTPUT_DIR is not set. Standard library only.
"""

import os
import sys

HAIKU = (
    "a breakpoint holds still\n"
    "the log line I buried wakes\n"
    "it calls me by name\n"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    out_path = os.path.join(out_dir, "entry.txt")

    # Gate validation: 1-200 characters, exactly three lines, not only whitespace.
    text = HAIKU
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 chars, got {len(text)}", file=sys.stderr)
        return 1
    lines = text.strip("\n").split("\n")
    if len(lines) != 3:
        print(f"entry must be exactly 3 lines, got {len(lines)}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {out_path} ({len(text)} chars, 3 lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
