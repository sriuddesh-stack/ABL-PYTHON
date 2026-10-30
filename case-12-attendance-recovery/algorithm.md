# Algorithm — Attendance Recovery Computation

1. Start the program.
2. Read the number of classes attended, classes conducted, and required attendance percentage.
3. Validate the inputs: attended classes cannot be negative or exceed conducted classes, and the target must be between 0 and 100.
4. If the input is invalid, display an error and stop.
5. If no classes have been conducted, display a suitable message and stop.
6. Calculate current attendance percentage using `attended / conducted × 100`.
7. If the current percentage is already at or above the target, display that the requirement is met.
8. Otherwise, initialize the number of additional classes to zero.
9. Calculate the projected attendance percentage assuming every additional class is attended.
10. While the projected percentage is below the target, increase the additional-class count by one.
11. Display the current attendance percentage and the minimum additional consecutive classes required.
12. Stop.

**Output:** Current attendance percentage and, when needed, the minimum number of future classes to attend.
