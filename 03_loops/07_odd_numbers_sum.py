limit = int(input("Enter the limit: "))

odd_sum = 0

for number in range(1, limit + 1):
    if number % 2 != 0:
        print(number)
        odd_sum += number

print("Sum of odd numbers:", odd_sum)