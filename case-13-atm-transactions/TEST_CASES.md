# Test Cases — Case Study 13: ATM Transaction Sequence Simulation

Transactions use pairs: `D amount` for deposit and `W amount` for withdrawal. Withdrawal limit is Rs. 10,000 per transaction.

| Test | Opening balance | Transaction input | Expected result |
|---|---:|---|---|
| 1 — Deposit and withdrawal | 1000 | `D 500 W 200` | Final balance Rs. 1300.00; accepted 2, rejected 0 |
| 2 — Insufficient balance | 100 | `W 200` | Withdrawal rejected; final balance Rs. 100.00 |
| 3 — Withdrawal limit | 15000 | `W 12000` | Withdrawal rejected because limit exceeded |
| 4 — Non-positive amount | 500 | `D 0 W -5` | Both transactions rejected |
| 5 — Unknown transaction | 500 | `X 100` | Unknown transaction type; rejected 1 |
| 6 — Odd number of tokens | 500 | `D 100 W` | Invalid transaction sequence |
| 7 — Negative opening balance | -1 | Any input | Opening balance cannot be negative; program stops |

Run: `python main.py`. Type the transaction sequence on one line, with spaces between tokens.
