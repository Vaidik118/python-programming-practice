# 08_json_file.py

import json

# Student information
student = {
    "name": "Vaidik",
    "age": 21,
    "city": "Ahmedabad",
    "skills": ["Python", "Django", "Machine Learning"]
}

# Write Python data into a JSON file
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully!")