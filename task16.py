# Task 16 - Library Management System

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date, timedelta


# Abstract Base Class

class LibraryItem(ABC):
    def __init__(self, title):
        self.title = title
        self._available = True

    @property
    def available(self):
        return self._available

    def checkout(self):
        if not self._available:
            raise ValueError(f"{self.title} is already checked out")

        self._available = False

    def return_item(self):
        self._available = True

    @abstractmethod
    def loan_period(self):
        pass

    def __repr__(self):
        return f"{type(self).__name__}('{self.title}')"

    def __lt__(self, other):
        return self.title < other.title


# Item Types

class Book(LibraryItem):
    def loan_period(self):
        return 14


class Magazine(LibraryItem):
    def loan_period(self):
        return 7


class DVD(LibraryItem):
    def loan_period(self):
        return 3


# Member

class Member:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Member('{self.name}')"


# Loan Dataclass

@dataclass
class Loan:
    item: LibraryItem
    member: Member
    checkout_date: date
    due_date: date


# Library

class Library:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.loans = []

    def add_item(self, item):
        self.items.append(item)

    def show_catalog(self):
        for item in sorted(self.items):
            print(item)

    def checkout(self, item, member):
        item.checkout()

        checkout_date = date.today()

        due_date = checkout_date + timedelta(
            days=item.loan_period()
        )

        loan = Loan(
            item,
            member,
            checkout_date,
            due_date
        )

        self.loans.append(loan)

        return loan

    def return_item(self, item):
        item.return_item()


# Deliverable / Demonstration

library = Library("City Library")

book = Book("1984")
magazine = Magazine("National Geographic")
dvd = DVD("Interstellar")

library.add_item(book)
library.add_item(magazine)
library.add_item(dvd)


# Demonstrate __repr__ and __lt__
print("Catalog:")
library.show_catalog()


# Member
member = Member("Mohammad")


# Polymorphic checkout
print("\nCheckout:")

loan1 = library.checkout(book, member)
loan2 = library.checkout(magazine, member)
loan3 = library.checkout(dvd, member)

print(loan1)
print(loan2)
print(loan3)


# Availability is protected
print("\nBook available:", book.available)


# Try checking out unavailable book
try:
    library.checkout(book, member)
except ValueError as error:
    print("Checkout rejected:", error)


# Return book
library.return_item(book)

print("Book available after return:", book.available)


# Concept Mapping

# Classes & Encapsulation:
# LibraryItem protects its availability using _available
# and controlled methods.

# Abstraction:
# LibraryItem is an abstract base class.

# Inheritance:
# Book, Magazine, and DVD inherit from LibraryItem.

# Polymorphism:
# Library.checkout() works with every LibraryItem type
# and uses each item's own loan_period().

# Dunder Methods:
# __repr__ makes items printable.
# __lt__ allows catalog items to be sorted by title.

# Dataclasses:
# Loan is implemented using @dataclass.

# Composition:
# Library contains LibraryItem and Loan objects.

# Single Responsibility:
# LibraryItem, Member, and Loan each represent
# separate responsibilities.
