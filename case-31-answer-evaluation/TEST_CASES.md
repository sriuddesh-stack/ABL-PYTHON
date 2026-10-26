# Test Cases — Case Study 31: String-Based Examination Answer Evaluation

Scoring: +1 for correct, -0.25 for incorrect, 0 for unanswered.

| Test | Answer key | Student answers | Expected result |
|---|---|---|---|
| 1 — All correct | `ABCD` | `ABCD` | Correct 4, incorrect 0, unanswered 0, score 4.00 / 4 |
| 2 — Mixed answers | `ABCD` | `AB-D` | Correct 3, incorrect 0, unanswered 1, score 3.00 / 4 |
| 3 — Wrong answers | `ABCD` | `DCBA` | Correct 0, incorrect 4, unanswered 0, score -1.00 / 4 |
| 4 — Mixed correct/wrong/blank | `ABCD` | `AX-$D` | Not a valid same-length example; use Test 5 instead |
| 5 — Mixed scoring | `ABCD` | `AX-D` | Correct 2, incorrect 1, unanswered 1, score 1.75 / 4 |
| 6 — Length mismatch | `ABC` | `AB` | Equal non-zero length error message |
| 7 — Spaces and lowercase | `a b c` | `A B c` | Spaces removed and letters uppercased; correct 3, score 3.00 / 3 |

Run: `python main.py`.
