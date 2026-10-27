from functools import reduce


# Example 1: Find the sum of numbers

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print("Sum:", total)


# Example 2: Find the product of numbers

product = reduce(lambda a, b: a * b, numbers)

print("Product:", product)


# Example 3: Find the largest number

largest = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print("Largest number:", largest)


# Example 4: Sum numbers with an initial value

total_with_initial = reduce(
    lambda a, b: a + b,
    numbers,
    10
)

print("Sum with initial value:", total_with_initial)