from __future__ import annotations
from datetime import date
from pathlib import Path
import csv
REQUIRED={"product_id","medicine_name","category","batch_no","expiry_date","quantity","reorder_level","unit_cost","supplier"}
def load_stock(path: str|Path)->list[dict]:
    with open(path,newline="",encoding="utf-8-sig") as f: rows=list(csv.DictReader(f))
    validate_rows(rows); return rows
def validate_rows(rows:list[dict])->None:
    if not rows: raise ValueError("No data rows")
    missing=REQUIRED.difference(rows[0].keys())
    if missing: raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    seen=set()
    for n,r in enumerate(rows,2):
        for k in REQUIRED:
            if not str(r.get(k,"")).strip(): raise ValueError(f"Row {n}: {k} required")
        if r['batch_no'] in seen: raise ValueError(f"Row {n}: duplicate batch")
        seen.add(r['batch_no'])
        try:
            date.fromisoformat(r['expiry_date']); q=int(r['quantity']); level=int(r['reorder_level']); cost=float(r['unit_cost'])
        except (ValueError,TypeError) as e: raise ValueError(f"Row {n}: invalid date/numeric value") from e
        if q<0 or level<0 or cost<0 or cost==float('inf'): raise ValueError(f"Row {n}: values must be finite and non-negative")
def summarize(rows:list[dict],as_of:date|None=None)->dict:
    validate_rows(rows); as_of=as_of or date.today(); expired=near=low=0
    for r in rows:
        days=(date.fromisoformat(r['expiry_date'])-as_of).days; q=int(r['quantity'])
        if days<0: expired+=q
        elif days<=90: near+=q
        if q<int(r['reorder_level']): low+=1
    return {"records":len(rows),"total_units":sum(int(r['quantity']) for r in rows),"illustrative_stock_value":round(sum(int(r['quantity'])*float(r['unit_cost']) for r in rows),2),"expired_units":expired,"near_expiry_units_90d":near,"low_stock_batches":low}
def review_rows(rows:list[dict],as_of:date|None=None)->list[dict]:
    validate_rows(rows); as_of=as_of or date.today(); out=[]
    for r in rows:
        days=(date.fromisoformat(r['expiry_date'])-as_of).days; flags=[]
        if days<0: flags.append('EXPIRED_REVIEW')
        elif days<=90: flags.append('NEAR_EXPIRY_REVIEW')
        if int(r['quantity'])<int(r['reorder_level']): flags.append('LOW_STOCK_REVIEW')
        out.append({**r,'days_to_expiry':days,'review_flags':'|'.join(flags) or 'NONE'})
    return out
