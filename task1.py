# Task 1 - Your First Class

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        return f"{self.title} by {self.author}, {self.pages} pages"


# Create two books and print their summaries

book1 = Book("1984", "George Orwell", 328)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)

print(book1.summary())
print(book2.summary())
