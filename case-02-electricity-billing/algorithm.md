# Algorithm — Progressive Electricity Billing

1. Start the program.
2. Read the electricity units consumed.
3. If the units are negative, display an error message and stop.
4. Initialize `remaining` with the entered units and `energy_charge` with zero.
5. Calculate the charge for up to the first 100 units at Rs. 1.50 per unit.
6. Subtract the charged units from `remaining`.
7. Calculate the charge for up to the next 100 units at Rs. 2.50 per unit and update `remaining`.
8. Calculate the charge for up to the next 100 units at Rs. 4.00 per unit and update `remaining`.
9. If any units remain, charge them at Rs. 6.00 per unit.
10. Set the fixed charge to Rs. 50.
11. Add the fixed charge to the energy charge to calculate the total bill.
12. Display the energy charge, fixed charge, and total bill.
13. Stop.

**Output:** An itemized electricity bill, or an error message for negative input.
