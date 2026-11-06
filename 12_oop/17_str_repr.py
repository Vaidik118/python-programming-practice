# 17_str_repr.py

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.name} is {self.age} years old and studies {self.course}."

    def __repr__(self):
        return (
            f"Student(name={self.name!r}, "
            f"age={self.age}, course={self.course!r})"
        )


student1 = Student("Vaidik", 21, "Computer Engineering")

print(student1)
print(str(student1))
print(repr(student1))