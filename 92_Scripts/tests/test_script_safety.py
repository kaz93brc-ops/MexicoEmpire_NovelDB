from __future__ import annotations

import argparse
import csv
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPT_DIR))

import auto_resolve_links  # noqa: E402
import csv_to_md  # noqa: E402
import reclassify_generated_notes  # noqa: E402
import vault_maintenance  # noqa: E402


class AutoResolveLinksTests(unittest.TestCase):
    def test_analyze_no_report_does_not_create_output_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "note.md").write_text("[[Missing Target]]\n", encoding="utf-8")

            code = auto_resolve_links.run(
                argparse.Namespace(
                    mode="analyze",
                    limit=20,
                    root=str(root),
                    rules="",
                    no_report=True,
                    unlink_generics=False,
                )
            )

            self.assertEqual(code, 0)
            self.assertFalse((root / "08_Outputs").exists())

    def test_link_collection_ignores_code_escaped_image_and_empty_links(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            text = "\n".join(
                [
                    r"\[[Escaped]]",
                    "![[Embedded_Image]]",
                    "[[   ]]",
                    "```",
                    "[[Inside_Code]]",
                    "```",
                    "[[Real_Target#Heading|alias]]",
                ]
            )
            (root / "note.md").write_text(text, encoding="utf-8")

            counts, _locations = auto_resolve_links.collect_unresolved(root)

            self.assertEqual(dict(counts), {"Real_Target": 1})

    def test_finalize_does_not_unlink_generics_without_flag(self) -> None:
        counts = {"lowercase generic": 2}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidates, unlink, skipped = auto_resolve_links.build_finalize_candidates(
                root,
                counts,  # type: ignore[arg-type]
                {"unlink_generics": False},
            )

            self.assertEqual(candidates, [])
            self.assertEqual(unlink, [])
            self.assertEqual(len(skipped), 1)


class CsvToMdTests(unittest.TestCase):
    def test_dry_run_does_not_create_output_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            csv_path = root / "facts.csv"
            fields = sorted(csv_to_md.REQUIRED_COLUMNS["fact_cards"])
            row = {field: "" for field in fields}
            row.update(
                {
                    "id": "FACT_TEST_0001",
                    "title": "Test fact",
                    "source_id": "SRC_HAMNETT_1994_JUAREZ",
                    "evidence_category": "author_interpretation",
                    "confidence": "probable",
                    "claim": "A test claim.",
                }
            )
            with csv_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow(row)

            csv_to_md.convert(
                argparse.Namespace(
                    vault=str(root / "vault"),
                    csv=str(csv_path),
                    kind="fact_cards",
                    overwrite=False,
                    dry_run=True,
                )
            )

            self.assertFalse((root / "vault" / "02_Fact_Cards").exists())

    def test_hamnett_fact_card_uses_hamnett_tags(self) -> None:
        content, _title = csv_to_md.render_fact_card(
            {
                "id": "FACT_TEST_0001",
                "title": "Hamnett test",
                "source_id": "SRC_HAMNETT_1994_JUAREZ",
                "evidence_category": "author_interpretation",
                "confidence": "probable",
                "claim": "A test claim.",
            }
        )

        self.assertIn('tags: "fact-card;hamnett;juarez"', content)
        self.assertNotIn("shawcross", content)


class VaultMaintenanceTests(unittest.TestCase):
    def test_printed_page_status_defaults_to_not_verified(self) -> None:
        note = vault_maintenance.Note(
            path=Path("FACT_TEST.md"),
            text="",
            frontmatter={"printed_page": "p.1"},
        )

        self.assertEqual(vault_maintenance.printed_page_status_value(note), "not_verified")

    def test_collect_outlinks_ignores_code_escaped_image_and_empty_links(self) -> None:
        text = "\n".join(
            [
                r"\[[Escaped]]",
                "![[Embedded_Image]]",
                "[[   ]]",
                "```",
                "[[Inside_Code]]",
                "```",
                "[[Real_Target#Heading|alias]]",
            ]
        )

        self.assertEqual(vault_maintenance.collect_outlinks(text), {"Real_Target"})

    def test_frontmatter_parser_handles_multiline_and_inline_lists(self) -> None:
        text = "\n".join(
            [
                "---",
                "type: fact_card",
                "people:",
                '  - "Benito_Juarez"',
                "themes: [Liberalism, Constitutionalism]",
                "---",
                "",
                "# Note",
            ]
        )

        parsed = vault_maintenance.parse_frontmatter(text)

        self.assertEqual(parsed["people"], ["Benito_Juarez"])
        self.assertEqual(parsed["themes"], ["Liberalism", "Constitutionalism"])


class ReclassifyGeneratedNotesTests(unittest.TestCase):
    def test_no_report_does_not_create_report_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old_root = reclassify_generated_notes.ROOT
            old_kind_dirs = reclassify_generated_notes.KIND_DIRS
            try:
                reclassify_generated_notes.ROOT = root
                reclassify_generated_notes.KIND_DIRS = {
                    "event": root / "04_Events",
                    "organization": root / "03_Entities" / "Organizations",
                    "place": root / "03_Entities" / "Places",
                    "theme": root / "03_Entities" / "Themes",
                }
                code = reclassify_generated_notes.run(
                    argparse.Namespace(apply=False, no_report=True, check=False)
                )
            finally:
                reclassify_generated_notes.ROOT = old_root
                reclassify_generated_notes.KIND_DIRS = old_kind_dirs

            self.assertEqual(code, 0)
            self.assertFalse((root / "08_Outputs").exists())

    def test_check_returns_nonzero_when_items_are_skipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old_root = reclassify_generated_notes.ROOT
            old_kind_dirs = reclassify_generated_notes.KIND_DIRS
            try:
                reclassify_generated_notes.ROOT = root
                reclassify_generated_notes.KIND_DIRS = {
                    "event": root / "04_Events",
                    "organization": root / "03_Entities" / "Organizations",
                    "place": root / "03_Entities" / "Places",
                    "theme": root / "03_Entities" / "Themes",
                }
                code = reclassify_generated_notes.run(
                    argparse.Namespace(apply=False, no_report=True, check=True)
                )
            finally:
                reclassify_generated_notes.ROOT = old_root
                reclassify_generated_notes.KIND_DIRS = old_kind_dirs

            self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
