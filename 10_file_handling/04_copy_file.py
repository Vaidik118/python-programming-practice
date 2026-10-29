
source = open("sample.txt", "r", encoding="utf-8")

content = source.read()

source.close()

destination = open("destination.txt", "w", encoding="utf-8")

destination.write(content)

destination.close()

print("File copied successfully!")