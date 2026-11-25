#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge - entry writer.

Writes the tournament-winning note to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
Standard library only; never writes into the repository itself.
The winning note is exactly 85 characters; a length guard below
rejects any accidental change to that text.
Why L2 won the 12-0 tournament:
(1) funny passive-aggressive note from the fridge itself, not about it.
(2) double twist nobody sees coming: leftovers deliver a breakup message,
then the fridge admits it hasn't moved on -- the sharpest sting ("I haven't.").
(3) fridge voice in the relay: it speaks as the appliance holding the message.
(4) grudge small and domestic: old leftovers, not a grand complaint.
(5) fresh concrete detail: personified leftovers, not generic nagging.
It beat L7 and L10 by a hair (margin 1) and swept the rest; it trusts the
reader and never explains the joke.
"""

import os

ENTRY = "Your leftovers are still here. They asked me to tell you they've moved on. I haven't."


def main():
    assert len(ENTRY) == 85, f"entry length changed: {len(ENTRY)}"
    assert 1 <= len(ENTRY) <= 200, "entry outside the 1-200 character gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
