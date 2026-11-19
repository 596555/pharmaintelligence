# Machine learning for pharmacy operations

## Sequence
1. Establish a transparent baseline (moving average or last-period use).
2. Split by time, never randomize future observations into training.
3. Compare MAE and RMSE; use MAPE only when zero/near-zero demand is handled explicitly.
4. Check stockout periods because observed issues may be censored by unavailable stock.
5. Predict only an operational quantity such as next-period demand or expiry-review priority.
6. Report uncertainty and compare against the baseline.
7. Keep pharmacist/procurement approval in the loop.

## Portfolio task
Create a synthetic 12-month product-level issue history, forecast the next month using a naive and moving-average baseline, backtest across rolling cutoffs, and publish error metrics by medicine and category.

## Do not
- Predict diagnosis, treatment choice or patient response.
- Treat model output as a purchase order.
- Claim causality from correlation.
- Train/test split randomly across time series.
