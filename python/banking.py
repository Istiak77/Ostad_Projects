class BankAccount:
    def __init__(self, user_name, initial_balance=0):
        self.user_name = user_name
        self.balance = max(0, initial_balance)

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount. Please enter a positive value."
        self.balance += amount
        return f"Successfully deposited {amount}. New balance is {self.balance}."

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive value."
        if amount > self.balance:
            return "Insufficient balance. Transaction failed."
        self.balance -= amount
        return f"Successfully withdrew {amount}. New balance is {self.balance}."

    def get_balance(self):
        return f"Current balance: {self.balance}"

    def __str__(self):
        return f"Bank Account of {self.user_name} | Balance: {self.balance}"


account = BankAccount("Ostad", 10000)
print(account)
print(account.deposit(1000))
print(account.get_balance())
print(account.withdraw(2000))
print(account.get_balance())
print(account.deposit(-500))
print(account.withdraw(15000))
