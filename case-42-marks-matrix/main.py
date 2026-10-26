# Case Study 42: Student Marks Matrix Analysis
students = ["Student 1", "Student 2", "Student 3"]
subjects = ["Python", "Maths", "English"]
marks = []

for student in students:
    row = []
    print("Enter marks for", student)
    for subject in subjects:
        mark = float(input(f"  {subject}: "))
        if mark < 0 or mark > 100:
            print("Invalid mark. Use values from 0 to 100.")
            raise SystemExit
        row.append(mark)
    marks.append(row)

print("\nStudent totals and averages")
for i in range(len(students)):
    total = sum(marks[i])
    print(students[i], "total:", total, "average:", round(total / len(subjects), 2))

print("\nSubject averages")
for j in range(len(subjects)):
    column_total = 0
    for i in range(len(students)):
        column_total += marks[i][j]
    average = column_total / len(students)
    print(subjects[j], "average:", round(average, 2))

best_index = 0
for i in range(1, len(students)):
    if sum(marks[i]) > sum(marks[best_index]):
        best_index = i
print("Top performer:", students[best_index])