#!/usr/bin/env python3
"""Stamp SHA256 of every raw source body into its frontmatter.

Implements SKILL.md § Ingest step 1. The hash covers the body below the
frontmatter, so editing frontmatter (title, ingested, notes) never invalidates
a stamp, but editing the text of a source does.

Usage:
    python3 scripts/stamp_sources.py examples/halden-safe            # stamp PENDING / missing
    python3 scripts/stamp_sources.py examples/halden-safe --check    # report drift only
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_matter import parse_frontmatter, sha256_body  # noqa: E402

SHA_LINE = re.compile(r"^sha256:\s*(.*)$", re.MULTILINE)


def stamp_file(path: Path, check_only: bool) -> str:
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    digest = sha256_body(text)
    if digest is None:
        return f"ERROR   {path.name}: unreadable"

    current = fm.get("sha256", "").strip()

    if current == digest:
        return f"OK      {path.name}: {digest[:16]}…"

    if check_only:
        state = "MISSING" if not current else ("PENDING" if current == "PENDING" else "DRIFT")
        return f"{state:7} {path.name}: on disk {digest[:16]}… vs recorded {current[:16] or '—'}"

    if SHA_LINE.search(text):
        text = SHA_LINE.sub(f"sha256: {digest}", text, count=1)
    else:
        # no sha256 key at all — insert after the opening frontmatter line
        text = text.replace("---\n", f"---\nsha256: {digest}\n", 1)
    path.write_text(text, encoding="utf-8")
    return f"STAMPED {path.name}: {digest[:16]}…"


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Stamp SHA256 of raw source bodies")
    parser.add_argument("matter_path", help="Matter root (contains raw/)")
    parser.add_argument("--check", action="store_true", help="Report only, do not write")
    args = parser.parse_args(argv)

    raw = Path(args.matter_path) / "raw"
    if not raw.is_dir():
        print(f"No raw/ directory at {raw}", file=sys.stderr)
        return 2

    sources = sorted(raw.rglob("*.md"))
    if not sources:
        print(f"No .md sources in {raw}", file=sys.stderr)
        return 2

    bad = 0
    for path in sources:
        line = stamp_file(path, args.check)
        print(line)
        if line.startswith(("ERROR", "MISSING", "PENDING", "DRIFT")):
            bad += 1

    print(f"\n{len(sources)} sources, {bad} needing attention")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
