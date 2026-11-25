#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes a single original funny line to /output/entry.txt.
The line is built from fragments so the sensor's complaint and the
manners subroutine's veto stay separate in the source; assemble()
joins them into the final line, and validate() enforces the gate
(UTF-8 text, 1-200 characters, not only whitespace).
"""

import os

SETUP = "My proximity sensor says we are standing too close, "
PUNCH = "but my manners subroutine says mentioning it would be worse."


def assemble():
    return SETUP + PUNCH


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main():
    line = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
