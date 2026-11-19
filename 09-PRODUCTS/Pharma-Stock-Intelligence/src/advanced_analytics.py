"""Pharmacy-focused inventory analytics; educational synthetic-data prototype."""
from __future__ import annotations
from collections import defaultdict
from datetime import date
from pathlib import Path
import csv, math

def read_csv(path: str | Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def consumption_summary(stock_rows: list[dict], usage_rows: list[dict], as_of: date,
                        lookback_days: int = 120, lead_time_days: int = 21,
                        safety_days: int = 14, target_days: int = 45) -> list[dict]:
    """Estimate administrative replenishment review from recorded issues.
    Assumes the supplied usage window is representative; never auto-orders.
    """
    if lookback_days <= 0 or lead_time_days < 0 or safety_days < 0 or target_days <= 0:
        raise ValueError("Invalid planning horizon")
    by_product = defaultdict(int)
    for row in usage_rows:
        try:
            issue_date = date.fromisoformat(row["issue_date"])
            qty = int(row["quantity_issued"])
        except (KeyError, ValueError, TypeError) as exc:
            raise ValueError("Invalid consumption record") from exc
        if qty < 0:
            raise ValueError("Quantity issued cannot be negative")
        age = (as_of - issue_date).days
        if 0 <= age < lookback_days:
            by_product[row["product_id"]] += qty
    stock_by_product = defaultdict(int)
    meta = {}
    for row in stock_rows:
        pid = row["product_id"]
        stock_by_product[pid] += int(row["quantity"])
        meta[pid] = row
    result = []
    for pid, row in meta.items():
        issued = by_product[pid]
        daily = issued / lookback_days
        available = stock_by_product[pid]
        safety = math.ceil(daily * safety_days)
        reorder_point = math.ceil(daily * (lead_time_days + safety_days))
        target = math.ceil(daily * target_days + safety)
        suggestion = max(0, target - available)
        result.append({
            "product_id": pid, "medicine_name": row["medicine_name"],
            "quantity_on_hand": available, "issued_in_lookback": issued,
            "average_daily_issues": round(daily, 3),
            "estimated_days_of_stock": round(available / daily, 1) if daily else None,
            "lead_time_days_assumed": lead_time_days, "safety_stock_units": safety,
            "estimated_reorder_point": reorder_point,
            "suggested_review_quantity": suggestion,
            "review_status": "REPLENISHMENT_REVIEW" if available <= reorder_point else "MONITOR",
            "assumption": "Historical issues assumed representative; pharmacist/procurement approval required"
        })
    return sorted(result, key=lambda x: (x["review_status"] != "REPLENISHMENT_REVIEW", x["medicine_name"]))

def abc_analysis(stock_rows: list[dict], usage_rows: list[dict], as_of: date,
                 lookback_days: int = 120) -> list[dict]:
    """ABC by annualized usage value (issues × listed unit cost), not clinical importance."""
    used = defaultdict(int)
    for row in usage_rows:
        d = date.fromisoformat(row["issue_date"])
        q = int(row["quantity_issued"])
        if q < 0:
            raise ValueError("Quantity issued cannot be negative")
        if 0 <= (as_of - d).days < lookback_days:
            used[row["product_id"]] += q
    products = {}
    for row in stock_rows:
        products[row["product_id"]] = row
    ranked = []
    for pid, row in products.items():
        value = used[pid] * float(row["unit_cost"])
        ranked.append({"product_id": pid, "medicine_name": row["medicine_name"],
                       "usage_value_in_window": round(value, 2)})
    ranked.sort(key=lambda x: x["usage_value_in_window"], reverse=True)
    total = sum(x["usage_value_in_window"] for x in ranked)
    cumulative = 0.0
    for item in ranked:
        share = item["usage_value_in_window"] / total if total else 0
        cumulative += share
        item["cumulative_value_share"] = round(cumulative, 4)
        item["abc_class"] = "A" if cumulative - share < 0.80 else ("B" if cumulative - share < 0.95 else "C")
    return ranked

def fefo_review(stock_rows: list[dict], as_of: date, horizon_days: int = 120) -> list[dict]:
    """Return earliest-expiry batches first; flags are prompts, not disposition decisions."""
    out = []
    for row in stock_rows:
        expiry = date.fromisoformat(row["expiry_date"])
        days = (expiry - as_of).days
        if days <= horizon_days:
            out.append({**row, "days_to_expiry": days,
                        "fefo_flag": "EXPIRED_QUARANTINE_REVIEW" if days < 0 else "EXPIRY_REVIEW"})
    return sorted(out, key=lambda x: (x["days_to_expiry"], x["medicine_name"]))

def fsn_classification(usage_rows: list[dict], as_of: date, product_ids: list[str],
                       fast_days: int = 30, slow_days: int = 90) -> list[dict]:
    last = {}
    for row in usage_rows:
        d = date.fromisoformat(row["issue_date"])
        pid = row["product_id"]
        if pid not in last or d > last[pid]:
            last[pid] = d
    out = []
    for pid in product_ids:
        days = (as_of - last[pid]).days if pid in last else None
        cls = "N" if days is None or days > slow_days else ("F" if days <= fast_days else "S")
        out.append({"product_id": pid, "days_since_last_issue": days, "fsn_class": cls})
    return out
