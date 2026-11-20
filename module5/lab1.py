class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.balance)


# Main Program
initial = float(input("Enter initial balance: "))
acc = BankAccount(initial)

dep = float(input("Enter amount to deposit: "))
acc.deposit(dep)

wit = float(input("Enter amount to withdraw: "))
acc.withdraw(wit)

acc.check_balance()