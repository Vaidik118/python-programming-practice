numbers = {11, 22, 33, 44, 55}

value = int(input("Enter the number to remove: "))

if value in numbers:
    numbers.remove(value)
    print(f"{value} removed successfully.")
else:
    print(f"{value} does not exist in the set.")

print("Updated set:", numbers)