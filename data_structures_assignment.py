# 1. Create a list named products with at least 6 products [cite: 14]
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam", "Headset"]

# 2. Create a tuple named sample_product (name, price, category) [cite: 15]
sample_product = ("Laptop", 1200.50, "Electronics")

# 3. Print the 2nd and last product [cite: 16]
print(f"2nd Product: {products[1]}")
print(f"Last Product: {products[-1]}")

# 4. Append two new product names and print updated list [cite: 17]
products.append("USB Hub")
products.append("Desk Mat")
print(f"Updated Products: {products}")

# Extra: Modify tuple by converting to list and back [cite: 18, 19, 20]
temp_list = list(sample_product)
temp_list[1] = 1150.00
sample_product = tuple(temp_list)
print(f"Updated sample_product: {sample_product}")


# 1. Create a set of categories [cite: 22, 23]
# Using a parallel list as suggested if names don't contain categories
categories_list = ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics", "Audio", "Accessories", "Accessories"]
categories_set = set(categories_list)

# 2. Add a new category and show duplicates are ignored [cite: 24]
categories_set.add("Furniture")
categories_set.add("Electronics") # Duplicate
print(f"Categories Set: {categories_set}")

# 3. Check if a category exists [cite: 25]
print(f"Is 'Audio' in categories? {'Audio' in categories_set}")

# Extra: Total number of unique categories [cite: 26]
print(f"Total unique categories: {len(categories_set)}")

# 1. Create price_dict with at least 6 entries [cite: 28, 29]
price_dict = {
    "Laptop": 1200.00,
    "Mouse": 25.00,
    "Keyboard": 45.00,
    "Monitor": 200.00,
    "Webcam": 60.00,
    "Headset": 80.00
}

# 2. Add and Update [cite: 31, 32]
price_dict["USB Hub"] = 15.00 # Add new
price_dict["Mouse"] = 30.00   # Update existing

# 3. Remove product (handling non-existent case) [cite: 33]
product_to_remove = "Speaker"
price_dict.pop(product_to_remove, None) # Safely handles missing key

# 4. Print average price [cite: 34]
avg_price = sum(price_dict.values()) / len(price_dict)
print(f"Average Price: {avg_price:.2f}")

# Extra: Max and Min prices [cite: 35]
max_prod = max(price_dict, key=price_dict.get)
min_prod = min(price_dict, key=price_dict.get)
print(f"Max: {max_prod} (${price_dict[max_prod]}), Min: {min_prod} (${price_dict[min_prod]})")

# 1. Create catalog (list of tuples) [cite: 37]
# Using the products list and prices; assigning dummy categories for demonstration
catalog = []
for i in range(len(products)):
    name = products[i]
    price = price_dict.get(name, 0.0)
    category = categories_list[i] if i < len(categories_list) else "Other"
    catalog.append((name, price, category))

# 2. Map category to list of product names [cite: 38]
category_to_products = {}
for name, price, cat in catalog:
    if cat not in category_to_products:
        category_to_products[cat] = []
    category_to_products[cat].append(name)

# 3. Print products from the category with the most items [cite: 39, 40]
max_cat = max(category_to_products, key=lambda k: len(category_to_products[k]))
print(f"Category with most products ({max_cat}): {category_to_products[max_cat]}")