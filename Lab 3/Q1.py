# Q1: Create a class Rectangle with two attributes width and height. The
# class should have a method area() that returns the area of the
# rectangle.

print("Enter the Width")

inputWidth = int(input())

print("Enter the Height")

inputHeight = int(input())


class Square:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


sq1 = Square(inputWidth, inputHeight)
print(f"Square Area = {sq1.area()}")
