# Algorithm — ATM Transaction Sequence Simulation

1. Start the program.
2. Read the opening account balance.
3. If the opening balance is negative, display an error and stop.
4. Read the transaction sequence as pairs of transaction type and amount.
5. Check that the sequence contains a complete pair for every transaction. If not, display an error and stop.
6. Initialize accepted and rejected transaction counters to zero.
7. Process each transaction pair in order.
8. Convert the transaction amount to a number. If conversion fails or the amount is not positive, reject the transaction and update the rejected counter.
9. If the transaction type is D, add the amount to the balance and update the accepted counter.
10. If the transaction type is W, check that the amount does not exceed the balance or Rs. 10,000.
11. If the withdrawal is allowed, subtract the amount from the balance and update the accepted counter; otherwise, reject it and update the rejected counter.
12. If the transaction type is neither D nor W, reject the transaction.
13. After all transactions are processed, display the final balance and accepted/rejected counts.
14. Stop.

**Output:** Updated account balance and transaction summary.
