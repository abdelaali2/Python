# Q9: [Multiple inheritance] Create a class Animal with an attribute name.
# Create a class Pet with an attribute owner.

# Q10: Create a subclass Dog that inherits from both Animal and Pet and
# has an attribute breed. Implement a method in Dog that returns the
# name, owner, and breed of the dog.


class Animal:
    def __init__(self, name):
        self.name = name


class Pet:
    def __init__(self, owner):
        self.owner = owner


class Dog(Animal, Pet):
    def __init__(self, name, owner, breed):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)
        self.breed = breed

    def getInfo(self):
        return print(
            f"Dog's name:\t{self.name}\nDog's owner:\t{self.owner}\nDog's breed:\t{self.breed}"
        )


d1 = Dog("Max", "John", "Bulldog")

d1.getInfo()
