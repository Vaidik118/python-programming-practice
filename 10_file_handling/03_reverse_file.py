# 03_reverse_file.py

# Open the file
file = open("sample.txt", "r", encoding="utf-8")

# Read the entire file
content = file.read()

# Close the file
file.close()

# Reverse the content
reversed_content = content[::-1]

# Display the reversed content
print("Original content:", content)
print("Reversed content:", reversed_content)