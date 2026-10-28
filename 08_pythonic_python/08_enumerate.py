# Example 1: Print list elements with their indexes

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# Example 2: Start indexing from 1

print("\nFruit list:")

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# Example 3: Display student marks

students = ["Amit", "Rahul", "Vaidik"]
marks = [75, 80, 90]

print("\nStudent marks:")

for index, student in enumerate(students):
    print(student, ":", marks[index])


# Example 4: Find the index of a particular number

numbers = [10, 20, 30, 40, 50]

for index, number in enumerate(numbers):
    if number == 30:
        print("\nNumber found at index:", index)
        break