numbers = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print("Original:", numbers)
print("Odd numbers:", odd_numbers)