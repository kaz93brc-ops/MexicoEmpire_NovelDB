from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class WorkflowDocumentationTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        path = ROOT / relative
        self.assertTrue(path.exists(), f"missing required workflow file: {relative}")
        return path.read_text(encoding="utf-8")

    def test_agents_has_repository_and_publish_completion_gates(self) -> None:
        agents = self.read("AGENTS.md")
        for required in (
            "## Repository preflight",
            "git rev-parse --show-toplevel",
            "git status --short --branch",
            "専用branch",
            "commit・push",
            "PR URL",
            "ローカルDB更新完了・GitHub反映未完了",
        ):
            self.assertIn(required, agents)

    def test_references_point_to_tracked_canonical_files(self) -> None:
        readme = self.read("README.md")
        prompt = self.read("93_Docs/ChatGPT_DB_Update_Prompt_README.md")
        workflow = self.read("93_Docs/GitHub_Workflow.md")
        self.assertIn("このリポジトリ内の `AGENTS.md` を正本", readme)
        self.assertIn("git rev-parse --show-toplevel", prompt)
        self.assertIn("repository rootの `AGENTS.md` を正本", workflow)

    def test_pr_template_requires_measured_github_identifiers(self) -> None:
        template = self.read(".github/pull_request_template.md")
        self.assertIn("vault rootを確認", template)
        self.assertIn("branch名、commit SHA、PR URLを実測", template)


if __name__ == "__main__":
    unittest.main()
