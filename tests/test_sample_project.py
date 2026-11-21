import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class SampleProjectTests(unittest.TestCase):
    def setUp(self):
        self.project = json.loads((ROOT / "examples/sample-project.json").read_text(encoding="utf-8"))

    def test_schema_board_format(self):
        self.assertEqual(self.project["format"], "schema-board")
        self.assertEqual(self.project["version"], 1)

    def test_relationship_endpoints_exist(self):
        tables = {t["id"]: t for t in self.project["tables"]}
        for rel in self.project["rels"]:
            self.assertIn(rel["from"]["t"], tables)
            self.assertIn(rel["to"]["t"], tables)
            from_cols = {c["id"] for c in tables[rel["from"]["t"]]["columns"]}
            to_cols = {c["id"] for c in tables[rel["to"]["t"]]["columns"]}
            self.assertIn(rel["from"]["c"], from_cols)
            self.assertIn(rel["to"]["c"], to_cols)

    def test_examples_are_fictional(self):
        raw = json.dumps(self.project, ensure_ascii=False).lower()
        self.assertIn("demo_catalog", raw)
        self.assertIn("customers_demo", raw)
        self.assertNotIn("martech_dev", raw)
        self.assertNotIn("production", raw)

if __name__ == "__main__":
    unittest.main()
