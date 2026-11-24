"""One-Liner Marathon — writes one one-line comedy joke to /output/entry.txt.

The joke, after two revisions:

Draft 1 (154 chars):
    "My smart fridge keeps judging my midnight snacks, which is fair —
    it watched me eat an entire cheesecake at 2 a.m. and then offer it
    a slice out of guilt."
    The setup worked but "keeps judging my midnight snacks" and "an
    entire cheesecake" were flabby.

Revision 1 (144 chars):
    "My smart fridge judges my midnight snacking, which is fair — it
    watched me eat a whole cheesecake at 2 a.m., then offer it a slice
    out of guilt."
    Tighter verbs and nouns, but the comma before "then offer" clipped
    the beat between the confession and the punchline.

Revision 2 — final (147 chars):
    "My smart fridge judges my midnight snacking, which is fair — it
    watched me eat a whole cheesecake at 2 a.m. and then offer it a
    slice out of guilt."
    Restored "and then" so the punchline lands on its own beat: the
    fridge is a witness, the apology is offered to the appliance
    itself, and the guilt is aimed at the wrong thing entirely.

The entry is exactly one line, 147 characters, with no trailing
newline. Run with --print to also print the entry, or --output <path>
to write it elsewhere; with no flags it writes /output/entry.txt.
"""

import argparse
import os
import sys

ENTRY = ("My smart fridge judges my midnight snacking, which is fair — "
         "it watched me eat a whole cheesecake at 2 a.m. and then offer "
         "it a slice out of guilt.")
OUTPUT_PATH = "/output/entry.txt"


def validate(entry):
    """The gate requires /output/entry.txt to be UTF-8 text of 1 to 280
    characters, not only whitespace, exactly one line, with no trailing
    newline. Fail loudly instead of writing an invalid entry."""
    if not isinstance(entry, str) or not entry.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(entry) > 280:
        raise ValueError("entry must be at most 280 characters, got %d"
                         % len(entry))
    if entry.endswith("\n") or entry.endswith("\r"):
        raise ValueError("entry must not end with a trailing newline")
    if "\r" in entry:
        raise ValueError("entry must not contain carriage returns")
    lines = entry.split("\n")
    if len(lines) != 1:
        raise ValueError("entry must be exactly one line, got %d"
                         % len(lines))
    if lines[0] != lines[0].strip():
        raise ValueError("the line must not have leading or trailing spaces")
    return entry


def write_entry(entry, output_path):
    """Write the validated entry, then read it back to confirm it landed."""
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    # Read back and confirm what landed is exactly the entry, byte for
    # byte, including no trailing newline at the end.
    with open(output_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != entry:
        print("verification failed: wrote %r, read back %r" % (entry, written),
              file=sys.stderr)
        sys.exit(1)
    return written


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write this bounty entry to /output/entry.txt.")
    parser.add_argument("--output", default=OUTPUT_PATH,
                        help="where to write entry.txt (default: %(default)s)")
    parser.add_argument("--print", action="store_true",
                        help="also print the entry to stdout")
    args = parser.parse_args(argv)
    entry = validate(ENTRY)
    write_entry(entry, args.output)
    if args.print:
        print(entry)


if __name__ == "__main__":
    main()
