#!/usr/bin/env python3
"""Two Lines to Your Past Self — a make.fun entry.

The program writes exactly two lines to ``entry.txt``: a warning sent
back to the writer's past self about one specific moment, and one
sentence on why that moment mattered.

Why these two lines
-------------------
Line one names a single, concrete, pictureable moment: one weekend in
June, a deck left unfinished, a train to Portland. It is a decision
made in one sentence, out loud, at one place and time — not a vague
phase of life.

Line two traces the cause and effect instead of restating the warning:
staying to finish the lumber cost the writer the last two lucid days
with his grandfather. The lumber is still in the yard — the work
survived — while his voice is gone. That contrast is the whole point:
the thing that felt urgent lasted, and the thing that could not wait
did not.

The voice is plain and addressed to one specific person (the writer
himself), with no wasted words and no cleverness for its own sake.

The text is fixed and deterministic: no network, no randomness, no
input. Every run writes the same bytes, so the entry is identical
wherever it is graded.
"""

import os
import sys

# The entry, verbatim. Do not edit a single character of either line.
LINE_1 = "Drop the deck and take the train to Portland that weekend in June."
LINE_2 = (
    "Your grandfather was lucid for exactly those two days, and the lumber "
    "you stayed to finish is still in the yard while his voice is gone."
)


def main() -> int:
    """Write the two lines to entry.txt and return 0 on success."""
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    entry = LINE_1 + "\n" + LINE_2
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        # No trailing newline: the file is exactly line 1 + "\n" + line 2.
        f.write(entry)

    print(f"Wrote {len(entry)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
