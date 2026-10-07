students = [
    ("Amit", "Python"),
    ("Rahul", "Django"),
    ("Disha", "Python"),
    ("Karan", "Django"),
    ("Meena", "Data Science")
]

groups = {}

for name, course in students:
    groups.setdefault(course, []).append(name)

print("Grouped students:")

for course, names in groups.items():
    print(f"{course}: {names}")