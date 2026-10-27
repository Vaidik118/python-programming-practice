# Example 1: Create a list of squares

squares = [number * number for number in range(1, 6)]

print("Squares:", squares)


# Example 2: Create a list of even numbers

even_numbers = [
    number
    for number in range(1, 11)
    if number % 2 == 0
]

print("Even numbers:", even_numbers)


# Example 3: Convert words to uppercase

words = ["python", "java", "django"]

uppercase_words = [word.upper() for word in words]

print("Uppercase words:", uppercase_words)


# Example 4: Double every number

numbers = [2, 4, 6, 8]

doubled_numbers = [number * 2 for number in numbers]

print("Doubled numbers:", doubled_numbers)