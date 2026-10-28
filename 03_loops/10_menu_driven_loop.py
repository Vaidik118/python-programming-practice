while True:
    print("\n--- MENU ---")
    print("1. Square")
    print("2. Cube")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            number = int(input("Enter a number: "))
            print("Square:", number ** 2)

        elif choice == 2:
            number = int(input("Enter a number: "))
            print("Cube:", number ** 3)

        elif choice == 3:
            print("Thank you!")
            break

        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid integer.")
