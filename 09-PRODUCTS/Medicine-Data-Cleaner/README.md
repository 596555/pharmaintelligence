# Medicine Master Data Validator — MVP 0.1

A pharmacy-informatics utility that validates the **structure and completeness** of a medicine catalogue. It does not decide clinical equivalence, recommend therapy or silently correct drug information.

## Run
From repository root:
```powershell
py 09-PRODUCTS/Medicine-Data-Cleaner/medicine_validator.py 09-PRODUCTS/Medicine-Data-Cleaner/data/synthetic_medicine_master.csv
py -m unittest discover -s 09-PRODUCTS/Medicine-Data-Cleaner/tests -v
```

## Checks
- Required ingredient, brand, strength, unit, dosage form, route and pack size.
- Numeric positive strength and pack size.
- Controlled values for strength unit, dosage form and route.
- Duplicate key candidates using ingredient + strength + unit + form + route.
- Explicit validation issue report; no auto-merge or clinical inference.

All records are synthetic. A pharmacist or authorized medicines-information professional must verify clinical meaning against authoritative local sources.
