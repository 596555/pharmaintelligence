# Case study — Pharma Stock Intelligence

## Summary
A local dashboard prototype summarizes fictional batch inventory and flags records for human review.

## Data
Ten synthetic batch rows created for this repository. No real pharmacy, supplier or patient data is included.

## Method
Python validation and KPI calculations, pandas for tabular analysis, Streamlit for the local interface. The analysis date is selectable and expiry review uses a 90-day window.

## Quality checks
Unit tests cover loading, total units, expiry flags and rejection of negative quantities. Validation errors stop the dashboard rather than silently accepting invalid data.

## Limitations
Costs are fictional. No demand history means days-of-cover is unavailable. A low-stock flag is not a purchase order. No clinical decision is supported.

## Reproduction
Follow the product README in `09-PRODUCTS/Pharma-Stock-Intelligence/`.
