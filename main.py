#!/usr/bin/env python3
"""One-line excuse for a missed deadline, written to /output/entry.txt.

The gag: a worker who did submit on time, by the clock on their own
laptop — only the laptop was set to the wrong office. The deadline is
personified as a colleague who has already clocked out, eaten, and
gone to bed, so the excuse lands as a shrug, not a plea. Tightened in
revision: the clock became the laptop clock, the office became Sydney
itself, so every word earns its place.
"""

from pathlib import Path

# The line is assembled from three movements: the claim, the catch, the sting.
BEATS = (
    "I submitted it at 11:59, ",
    "only my laptop clock was set to the Sydney office, ",
    "so the deadline had already left, had dinner, and gone to bed.",
)

OUT = Path("/output/entry.txt")


def compose() -> str:
    return "".join(BEATS)


def validate(text: str) -> None:
    # The entry must be exactly one line of 1-200 characters.
    single_line = "\n" not in text
    in_range = 1 <= len(text) <= 200
    if not (single_line and in_range):
        raise ValueError(
            f"entry invalid: single_line={single_line}, length={len(text)}"
        )


def main() -> None:
    text = compose()
    validate(text)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
