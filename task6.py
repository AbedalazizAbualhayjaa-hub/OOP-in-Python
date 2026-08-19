# Task 6 - Inspect the MRO

class A:
    def show(self):
        print("A")
        super().__init__()


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()


# Deliverable

d = D()

print("Method execution order:")
d.show()

print("\nMRO:")
print(D.__mro__)

# Explanation:
# The methods run in the order D -> B -> C -> A.
# This happens because super() follows Python's Method Resolution Order (MRO).
