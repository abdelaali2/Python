# Q16: Create a class Calculator with a class method add that takes two
# numbers as arguments and returns their sum.


class Calculator:
    def __init__(self):
        pass

    @classmethod
    def add(self, x, y):
        return x + y

    @classmethod
    def sub(self, x, y):
        return x - y

    @classmethod
    def mul(self, x, y):
        return x * y

    @classmethod
    def div(self, x, y):
        return x / y


num1 = int(input("Enter first Number\n"))
num2 = int(input("Enter second Number\n"))

print(
    f"Sum = {Calculator.add(num1,num2)}\nSub = {Calculator.sub(num1,num2)}\nMul = {Calculator.mul(num1,num2)}\nDiv = {round(Calculator.div(num1,num2),3)}"
)
