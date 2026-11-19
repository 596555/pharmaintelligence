# Advanced pharmacy inventory analytics

This extension shifts the project from simple stock totals toward pharmacy-specific decision support for **human review**.

## Methods implemented
- **Consumption-based planning:** observed issues in a configurable lookback window are converted to average daily issues.
- **Estimated days of stock:** on-hand quantity divided by average daily issues. Undefined when there are no issues.
- **Reorder point:** average daily issues × (assumed supplier lead time + safety days).
- **Safety stock:** average daily issues × assumed safety days.
- **Suggested review quantity:** target-days demand plus safety stock minus stock on hand, floored at zero.
- **ABC:** ranks products by issue quantity × listed unit cost over the selected period. ABC measures usage value, not therapeutic importance.
- **FSN:** fast/slow/non-moving classification based on days since last recorded issue. Thresholds are configurable.
- **FEFO:** sorts batches by expiry date and flags batches inside the review horizon.

## Critical assumptions
The included issue history is fictional and short. The default lead time, safety days and target days are illustrative. Real use requires verified stock balances, pack/unit normalization, actual lead times, backorders, stockout periods, seasonality, returns, transfers, minimum order quantities and local policy. A period with stockouts can understate true demand.

## Clinical and operational safeguards
- No automatic purchase orders, substitutions, dispensing or clinical recommendations.
- Expired stock is a quarantine/disposition review prompt; follow local law and SOP.
- ABC is not VEN. VEN requires a locally governed clinical criticality assessment by qualified pharmacy/clinical leadership.
- Do not pool different strengths, dosage forms, routes or pack sizes without a validated conversion.
- Human review and documented approval are mandatory.
- Do not upload patient-identifiable or confidential pharmacy data.

## Learning objectives
Explain why issue history is not necessarily demand, calculate a reorder point by hand, identify data leakage, compare ABC and VEN, interpret FSN, and defend FEFO as an operational principle.
