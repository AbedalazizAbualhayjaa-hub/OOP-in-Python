# Task 15 - Spot the SRP Violation


# BEFORE: Bad design

class BadUser:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def validate_email(self):
        return "@" in self.email

    def save_to_file(self):
        with open("users.txt", "a") as file:
            file.write(f"{self.name}, {self.email}\n")


bad_user = BadUser("Mohammad", "mohammad@example.com")

print("Before refactoring:")
print("Email valid:", bad_user.validate_email())


# AFTER: Refactored design

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class EmailValidator:
    @staticmethod
    def validate(email):
        return "@" in email


class UserFileRepository:
    @staticmethod
    def save(user):
        with open("users.txt", "a") as file:
            file.write(f"{user.name}, {user.email}\n")


# Deliverable

user = User("Mohammad", "mohammad@example.com")

print("\nAfter refactoring:")
print("Email valid:", EmailValidator.validate(user.email))

UserFileRepository.save(user)

print("User saved successfully.")


# Explanation:
# User is responsible only for storing user data.
# EmailValidator is responsible only for email validation.
# UserFileRepository is responsible only for file storage.
#
# This refactoring follows:
# S - Single Responsibility Principle
# Each class now has only one reason to change.
