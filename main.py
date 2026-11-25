"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text — an alien tourist's review of
planet Earth, at most 200 characters — to /output/entry.txt.

Run it with:

    python3 main.py

To validate the entry without writing anything:

    python3 main.py --verify
"""

import argparse
import os
import sys
import tempfile

ENTRY_TEXT = (
    "Three stars. Beautiful sunsets, but the locals pay monthly rent "
    "for the privilege of sleeping indoors. Would orbit again, briefly."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def format_entry() -> str:
    """Return the entry exactly as it must appear in the file."""
    return ENTRY_TEXT


def validate_entry(text: str) -> None:
    """Raise ValueError unless the text is a valid single-line entry."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} cap"
        )


def _ensure_output_dir(path: str) -> None:
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)


def _parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--verify",
        action="store_true",
        help="validate the entry without writing anything",
    )
    parser.add_argument(
        "--output",
        default=OUTPUT_PATH,
        help="where to write entry.txt (default: /output/entry.txt)",
    )
    return parser.parse_args(argv)


def write_entry(path: str) -> int:
    """Atomically write the validated entry; return its byte count."""
    text = format_entry()
    validate_entry(text)
    data = text.encode("utf-8")
    _ensure_output_dir(path)
    fd, tmp_path = tempfile.mkstemp(
        dir=os.path.dirname(path) or ".", prefix="entry-", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    return len(data)


def _run_verify() -> int:
    text = format_entry()
    validate_entry(text)
    print(
        f"entry valid: {len(text)} characters, "
        f"{len(text.encode('utf-8'))} bytes, single line"
    )
    return 0


def main(argv=None) -> int:
    args = _parse_args(argv)
    if args.verify:
        return _run_verify()
    size = write_entry(args.output)
    print(f"wrote {size} bytes to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
