import unittest

from development_analytics import (
    prioritize_risks,
    summarize_batches,
    validate_batch_records,
    validate_risk_records,
)


class DevelopmentAnalyticsTests(unittest.TestCase):
    def setUp(self):
        self.batch_rows = [
            {
                "batch_id": "B1", "formulation_id": "F-A", "stage": "screening",
                "assay_pct": "98.0", "dissolution_30min_pct": "80.0",
                "hardness_n": "65", "blend_uniformity_cv_pct": "4.0",
                "moisture_pct": "2.0",
            },
            {
                "batch_id": "B2", "formulation_id": "F-A", "stage": "screening",
                "assay_pct": "100.0", "dissolution_30min_pct": "90.0",
                "hardness_n": "75", "blend_uniformity_cv_pct": "6.0",
                "moisture_pct": "2.4",
            },
        ]

    def test_batch_summary_groups_and_averages(self):
        result = summarize_batches(self.batch_rows)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["record_count"], 2)
        self.assertEqual(result[0]["mean_assay_pct"], 99.0)
        self.assertEqual(result[0]["mean_dissolution_30min_pct"], 85.0)

    def test_duplicate_batch_ids_are_rejected(self):
        duplicate = [dict(self.batch_rows[0]), dict(self.batch_rows[0])]
        with self.assertRaisesRegex(ValueError, "duplicate batch_id"):
            validate_batch_records(duplicate)

    def test_percent_above_100_is_rejected(self):
        invalid = [dict(self.batch_rows[0])]
        invalid[0]["assay_pct"] = "101"
        with self.assertRaisesRegex(ValueError, "between 0 and 100"):
            validate_batch_records(invalid)

    def test_risk_register_is_sorted_by_rpn(self):
        risks = [
            {
                "risk_id": "R1", "parameter_type": "CQA", "parameter": "Dissolution",
                "severity": "5", "occurrence": "2", "detectability": "2",
                "rationale": "Training rationale", "current_control": "Training control",
                "review_owner": "Reviewer",
            },
            {
                "risk_id": "R2", "parameter_type": "CPP", "parameter": "Mixing time",
                "severity": "3", "occurrence": "3", "detectability": "3",
                "rationale": "Training rationale", "current_control": "Training control",
                "review_owner": "Reviewer",
            },
        ]
        ranked = prioritize_risks(risks)
        self.assertEqual(ranked[0]["risk_id"], "R2")
        self.assertEqual(ranked[0]["rpn_screening_value"], 27)

    def test_invalid_risk_rating_is_rejected(self):
        risks = [{
            "risk_id": "R1", "parameter_type": "CQA", "parameter": "Dissolution",
            "severity": "0", "occurrence": "2", "detectability": "2",
            "rationale": "Training rationale", "current_control": "Training control",
            "review_owner": "Reviewer",
        }]
        with self.assertRaisesRegex(ValueError, "from 1 to 5"):
            validate_risk_records(risks)


if __name__ == "__main__":
    unittest.main()
