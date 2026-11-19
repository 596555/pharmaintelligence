# First Product — Pharma Stock Intelligence

## What it does
A reproducible command-line prototype that reads a synthetic batch-level CSV, validates rows, and produces a JSON report with stock totals, estimated stock value, near-expiry/expired batches, low-days-of-cover flags and rejected-row explanations.

## Run on Windows 11
```powershell
py --version
py -m unittest -v
py stock_intelligence.py sample_stock_batches.csv --as-of 2026-11-19 --output demo_report.json
```

The program uses Python's standard library; no paid service or package installation is needed.

## Data dictionary
- `product_id`: synthetic internal medicine identifier
- `medicine_name`: illustrative label only
- `batch_no`: synthetic batch identifier
- `expiry_date`: ISO date (YYYY-MM-DD)
- `quantity`: non-negative units on hand
- `unit_cost`: illustrative cost per unit in unspecified currency units
- `monthly_usage`: assumed average units used per month

## KPI definitions
- Stock value = sum(quantity × unit_cost), only meaningful if the supplied costs and currency are valid.
- Near expiry = batches expiring from the reference date through the configured expiry window.
- Days of cover = total product quantity ÷ monthly usage × 30; only a rough operational estimate.
- Low cover flag = estimated cover under 30 days. This is a review queue, not an automatic reorder instruction.

## Limitations and safety
All included data are synthetic. Do not upload patient data, confidential pharmacy exports or credentials. This prototype does not recommend substitutions, doses, prescribing or dispensing actions. Expired stock is flagged for authorized staff review; the script does not direct disposal. Human verification is mandatory.
