from collections import Counter

numbers = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

frequency = Counter(numbers)

unique_elements = [
    number for number in numbers
    if frequency[number] == 1
]

print("Unique elements:", unique_elements)