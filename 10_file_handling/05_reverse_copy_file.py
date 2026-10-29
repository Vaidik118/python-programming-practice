
with open("sample.txt", "r", encoding="utf-8") as source:
    content = source.read()

reversed_content = content[::-1]

with open("destination.txt", "w", encoding="utf-8") as destination:
    destination.write(reversed_content)

print("File reversed and copied successfully!")
