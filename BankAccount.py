class BankAccount:

    def __init__ (self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw (self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print ("Insufficient funds, A $5 penalty has been charged to your account")
            self.balnce -= 5
        return self
    
    def display__bankaccount_info(self):
        print (f'Balance: ${self.balance}')
        return self
    
    def yield_interest(self):
        self.balance = self.int_rate * self.balance + self.balance
        return self

BankAccount1 = BankAccount (.08, 2500)
BankAccount2 = BankAccount (.03, 6000)

print(BankAccount1.balance)

BankAccount1.yield_interest()

print(BankAccount1.balance)

BankAccount1.deposit(1200).deposit(800).deposit(550).withdraw(55).yield_interest().display__bankaccount_info()

print(BankAccount1)

BankAccount2.deposit(5500).deposit(800000).withdraw(50).withdraw(10000).withdraw(90).withdraw(750).yield_interest().display__bankaccount_info()

print(BankAccount2)

