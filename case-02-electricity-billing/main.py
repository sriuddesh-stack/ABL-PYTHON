# Case Study 2: Progressive Electricity Billing
# Sample slab rates for educational use.

units = float(input("Enter units consumed: "))

if units < 0:
    print("Units cannot be negative.")
else:
    remaining = units
    energy_charge = 0

    # First 100 units at Rs. 1.50 per unit
    slab = min(remaining, 100)
    energy_charge = energy_charge + slab * 1.50
    remaining = remaining - slab

    # Next 100 units at Rs. 2.50 per unit
    slab = min(remaining, 100)
    energy_charge = energy_charge + slab * 2.50
    remaining = remaining - slab

    # Next 100 units at Rs. 4.00 per unit
    slab = min(remaining, 100)
    energy_charge = energy_charge + slab * 4.00
    remaining = remaining - slab

    # Any units above 300 at Rs. 6.00 per unit
    if remaining > 0:
        energy_charge = energy_charge + remaining * 6.00

    fixed_charge = 50
    total_bill = energy_charge + fixed_charge

    print(f"Energy charge: Rs. {energy_charge:.2f}")
    print(f"Fixed charge: Rs. {fixed_charge:.2f}")
    print(f"Total bill: Rs. {total_bill:.2f}")
