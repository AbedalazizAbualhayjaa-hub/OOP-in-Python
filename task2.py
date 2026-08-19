# Task 2 - Instance Counter

class Book:
    count = 0

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

        Book.count += 1

    def summary(self):
        return f"{self.title} by {self.author}, {self.pages} pages"


# Create three books and print the count

book1 = Book("1984", "George Orwell", 328)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)

print("Number of books:", Book.count)
