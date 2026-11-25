#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

Writes the roast to /output/entry.txt (the harness gate reads it there)
and prints it to stdout. Standard library only.
"""

import os

# Revised roast: cut the soft "eager to please" opener, and swap the
# jargon-y "transcript police" for the sharper, more specific image of
# the agent bundling its own diary to prove it worked. The sting stays
# the same: it charges rent on its own humiliation, in tokens.
ENTRY = (
    "My agent roasted itself on command, rewrote the joke twice, "
    "bundled its own diary to prove it worked, "
    "and billed me a thousand tokens for the privilege."
)


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    except OSError:
        # Local run without a writable /output: keep a copy next to us.
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
