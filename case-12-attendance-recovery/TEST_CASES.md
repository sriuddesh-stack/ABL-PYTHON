# Test Cases — Case Study 12: Attendance Recovery Computation

| Test | Attended | Conducted | Required % | Expected result |
|---|---:|---:|---:|---|
| 1 — Already meets threshold | 45 | 50 | 75 | Current attendance 90.00%; requirement already met |
| 2 — Needs recovery | 30 | 40 | 75 | Current attendance 75.00%; requirement already met |
| 3 — Calculate extra classes | 20 | 40 | 75 | Current attendance 50.00%; minimum consecutive classes = 40 |
| 4 — No classes yet | 0 | 0 | 75 | No classes have been conducted yet |
| 5 — Invalid attended count | 41 | 40 | 75 | Invalid input |
| 6 — Invalid threshold | 20 | 40 | 110 | Invalid input |

Run: `python main.py`. These are practice inputs; the threshold is supplied by the user.
