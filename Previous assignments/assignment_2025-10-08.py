class BankAccount:
    bank_name = "Thomas Bank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} just deposited {amount}.")
        else:
            print("ERROR : Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"ERROR : {self.owner} has insufficient funds for withdrawal.")
        elif amount <= 0:
            print("ERROR : Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}.")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

# exmample
account1 = BankAccount("Thomas", 100)
account2 = BankAccount("Florian", 50)

account1.deposit(50)
account1.withdraw(30)
account1.show_balance()

account2.deposit(100)
account2.withdraw(200)  # test error
account2.show_balance()