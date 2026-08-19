# Task 7 - Shape Renderer

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def total_area(shapes):
    return sum(shape.area() for shape in shapes)


# Deliverable: mixed list

shapes = [
    Circle(3),
    Square(4),
    Triangle(5, 2)
]

print("Total area:", total_area(shapes))


# New class that total_area() has never seen

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes.append(Rectangle(4, 5))

print("Total area after adding Rectangle:", total_area(shapes))
