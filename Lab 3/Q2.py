# Q2: Create a class Circle with one attribute radius. The class should have
# a method circumference() that returns the circumference of the
# circle.

import math

print("Enter the Radius")

inputRadius = int(input())


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius


c1 = Circle(inputRadius)
print(f"Circumference = {c1.circumference()}")
