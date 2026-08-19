# Task 3 - Guard the Invariant

class Account:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount


# Deliverable

account = Account(100)

# Valid withdrawal
account.withdraw(40)
print("Balance after withdrawal:", account.balance)

# Invalid deposit
try:
    account.deposit(-10)
except ValueError as error:
    print("Deposit rejected:", error)

# Invalid withdrawal - overdraft
try:
    account.withdraw(100)
except ValueError as error:
    print("Withdrawal rejected:", error)
