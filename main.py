"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse to /output/entry.txt.
Stdlib only.
"""

LINE = "Sorry I'm late - I delegated the deadline to myself, and I ghosted myself."

MAX_CHARS = 200


def validate(text):
    """Enforce the kit's gate limits; refuse invalid output.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 200
    characters, not only white space, and the task requires exactly
    one line. Anything failing that raises instead of being written.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be str, got %r" % type(text).__name__)
    # Valid UTF-8: a round-trip through UTF-8 must reproduce the text.
    text.encode("utf-8").decode("utf-8")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")


def main():
    import os

    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Re-read and re-validate what was actually written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        validate(f.read())


if __name__ == "__main__":
    main()
