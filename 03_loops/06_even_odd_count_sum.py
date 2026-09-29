limit = int(input("Enter limit: "))

even_count = 0
odd_count = 0

even_sum = 0
odd_sum = 0

for number in range(1, limit + 1):
    if number % 2 == 0:
        even_count += 1
        even_sum += number
    else:
        odd_count += 1
        odd_sum += number

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)