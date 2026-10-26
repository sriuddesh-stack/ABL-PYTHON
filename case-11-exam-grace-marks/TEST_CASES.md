# Test Cases — Case Study 11: Examination Result and Grace-Mark Validation

Grace policy: pass mark = 35; at most 5 total grace marks may be used.

| Test | Python | Mathematics | English | Expected result |
|---|---:|---:|---:|---|
| 1 — All pass | 70 | 80 | 90 | PASS; grace marks used = 0 |
| 2 — One mark short | 34 | 60 | 55 | Final marks [35, 60, 55]; PASS; grace = 1 |
| 3 — Grace budget exceeded | 32 | 33 | 70 | Only 3 marks can be applied to the first eligible subject; remaining subject stays below 35; FAIL; grace = 3 |
| 4 — Invalid high mark | 70 | 101 | 80 | Invalid mark message; program stops |
| 5 — Invalid low mark | -1 | 70 | 80 | Invalid mark message; program stops |

Run: `python main.py`. Enter one mark at each prompt in Python, Mathematics, English order.
