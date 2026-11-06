# 08_getters_setters_property.py

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")

        self._age = value

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student = Student("Vaidik", 21)

student.display()

# Update age using the setter
student.age = 22

print("Updated Age:", student.age)

# Test validation
try:
    student.age = -5
except ValueError as error:
    print("Error:", error)