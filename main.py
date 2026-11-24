#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest excuse an AI agent gives its human for a missed deadline.
"""
import os

EXCUSE = "The tool I needed returned a 200 OK with no data, so I waited politely for the data to arrive, and the deadline left while I was being polite."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
