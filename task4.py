# Task 4 - Temperature with Validation

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32


# Deliverable

temp = Temperature(25)

# Get Celsius
print("Celsius:", temp.celsius)

# Set Celsius
temp.celsius = 30
print("New Celsius:", temp.celsius)

# Read Fahrenheit
print("Fahrenheit:", temp.fahrenheit)

# Invalid temperature
try:
    temp.celsius = -300
except ValueError as error:
    print("Rejected:", error)
