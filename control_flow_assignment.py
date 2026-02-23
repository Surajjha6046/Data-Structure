# Task 1: Discount Rules

try:
    order_amount = float(input("Enter order amount: "))

    # Apply discount rules
    if order_amount >= 2000:
        discount = 0.15
    elif order_amount >= 1500:
        discount = 0.10
    elif order_amount >= 1000:
        discount = 0.07
    else:
        discount = 0.0

    discount_amount = order_amount * discount
    subtotal = order_amount - discount_amount

    # Extra: tax 5%
    tax = subtotal * 0.05
    final_total = subtotal + tax

    print("Original amount:", order_amount)
    print("Discount:", discount_amount)
    print("Subtotal:", subtotal)
    print("Tax (5%):", tax)
    print("Final total:", final_total)

except ValueError:
    print("Error: Please enter a valid number.")

    # Task 2: Process Multiple Orders

    orders = [1200, 2500, 800, 1750, 3000]

    total_revenue = 0
    discount_count = 0

    print("\nOrder Summary:")
    print("Order | Discount | Final Amount")

    for order in orders:

        if order >= 2000:
            discount = order * 0.15
        elif order >= 1500:
            discount = order * 0.10
        elif order >= 1000:
            discount = order * 0.07
        else:
            discount = 0

        final_amount = order - discount
        total_revenue += final_amount

        if discount > 0:
            discount_count += 1

        print(order, "|", discount, "|", final_amount)

    print("\nTotal revenue after discount:", total_revenue)
    print("Number of orders with discount:", discount_count)

    # Task 3: User Menu

    orders = []

    while True:

        print("\nMenu")
        print("1 - Add order amount")
        print("2 - Show orders and totals")
        print("q - Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter order amount: "))
                orders.append(amount)
                print("Order added.")
            except ValueError:
                print("Invalid input. Try again.")

        elif choice == "2":
            total = 0
            print("\nOrders list:")

            for order in orders:

                if order >= 2000:
                    discount = order * 0.15
                elif order >= 1500:
                    discount = order * 0.10
                elif order >= 1000:
                    discount = order * 0.07
                else:
                    discount = 0

                final = order - discount
                total += final

                print("Order:", order, "Discount:", discount, "Final:", final)

            print("Total after discounts:", total)

        elif choice == "q":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")
            continue

            # Task 5: Loop Control with Conditions

            daily = [200, 150, 0, 400, 50, -1, 300]

            total_sales = 0

            for sale in daily:

                if sale == -1:
                    print("Corrupted data found. Stopping.")
                    break

                if sale == 0:
                    print("No sales today. Skipping.")
                    continue

                total_sales += sale
                print("Added:", sale, "Running total:", total_sales)

            print("Final total sales:", total_sales)