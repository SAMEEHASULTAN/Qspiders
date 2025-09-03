from abc import ABC,abstractmethod
class BankAccount(ABC):#abstarct class base
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance
    
    @abstractmethod
    def withdraw(self,amount):
        pass#forces chld class to implement this
class SavingAccount(BankAccount):
    rateofintrest=6
    def withdraw(self, amount):
obj=SavingAccount()