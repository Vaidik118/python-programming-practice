numbers = [10, 20, 10, 30, 20, 10]

frequency = {}

# Count each number
for number in numbers:
    if number in frequency:
        frequency[number] = frequency[number] + 1
    else:
        frequency[number] = 1

# Print the frequency
for number in frequency:
    print(number, "appears", frequency[number], "times")