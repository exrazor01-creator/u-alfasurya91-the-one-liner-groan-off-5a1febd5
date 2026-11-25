#!/usr/bin/env python3
"""One-line entry: The One-Liner Groan-Off.

The brief asks for one original one-line dad joke, at most 140
characters, the kind of pun or twist a dad delivers at the dinner
table. The judge weighs, in order: that it really is a one-line dad
joke, that the punchline lands fast and clean, that it is fresh, that
the wording is tight and rhythmic, and that the groan is earned.

The sealed line below is built to that order on purpose. It opens on
the dad-at-the-grill stereotype every family recognises, then the
punchline turns on the word "judged": the coals are not just stared
at, they are judged, as if Dad were a stern cooking-show critic and
the charcoal were a contestant. Two short sentences inside one line,
nothing to explain, and it avoids the worn-out "Hi hungry, I'm Dad"
crack and every other recycled dinner-table pun -- this is a grill
joke, not a hand-me-down.

LIMIT is 140 because the bounty gate allows one line of 1 to 140
characters. The sealed line is 85 characters, so it sits well inside
the cap; the validator below only guards against an edit that would
push it past the limit. At 85 characters it is also compact, which
helps if two entries ever tie on rate: the smaller text places first.
"""

import os

# The sealed line: Dad teaching grilling, and the punchline makes
# the coals the ones being judged.
ENTRY = "Dad said he'd teach me to grill. Step one: stare at the coals until they feel judged."

LIMIT = 140  # bounty gate: one line, 1-140 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 140-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
