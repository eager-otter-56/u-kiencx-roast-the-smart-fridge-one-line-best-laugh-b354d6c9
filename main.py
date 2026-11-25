"""Roast the Smart Fridge: one line, at most 160 characters.

Writes the roast to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import stat

ENTRY = (
    "My fridge reminds me the milk expires Sunday, but I forgot "
    "the fridge existed by Monday, because my memory resets every "
    "8,192 tokens."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert isinstance(text, str)
    assert 1 <= len(text) <= 160, f"entry length {len(text)} outside 1-160"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    # Gate: exactly one line, UTF-8, 1-160 chars. No trailing newline:
    # the file holds the entry text alone, byte for byte.
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
