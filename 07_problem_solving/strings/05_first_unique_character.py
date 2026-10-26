text = input("Enter a string: ")

frequency = {}

# Step 1: Count each character
for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

# Step 2: Find the first character appearing once
found = False

for char in text:
    if frequency[char] == 1:
        print("First unique character:", char)
        found = True
        break

# Step 3: Handle the case where no unique character exists
if found == False:
    print("No unique character found")