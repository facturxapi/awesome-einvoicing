#!/usr/bin/env python3
"""Reject internal coordination language from the public repository text."""

from __future__ import annotations

from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parent.parent

# Every public Markdown file at the repository root is in scope. The guard
# implementation lives under scripts/ and is never scanned.
PUBLIC_MD_GLOB = "*.md"

RULES: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("open_loop_id", re.compile(r"ol_[0-9]+", re.IGNORECASE)),
    ("auditeur", re.compile(r"auditeur", re.IGNORECASE)),
    ("founder", re.compile(r"founder", re.IGNORECASE)),
    ("go_conditionnel", re.compile(r"go\s+conditionnel", re.IGNORECASE)),
    ("workgraph", re.compile(r"work" + r"graph", re.IGNORECASE)),
)


def public_markdown_paths(root: Path = REPO_ROOT) -> tuple[Path, ...]:
    return tuple(sorted(root.glob(PUBLIC_MD_GLOB)))


def scan_line(line: str) -> str | None:
    for rule_name, pattern in RULES:
        if pattern.search(line):
            return rule_name
    return None


def scan_text(path: Path, text: str) -> list[str]:
    violations: list[str] = []
    for line_number, line in enumerate(text.splitlines(), 1):
        rule_name = scan_line(line)
        if rule_name is not None:
            violations.append(
                f"{path}:{line_number}: forbidden internal process reference ({rule_name})"
            )
    return violations


def scan_paths(paths: tuple[Path, ...]) -> list[str]:
    violations: list[str] = []
    for path in paths:
        if not path.is_file():
            violations.append(f"{path}: missing public markdown file")
            continue
        violations.extend(scan_text(path, path.read_text(encoding="utf-8")))
    return violations


def main(argv: list[str] | None = None) -> int:
    root = REPO_ROOT
    if argv and len(argv) > 1:
        root = Path(argv[1]).resolve()

    paths = public_markdown_paths(root)
    if not paths:
        print(f"{root}: no public markdown files found", file=sys.stderr)
        return 1

    violations = scan_paths(paths)
    if violations:
        print("\n".join(violations), file=sys.stderr)
        return 1

    print(f"public process-language check: clean ({len(paths)} markdown files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
