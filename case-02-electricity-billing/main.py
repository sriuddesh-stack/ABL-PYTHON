# Case Study 2: Progressive Electricity Billing
units = float(input("Enter units consumed: "))

if units < 0:
    print("Units cannot be negative.")
else:
    remaining = units
    energy_charge = 0

    slab = min(remaining, 100)
    energy_charge += slab * 1.50
    remaining -= slab

    slab = min(remaining, 100)
    energy_charge += slab * 2.50
    remaining -= slab

    slab = min(remaining, 100)
    energy_charge += slab * 4.00
    remaining -= slab

    if remaining > 0:
        energy_charge += remaining * 6.00

    fixed_charge = 50
    print(f"Energy charge: Rs. {energy_charge:.2f}")
    print(f"Fixed charge: Rs. {fixed_charge:.2f}")
    print(f"Total bill: Rs. {energy_charge + fixed_charge:.2f}")