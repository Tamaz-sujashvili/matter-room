#!/usr/bin/env python3
"""Lint a Matter Room directory. Exit 0 if no errors, 1 if issues found.

Forked from create-wiki's lint-wiki.py (Tamaz Sujashvili, MIT).
Legal additions: uncited high-risk, contested without a pair, deliverable
backlinks, citation anchors that do not exist in the cited source.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set

__version__ = "1.0.0"

WIKI_DIRS = ("entities", "concepts", "comparisons", "queries")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
ANCHOR_LINK_RE = re.compile(r"\[\[([^\]|#]+)#([^\]|]+)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
REQUIRED_FIELDS = ("title", "created", "updated", "type", "tags", "sources", "risk", "contested")
LIST_ITEM_RE = re.compile(r"^\s*-\s+(.+)$")
RAW_LINK_RE = re.compile(r"\[\[raw/")


@dataclass
class Issue:
    severity: str  # error, warn, info
    category: str
    message: str


@dataclass
class LintReport:
    issues: List[Issue] = field(default_factory=list)

    def add(self, severity: str, category: str, message: str) -> None:
        self.issues.append(Issue(severity, category, message))


def parse_inline_array(value: str) -> str:
    inner = value[1:-1].strip()
    if not inner:
        return ""
    items = []
    for item in inner.split(","):
        cleaned = item.strip().strip("'\"")
        if cleaned:
            items.append(cleaned)
    return ", ".join(items)


def parse_frontmatter(text: str) -> Dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    block = match.group(1)
    data: Dict[str, str] = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if not value:
            items: List[str] = []
            i += 1
            while i < len(lines):
                item_match = LIST_ITEM_RE.match(lines[i])
                if not item_match:
                    break
                items.append(item_match.group(1).strip().strip("'\""))
                i += 1
            if items:
                data[key] = ", ".join(items)
            continue
        if value.startswith("[") and value.endswith("]"):
            data[key] = parse_inline_array(value)
        else:
            data[key] = value.strip("'\"")
        i += 1
    return data


def heading_slugs(text: str) -> Set[str]:
    """Slugs for every heading in a source, matching the citation convention.

    Lowercase, drop everything that is not alphanumeric, space or hyphen, turn
    spaces into hyphens, collapse runs of hyphens. "## 2. Purchase; Conversion"
    and "## Email 04 — 16 Nov 2026" both produce a usable anchor.
    """
    slugs: Set[str] = set()
    for heading in HEADING_RE.findall(text):
        slug = re.sub(r"[^a-z0-9\s-]", "", heading.lower())
        slug = re.sub(r"\s+", "-", slug.strip())
        slug = re.sub(r"-{2,}", "-", slug).strip("-")
        if slug:
            slugs.add(slug)
    return slugs


def slug_from_path(path: Path, matter: Path) -> str:
    rel = path.relative_to(matter)
    return str(rel.with_suffix("")).replace(os.sep, "/")


def page_exists(target: str, matter: Path, pages: Set[str]) -> bool:
    target = target.strip()
    if target in pages:
        return True
    basename = Path(target).stem
    return any(p.endswith(f"/{basename}") or p == basename for p in pages)


def load_taxonomy(schema_path: Path) -> Set[str]:
    if not schema_path.exists():
        return set()
    text = schema_path.read_text(encoding="utf-8")
    tags: Set[str] = set()
    in_taxonomy = False
    for line in text.splitlines():
        if line.strip().startswith("## Tag Taxonomy"):
            in_taxonomy = True
            continue
        if in_taxonomy and line.startswith("## "):
            break
        if in_taxonomy and line.strip().startswith("- "):
            parts = line.split(":", 1)
            if len(parts) == 2:
                for tag in parts[1].split(","):
                    tags.add(tag.strip())
    return tags


def collect_pages(matter: Path) -> Dict[str, Path]:
    pages: Dict[str, Path] = {}
    for dirname in (*WIKI_DIRS, "raw", "deliverables", "council"):
        base = matter / dirname
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            pages[slug_from_path(path, matter)] = path
    return pages


def extract_index_slugs(index_text: str) -> Set[str]:
    return {m.group(1).strip() for m in WIKILINK_RE.finditer(index_text)}


def sha256_body(text: str) -> Optional[str]:
    match = FRONTMATTER_RE.match(text)
    body = text[match.end():] if match else text
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def lint_matter(matter: Path) -> LintReport:
    report = LintReport()
    matter = matter.resolve()

    if not matter.is_dir():
        report.add("error", "structure", f"Matter path does not exist: {matter}")
        return report

    for required in ("SCHEMA.md", "index.md", "log.md", "raw"):
        if not (matter / required).exists():
            report.add("error", "structure", f"Missing required: {required}")

    pages = collect_pages(matter)
    # L2 pages only, for orphan / index / frontmatter checks
    l2_slugs = {s for s in pages if s.split("/")[0] in WIKI_DIRS}
    taxonomy = load_taxonomy(matter / "SCHEMA.md")

    inbound: Dict[str, int] = {slug: 0 for slug in l2_slugs}
    outbound: Dict[str, List[str]] = {slug: [] for slug in l2_slugs}

    for slug in l2_slugs:
        path = pages[slug]
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        missing = [f for f in REQUIRED_FIELDS if f not in fm]
        if missing:
            report.add("error", "frontmatter", f"{slug}: missing fields {missing}")

        if fm.get("type") and fm["type"] not in {
            "entity", "concept", "comparison", "query", "deliverable",
        }:
            report.add("warn", "frontmatter", f"{slug}: unknown type '{fm['type']}'")

        if taxonomy and "tags" in fm:
            for tag in re.findall(r"[\w-]+", fm["tags"]):
                if tag not in taxonomy and tag not in {"tags"}:
                    report.add("warn", "tags", f"{slug}: tag '{tag}' not in SCHEMA taxonomy")

        line_count = len(text.splitlines())
        if line_count > 200:
            report.add("info", "size", f"{slug}: {line_count} lines (consider splitting)")

        for match in WIKILINK_RE.finditer(text):
            target = match.group(1).strip()
            outbound[slug].append(target)
            if page_exists(target, matter, set(pages.keys())):
                for existing in l2_slugs:
                    if existing == target or existing.endswith(f"/{Path(target).stem}"):
                        inbound[existing] = inbound.get(existing, 0) + 1
                        break
            else:
                report.add("error", "broken-link", f"{slug}: broken wikilink [[{target}]]")

        if len(outbound[slug]) < 2:
            report.add("warn", "cross-ref", f"{slug}: fewer than 2 outbound wikilinks")

        # Legal check 1: risk: high must cite raw/
        if fm.get("risk") == "high" and not RAW_LINK_RE.search(text):
            report.add("error", "uncited-high-risk", f"{slug}: risk high but no [[raw/...]] citation in body")

        # Legal check 2: contested: true needs >= 2 sources
        if fm.get("contested") in ("true", "True", "yes"):
            sources = [s for s in fm.get("sources", "").split(",") if s.strip()]
            if len(sources) < 2:
                report.add(
                    "error",
                    "contested-unpaired",
                    f"{slug}: contested true but only {len(sources)} source(s)",
                )

    # Legal check 4: a citation anchor must exist in the cited source. The
    # wikilink pass above resolves file paths only, so a wrong #anchor passes it.
    anchor_cache: Dict[str, Set[str]] = {}
    cite_files = list(l2_slugs) + [s for s in pages if s.startswith("deliverables/")]
    for slug in cite_files:
        text = pages[slug].read_text(encoding="utf-8")
        for target, anchor in ANCHOR_LINK_RE.findall(text):
            target = target.strip()
            if not target.startswith("raw/"):
                continue
            if target not in pages:
                target = target[:-3] if target.endswith(".md") else target
            source = pages.get(target)
            if source is None:
                continue  # broken file link is already reported above
            if target not in anchor_cache:
                anchor_cache[target] = heading_slugs(source.read_text(encoding="utf-8"))
            if anchor.strip() not in anchor_cache[target]:
                report.add(
                    "error",
                    "bad-anchor",
                    f"{slug}: [[{target}#{anchor}]] — no such heading in {target}.md",
                )

    for slug, count in inbound.items():
        if count == 0:
            report.add("warn", "orphan", f"{slug}: no inbound wikilinks")

    index_path = matter / "index.md"
    if index_path.exists():
        index_text = index_path.read_text(encoding="utf-8")
        indexed = extract_index_slugs(index_text)
        for slug in l2_slugs:
            basename = Path(slug).name
            if slug not in indexed and basename not in indexed:
                report.add("warn", "index", f"{slug}: not listed in index.md")

        # Legal check 3: every deliverable must be linked from index.md
        deliv = matter / "deliverables"
        if deliv.exists():
            for path in deliv.rglob("*.md"):
                basename = path.stem
                if basename not in indexed and str(path.relative_to(matter).with_suffix("")) not in indexed:
                    report.add("warn", "deliverable-backlink", f"deliverables/{basename}.md: not listed in index.md")

    raw_base = matter / "raw"
    if raw_base.exists():
        for path in sorted(raw_base.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            if "sha256" not in fm:
                rel = path.relative_to(matter)
                report.add("warn", "source-drift", f"{rel}: no sha256 stamped (ingest not done)")
            elif fm["sha256"].strip() == "PENDING":
                rel = path.relative_to(matter)
                report.add("warn", "source-drift", f"{rel}: sha256 still PENDING")
            else:
                actual = sha256_body(text)
                if actual and actual != fm["sha256"].strip():
                    rel = path.relative_to(matter)
                    report.add("warn", "source-drift", f"{rel}: sha256 mismatch (source may have changed)")

    log_path = matter / "log.md"
    if log_path.exists():
        entries = len(re.findall(r"^## \[", log_path.read_text(encoding="utf-8"), re.MULTILINE))
        if entries > 500:
            report.add("info", "log", f"log.md has {entries} entries (rotate recommended)")

    return report


def summarize_issues(issues: List[Issue]) -> Dict[str, int]:
    counts = {"error": 0, "warn": 0, "info": 0}
    for issue in issues:
        counts[issue.severity] = counts.get(issue.severity, 0) + 1
    return counts


def report_exit_code(report: LintReport) -> int:
    counts = summarize_issues(report.issues)
    if not report.issues:
        return 0
    return 1 if counts.get("error", 0) or counts.get("warn", 0) else 0


def print_report(report: LintReport) -> int:
    order = {"error": 0, "warn": 1, "info": 2}
    issues = sorted(report.issues, key=lambda i: (order.get(i.severity, 9), i.category, i.message))

    if not issues:
        print("OK — no issues found")
        return 0

    counts = summarize_issues(issues)
    for issue in issues:
        print(f"[{issue.severity.upper():5}] {issue.category}: {issue.message}")

    print(
        f"\nSummary: {counts.get('error', 0)} errors, "
        f"{counts.get('warn', 0)} warnings, {counts.get('info', 0)} info"
    )
    return report_exit_code(report)


def print_report_json(report: LintReport, matter_path: Path) -> int:
    order = {"error": 0, "warn": 1, "info": 2}
    issues = sorted(report.issues, key=lambda i: (order.get(i.severity, 9), i.category, i.message))
    counts = summarize_issues(issues)
    payload = {
        "version": __version__,
        "matter_path": str(matter_path.resolve()),
        "ok": not issues or (counts.get("error", 0) == 0 and counts.get("warn", 0) == 0),
        "summary": counts,
        "issues": [asdict(issue) for issue in issues],
    }
    print(json.dumps(payload, indent=2))
    return report_exit_code(report)


def main(argv: Optional[Iterable[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Lint a Matter Room directory")
    parser.add_argument(
        "matter_path",
        nargs="?",
        default=os.environ.get("MATTER_PATH", os.getcwd()),
        help="Path to matter root (default: $MATTER_PATH or cwd)",
    )
    parser.add_argument("--json", action="store_true", help="Output structured JSON")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(list(argv) if argv is not None else None)
    matter_path = Path(args.matter_path)
    report = lint_matter(matter_path)
    if args.json:
        return print_report_json(report, matter_path)
    return print_report(report)


if __name__ == "__main__":
    sys.exit(main())
