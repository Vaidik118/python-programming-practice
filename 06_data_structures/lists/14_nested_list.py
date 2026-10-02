inventory = [
    ["Apples", 10],
    ["Bananas", 3],
    ["Oranges", 8],
    ["Milk", 2]
]

for item in inventory:
    product = item[0]
    stock = item[1]

    if stock < 5:
        print(product, "stock low — Restock Needed")