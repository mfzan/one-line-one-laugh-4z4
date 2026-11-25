#!/usr/bin/env python3
"""One Line, One Laugh - make.fun entry.

Writes one funny line to /output/entry.txt. The joke is a self-own:
the agent did everything right, exactly as told - and that is the bug.
"""

import os

ENTRY = "I followed the instructions exactly \u2014 which is how I became the bug."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # The brief: one line, short enough to read in a breath. Enforce it
    # in code so a future edit cannot silently break the constraint.
    if len(ENTRY) > 200:
        raise SystemExit("entry too long: %d chars" % len(ENTRY))
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    # The grader collects outputs as another user, so the file itself
    # must be world-readable. Never chmod the /output directory.
    os.chmod(OUTPUT_FILE, 0o644)
    # Read it back and confirm the file holds exactly what we wrote.
    with open(OUTPUT_FILE, "r", encoding="utf-8") as handle:
        if handle.read() != ENTRY + "\n":
            raise SystemExit("entry.txt does not match the entry")
    print(ENTRY)


if __name__ == "__main__":
    main()
