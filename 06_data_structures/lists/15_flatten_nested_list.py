orders = [["Apples", "Bananas"], ["Milk", "Bread"], ["Eggs", "Butter"]]

combined_orders = []

for shop in orders:
    for item in shop:
        combined_orders.append(item)

print("Combined Orders:", combined_orders)