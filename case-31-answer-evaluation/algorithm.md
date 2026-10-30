# Algorithm — String-Based Examination Answer Evaluation

1. Start the program.
2. Read the answer key and the student's answers.
3. Remove spaces from both strings and convert them to uppercase.
4. Check whether both strings have the same non-zero length. If not, display an error and stop.
5. Initialize correct, incorrect, and unanswered counts to zero and score to zero.
6. Compare the student's answer with the key at each position.
7. If the student's answer is `-`, increase the unanswered count and do not change the score.
8. If the answer matches the key, increase the correct count and add 1 to the score.
9. Otherwise, increase the incorrect count and subtract 0.25 from the score.
10. Repeat steps 6–9 until every position has been checked.
11. Display the correct, incorrect, and unanswered counts.
12. Display the final score.
13. Stop.

**Output:** Answer counts and final score after negative marking.
