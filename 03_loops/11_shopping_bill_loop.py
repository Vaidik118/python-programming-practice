total = 0

while True:
    print("\n--- MENU ---")
    print("s. Sandwich - ₹200")
    print("m. Mango    - ₹300")
    print("p. Pizza    - ₹500")
    print("b. Burger   - ₹100")
    print("a. Apple    - ₹150")
    print("e. Exit")

    choice = input("Enter choice: ").lower()

    if choice == "e":
        print("Thank you!")
        break

    if choice == "s":
        price = 200
    elif choice == "m":
        price = 300
    elif choice == "p":
        price = 500
    elif choice == "b":
        price = 100
    elif choice == "a":
        price = 150
    else:
        print("Invalid choice.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        continue

    item_total = price * quantity
    total += item_total

    print("Item total:", item_total)
    print("Current total:", total)

print("Final total:", total)