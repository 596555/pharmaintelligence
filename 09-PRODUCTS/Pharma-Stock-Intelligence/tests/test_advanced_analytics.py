import sys,unittest
from datetime import date
from pathlib import Path
HERE=Path(__file__).resolve()
sys.path.insert(0,str(HERE.parents[1]))
from src.stock_intelligence import load_stock
from src.advanced_analytics import read_csv,consumption_summary,abc_analysis,fefo_review,fsn_classification
BASE=HERE.parents[1]
STOCK=load_stock(BASE/'data'/'synthetic_stock.csv')
USAGE=read_csv(BASE/'data'/'synthetic_consumption.csv')
ASOF=date(2026,11,19)
class AdvancedTests(unittest.TestCase):
 def test_consumption_has_all_products(self):
  rows=consumption_summary(STOCK,USAGE,ASOF); self.assertEqual(len(rows),10)
  self.assertTrue(all(x['average_daily_issues']>=0 for x in rows))
 def test_replenishment_status_values(self):
  rows=consumption_summary(STOCK,USAGE,ASOF)
  self.assertTrue(all(x['review_status'] in {'REPLENISHMENT_REVIEW','MONITOR'} for x in rows))
 def test_abc_classes(self):
  rows=abc_analysis(STOCK,USAGE,ASOF); self.assertEqual(len(rows),10)
  self.assertTrue(set(x['abc_class'] for x in rows).issubset({'A','B','C'}))
 def test_fefo_earliest_first(self):
  rows=fefo_review(STOCK,ASOF,500)
  self.assertEqual(rows,sorted(rows,key=lambda x:(x['days_to_expiry'],x['medicine_name'])))
 def test_fsn_classes(self):
  rows=fsn_classification(USAGE,ASOF,[x['product_id'] for x in STOCK])
  self.assertEqual(len(rows),10); self.assertTrue(set(x['fsn_class'] for x in rows).issubset({'F','S','N'}))
 def test_negative_issue_rejected(self):
  bad=[{'product_id':'P1','issue_date':'2026-11-01','quantity_issued':'-2'}]
  with self.assertRaises(ValueError): consumption_summary(STOCK,bad,ASOF)
if __name__=='__main__': unittest.main()
