# 04_book_class.py

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price: ₹", self.price)
        print()


book1 = Book(1, "Python Basics", "Amit", 350)
book2 = Book(2, "Machine Learning", "Rahul", 500)

book1.display_details()
book2.display_details()