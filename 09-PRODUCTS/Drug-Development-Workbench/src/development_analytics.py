"""Educational analytics for synthetic pharmaceutical development records.

This module is not a GMP system and must not be used for batch release,
specification setting, process validation, or manufacturing instructions.
Only synthetic training data is included in this repository.
"""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import fmean
from typing import Iterable

BATCH_REQUIRED = {
    "batch_id", "formulation_id", "stage", "assay_pct",
    "dissolution_30min_pct", "hardness_n",
    "blend_uniformity_cv_pct", "moisture_pct",
}
PERCENT_FIELDS = {
    "assay_pct", "dissolution_30min_pct",
    "blend_uniformity_cv_pct", "moisture_pct",
}
POSITIVE_FIELDS = {"hardness_n"}
RISK_REQUIRED = {
    "risk_id", "parameter_type", "parameter", "severity",
    "occurrence", "detectability", "rationale",
    "current_control", "review_owner",
}
RISK_TYPES = {"CQA", "CMA", "CPP"}


def read_csv(path: str | Path) -> list[dict[str, str]]:
    """Read a UTF-8 CSV file and return rows as dictionaries."""
    with Path(path).open("r", newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def _required_columns(rows: list[dict[str, str]], required: set[str], label: str) -> None:
    if not rows:
        raise ValueError(f"{label} file has no data rows.")
    missing = required - set(rows[0].keys())
    if missing:
        raise ValueError(f"{label} file is missing columns: {', '.join(sorted(missing))}")


def validate_batch_records(rows: list[dict[str, str]]) -> None:
    """Raise ValueError for missing, duplicate or invalid synthetic batch records."""
    _required_columns(rows, BATCH_REQUIRED, "Batch")
    seen: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        batch_id = row.get("batch_id", "").strip()
        if not batch_id:
            raise ValueError(f"Line {line_number}: batch_id is required.")
        if batch_id in seen:
            raise ValueError(f"Line {line_number}: duplicate batch_id '{batch_id}'.")
        seen.add(batch_id)
        for field in ("formulation_id", "stage"):
            if not row.get(field, "").strip():
                raise ValueError(f"Line {line_number}: {field} is required.")
        for field in PERCENT_FIELDS | POSITIVE_FIELDS:
            raw = row.get(field, "").strip()
            try:
                value = float(raw)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Line {line_number}: {field} must be numeric.") from exc
            if field in PERCENT_FIELDS and not 0 <= value <= 100:
                raise ValueError(f"Line {line_number}: {field} must be between 0 and 100.")
            if field in POSITIVE_FIELDS and value <= 0:
                raise ValueError(f"Line {line_number}: {field} must be greater than zero.")


def summarize_batches(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    """Return descriptive averages grouped by formulation and development stage."""
    validate_batch_records(rows)
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(row["formulation_id"].strip(), row["stage"].strip())].append(row)

    result: list[dict[str, object]] = []
    measure_fields = (
        "assay_pct", "dissolution_30min_pct", "hardness_n",
        "blend_uniformity_cv_pct", "moisture_pct",
    )
    for (formulation_id, stage), group in sorted(grouped.items()):
        summary: dict[str, object] = {
            "formulation_id": formulation_id,
            "stage": stage,
            "record_count": len(group),
        }
        for field in measure_fields:
            summary[f"mean_{field}"] = round(
                fmean(float(row[field]) for row in group), 3
            )
        result.append(summary)
    return result


def validate_risk_records(rows: list[dict[str, str]]) -> None:
    """Validate completeness and the illustrative 1–5 rating scale."""
    _required_columns(rows, RISK_REQUIRED, "Risk register")
    seen: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        risk_id = row.get("risk_id", "").strip()
        if not risk_id:
            raise ValueError(f"Line {line_number}: risk_id is required.")
        if risk_id in seen:
            raise ValueError(f"Line {line_number}: duplicate risk_id '{risk_id}'.")
        seen.add(risk_id)
        if row.get("parameter_type", "").strip().upper() not in RISK_TYPES:
            raise ValueError(f"Line {line_number}: parameter_type must be CQA, CMA or CPP.")
        for field in ("parameter", "rationale", "current_control", "review_owner"):
            if not row.get(field, "").strip():
                raise ValueError(f"Line {line_number}: {field} is required.")
        for field in ("severity", "occurrence", "detectability"):
            try:
                score = int(row[field])
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Line {line_number}: {field} must be an integer from 1 to 5.") from exc
            if score < 1 or score > 5:
                raise ValueError(f"Line {line_number}: {field} must be an integer from 1 to 5.")


def prioritize_risks(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    """Sort documented risks by illustrative RPN; this is not an acceptability decision."""
    validate_risk_records(rows)
    result = []
    for row in rows:
        item: dict[str, object] = dict(row)
        item["rpn_screening_value"] = (
            int(row["severity"]) * int(row["occurrence"]) * int(row["detectability"])
        )
        result.append(item)
    return sorted(result, key=lambda item: int(item["rpn_screening_value"]), reverse=True)


def write_csv(rows: list[dict[str, object]], output_path: str | Path) -> None:
    if not rows:
        raise ValueError("No output rows to write.")
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Educational analysis of synthetic pharmaceutical development records."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("batches", "risks"):
        sub = subparsers.add_parser(command)
        sub.add_argument("input_csv", help="Path to a synthetic CSV training file.")
        sub.add_argument("--out", help="Optional output CSV path.")
    args = parser.parse_args()

    rows = read_csv(args.input_csv)
    output = summarize_batches(rows) if args.command == "batches" else prioritize_risks(rows)
    if args.out:
        write_csv(output, args.out)
        print(f"Wrote {len(output)} rows to {args.out}")
    else:
        for row in output:
            print(row)


if __name__ == "__main__":
    main()
