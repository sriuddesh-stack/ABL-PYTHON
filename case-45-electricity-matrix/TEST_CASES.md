# Test Cases — Case Study 45: Weekly Electricity Consumption Matrix

Enter 7 non-negative daily values for each appliance in order: Fan, Light, Computer. Values are example units.

| Test | Input pattern | Expected result |
|---|---|---|
| 1 — Zero usage | Enter 0 for all 21 values | Every appliance weekly total and every daily total is 0.0 units |
| 2 — Constant usage | Fan: seven 1s; Light: seven 2s; Computer: seven 3s | Weekly totals: Fan 7.0, Light 14.0, Computer 21.0; each daily total 6.0 units |
| 3 — Different daily values | Fan: 1,2,3,4,5,6,7; Light and Computer: all 0 | Fan weekly total 28.0; daily totals follow 1 through 7 |
| 4 — Invalid negative usage | Enter -1 for any day | Usage cannot be negative; program stops |

Run: `python main.py`.
