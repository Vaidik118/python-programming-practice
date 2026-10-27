numbers = [0, 1, 0, 3, 12]

result = []
zero_count = 0

# Step 1: Collect non-zero numbers
for number in numbers:
    if number == 0:
        zero_count = zero_count + 1
    else:
        result.append(number)

# Step 2: Add zeros at the end
for i in range(zero_count):
    result.append(0)

# Step 3: Print the result
print("Original list:", numbers)
print("After moving zeros:", result)