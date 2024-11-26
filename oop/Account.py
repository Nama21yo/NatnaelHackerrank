class MinimumBalanceError(Exception):
    pass
class Account:
    accountNumber = 1000
    def __init__(self,name, balance):
        if balance < 1000:
            raise MinimumBalanceError("Account can't be Created")
        self.name = name
        Account.accountNumber += 1
        self.account_number = Account.accountNumber
        self.balance = balance
    
    def deposit(self,amount): 
        self.balance += amount
    def withdraw(self,amount):
        if self.balance - amount > 1000:
            self.balance -= amount
        else:
            raise MinimumBalanceError("Account can't be Created")
    def show_details(self):
        print("Account Number", self.account_number)
        print("Name ", self.name)
        print("Balance ", self.balance)