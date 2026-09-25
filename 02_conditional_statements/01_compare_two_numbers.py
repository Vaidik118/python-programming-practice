value1 = int(input("Enter value 1: "))
value2 = int(input("Enter value 2: "))

if value1 > value2:
    print(value1, "is greater")
elif value2 > value1:
    print(value2, "is greater")
else:
    print("Both numbers are equal")