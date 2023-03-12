# Q7: [Single Inheritance] Create a class Vehicle with an attribute speed.
# Create a subclass Car that inherits from Vehicle and has an attribute
# brand. Implement a method in Car that returns the brand and speed
# of the car.


class Vehicle:
    def __init__(self, speed):
        self.speed = speed


class Car(Vehicle):
    def __init__(self, speed, brand):
        Vehicle.__init__(self, speed)
        self.brand = brand

    def getInfo(self):
        return print(f"Brand:\t{self.brand}\nSpeed:\t{self.speed}")


c1 = Car(300, "Ford Mustang")

c1.getInfo()
