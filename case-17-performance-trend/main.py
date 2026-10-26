# Case Study 17: Student Performance Trend Analysis
subjects = ["Python", "Mathematics", "English"]
previous = []
current = []

for subject in subjects:
    previous.append(float(input(f"Previous exam mark in {subject}: ")))
for subject in subjects:
    current.append(float(input(f"Current exam mark in {subject}: ")))

print("\nPerformance trend")
for i in range(len(subjects)):
    change = current[i] - previous[i]
    if change > 0:
        status = "Improved"
    elif change < 0:
        status = "Declined"
    else:
        status = "No change"
    print(f"{subjects[i]}: {status} ({change:+.1f})")

weak = []
for i in range(len(subjects)):
    if current[i] < 40:
        weak.append(subjects[i])
print("Subjects needing attention:", weak if weak else "None")