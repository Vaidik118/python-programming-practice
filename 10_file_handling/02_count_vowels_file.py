# 02_count_vowels_file.py

# Open the file
file = open("sample.txt", "r", encoding="utf-8")

# Read the complete file and convert text to lowercase
content = file.read().lower()

# Define vowels
vowels = "aeiou"

# Initialize the counter
count = 0

# Check every character
for ch in content:
    if ch in vowels:
        print(ch, end=" ")
        count += 1

# Display total vowels
print("\nTotal vowels:", count)

# Close the file
file.close()