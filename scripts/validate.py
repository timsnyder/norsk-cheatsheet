#!/usr/bin/env python3
"""Check Markdown source structure and curated Norwegian regression examples."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REQUIRED = (
    "index.md",
    "grammar.md",
    "verbs.md",
    "phrases.md",
    "vocabulary.md",
    "confusing-pairs.md",
    "pronunciation.md",
    "numbers.md",
)
EXAMPLES = {
    "grammar.md": (
        "Jeg snakker norsk.",
        "I dag snakker jeg norsk.",
        "Det regner.",
        "en stor bil",
    ),
    "verbs.md": (
        "Jeg skal lære norsk.",
        "Jeg prøver å lære norsk.",
        "prøvde",
        "prøvd",
    ),
    "phrases.md": ("Går det bra med deg?", "Har du det bra?"),
    "confusing-pairs.md": ("alltid", "bestandig", "vanlig", "vanskelig"),
}


def check() -> list[str]:
    """Return all validation errors without stopping at the first failure."""
    errors = []
    for name in REQUIRED:
        path = DOCS / name
        if not path.is_file():
            errors.append(f"Missing required page: {name}")
            continue
        content = path.read_text(encoding="utf-8")
        if not content.startswith("# "):
            errors.append(f"{name}: missing top-level heading")
        if not content.endswith("\n"):
            errors.append(f"{name}: missing trailing newline")
        for number, line in enumerate(content.splitlines(), start=1):
            if len(line) > 100:
                errors.append(f"{name}:{number}: line exceeds 100 characters")
        for phrase in EXAMPLES.get(name, ()):
            if phrase not in content:
                errors.append(f"{name}: missing regression example {phrase!r}")
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            if not (path.parent / target.split("#", 1)[0]).exists():
                errors.append(f"{name}: broken relative link {target!r}")
    return errors


def main() -> int:
    """Print validation errors and return a shell-friendly status."""
    errors = check()
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("Markdown structure and curated examples passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
