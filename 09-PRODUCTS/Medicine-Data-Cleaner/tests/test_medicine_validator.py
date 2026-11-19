import sys,unittest
from pathlib import Path
HERE=Path(__file__).resolve()
sys.path.insert(0,str(HERE.parents[1]))
from medicine_validator import validate
DATA=HERE.parents[1]/"data"/"synthetic_medicine_master.csv"
import csv
def load():
 with open(DATA,newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
class MedicineValidatorTests(unittest.TestCase):
 def test_synthetic_catalog_passes(self): self.assertEqual(validate(load()),[])
 def test_missing_strength_flagged(self):
  rows=load(); rows[0]["strength_value"]=""
  self.assertIn("MISSING_VALUE",{x["issue"] for x in validate(rows)})
 def test_invalid_route_flagged(self):
  rows=load(); rows[0]["route"]="unknown"
  self.assertIn("UNRECOGNIZED_ROUTE_REVIEW",{x["issue"] for x in validate(rows)})
 def test_duplicate_identity_flagged(self):
  rows=load(); duplicate=dict(rows[0]); duplicate["product_id"]="M999"; duplicate["brand_name"]="AnotherBrand"; rows.append(duplicate)
  self.assertTrue(any(x["issue"].startswith("POSSIBLE_DUPLICATE") for x in validate(rows)))
if __name__=="__main__":unittest.main()
