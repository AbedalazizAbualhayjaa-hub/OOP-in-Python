# Task 11 - Alternative Constructors

from datetime import date


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)

    @classmethod
    def today(cls):
        current = date.today()
        return cls(current.year, current.month, current.day)

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Deliverable

date1 = Date.from_string("2026-08-03")
print("From string:", date1)

today = Date.today()
print("Today:", today)

print("2024 is leap year:", Date.is_leap_year(2024))
print("2026 is leap year:", Date.is_leap_year(2026))
