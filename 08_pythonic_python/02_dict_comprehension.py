# Example 1: Create a dictionary of squares

squares = {number: number * number for number in range(1, 6)}

print("Squares:", squares)


# Example 2: Create a dictionary of cubes

cubes = {number: number ** 3 for number in range(1, 6)}

print("Cubes:", cubes)


# Example 3: Convert a list into a dictionary

names = ["Amit", "Rahul", "Vaidik"]

name_lengths = {name: len(name) for name in names}

print("Name lengths:", name_lengths)


# Example 4: Store numbers and their doubled values

numbers = [2, 4, 6, 8]

doubled = {number: number * 2 for number in numbers}

print("Doubled values:", doubled)