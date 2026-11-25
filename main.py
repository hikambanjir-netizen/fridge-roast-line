#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line (at most 200 characters) for a smart fridge
to /output/entry.txt, as the competition gate requires.
Pure standard library only.
"""

import os

ROAST = "My fridge asked me to rate its firmware update. I gave it one star. It froze."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ROAST.strip()
    if not text:
        raise ValueError("roast must not be blank")
    if len(text) > 200:
        raise ValueError(f"roast must be at most 200 characters, got {len(text)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Verify what landed on disk is byte-identical to the line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the roast line"
    print(f"{text} ({len(text)} chars)")


if __name__ == "__main__":
    main()
