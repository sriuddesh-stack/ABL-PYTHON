# Case Study 49: Tuple-Based Product Catalogue Audit
products = [
    ("P101", "Notebook", 45.0, 20),
    ("P102", "Pen", 10.0, 100),
    ("P103", "Folder", 30.0, 0),
    ("P104", "Marker", -5.0, 12),
]

print("Product catalogue audit")
total_inventory_value = 0
for product in products:
    product_id, name, price, stock = product  # tuple unpacking
    if price < 0 or stock < 0:
        print(product_id, name, "INVALID RECORD")
    else:
        value = price * stock
        total_inventory_value += value
        print(f"{product_id} | {name} | Rs. {price:.2f} | Stock: {stock} | Value: Rs. {value:.2f}")
        if stock < 5:
            print("  Replenishment required")
print(f"Total valid inventory value: Rs. {total_inventory_value:.2f}")