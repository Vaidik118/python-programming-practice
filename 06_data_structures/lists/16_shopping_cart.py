cart = ["Milk", "Eggs", "Butter", "Milk", "Eggs", "Jam"]

unique_cart = []

for item in cart:
    if item not in unique_cart:
        unique_cart.append(item)

print(unique_cart)