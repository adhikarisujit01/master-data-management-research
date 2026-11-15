import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from mdm_demo import build_view, evaluate, normalize_email


class TestMdmDemo(unittest.TestCase):
    def test_normalize_email(self):
        self.assertEqual(normalize_email("  A@EXAMPLE.TEST "), "a@example.test")

    def test_duplicate_sources_merge_with_lineage(self):
        rows = [
            {"source": "orders", "record_id": "2", "name": " Ana ", "email": "ANA@EXAMPLE.TEST", "city": ""},
            {"source": "crm", "record_id": "1", "name": "Ana", "email": "ana@example.test", "city": "SF"},
        ]
        view = build_view(rows)
        self.assertEqual(len(view), 1)
        self.assertEqual(view[0]["city"], "SF")
        self.assertEqual(view[0]["source_count"], 2)
        self.assertEqual(len(view[0]["source_record_ids"]), 2)
        self.assertEqual(evaluate(rows, view)["duplicate_excess_under_exact_email_key"], 1)

    def test_distinct_emails_not_merged_on_name(self):
        rows = [
            {"source": "crm", "record_id": "1", "name": "Alex Kim", "email": "a@example.test", "city": "SF"},
            {"source": "orders", "record_id": "2", "name": "Alex Kim", "email": "b@example.test", "city": "SF"},
        ]
        self.assertEqual(len(build_view(rows)), 2)

    def test_missing_key_fails_closed(self):
        with self.assertRaises(ValueError):
            build_view([{"source": "crm", "record_id": "1", "name": "X", "email": "", "city": ""}])


if __name__ == "__main__":
    unittest.main()
