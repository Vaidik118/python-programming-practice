# Dictionary Comprehension Practice

numbers = [1, 2, 3, 4, 5]

# 1. Square mapping
squares = {
    number: number ** 2
    for number in numbers
}

# 2. Even numbers only
even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

# 3. String length mapping
names = ["Ram", "Rahul", "Disha"]

name_lengths = {
    name: len(name)
    for name in names
}

print("Squares:", squares)
print("Even squares:", even_squares)
print("Name lengths:", name_lengths)