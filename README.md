It demonstrates the use of:

Conditional statements (if, elif, else)

Exception handling (try, except)

Loops (for, while)

Lists

User input handling

Basic business logic (discount, tax, revenue calculation)

📌 Features
Task 1: Discount Rules with Tax Calculation

The program:

Takes order amount as input from user

Applies discount based on rules:

Order Amount	Discount
₹2000 or more	15%
₹1500 – ₹1999	10%
₹1000 – ₹1499	7%
Less than ₹1000	No discount

Calculates:

Discount amount

Subtotal after discount

Tax (5%)

Final total amount

Handles invalid input using exception handling

Task 2: Process Multiple Orders

The program processes a predefined list of orders:

orders = [1200, 2500, 800, 1750, 3000]

It calculates:

Discount for each order

Final amount after discount

Total revenue after discount

Number of orders that received a discount

Output example:

Order | Discount | Final Amount
1200 | 84 | 1116
2500 | 375 | 2125
...
Task 3: Interactive User Menu

Provides a menu-driven system where user can:

1 - Add order amount
2 - Show orders and totals
q - Quit

Features:

Add multiple orders dynamically

View all orders

View discount applied to each order

View final total after discount

Task 4: Loop Control with Conditions

Processes daily sales data:

daily = [200, 150, 0, 400, 50, -1, 300]

Logic:

Stops program if corrupted data (-1) is found

Skips days with zero sales

Adds valid sales to total

Output example:

Added: 200 Running total: 200
No sales today. Skipping.
Corrupted data found. Stopping.
Final total sales: 800
