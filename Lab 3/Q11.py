# Q11: [Multilevel inheritance] Create a class Person with an attribute
# name. Create a subclass Employee that inherits from Person and has
# an attribute salary. Create a subclass Manager that inherits from
# Employee and has an attribute department. Implement a method in
# Manager that returns the name, salary, and department of the
# manager.


class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

    def getInfo(self):
        return print(
            f"Name:\t\t{self.name}\nSalary:\t\t{self.salary}\nDepartment:\t{self.department}"
        )


m1 = Manager("Ibrahim", 250_000, "CyberSecurity")
m1.getInfo()
