# Test Cases — Case Study 17: Student Performance Trend Analysis

Enter the three previous marks first (Python, Mathematics, English), then the three current marks in the same order.

| Test | Previous marks | Current marks | Expected result |
|---|---|---|---|
| 1 — All improve | 50, 60, 70 | 60, 65, 80 | Improvements +10.0, +5.0, +10.0; no subjects below 40 |
| 2 — Mixed trend | 70, 55, 40 | 65, 55, 45 | Python declined -5.0; Mathematics no change; English improved +5.0 |
| 3 — Weak current subject | 60, 30, 55 | 65, 35, 38 | Subjects needing attention: Mathematics, English |
| 4 — No change | 50, 50, 50 | 50, 50, 50 | All subjects show No change (+0.0) |

Run: `python main.py`.
