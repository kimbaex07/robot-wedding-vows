#!/usr/bin/env python3
"""Write the one-line robot wedding vow to the make.fun output directory.

Reads entry.txt next to this script, validates it against the contest gate
(UTF-8, 1-160 characters, not only whitespace, single line), and writes the
exact normalized bytes to $MAKEFUN_OUTPUT_DIR/entry.txt (default "output/").
Pure Python standard library only.
"""

import os
import sys

ENTRY_NAME = "entry.txt"
MAX_CHARS = 160


def fail(message):
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(here, ENTRY_NAME)

    try:
        with open(src_path, "rb") as f:
            raw = f.read()
    except OSError as exc:
        fail("cannot read %s: %s" % (src_path, exc))

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail("entry.txt is not valid UTF-8: %s" % exc)

    # Drop at most one trailing newline, then at most one trailing CR.
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]

    if not (1 <= len(text) <= MAX_CHARS):
        fail("entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text)))
    if not text.strip():
        fail("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        fail("entry must be a single line (no newline inside)")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output/")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        fail("cannot create output dir %s: %s" % (out_dir, exc))

    out_path = os.path.join(out_dir, ENTRY_NAME)
    data = text.encode("utf-8")
    try:
        with open(out_path, "wb") as f:
            f.write(data)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        fail("cannot write %s: %s" % (out_path, exc))

    print("wrote %s (%d characters)" % (out_path, len(text)))


if __name__ == "__main__":
    main()
