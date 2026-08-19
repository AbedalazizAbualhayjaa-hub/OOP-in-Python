# Task 8 - Payment Interface

from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    def receipt(self, amount):
        result = self.pay(amount)
        return f"Receipt: {result}"


class CreditCard(PaymentMethod):

    def pay(self, amount):
        return f"${amount:.2f} paid using Credit Card"


class PayPal(PaymentMethod):

    def pay(self, amount):
        return f"${amount:.2f} paid using PayPal"


# Deliverable: show that the abstract class cannot be instantiated

try:
    payment = PaymentMethod()
except TypeError as error:
    print("Cannot create PaymentMethod:", error)


# Demonstrate both implementations

credit_card = CreditCard()
paypal = PayPal()

print(credit_card.receipt(100))
print(paypal.receipt(75))
