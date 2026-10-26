# Test Cases — Case Study 42: Student Marks Matrix Analysis

Enter marks row by row: Student 1, Student 2, Student 3; each row is Python, Maths, English.

| Test | Marks by student | Expected result |
|---|---|---|
| 1 — Standard matrix | S1: 80,70,90; S2: 60,75,65; S3: 90,85,95 | Totals 240, 200, 270; averages 80.0, 66.67, 90.0; subject averages Python 76.67, Maths 76.67, English 83.33; top performer Student 3 |
| 2 — Tie | S1: 50,50,50; S2: 50,50,50; S3: 40,40,40 | Student 1 is reported as top performer because it is the first maximum |
| 3 — Invalid mark | Any row contains 101 or a negative mark | Invalid mark message; program stops |

Run: `python main.py`.
