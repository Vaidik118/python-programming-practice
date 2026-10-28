# Example 1: Using any()

numbers = [2, 4, 6, 7, 8]

# Check whether at least one number is odd
result = any(number % 2 != 0 for number in numbers)

print("Is any number odd?", result)


# Example 2: Using all()

numbers = [2, 4, 6, 8, 10]

# Check whether every number is even
result = all(number % 2 == 0 for number in numbers)

print("Are all numbers even?", result)


# Example 3: Check passing marks

marks = [80, 25, 65, 30, 45]

# Check whether at least one student passed
result = any(mark >= 35 for mark in marks)

print("Did any student pass?", result)


# Example 4: Check whether everyone passed

result = all(mark >= 35 for mark in marks)

print("Did every student pass?", result)