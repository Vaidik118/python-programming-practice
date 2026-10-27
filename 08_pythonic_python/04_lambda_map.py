# Example 1: Lambda function to add two numbers

add = lambda a, b: a + b

print("Addition:", add(10, 20))


# Example 2: Square a number using lambda

square = lambda number: number * number

print("Square:", square(5))


# Example 3: Double every number using map()

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda number: number * 2, numbers))

print("Doubled numbers:", doubled)


# Example 4: Square every number using map()

squares = list(map(lambda number: number * number, numbers))

print("Squares:", squares)


# Example 5: Convert words to uppercase using map()

words = ["python", "java", "django"]

uppercase_words = list(map(lambda word: word.upper(), words))

print("Uppercase words:", uppercase_words)