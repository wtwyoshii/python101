class Account:
    def __init__(self, inital_balance):
        self.balance = inital_balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient funds")

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, initial_balance, interest_rate =0.05):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate

class CheckingAccount(Account):
    def __init__(self, initial_balance, transaction_limit=10):
        super().__init__(initial_balance)
        self.transaction_limit = transaction_limit
        self.transaction_count = 0 
    
    def withdraw(self, amount):
        if self.transaction_count < self.transaction_limit:
            if amount <= self.balance:
                super().withdraw(amount)
                self.transaction_count +=1
                print(f"Transaction count: {self.transaction_count}/{self.transaction_limit}")
            else:
                print("Insufficient funds")
        else:
            print("Transaction limit reached")

    def calculate_interest(self):
        print("Checking accounts do not earn interest")

savings = SavingsAccount(1000)
savings.deposit(500)
savings.calculate_interest()
print(f"Savings blance: ${savings.balance:.2f}")

checking = CheckingAccount(500)
checking.withdraw(100)
checking.calculate_interest()
print(f"Checking balance: ${checking.balance:.2f}")
       

