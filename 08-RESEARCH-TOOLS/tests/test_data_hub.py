import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from data_hub import build_request, run_query, safe_filename

class DataHubTests(unittest.TestCase):
    def test_safe_filename(self):
        self.assertEqual(safe_filename("Aspirin 500 mg"), "Aspirin_500_mg")

    def test_rejects_empty_term_and_invalid_limit(self):
        with self.assertRaises(ValueError):
            build_request("pubchem", " ")
        with self.assertRaises(ValueError):
            build_request("rxnorm", "metformin", 101)

    def test_pubchem_url(self):
        url, label = build_request("pubchem", "acetylsalicylic acid")
        self.assertIn("acetylsalicylic%20acid", url)
        self.assertIn("PubChem", label)

    def test_openfda_event_url(self):
        url, _ = build_request("openfda-events", "aspirin", 5)
        self.assertIn("api.fda.gov/drug/event.json", url)
        self.assertIn("limit=5", url)

    def test_run_saves_provenance_and_payload(self):
        sample = {"results": [{"term": "example"}]}
        with tempfile.TemporaryDirectory() as folder:
            with patch("data_hub.fetch_json", return_value=sample):
                path = run_query("pubchem", "example", outdir=Path(folder))
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved["data"], sample)
            self.assertEqual(saved["metadata"]["query"], "example")
            self.assertIn("retrieved_at_utc", saved["metadata"])
            self.assertIn("source_url", saved["metadata"])

if __name__ == "__main__":
    unittest.main()
