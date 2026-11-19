# Pharma Stock Intelligence — runnable MVP 0.1

A local learning dashboard for **fictional inventory only**. It summarizes batch quantities, expiry exposure and low-stock records. It does not place orders or support clinical decisions.

## Run on Windows 11
From repository root:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r 09-PRODUCTS/Pharma-Stock-Intelligence/requirements.txt
streamlit run 09-PRODUCTS/Pharma-Stock-Intelligence/app.py
```

## Run tests
```powershell
py -m unittest discover -s 09-PRODUCTS/Pharma-Stock-Intelligence/tests -v
```

## KPI definitions
- Total units: sum of non-negative quantities.
- Expired units: quantity in batches with expiry before the selected analysis date.
- Near expiry: quantity in batches expiring from the analysis date through 90 days later.
- Low-stock batches: count of batches with quantity below reorder level.
- Illustrative value: quantity × fictional unit cost; no real currency or valuation is implied.

No demand history is included, so days-of-cover is intentionally not calculated. Flags are administrative review prompts only. Never use real patient or confidential pharmacy data.
