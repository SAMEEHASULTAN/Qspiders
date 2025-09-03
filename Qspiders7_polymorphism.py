#POLYMORPHISIM
#method overriding
'''class BankAccount:
    def intrest(self):
        return 4
class savings(BankAccount):
    type_of="saving"
s=savings()
print(s.intrest())
#the two code demonstrates the method overring by using same function with different parameters
class BankAccount:
    def intrest(self):
        return 4
class savings(BankAccount):
    type_of="saving"
    def intrest(self):
        return 7
s=savings()
print(s.intrest())'''



#method overloading
#we do not have method overloading in python,it can be implemented by default arguments
'''def add(a,c=0,d=0):
    return a+c+d
print(add(1,2,3))
print(add(1,2))
print(add(3))'''


#operator overriding
'''class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def __add__(self,other):
        return self.balance+other.balance
obj1=BankAccount(1000)
obj2=BankAccount(5000)
print(obj1+obj2)'''

#Duck typing
'''class SavingsAccount:
    def withdraw():
        return "withdraw from savings"
class CurrentAccount:
    def withdraw():
        return "withdraw from current account"
def process_withdraw(account):
    print(account.withdraw())
process_withdraw(SavingsAccount)
print()
process_withdraw(CurrentAccount)'''


#Monkey Patching
'''a=print
a("sam",123)
print(a)'''

class BankAccount:
    def __init__(self,holder,balance=0):
        self.holder=holder
        self.balance=balance
    def showBalance(self):
            return f"{self.holder} has {self.balance} balance"
def hacked_method(self):
    return "This accont is hacked"
BankAccount.show_balance=hacked_method
acc=BankAccount("sameeha",4500)
print(acc.show_balance())




