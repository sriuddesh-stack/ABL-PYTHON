# Case Study 11: Examination Result and Grace-Mark Validation
subjects = ["Python", "Mathematics", "English"]
pass_mark = 35
max_mark = 100
grace_limit = 5
marks = []

for subject in subjects:
    mark = int(input(f"Enter marks for {subject} (0-100): "))
    if mark < 0 or mark > max_mark:
        print("Invalid mark. Enter a value from 0 to 100.")
        raise SystemExit
    marks.append(mark)

used_grace = 0
final_marks = []
for mark in marks:
    if mark < pass_mark and pass_mark - mark <= grace_limit and used_grace + (pass_mark - mark) <= grace_limit:
        used_grace += pass_mark - mark
        final_marks.append(pass_mark)
    else:
        final_marks.append(mark)

print("Final marks:", final_marks)
if all(mark >= pass_mark for mark in final_marks):
    print("Result: PASS")
else:
    print("Result: FAIL")
print("Grace marks used:", used_grace)