# Drug Development & Manufacturing Intelligence Workbench

**Status:** Educational MVP 0.1 — synthetic data only.

## Purpose

A small practical tool for learning how development and manufacturing data can be validated and summarized. It complements the Pharma Stock Intelligence product by moving upstream from medicine supply into formulation/process development and quality-by-design documentation.

## Current features

- Validate synthetic development-batch CSV fields, numeric ranges and unique batch identifiers.
- Summarize formulation/stage observations descriptively (record counts and mean assay, dissolution, hardness and blend-uniformity CV).
- Validate QbD risk-register fields and 1–5 ratings.
- Calculate a transparent Severity × Occurrence × Detectability (RPN) sorting aid for documented risks.
- Export summary CSV files from the command line.
- Unit tests using Python's standard library only.

## Run on Windows 11

From the repository root:

```powershell
py -m unittest discover -s 09-PRODUCTS/Drug-Development-Workbench/tests -v
py 09-PRODUCTS/Drug-Development-Workbench/src/development_analytics.py batches 09-PRODUCTS/Drug-Development-Workbench/data/synthetic_development_batches.csv
py 09-PRODUCTS/Drug-Development-Workbench/src/development_analytics.py risks 09-PRODUCTS/Drug-Development-Workbench/data/synthetic_qbd_risk_register.csv
```

Optional CSV exports:

```powershell
py 09-PRODUCTS/Drug-Development-Workbench/src/development_analytics.py batches 09-PRODUCTS/Drug-Development-Workbench/data/synthetic_development_batches.csv --out batch_summary.csv
py 09-PRODUCTS/Drug-Development-Workbench/src/development_analytics.py risks 09-PRODUCTS/Drug-Development-Workbench/data/synthetic_qbd_risk_register.csv --out risk_review.csv
```

## Data dictionary

### Development batch file

- `batch_id`: synthetic unique identifier.
- `formulation_id`: fictional formulation/version identifier.
- `stage`: development stage label.
- `assay_pct`, `dissolution_30min_pct`, `hardness_n`, `blend_uniformity_cv_pct`, `moisture_pct`: fictional observations for data analysis practice.

### QbD risk register

- `risk_id`: unique training identifier.
- `parameter_type`: CQA, CMA or CPP label used in the example.
- `parameter`: documented attribute/parameter name.
- `severity`, `occurrence`, `detectability`: example ratings from 1 to 5.
- `rationale`, `current_control`, `review_owner`: fields that must be scientifically justified by the responsible team.

## Critical limitations

- All included data and scores are synthetic and are not pharmaceutical specifications or manufacturing instructions.
- The program does not perform process validation, capability analysis, stability assessment, analytical-method validation, batch disposition or product release.
- RPN is only a sortable review aid. It is not a universal risk threshold and does not replace a documented, context-specific quality-risk assessment.
- A higher or lower numerical score cannot decide patient risk or quality acceptability by itself.
- No real or confidential manufacturing data should be uploaded to this public repository.
