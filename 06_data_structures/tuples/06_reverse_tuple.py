tupleD = (11, -22, 33, -44, 55)

new_tuple = ()

for x in reversed(tupleD):
    new_tuple += (x,)

print(new_tuple)

#2
numbers = (11, -22, 33, -44, 55)

reversed_numbers = numbers[::-1]

print("Original:", numbers)
print("Reversed:", reversed_numbers)