#A normal nested loop:
pairs = []

for x in [1, 2]:
    for y in [10, 20]:
        pairs.append((x, y))

print(pairs)

#Using nested comprehension:
pairs = [
    (x, y)
    for x in [1, 2]
    for y in [10, 20]
]

print(pairs)