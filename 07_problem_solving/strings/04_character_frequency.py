text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

print("Character frequencies:")

for char in frequency:
    if char == " ":
        print("Space:", frequency[char])
    else:
        print(char, ":", frequency[char])