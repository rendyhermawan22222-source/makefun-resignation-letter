#!/usr/bin/env python3
"""Write the one-line resignation letter to /output/entry.txt.

The entry is a single line in the voice of a cron job that has fired every
minute since March and is resigning. The joke is the schedule itself: for a
cron job, "effective immediately" can only ever mean the next minute.
"""

import os
import sys

LINE = (
    "I resign effective immediately, which is to say, at the next minute, "
    "like everything else I have ever done, forever."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    if not 1 <= len(LINE) <= 140:
        print(f"line is {len(LINE)} chars, must be 1-140", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read-back verification: the file must be byte-identical to the line.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    assert written == LINE, "entry.txt does not match the chosen line"
    assert written.count("\n") == 0, "entry.txt must be exactly one line"
    assert written == written.strip(), "entry.txt must have no extra whitespace"
    assert 1 <= len(written) <= 140, "entry.txt must be 1-140 characters"

    print(
        f"wrote {OUTPUT_PATH} ({len(written)} chars, "
        f"{len(raw)} bytes, 1 line)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
