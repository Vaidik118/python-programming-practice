items = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Basic slicing: start:stop
print(items[0:4])

# From index 2 up to the end
print(items[2:])

# From the beginning up to index 4
print(items[:4])

# Every 2nd element
print(items[::2])

# Reverse the list
print(items[::-1])

# Slice assignment
items[0:4] = ["x", "y"]

print(items)