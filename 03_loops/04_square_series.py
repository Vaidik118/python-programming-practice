limit = int(input("Enter the limit: "))

for number in range(1, limit + 1):
    square = number ** 2
    print(number, "->", square)