# Q15:[Polymorphism] Create a class Animal with an abstract method
# speak(). Implement subclasses Dog and Cat that override speak() to
# output the respective animal sounds.

from abc import abstractmethod


class Animal:
    def __init__(self):
        pass

    @abstractmethod
    def speak():
        pass


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)

    def speak(self):
        print(f"Woof")


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)

    def speak(self):
        print(f"Meow")


d1 = Dog()
c1 = Cat()
d1.speak()
c1.speak()
