import unittest
from datetime import date
from stock_intelligence import analyze

class StockIntelligenceTests(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {"product_id":"A","medicine_name":"Demo","batch_no":"B1","expiry_date":"2026-12-01","quantity":"10","unit_cost":"2.5","monthly_usage":"30"},
            {"product_id":"A","medicine_name":"Demo","batch_no":"B2","expiry_date":"2027-06-01","quantity":"20","unit_cost":"2.5","monthly_usage":"30"},
        ]

    def test_summary_and_cover(self):
        result=analyze(self.rows,date(2026,11,19),90)
        self.assertEqual(result["summary"]["total_units_on_hand"],30)
        self.assertEqual(result["summary"]["near_expiry_batches"],1)
        self.assertEqual(result["summary"]["estimated_stock_value"],75.0)
        self.assertEqual(result["low_cover"][0]["estimated_days_cover"],30.0)

    def test_rejects_duplicate_batch(self):
        result=analyze(self.rows+[self.rows[0]],date(2026,11,19))
        self.assertEqual(result["summary"]["rejected_rows"],1)
        self.assertIn("duplicate",result["data_quality_issues"][0]["reason"])

    def test_rejects_negative_quantity(self):
        bad={**self.rows[0],"batch_no":"NEG","quantity":"-2"}
        result=analyze([bad],date(2026,11,19))
        self.assertEqual(result["summary"]["valid_rows"],0)
        self.assertEqual(result["summary"]["rejected_rows"],1)

if __name__=="__main__":
    unittest.main()
