# Task 14 - Refactor Inheritance to Composition


class FlyingModule:
    def move(self):
        return "Robot is flying"


class WalkingModule:
    def move(self):
        return "Robot is walking"


class SwimmingModule:
    def move(self):
        return "Robot is swimming"


class Robot:
    def __init__(self):
        self.movement_modules = []

    def add_module(self, module):
        self.movement_modules.append(module)

    def remove_module(self, module):
        if module in self.movement_modules:
            self.movement_modules.remove(module)

    def move(self):
        for module in self.movement_modules:
            print(module.move())


# Deliverable

robot = Robot()

walking = WalkingModule()
flying = FlyingModule()

robot.add_module(walking)
robot.add_module(flying)

print("Initial abilities:")
robot.move()


# Add a new ability at runtime
swimming = SwimmingModule()
robot.add_module(swimming)

print("\nAfter adding swimming:")
robot.move()


# Remove an ability at runtime
robot.remove_module(flying)

print("\nAfter removing flying:")
robot.move()


# Explanation:
# Composition is better because Robot HAS movement modules instead of being permanently tied to them through inheritance.
# Modules can be added or removed at runtime without changing Robot.
