# Task 5 - Vehicle Hierarchy

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"{self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def describe(self):
        return f"{super().describe()}, Doors: {self.num_doors}"


class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar

    def describe(self):
        return f"{super().describe()}, Sidecar: {self.has_sidecar}"


# Deliverable

car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Honda", "CBR500R", False)

print("Car:", car.describe())
print("Motorcycle:", motorcycle.describe())
