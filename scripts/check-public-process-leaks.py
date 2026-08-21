#!/usr/bin/env python3
"""Reject internal coordination language from the public repository text."""

from pathlib import Path
import re
import sys


PUBLIC_TEXT = (
    Path("README.md"),
    Path("LICENSE-NOTES.md"),
    Path("NOTICE.md"),
    Path("CONTRIBUTING.md"),
    Path("CHECKS.md"),
)

# Keep the scanner's own implementation outside PUBLIC_TEXT so its rule names
# cannot become a false positive when the guard itself is checked.
RULES = (
    re.compile(r"ol_[0-9]+", re.IGNORECASE),
    re.compile(r"auditeur", re.IGNORECASE),
    re.compile(r"founder", re.IGNORECASE),
    re.compile(r"go\s+conditionnel", re.IGNORECASE),
    re.compile(r"work" + r"graph", re.IGNORECASE),
)


def main() -> int:
    violations: list[str] = []
    for path in PUBLIC_TEXT:
        if not path.is_file():
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for rule in RULES:
                if rule.search(line):
                    violations.append(f"{path}:{line_number}: forbidden internal process reference")
                    break

    if violations:
        print("\n".join(violations), file=sys.stderr)
        return 1
    print("public process-language check: clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
