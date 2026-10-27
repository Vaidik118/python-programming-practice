numbers = [1, 2, 4, 5]

n = len(numbers) + 1

for number in range(1, n + 1):

    if number not in numbers:
        print("Missing number:", number)
        break