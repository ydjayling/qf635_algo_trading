"""
In object-oriented programming, A class represents an entity with properties and behavior (methods).

Reference: https://realpython.com/python3-object-oriented-programming/#what-is-object-oriented-programming-in-python

"""


# Define an Account class
class Account:
    # A constructor method to initialize account with an identifier
    def __init__(self, identifier, balance=1000):
        self.identifier = identifier
        self.balance = balance

    # Provide output when account object is printed # dunder method
    def __str__(self):
        return "Account identifier={}, balance={:.2f}".format(self.identifier, self.balance)

    # To get balance of this account
    def balance(self):
        return self.balance

    # to deposit money to this account
    def deposit(self, amount):
        self.balance += amount

    # to withdraw money from this account
    def withdraw(self, amount):
        self.balance -= amount


# Define a main method
if __name__ == '__main__':
    pass
    # TODO create an account, and print the object
    account = Account('acc1', 1000)
    print("New account created with balance: ", account)

    # TODO deposit some money to this account, and print the object
    # Money before = 1000, money after = 2000
    print("Account before deposit: ", account)
    account.deposit(1000)
    print("Account after deposit: ", account)

    # TODO withdraw some money from this account, and print the object
    # Money before = 2000, money after = 500
    print("Account before withdraw: ", account)
    account.withdraw(1500)
    print("Account after withdraw: ", account)

    # TODO create another account, and print the object
    another_account = Account('acc2', 500)
    print("Another account created with balance:", another_account)
