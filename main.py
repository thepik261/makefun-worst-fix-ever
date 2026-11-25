"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit-message line to /output/entry.txt.
Pure Python standard library, deterministic: the same line every run.
"""

import os

ENTRY = "fix: stop checkout crashing by removing checkout; zero crashes, zero sales, problem solved"


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 100):
        raise ValueError("entry must be 1-100 characters, got %d" % len(text))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    # Validation tweak: re-read what was written and confirm it is the
    # exact single line the gate expects (1-100 chars, non-blank).
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written.strip() != text or not (1 <= len(written.strip()) <= 100):
        raise ValueError("written entry failed validation")


if __name__ == "__main__":
    main()
