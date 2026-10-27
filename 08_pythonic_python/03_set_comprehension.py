# Example 1: Create a set of squares

squares = {number * number for number in range(1, 6)}

print("Squares:", squares)


# Example 2: Create a set of even numbers

even_numbers = {
    number
    for number in range(1, 11)
    if number % 2 == 0
}

print("Even numbers:", even_numbers)


# Example 3: Remove duplicates from a list

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = {number for number in numbers}

print("Unique numbers:", unique_numbers)


# Example 4: Convert words to uppercase

words = ["python", "java", "django"]

uppercase_words = {word.upper() for word in words}

print("Uppercase words:", uppercase_words)