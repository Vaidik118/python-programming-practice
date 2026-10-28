# Example 1: Sort numbers in ascending order

numbers = [40, 10, 30, 20]

print("Ascending:", sorted(numbers))


# Example 2: Sort numbers in descending order

print("Descending:", sorted(numbers, reverse=True))


# Example 3: Sort words alphabetically

words = ["banana", "apple", "mango", "cherry"]

print("Alphabetical order:", sorted(words))


# Example 4: Sort words by length

words = ["banana", "kiwi", "apple", "watermelon"]

print("Sorted by length:", sorted(words, key=len))


# Example 5: Sort words without considering uppercase/lowercase

words = ["banana", "Apple", "cherry", "Mango"]

print("Case-insensitive order:", sorted(words, key=str.lower))


# Example 6: Sort student records by marks

students = [
    {"name": "Amit", "marks": 75},
    {"name": "Rahul", "marks": 90},
    {"name": "Vaidik", "marks": 80}
]

result = sorted(students, key=lambda student: student["marks"])

print("Students sorted by marks:", result)