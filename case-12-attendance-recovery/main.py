# Case Study 12: Attendance Recovery Computation
attended = int(input("Classes attended so far: "))
conducted = int(input("Classes conducted so far: "))
threshold = float(input("Required attendance percentage: "))

if conducted < 0 or attended < 0 or attended > conducted or threshold < 0 or threshold > 100:
    print("Invalid input.")
elif conducted == 0:
    print("No classes have been conducted yet.")
else:
    percentage = attended / conducted * 100
    print(f"Current attendance: {percentage:.2f}%")
    if percentage >= threshold:
        print("You already meet the requirement.")
    else:
        extra = 0
        while (attended + extra) / (conducted + extra) * 100 < threshold:
            extra += 1
        print("Minimum consecutive classes to attend:", extra)