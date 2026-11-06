# 16_magic_methods.py

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        return self.title == other.title and self.author == other.author


book1 = Book("Python Basics", "Amit", 150)
book2 = Book("Python Basics", "Amit", 150)
book3 = Book("Machine Learning", "Rahul", 200)

print(book1)
print("Pages:", len(book1))
print("Book 1 equals Book 2:", book1 == book2)
print("Book 1 equals Book 3:", book1 == book3)