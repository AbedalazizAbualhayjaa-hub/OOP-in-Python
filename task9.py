# Task 9 - A Vector Class

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


# Deliverable: demonstrate every operator

v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = Vector(3, 4)

# __repr__
print("v1:", v1)

# __eq__
print("v1 == v3:", v1 == v3)

# __add__
print("v1 + v2:", v1 + v2)

# __sub__
print("v1 - v2:", v1 - v2)

# __mul__
print("v1 * 2:", v1 * 2)

# __abs__
print("Length of v1:", abs(v1))
