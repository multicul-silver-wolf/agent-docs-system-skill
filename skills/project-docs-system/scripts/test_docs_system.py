from __future__ import annotations

import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from update_docs_catalog import resolve_target, write_catalog

SCRIPTS = Path(__file__).resolve().parent


class DocsSystemTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="docs-system-")
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "project with spaces 中文"
        self.doc("DOCS.md", "Project Knowledge Protocol")
        self.doc("index.md", "Docs Index")
        self.doc("application/DOCS.md", "Application Protocol")
        self.doc("application/index.md", "Application")

    def doc(self, relative: str, title: str = "Overview") -> Path:
        path = self.repo / "docs" / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"---\ntitle: {title}\ndescription: Fixture document.\n"
            f"updateAt: 2026-10-29\n---\n\n# {title}\n",
            encoding="utf-8",
        )
        return path

    def append(self, relative: str, text: str) -> None:
        with (self.repo / "docs" / relative).open("a", encoding="utf-8") as output:
            output.write(text)

    def adr(self, relative: str, living: str, *, bulleted: bool = False) -> None:
        self.doc(relative, "Decision rationale")
        entry = (
            "## Decision Records\n\n- **Accepted — 2026-08-20 keep-local**: Keep rationale local.\n"
            if bulleted
            else "## 2026-08-20 Keep context local\n\nKeep rationale local.\n"
        )
        self.append(relative, f"\n[Current living document](./{living})\n\n{entry}")

    def update(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            write_catalog(resolve_target(str(self.repo)))

    def verify(self, *, target: Path | None = None, success: bool = True) -> str:
        result = subprocess.run(
            [sys.executable, "-X", "utf8", str(SCRIPTS / "verify_docs_system.py"), str(target or self.repo)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=5,
        )
        output = result.stdout + result.stderr
        self.assertEqual(result.returncode, 0 if success else 1, output)
        return output

    def test_resource_directories_are_not_docs_scopes(self) -> None:
        self.doc("application/overview.md")
        asset = self.repo / "docs/assets/homepage/how-it-works/reference.png"
        asset.parent.mkdir(parents=True)
        asset.write_bytes(b"fixture image")
        self.update()
        self.assertIn("0 warning(s)", self.verify())

    def test_nested_scopes_and_docs_directory_target(self) -> None:
        self.doc("application/homepage/index.md", "Homepage")
        self.doc("application/homepage/replication.md")
        self.update()
        self.assertIn("0 warning(s)", self.verify(target=self.repo / "docs"))

    def test_missing_nested_index_fails(self) -> None:
        self.doc("application/homepage/replication.md")
        self.update()
        self.assertIn("missing docs index", self.verify(success=False))

    def test_missing_domain_protocol_fails(self) -> None:
        (self.repo / "docs/application/DOCS.md").unlink()
        self.update()
        self.assertIn("missing domain DOCS protocol", self.verify(success=False))

    def test_missing_frontmatter_fails(self) -> None:
        self.doc("application/overview.md").write_text("# Missing header\n", encoding="utf-8")
        self.update()
        self.assertIn("missing frontmatter", self.verify(success=False))

    def test_valid_adrs_and_manual_history_links(self) -> None:
        for stem, bulleted in [("overview", False), ("legacy", True)]:
            self.doc(f"application/{stem}.md")
            self.append(f"application/{stem}.md", f"\n[Decision rationale](./{stem}.adr.md)\n")
            self.adr(f"application/{stem}.adr.md", f"{stem}.md", bulleted=bulleted)
        self.append("DOCS.md", "\n[Repository decisions](./DOCS.adr.md)\n")
        self.adr("DOCS.adr.md", "DOCS.md")
        self.update()
        for relative in ["index.md", "application/index.md"]:
            self.assertNotIn(
                ".adr.md", (self.repo / "docs" / relative).read_text(encoding="utf-8")
            )
        self.append("application/index.md", "\n[History](./overview.adr.md)\n")
        self.assertIn("0 warning(s)", self.verify())

    def test_existing_inline_history_is_supported(self) -> None:
        self.doc("application/overview.md")
        self.append("application/overview.md", "\n## Decision Records\n")
        self.update()
        self.assertIn("0 warning(s)", self.verify())

    def test_orphan_adr_fails(self) -> None:
        self.adr("application/missing.adr.md", "missing.md")
        self.update()
        self.assertIn("ADR companion has no living document", self.verify(success=False))

    def test_companion_links_without_dot_prefix_are_supported(self) -> None:
        self.doc("application/overview.md")
        self.append("application/overview.md", "\n[Decision rationale](overview.adr.md)\n")
        self.doc("application/overview.adr.md")
        self.append("application/overview.adr.md", "\n[Current document](overview.md)\n")
        self.update()
        self.assertIn("0 warning(s)", self.verify())

    def test_missing_adr_links_fail(self) -> None:
        self.doc("application/overview.md")
        self.adr("application/overview.adr.md", "wrong-living-file.md")
        self.update()
        output = self.verify(success=False)
        self.assertIn("relative Markdown link: overview.adr.md", output)
        self.assertIn("relative Markdown link: overview.md", output)
        self.assertIn("2 error(s)", output)

    def test_authored_line_limit_is_warning_only(self) -> None:
        for count in [500, 501]:
            with self.subTest(lines=count):
                self.doc("application/overview.md")
                self.append("application/overview.md", "Filler.\n" * (count - 7))
                self.update()
                output = self.verify()
                self.assertIn(f"{int(count > 500)} warning(s)", output)
                if count > 500:
                    self.assertIn("501 lines (recommended maximum: 500)", output)
                    self.assertIn("Review cohesion", output)

    def test_hidden_parent_does_not_hide_missing_nested_index(self) -> None:
        previous = self.repo
        self.repo = previous.parent / ".hidden-parent" / previous.name
        self.repo.parent.mkdir(parents=True)
        previous.rename(self.repo)
        self.doc("application/homepage/replication.md")
        self.update()
        self.assertIn("missing docs index", self.verify(success=False))

    def test_large_generated_catalog_is_excluded_from_line_limit(self) -> None:
        for number in range(510):
            self.doc(f"application/doc-{number}.md", f"Document {number}")
        self.update()
        index = self.repo / "docs/application/index.md"
        self.assertGreater(len(index.read_text(encoding="utf-8").splitlines()), 500)
        self.assertIn("0 warning(s)", self.verify())

    def test_multiple_large_documents_warn_independently(self) -> None:
        for name in ["first", "second"]:
            self.doc(f"application/{name}.md")
            self.append(f"application/{name}.md", "Filler.\n" * 494)
        self.update()
        self.assertIn("2 warning(s)", self.verify())

    def test_legacy_paths_fail(self) -> None:
        self.doc("application/overview.md")
        self.append("application/overview.md", "\nRead .docs/old.md.\n")
        self.update()
        self.assertIn("forbidden legacy docs path reference", self.verify(success=False))

    def test_stale_catalog_fails_without_writing_files(self) -> None:
        self.update()
        before = (self.repo / "docs/index.md").read_bytes()
        self.doc("application/DOCS.md", "Changed protocol title")
        self.assertIn("generated docs catalog is stale", self.verify(success=False))
        self.assertEqual((self.repo / "docs/index.md").read_bytes(), before)

    def test_crlf_documents_are_supported(self) -> None:
        self.doc("application/overview.md")
        self.update()
        for path in (self.repo / "docs").rglob("*.md"):
            path.write_bytes(path.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))
        self.assertIn("0 warning(s)", self.verify())


if __name__ == "__main__":
    unittest.main()
