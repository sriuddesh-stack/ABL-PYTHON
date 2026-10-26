# Case Study 2 — Test Cases

Run `python main.py` and enter each value when prompted.

| Test | Input | Expected result |
|---|---:|---|
| Zero usage | 0 | Total bill Rs. 50.00 |
| First slab boundary | 100 | Total bill Rs. 200.00 |
| Within second slab | 150 | Total bill Rs. 325.00 |
| Within third slab | 250 | Total bill Rs. 650.00 |
| Above 300 units | 350 | Total bill Rs. 1,150.00 |
| Invalid negative value | -2 | "Units cannot be negative." |

## Calculation checks
- 150 units: (100 × 1.50) + (50 × 2.50) = Rs. 275.00 energy charge; plus Rs. 50 fixed charge = Rs. 325.00.
- 250 units: (100 × 1.50) + (100 × 2.50) + (50 × 4.00) = Rs. 600.00 energy charge; plus Rs. 50 fixed charge = Rs. 650.00.
- 350 units: (100 × 1.50) + (100 × 2.50) + (100 × 4.00) + (50 × 6.00) = Rs. 1,100.00 energy charge; plus Rs. 50 fixed charge = Rs. 1,150.00.
