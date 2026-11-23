"""One Letter for Your Day — entry program.

The entry is exactly one character: the letter H.

Hidden word behind H: "hangry" — hungry to the point of irritable.
A whole day distilled to one sensation: skipped lunch, stomach growling,
temper shortening with every unread message. It is vivid (you can picture
the person snapping at nothing over an empty stomach), funny (the word
itself is a joke everyone repeats), and true (a real, ordinary day's
report, not a performance). H is also the letter a judge most readily
reads as "hangry": it is the standout H day-word, unlike the generic
happy/hungry, and unlike the flooded Z (zero sleep), U (unhinged),
X (exhausted) and O (overtime) letters already crowding this field.

The program writes exactly that one letter, and nothing else, to
/output/entry.txt — no word, no gloss, no punctuation, no newline.
"""

import os
import sys

LETTER = "H"
DEFAULT_OUTPUT_DIR = "/output"


def main() -> int:
    # Gate guard: the entry must be exactly one A-Z letter, nothing else.
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", LETTER
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Verify what was actually written: one byte, the letter, no newline.
    with open(entry_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LETTER, repr(written)
    print(LETTER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
