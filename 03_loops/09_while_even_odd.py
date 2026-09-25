limit = int(input("Enter limit: "))

number = 1

while number <= limit:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

    number += 1