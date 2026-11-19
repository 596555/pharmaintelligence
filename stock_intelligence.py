"""PHARMAINTELLIGENCE 365 — Pharma Stock Intelligence (educational MVP).
Uses only Python's standard library. Synthetic/demo data only; never use for dispensing.
"""
from __future__ import annotations
import argparse, csv, json
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

REQUIRED = ("product_id", "medicine_name", "batch_no", "expiry_date", "quantity", "unit_cost", "monthly_usage")

def load_rows(path: Path):
    with path.open("r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        missing = [c for c in REQUIRED if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError("Missing required columns: " + ", ".join(missing))
        return list(reader)

def analyze(rows, as_of: date, expiry_window_days: int = 90):
    issues, valid, seen = [], [], set()
    for line, row in enumerate(rows, start=2):
        clean = {k: (v or "").strip() for k, v in row.items()}
        try:
            if any(not clean.get(k) for k in REQUIRED):
                raise ValueError("required field is blank")
            expiry = date.fromisoformat(clean["expiry_date"])
            qty = int(clean["quantity"])
            cost = float(clean["unit_cost"])
            usage = float(clean["monthly_usage"])
            if qty < 0 or cost < 0 or usage < 0:
                raise ValueError("quantity, cost and usage must be non-negative")
            if not clean["product_id"] or not clean["batch_no"]:
                raise ValueError("product_id and batch_no are required")
            key = (clean["product_id"], clean["batch_no"])
            if key in seen:
                raise ValueError("duplicate product_id + batch_no")
            seen.add(key)
            valid.append({**clean, "_expiry": expiry, "_qty": qty, "_cost": cost, "_usage": usage})
        except (ValueError, TypeError) as exc:
            issues.append({"row": line, "product_id": clean.get("product_id",""), "reason": str(exc)})
    near = [r for r in valid if 0 <= (r["_expiry"] - as_of).days <= expiry_window_days]
    expired = [r for r in valid if r["_expiry"] < as_of]
    by_product = defaultdict(lambda: {"name":"", "quantity":0, "monthly_usage":0.0, "stock_value":0.0})
    for r in valid:
        p = by_product[r["product_id"]]
        p["name"] = r["medicine_name"]
        p["quantity"] += r["_qty"]
        p["monthly_usage"] += r["_usage"]
        p["stock_value"] += r["_qty"] * r["_cost"]
    low = []
    for pid, p in by_product.items():
        days_cover = (p["quantity"] / p["monthly_usage"] * 30) if p["monthly_usage"] > 0 else None
        if days_cover is not None and days_cover < 30:
            low.append({"product_id":pid, "medicine_name":p["name"], "quantity":p["quantity"], "estimated_days_cover":round(days_cover,1)})
    summary = {
        "as_of": as_of.isoformat(),
        "rows_received": len(rows),
        "valid_rows": len(valid),
        "rejected_rows": len(issues),
        "total_units_on_hand": sum(r["_qty"] for r in valid),
        "estimated_stock_value": round(sum(r["_qty"]*r["_cost"] for r in valid),2),
        "near_expiry_batches": len(near),
        "near_expiry_units": sum(r["_qty"] for r in near),
        "expired_batches": len(expired),
        "expired_units": sum(r["_qty"] for r in expired),
        "products_below_30_days_cover": len(low),
    }
    near_out = [{"product_id":r["product_id"],"medicine_name":r["medicine_name"],"batch_no":r["batch_no"],"expiry_date":r["expiry_date"],"quantity":r["_qty"]} for r in near]
    expired_out = [{"product_id":r["product_id"],"medicine_name":r["medicine_name"],"batch_no":r["batch_no"],"expiry_date":r["expiry_date"],"quantity":r["_qty"]} for r in expired]
    return {"summary":summary,"near_expiry":near_out,"expired":expired_out,"low_cover":low,"data_quality_issues":issues}

def main():
    parser=argparse.ArgumentParser(description="Analyze synthetic pharmacy stock batches.")
    parser.add_argument("input", type=Path, help="Input CSV")
    parser.add_argument("--as-of", default=date.today().isoformat(), help="Reference date YYYY-MM-DD")
    parser.add_argument("--expiry-window", type=int, default=90, help="Days to flag before expiry")
    parser.add_argument("--output", type=Path, default=Path("stock_report.json"))
    args=parser.parse_args()
    if args.expiry_window < 0: parser.error("--expiry-window must be non-negative")
    result=analyze(load_rows(args.input), date.fromisoformat(args.as_of), args.expiry_window)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(result["summary"],ensure_ascii=False,indent=2))
    print(f"Full report: {args.output}")
    if result["data_quality_issues"]:
        print("WARNING: some rows were rejected; inspect data_quality_issues in the report.")

if __name__ == "__main__":
    main()
