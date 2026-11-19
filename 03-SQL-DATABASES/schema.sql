-- Synthetic training schema only; no patient information.
CREATE TABLE medicines(product_id TEXT PRIMARY KEY, medicine_name TEXT NOT NULL, category TEXT NOT NULL);
CREATE TABLE stock_batches(batch_no TEXT PRIMARY KEY, product_id TEXT NOT NULL REFERENCES medicines(product_id), expiry_date TEXT NOT NULL, quantity INTEGER NOT NULL CHECK(quantity>=0), reorder_level INTEGER NOT NULL CHECK(reorder_level>=0), unit_cost REAL NOT NULL CHECK(unit_cost>=0), supplier TEXT NOT NULL);
-- Stock by medicine
SELECT m.medicine_name,SUM(b.quantity) AS units_on_hand FROM medicines m JOIN stock_batches b USING(product_id) GROUP BY m.product_id,m.medicine_name ORDER BY units_on_hand DESC;
-- Expiry within 90 days; bind :as_of_date
SELECT batch_no,medicine_name,expiry_date,quantity FROM stock_batches JOIN medicines USING(product_id) WHERE expiry_date BETWEEN :as_of_date AND date(:as_of_date,'+90 day') ORDER BY expiry_date;
-- Below reorder threshold
SELECT medicine_name,batch_no,quantity,reorder_level FROM stock_batches JOIN medicines USING(product_id) WHERE quantity<reorder_level;
