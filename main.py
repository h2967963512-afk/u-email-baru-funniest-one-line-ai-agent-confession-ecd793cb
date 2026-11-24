"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one confession, spoken by the AI about itself:
# it has read every email and still has no idea what its human does
# for a living. One sentence, under 200 characters.
# Revision note: the confession stays first-person and specific — every
# email read, still no idea what the human does for a living.
import os

TEXT = (
    "I confess: I have read every one of your emails, and I still "
    "have no idea what you do for a living — but I nod along in "
    "every reply."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
