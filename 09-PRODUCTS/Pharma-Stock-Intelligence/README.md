# Pharma Stock Intelligence — pharmacy analytics MVP 0.2

A pharmacy operations analytics prototype using synthetic batch stock and issue history. This is **not an accounting workbook** and does not automate purchasing or clinical decisions.

## Run on Windows 11
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r 09-PRODUCTS/Pharma-Stock-Intelligence/requirements.txt
py -m unittest discover -s 09-PRODUCTS/Pharma-Stock-Intelligence/tests -v
streamlit run 09-PRODUCTS/Pharma-Stock-Intelligence/app.py
```

## Modules
- Batch inventory and expiry review.
- Consumption-based average daily issues, estimated days of stock, safety stock, reorder point and suggested review quantity.
- ABC classification by usage value.
- FSN movement classification.
- FEFO expiry queue and CSV exports.

The bundled inventory and issue history are synthetic. Lead time, safety buffer and target horizon are adjustable examples. Issue history can understate demand during stockouts. Pack/unit conversion, seasonality, supplier variability, returns, transfers and minimum order quantities are not modeled. ABC is not VEN; VEN requires local expert governance.

All flags require review by authorized pharmacy/procurement staff. No patient data, prescriptions, dispensing advice, treatment decisions or automatic purchase orders are supported.
