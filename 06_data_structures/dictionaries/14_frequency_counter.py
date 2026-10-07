def count_frequency(items):
    frequency = {}

    for item in items:
        frequency[item] = frequency.get(item, 0) + 1

    return frequency


numbers = [10, 20, 10, 30, 20, 10, 40]

frequency = count_frequency(numbers)

print("Numbers:", numbers)
print("Frequency:", frequency)