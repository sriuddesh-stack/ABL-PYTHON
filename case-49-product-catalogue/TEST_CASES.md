# Test Cases — Case Study 49: Tuple-Based Product Catalogue Audit

The program contains four fixed sample product tuples; no input is required.

| Test | Catalogue record | Expected result |
|---|---|---|
| 1 — Valid stocked product | P101, Notebook, Rs. 45.00, stock 20 | Value Rs. 900.00 |
| 2 — Valid product | P102, Pen, Rs. 10.00, stock 100 | Value Rs. 1000.00 |
| 3 — Low stock | P103, Folder, Rs. 30.00, stock 0 | Value Rs. 0.00 and “Replenishment required” |
| 4 — Invalid price | P104, Marker, price -5.00, stock 12 | INVALID RECORD; excluded from total |
| 5 — Overall total | Valid records only | Total valid inventory value: Rs. 1900.00 |

Run: `python main.py`.
