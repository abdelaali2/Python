# Q5: Create a class Car with four attributes make, model, year, and
# mileage. The class should have a method drive() that increments the
# mileage of the car by a given amount.


class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance


myCar = Car("508", "Peugeot", "2022", 0)

myCar.drive(5000)
myCar.drive(10000)

print(f"Total mileage of the car = {myCar.mileage}")
