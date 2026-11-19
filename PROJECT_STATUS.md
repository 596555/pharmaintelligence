# Project status — 19 November 2026

## Published
- Initial project charter, 365-day roadmap, Windows setup and learning tracks.
- Pharma Stock Intelligence MVP: Python validation/KPI engine, synthetic batch CSV, Streamlit dashboard and unit tests.
- Windows run instructions and product-specific dependencies.
- Excel/Power BI exercise, SQL schema, automation blueprint and portfolio case study.
- GitHub Actions workflow to run the MVP unit tests on pushes and pull requests.

## Verification
The key source files, dataset, tests, execution plan and workflow were fetched successfully from the default branch after publishing. The GitHub Actions workflow is configured; a passing CI result must be confirmed in the Actions tab after its run completes. The code has not been executed on the user's Toshiba Windows device.

## Next local command
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r 09-PRODUCTS/Pharma-Stock-Intelligence/requirements.txt
py -m unittest discover -s 09-PRODUCTS/Pharma-Stock-Intelligence/tests -v
streamlit run 09-PRODUCTS/Pharma-Stock-Intelligence/app.py
```

## Safety
All included stock records and supplier labels are synthetic. Never upload patient-identifiable or confidential pharmacy data. All stock flags are administrative review prompts, not clinical or autonomous purchasing decisions.
