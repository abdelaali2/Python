# Q14: [Encapsulation] Create a class BankAccount with a private attribute
# balance. Implement methods deposit and withdraw to modify the
# balance, and a method get_balance to retrieve the balance.


class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def getBalance(self):
        return self._balance


myBA = BankAccount(250_000)
myBA.deposit(50_000)
myBA.withdraw(100_000)

# print(f"Current Balance: {myBA._balance()}") // Throws error as the balance attribute is private
print(f"Current Balance: {myBA.getBalance()}")
