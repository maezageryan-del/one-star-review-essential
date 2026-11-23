"""One-star review of something essential.

Writes a single-line deadpan one-star review of teeth to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The review is one line, 94 characters, no trailing newline.
"""

import os
import sys

REVIEW = "Teeth: they never hurt on a weekday. They wait until Friday night, when the dentist is closed."


def main() -> int:
    if not 1 <= len(REVIEW) <= 160:
        print(f"review is {len(REVIEW)} characters, must be 1-160", file=sys.stderr)
        return 1
    if REVIEW.strip() == "":
        print("review is only whitespace", file=sys.stderr)
        return 1
    if "\n" in REVIEW or "\r" in REVIEW:
        print("review must be a single line", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
