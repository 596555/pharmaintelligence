import sys,unittest
from datetime import date
from pathlib import Path
HERE=Path(__file__).resolve()
sys.path.insert(0,str(HERE.parents[1]))
from src.stock_intelligence import load_stock,summarize,review_rows,validate_rows
DATA=HERE.parents[1]/'data'/'synthetic_stock.csv'
class StockTests(unittest.TestCase):
 def test_dataset_loads(self): self.assertEqual(len(load_stock(DATA)),10)
 def test_total_units(self): self.assertEqual(summarize(load_stock(DATA),date(2026,11,19))['total_units'],818)
 def test_expired_and_low_flags(self):
  rows=[{'product_id':'X','medicine_name':'Demo','category':'Other','batch_no':'B1','expiry_date':'2026-11-18','quantity':'5','reorder_level':'10','unit_cost':'1','supplier':'Demo'}]
  flags=review_rows(rows,date(2026,11,19))[0]['review_flags']
  self.assertIn('EXPIRED_REVIEW',flags); self.assertIn('LOW_STOCK_REVIEW',flags)
 def test_negative_quantity_rejected(self):
  rows=[{'product_id':'X','medicine_name':'Demo','category':'Other','batch_no':'B1','expiry_date':'2027-01-01','quantity':'-1','reorder_level':'0','unit_cost':'1','supplier':'Demo'}]
  with self.assertRaises(ValueError): validate_rows(rows)
if __name__=='__main__': unittest.main()
