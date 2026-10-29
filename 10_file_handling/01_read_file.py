# 01_read_file.py

# Open the file in read mode
file = open("sample.txt", "r", encoding="utf-8")

# Read the complete file
content = file.read()

# Display the contents
print(content)

# Close the file
file.close()