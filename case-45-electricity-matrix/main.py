# Case Study 45: Weekly Electricity Consumption Matrix
appliances = ["Fan", "Light", "Computer"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
usage = []

for appliance in appliances:
    row = []
    print(f"Enter units used by {appliance} for each day")
    for day in days:
        units = float(input(f"  {day}: "))
        if units < 0:
            print("Usage cannot be negative.")
            raise SystemExit
        row.append(units)
    usage.append(row)

print("\nWeekly total by appliance")
for i in range(len(appliances)):
    print(appliances[i], ":", round(sum(usage[i]), 2), "units")

print("\nDaily total")
for j in range(len(days)):
    total = 0
    for i in range(len(appliances)):
        total += usage[i][j]
    print(days[j], ":", round(total, 2), "units")