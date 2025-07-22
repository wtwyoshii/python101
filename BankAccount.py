import threading

class Account:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, balance):
        self.accounts[name] = Account(balance)

    def transfer(self, from_acc, to_acc, amount):
        first, second = sorted([from_acc, to_acc])
        acc1 = self.accounts[first]
        acc2 = self.accounts[second]
        with acc1.lock:
            with acc2.lock:
                if self.accounts[from_acc].balance >= amount:
                    self.accounts[from_acc].balance -= amount
                    self.accounts[to_acc].balance += amount
                    print(f"Transferred{amount} from {from_acc} to {to_acc}")
                else:
                    print("Not enough funds")

bank = Bank()
bank.add_account("acc1", 200)
bank.add_account("acc2", 150)

def thread1():
    bank.transfer("acc1, 200")

def thread2():
    bank.transfer("acc2", "acc1", 50)

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join
t2.join

print(f"Final balance acc1: {bank.accounts['acc1'].balance}")