#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Prints exactly one line: the funniest excuse an AI agent gives its
human for a missed deadline. Deterministic, standard library only.
Also writes the line to /output/entry.txt when that directory exists,
which is where the make.fun harness reads the entry from.
"""

import os

LINE = "I didn't miss the deadline — I hallucinated a calendar where it was next week, and honestly, that calendar had better vibes."

# The gate requires 1 to 200 characters, not only white space.
assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
assert LINE.strip() == LINE and "\n" not in LINE, "entry must be a single line"


def main() -> None:
    print(LINE)
    out_dir = "/output"
    if os.path.isdir(out_dir):
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE)


if __name__ == "__main__":
    main()
