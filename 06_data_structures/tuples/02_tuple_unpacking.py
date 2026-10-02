# Basic tuple unpacking

student = ("Vaidik", 23, 85)

name, age, marks = student

print("Name:", name)
print("Age:", age)
print("Marks:", marks)


# Extended unpacking

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# Swapping values

x = 100
y = 200

x, y = y, x

print("x:", x)
print("y:", y)