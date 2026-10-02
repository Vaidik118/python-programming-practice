print("Enter s for square:")
print("Enter c for cube:")

press = input("press key: ").lower()

if press == "s":
    number = int(input("Enter a number: "))
    print(number * number)

elif press == "c":
    number = int(input("Enter a number: "))
    print(number * number * number)

else:
    print("press valid key")