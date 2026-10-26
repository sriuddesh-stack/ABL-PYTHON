# Case Study 13: ATM Transaction Sequence Simulation
balance = float(input("Enter opening balance: Rs. "))
if balance < 0:
    print("Opening balance cannot be negative.")
    raise SystemExit

transactions = input("Enter transactions separated by spaces (D amount or W amount), e.g. D 500 W 100: ").split()
if len(transactions) % 2 != 0:
    print("Invalid transaction sequence.")
    raise SystemExit

accepted = 0
rejected = 0
for i in range(0, len(transactions), 2):
    kind = transactions[i].upper()
    try:
        amount = float(transactions[i + 1])
    except ValueError:
        print("Invalid amount; transaction skipped.")
        rejected += 1
        continue
    if amount <= 0:
        print("Rejected: amount must be positive.")
        rejected += 1
    elif kind == "D":
        balance += amount
        accepted += 1
        print(f"Deposit accepted: Rs. {amount:.2f}")
    elif kind == "W" and amount <= balance and amount <= 10000:
        balance -= amount
        accepted += 1
        print(f"Withdrawal accepted: Rs. {amount:.2f}")
    elif kind == "W":
        print("Withdrawal rejected: insufficient balance or limit exceeded.")
        rejected += 1
    else:
        print("Unknown transaction type; use D or W.")
        rejected += 1
print(f"Final balance: Rs. {balance:.2f}")
print("Accepted:", accepted, "Rejected:", rejected)