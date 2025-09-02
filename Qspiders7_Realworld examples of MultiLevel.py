#02-09-2025
#REAL WORLD EXAMPLE OF MULTILEVEL INHERITANCE
class BankAccount:
    bname="SKSS bank"
    blocation="pallavaram"
    rateofI=7
    def __init__(self,username,accountno,balance,age):
        self.username=username
        self.accountno=accountno
        self.balance=balance
        self.age=age
    def withdraw(self,amount):
        if amount>0:
            if amount<self.balance:
                self.balance-=amount
            else:
                print("Withdrawal amount cannot be greater than the balanace")
        else:
            print("Please enter a valid amount")
    def deposit(self,newamount):
        if newamount>0:
            self.balance+=newamount
            print("your new Balance is:",self.balance)
        else:
            print("enter a valid number of deposit amount")
class SavingsAccount(BankAccount):
    rateofI=5
    def __init__(self,username,accountno,balance,age):
        if balance>999:
            super().__init__(username,accountno,balance,age)
            #above statement equals the below statement
            '''self.username=username
            self.accountno=accountno
            self.balance=balance
            self.age=age'''
        else:
            print("Enter a minimum amount of rupees 1000 or check if you are above 18 years")
class Current(BankAccount):
    rateofI=3
    def __init__(self,username,accountno,balance,age):
        if balance>4999:
              super().__init__(username,accountno,balance,age)
        else:
            print("Enter a valid amount")



class ChildSavingAccount(SavingsAccount):
    rateofI=4
    def __init__(self,username,accountno,balance,age):
        if age<18:
            super().__init__(username,accountno,balance,age)
            print("you are eligible to create a child account")


u2=SavingsAccount("SAMEEHA",798038348828,2500,18)
print("withdraw in class SavingsAccount")
u2.withdraw(1000)
print(u2.balance)
#u1=BankAccount("SAMEEHA",798038348828,2500,17)
#u1.withdraw(23)
#print(u1.balance," is the balance after withdrawal")
#u1.deposit(1000)
#print(u1.balance," is the balance after deposit")'''

u3=ChildSavingAccount("SAMEEHA",798038348828,2500,12)
print("after deposit and withdraw in childsavings account")
u3.deposit(1200)
u3.withdraw(100)
'''u4=Current("SAMEEHA",798038348828,2500,17)'''


class Loan:
    rateofI=3
    def __init__(self,pamount,years):
        self.pamount=pamount
        self.years=years
#MULTIPLE INHERITANCE
class LoanAcc(BankAccount,Loan):
    def __init__(self,username,accountno,balance,pamount,years):
        Loan.__init__(self,pamount,years)
        super().__init__(username,accountno,balance,pamount)
#l1=LoanAcc("asp",2334545,34454,355,3)
#print(l1.__dict__)
