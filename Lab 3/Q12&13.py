# Q12: [Hierarchical Inheritance] Create a class Shape with an attribute
# color. Create a subclass Rectangle that inherits from Shape and has
# attributes width and height.
#
# Q13: Create a subclass Circle that inherits from Shape and has an attribute
# radius. Implement a method in each subclass that returns the area
# of the shape.

from abc import abstractmethod
import math


class Shape:
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def getArea():
        pass


class Rectangle(Shape):
    def __init__(self, color, width, height):
        Shape.__init__(self, color)
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, color, radius):
        Shape.__init__(self, color)
        self.radius = radius

    def getArea(self):
        return self.radius * pow(math.pi, 2)


r1 = Rectangle("Red", 5, 6)
c1 = Circle("White", 4)

print(f"Rectangle area:\t{r1.getArea()}\nCircle area:\t{round(c1.getArea(),3)}")
