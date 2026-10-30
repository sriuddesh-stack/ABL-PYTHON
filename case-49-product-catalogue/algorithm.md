# Algorithm — Tuple-Based Product Catalogue Audit

1. Start the program.
2. Store the product records as tuples containing product ID, product name, unit price, and stock quantity.
3. Initialize the total valid inventory value to zero.
4. Select the next product tuple.
5. Unpack the tuple into product ID, name, price, and stock.
6. Check whether the price or stock quantity is negative.
7. If either value is negative, display that the product record is invalid.
8. Otherwise, calculate the product's inventory value by multiplying price by stock.
9. Add the product value to the total valid inventory value.
10. Display the product details and its inventory value.
11. If stock is below 5, display a replenishment warning.
12. Repeat steps 4–11 for every product tuple.
13. Display the total valid inventory value.
14. Stop.

**Output:** Product validation details, low-stock warnings, and total valid inventory value.
