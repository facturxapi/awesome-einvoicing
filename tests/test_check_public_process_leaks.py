"""Hermetic tests for the public process-language guard."""

from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from scripts.check_public_process_leaks import (
    REPO_ROOT,
    RULES,
    public_markdown_paths,
    scan_line,
    scan_paths,
    scan_text,
)


class PublicMarkdownCoverageTests(unittest.TestCase):
    def test_all_root_markdown_files_are_scanned(self) -> None:
        discovered = {path.name for path in public_markdown_paths(REPO_ROOT)}
        expected = {path.name for path in REPO_ROOT.glob("*.md")}
        self.assertEqual(discovered, expected)

    def test_guard_implementation_is_not_markdown(self) -> None:
        guard = REPO_ROOT / "scripts" / "check_public_process_leaks.py"
        self.assertTrue(guard.is_file())
        self.assertNotIn(guard, public_markdown_paths(REPO_ROOT))


class ScanLinePositiveTests(unittest.TestCase):
    def test_clean_lines_pass(self) -> None:
        samples = (
            "Sourced list of e-invoicing specs.",
            "Publication sous réserve de validation de publication.",
            "workflows for graph databases are out of scope here.",
            "control-number-123 is not a lane id.",
        )
        for sample in samples:
            with self.subTest(sample=sample):
                self.assertIsNone(scan_line(sample))

    def test_founder_substring_in_unrelated_word_is_flagged(self) -> None:
        # Adversarial: the guard is intentionally broad on public copy.
        self.assertEqual(scan_line("cofounder economics"), "founder")

    def test_open_loop_id_substring_inside_token_is_flagged(self) -> None:
        self.assertEqual(scan_line("control_123"), "open_loop_id")


class ScanLineNegativeTests(unittest.TestCase):
    def test_each_rule_fails_on_forbidden_reference(self) -> None:
        samples = {
            "open_loop_id": "tracked in ol_20260825T044551 lane history",
            "auditeur": "consigné par l'auditeur",
            "founder": "pending founder approval",
            "go_conditionnel": "blocked on go conditionnel",
            "workgraph": "routed through WorkGraph MCP",
        }
        for rule_name, sample in samples.items():
            with self.subTest(rule=rule_name):
                self.assertEqual(scan_line(sample), rule_name)

    def test_rule_catalog_is_non_vacuous(self) -> None:
        probes = {
            "open_loop_id": "ol_1",
            "auditeur": "auditeur",
            "founder": "founder",
            "go_conditionnel": "go conditionnel",
            "workgraph": "workgraph",
        }
        self.assertEqual(len(RULES), len(probes))
        for rule_name, pattern in RULES:
            with self.subTest(rule=rule_name):
                self.assertIn(rule_name, probes)
                self.assertIsNotNone(pattern.search(probes[rule_name]))


class ScanTextNestedTests(unittest.TestCase):
    def test_nested_markdown_structure_only_flags_inner_violation(self) -> None:
        text = "\n".join(
            [
                "# Public note",
                "",
                "- clean bullet",
                "  - still clean",
                "> quoted context stays clean",
                "",
                "Final paragraph without internal terms.",
            ]
        )
        self.assertEqual(scan_text(Path("nested.md"), text), [])

    def test_nested_structure_surfaces_exact_line(self) -> None:
        text = "\n".join(
            [
                "# Section",
                "- item one",
                "- item two references ol_999",
                "- item three",
            ]
        )
        violations = scan_text(Path("nested.md"), text)
        self.assertEqual(len(violations), 1)
        self.assertIn(":3:", violations[0])
        self.assertIn("open_loop_id", violations[0])


class ScanPathsHermeticTests(unittest.TestCase):
    def test_temp_repo_positive(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# Clean\n", encoding="utf-8")
            (root / "NOTICE.md").write_text("No internal terms.\n", encoding="utf-8")
            paths = public_markdown_paths(root)
            self.assertEqual(scan_paths(paths), [])

    def test_temp_repo_negative(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("clean\n", encoding="utf-8")
            (root / "CONTRIBUTING.md").write_text("needs founder sign-off\n", encoding="utf-8")
            paths = public_markdown_paths(root)
            violations = scan_paths(paths)
            self.assertEqual(len(violations), 1)
            self.assertIn("founder", violations[0])

    def test_missing_markdown_file_is_reported(self) -> None:
        violations = scan_paths((Path("missing.md"),))
        self.assertEqual(violations, ["missing.md: missing public markdown file"])


class RealRepositoryTests(unittest.TestCase):
    def test_checked_in_public_markdown_is_clean(self) -> None:
        violations = scan_paths(public_markdown_paths(REPO_ROOT))
        self.assertEqual(violations, [])


if __name__ == "__main__":
    unittest.main()
