# Task 12 - Refactor to a Dataclass

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int

    def summary(self):
        return f"{self.title} by {self.author}, {self.pages} pages"


# Deliverable

book1 = Book("1984", "George Orwell", 328)
book2 = Book("1984", "George Orwell", 328)

# Generated __repr__
print("Book:", book1)

# Generated __eq__
print("Books are equal:", book1 == book2)

# Original behavior still works
print("Summary:", book1.summary())
