# 06_with_open_context_manager.py

# Open the file and read its contents
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

# The file has automatically closed here
print(content)