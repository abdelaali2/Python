# Q6: Create a class Person with two attributes name and age. The class
# should have a constructor that initializes the name and age
# attributes. Also, implement a destructor for the class that prints a
# message when the object is destroyed.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"My name was {self.name}\nMy age was {self.age}")


p1 = Person("Lionel", 35)
