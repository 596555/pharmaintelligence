-- Pharmacy inventory analysis patterns (SQLite compatible)
-- 1. Monthly issues by medicine
SELECT product_id, substr(issue_date,1,7) AS issue_month, SUM(quantity_issued) AS units_issued
FROM consumption GROUP BY product_id, issue_month ORDER BY product_id, issue_month;

-- 2. Current stock by product (batch-level table)
SELECT product_id, SUM(quantity) AS units_on_hand, MIN(expiry_date) AS earliest_expiry
FROM stock_batches GROUP BY product_id;

-- 3. Expiry review queue
SELECT product_id, batch_no, expiry_date, quantity
FROM stock_batches WHERE expiry_date <= date(:as_of_date, '+120 day')
ORDER BY expiry_date ASC;

-- 4. Low stock by medicine (compare against a product-level reorder point table)
SELECT s.product_id, SUM(s.quantity) AS on_hand, p.reorder_point
FROM stock_batches s JOIN product_planning p USING(product_id)
GROUP BY s.product_id, p.reorder_point
HAVING SUM(s.quantity) <= p.reorder_point;

-- 5. Duplicate medicine master keys should be investigated, not auto-merged
SELECT normalized_ingredient, strength, dosage_form, route, COUNT(*) AS records
FROM medicine_master
GROUP BY normalized_ingredient, strength, dosage_form, route
HAVING COUNT(*) > 1;
