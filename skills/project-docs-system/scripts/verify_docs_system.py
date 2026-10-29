from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from update_docs_catalog import (
    BEGIN_MARKER,
    END_MARKER,
    CatalogError,
    DocsTarget,
    check_catalog,
    resolve_target,
)

MAX_AUTHORED_LINES = 500
LEGACY_PATH = re.compile(r"(^|[^\w])\.docs(/|[^\w]|$)|domains/DOCS\.md")


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def authored_line_count(lines: list[str]) -> int:
    count = 0
    in_catalog = False
    for line in lines:
        if line == BEGIN_MARKER:
            in_catalog = True
        elif line == END_MARKER:
            in_catalog = False
        elif not in_catalog:
            count += 1
    return count


def check_document(path: Path, text: str, repo_root: Path, report: Report) -> None:
    lines = text.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        report.errors.append(f"missing frontmatter: {path}")

    count = authored_line_count(lines)
    if count > MAX_AUTHORED_LINES:
        relative = path.relative_to(repo_root).as_posix()
        report.warnings.append(
            f"{relative} has {count} lines (recommended maximum: {MAX_AUTHORED_LINES}). "
            "Review cohesion: move decision history to a companion ADR, split distinct "
            "domains, or trim unnecessary content to reduce reading context; "
            "do not split mechanically."
        )

    for number, line in enumerate(lines, start=1):
        if LEGACY_PATH.search(line):
            report.errors.append(f"forbidden legacy docs path reference: {path}:{number}:{line}")


def check_adr(path: Path, texts: dict[Path, str], report: Report) -> None:
    living = path.with_name(path.name.removesuffix(".adr.md") + ".md")
    if living not in texts:
        report.errors.append(f"ADR companion has no living document: {path}")
        return
    for source, destination in [(living, path), (path, living)]:
        if not any(
            f"]({prefix}{destination.name})" in texts[source] for prefix in ["./", ""]
        ):
            report.errors.append(
                f"{source} must link its companion document with a relative Markdown link: "
                f"{destination.name}"
            )


def docs_scopes(docs_dir: Path, texts: dict[Path, str]) -> set[Path]:
    scopes: set[Path] = set()
    for path in texts:
        if any(part.startswith(".") for part in path.relative_to(docs_dir).parts):
            continue
        scope = path.parent
        while scope != docs_dir.parent:
            scopes.add(scope)
            scope = scope.parent
    return scopes


def check_scope(scope: Path, scopes: set[Path], texts: dict[Path, str], report: Report) -> None:
    index = scope / "index.md"
    if index not in texts:
        report.errors.append(f"missing docs index: {index}")
        return

    for path in texts:
        if path.parent != scope or path.name in {"index.md", "DOCS.md"} or path.name.endswith(".adr.md"):
            continue
        if path.name not in texts[index]:
            report.errors.append(f"{index} does not link direct docs file: {path.name}")
    for child in sorted(scopes):
        if child.parent == scope and f"{child.name}/index.md" not in texts[index]:
            report.errors.append(f"{index} does not link child docs index: {child.name}/index.md")


def verify_structure(target: DocsTarget) -> Report:
    report = Report()
    docs_dir = target.docs_dir
    if (target.repo_root / ".docs").is_dir():
        report.errors.append(f"legacy .docs directory exists at {target.repo_root / '.docs'}")
    for name in ["index.md", "DOCS.md"]:
        if not (docs_dir / name).is_file():
            report.errors.append(f"missing required file: {docs_dir / name}")

    texts = {
        path: path.read_text(encoding="utf-8")
        for path in sorted(docs_dir.rglob("*.md"))
        if path.is_file()
    }
    for path, text in texts.items():
        check_document(path, text, target.repo_root, report)
        if path.name.endswith(".adr.md"):
            check_adr(path, texts, report)
        if path.parent == docs_dir and path.name not in {"index.md", "DOCS.md", "DOCS.adr.md"}:
            report.warnings.append(f"root-level docs markdown is outside the canonical layout: {path}")

    scopes = docs_scopes(docs_dir, texts)
    for scope in sorted(scopes):
        if scope.parent == docs_dir and not (scope / "DOCS.md").is_file():
            report.errors.append(f"missing domain DOCS protocol: {scope / 'DOCS.md'}")
        check_scope(scope, scopes, texts, report)
    return report


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Verify the project docs structure and generated catalogs.")
    parser.add_argument("target", nargs="?", default=".", help="repository root or docs directory")
    args = parser.parse_args(argv)
    try:
        target = resolve_target(args.target)
    except CatalogError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Verifying docs system: {target.docs_dir}", flush=True)
    report = verify_structure(target)
    if not report.errors:
        try:
            if check_catalog(target):
                report.errors.append("generated docs catalog check failed")
        except CatalogError as error:
            report.errors.append(str(error))
    for warning in report.warnings:
        print(f"WARN: {warning}", file=sys.stderr)
    for error in report.errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if report.errors:
        print(
            f"Docs system verification failed: {len(report.errors)} error(s), "
            f"{len(report.warnings)} warning(s).",
            file=sys.stderr,
        )
        return 1
    print(f"Docs system verification passed: 0 errors, {len(report.warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
