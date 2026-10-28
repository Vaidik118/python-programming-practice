# Example 1: Combine two lists

names = ["Amit", "Rahul", "Vaidik"]
marks = [75, 80, 90]

result = list(zip(names, marks))

print("Names and marks:", result)


# Example 2: Combine names and ages

names = ["Amit", "Rahul", "Vaidik"]
ages = [21, 22, 23]

result = list(zip(names, ages))

print("Names and ages:", result)


# Example 3: Combine two lists and display each pair

fruits = ["Apple", "Banana", "Mango"]
prices = [100, 40, 80]

for fruit, price in zip(fruits, prices):
    print(fruit, "costs Rs.", price)


# Example 4: Combine three lists

names = ["Amit", "Rahul", "Vaidik"]
ages = [21, 22, 23]
cities = ["Ahmedabad", "Surat", "Vadodara"]

result = list(zip(names, ages, cities))

print("Student details:", result)