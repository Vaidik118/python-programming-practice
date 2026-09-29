limit = int(input("Enter the limit: "))

for number in range(1, limit + 1):
    cube = number ** 3
    print(number, "->", cube)