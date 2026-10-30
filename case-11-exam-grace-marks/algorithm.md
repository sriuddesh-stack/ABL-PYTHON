# Algorithm — Examination Result and Grace-Mark Validation

1. Start the program.
2. Define the subjects, pass mark (35), maximum mark (100), and total grace-mark limit (5).
3. Read the marks for each subject.
4. Validate every mark. If any mark is below 0 or above 100, display an error and stop.
5. Initialize the grace marks used to zero.
6. Examine each subject mark one by one.
7. If a mark is below 35 by 5 marks or fewer, and the remaining grace allowance is sufficient, add the required grace marks to that subject.
8. Otherwise, keep the original mark unchanged.
9. Store each subject's final mark.
10. Check whether all final marks are at least 35.
11. Display the final marks and the grace marks used.
12. Display PASS if all subjects meet the pass mark; otherwise, display FAIL.
13. Stop.

**Output:** Final subject marks, result, and total grace marks used.
