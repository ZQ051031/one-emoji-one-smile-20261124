#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the hugging face.

Why this emoji: an open-arms hug is the warmest gesture a stranger can
make at first glance — friendly and gently funny with no context needed,
universal across ages and backgrounds, and it feels chosen for the moment
rather than the first smiley that comes to mind, while staying instantly
readable. A virtual hug carries no intimacy, sarcasm, or flirtation.
"""

import os

EMOJI = "\U0001F917"  # 🤗 hugging face


def validate_entry(text):
    """The gate: UTF-8 text of 1 to 8 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 8:
        raise ValueError("entry must be 1 to 8 characters, got %d" % len(text))
    if text.isspace():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def output_path():
    """Resolve the entry file, honouring the grader's output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def write_entry(text, path):
    """Write exactly the entry text — nothing else, no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    write_entry(validate_entry(EMOJI), output_path())


if __name__ == "__main__":
    main()
