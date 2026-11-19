"""Structural medicine catalogue validation; not clinical verification."""
from __future__ import annotations
import csv, sys
from pathlib import Path

REQUIRED={"product_id","generic_name","brand_name","strength_value","strength_unit","dosage_form","route","pack_size","manufacturer"}
ALLOWED_UNITS={"mg","mcg","g","mg/mL","mcg/mL","IU","%"}
ALLOWED_FORMS={"tablet","capsule","oral_solution","oral_suspension","injection","cream","ointment","inhaler","eye_drops"}
ALLOWED_ROUTES={"oral","IV","IM","SC","topical","inhalation","ophthalmic"}

def validate(rows:list[dict])->list[dict]:
    issues=[]
    if not rows: return [{"row":0,"product_id":"","field":"dataset","issue":"EMPTY_DATASET"}]
    missing=REQUIRED.difference(rows[0].keys())
    if missing: return [{"row":1,"product_id":"","field":f,"issue":"MISSING_COLUMN"} for f in sorted(missing)]
    seen={}
    for n,row in enumerate(rows,2):
        pid=row.get("product_id","")
        for field in REQUIRED:
            if not str(row.get(field,"")).strip():
                issues.append({"row":n,"product_id":pid,"field":field,"issue":"MISSING_VALUE"})
        try:
            strength=float(row.get("strength_value",""))
            if strength<=0: raise ValueError
        except ValueError:
            issues.append({"row":n,"product_id":pid,"field":"strength_value","issue":"INVALID_POSITIVE_NUMBER"})
        try:
            pack=int(row.get("pack_size",""))
            if pack<=0: raise ValueError
        except ValueError:
            issues.append({"row":n,"product_id":pid,"field":"pack_size","issue":"INVALID_POSITIVE_INTEGER"})
        if row.get("strength_unit") not in ALLOWED_UNITS:
            issues.append({"row":n,"product_id":pid,"field":"strength_unit","issue":"UNRECOGNIZED_UNIT_REVIEW"})
        if row.get("dosage_form") not in ALLOWED_FORMS:
            issues.append({"row":n,"product_id":pid,"field":"dosage_form","issue":"UNRECOGNIZED_FORM_REVIEW"})
        if row.get("route") not in ALLOWED_ROUTES:
            issues.append({"row":n,"product_id":pid,"field":"route","issue":"UNRECOGNIZED_ROUTE_REVIEW"})
        key=tuple(str(row.get(k,"")).strip().lower() for k in ("generic_name","strength_value","strength_unit","dosage_form","route"))
        if all(key):
            if key in seen:
                issues.append({"row":n,"product_id":pid,"field":"medicine_identity","issue":f"POSSIBLE_DUPLICATE_OF_ROW_{seen[key]}"})
            else: seen[key]=n
    return issues

def main(path:str)->int:
    with open(path,newline="",encoding="utf-8-sig") as f: rows=list(csv.DictReader(f))
    issues=validate(rows)
    print(f"Rows reviewed: {len(rows)} | Issues: {len(issues)}")
    if issues:
        for issue in issues: print(" | ".join(f"{k}={v}" for k,v in issue.items()))
        return 1
    print("Structural checks passed. Clinical verification is still required.")
    return 0

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Usage: python medicine_validator.py <medicine_master.csv>"); raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
