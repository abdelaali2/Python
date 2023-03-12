# Q3: Create a class Employee with three attributes name, age, and salary.
# The class should have a method raise_salary() that increases the
# employee's salary by a given percentage.


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def raiseSalary(self, ratio):
        self.salary *= 1 + ratio
        return self.salary


ibrahim = Employee("Ibrahim", 25, 20_000)

print(f"My New Salary = {ibrahim.raiseSalary(0.5)}")
