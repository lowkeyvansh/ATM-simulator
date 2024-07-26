class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Balance: {self.balance}")

atm = ATM(1000)
while True:
    action = input("Choose action (deposit, withdraw, check, exit): ").lower()
    if action == 'deposit':
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif action == 'withdraw':
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif action == 'check':
        atm.check_balance()
    elif action == 'exit':
        break
    else:
        print("Invalid action")
