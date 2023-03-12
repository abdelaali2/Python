# Q7: Create a class BankAccount with two attributes account_number
# and balance. The class should have a constructor that initializes the
# account_number and balance attributes. Also, implement a
# destructor for the class that prints a message when the object is
# destroyed.


class BankAccount:
    def __init__(self, accountNo, balance):
        self.accountNo = accountNo
        self.balance = balance

    def __del__(self):
        print(
            f"Terminating account No. {self.accountNo}.\nYour last balance = {self.balance}"
        )


myBA = BankAccount("a24a-01988a4ca23d", 250_000)
