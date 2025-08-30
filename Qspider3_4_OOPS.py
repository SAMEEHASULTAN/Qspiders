#28-08-2025
'''class Panimalar:
    dept="cse"
    HOD="Jabasheela"
    year=2
    course='Python'
obj1=Panimalar()
print(obj1.dept)
print(obj1.HOD)
print(obj1.year)
print(obj1.course)'''


'''class Library:
    genere="Friction"
    book_id=101
    book_name="Cindrella"
    book_price=230
    Author="xyz"
obj1=Library()
obj2=Library()
print(obj2.Author)'''


'''class comy:
    com_location="Delhi"
    com_pincode=600070
    emp_id=101
    emp_name="Sameeha"
    emp_salary=55000
    emp_role="Data analyst"    
    emp_exp=2
obj1=comy()
obj1.com_location="Banglore"
print(obj1.com_location,obj1.com_pincode,obj1.emp_id,obj1.emp_name,obj1.emp_salary,obj1.emp_role,obj1.emp_exp)
print(comy.com_location,comy.com_pincode,comy.emp_id,comy.emp_name,comy.emp_salary,comy.emp_role,comy.emp_exp)'''



#29-08-2025
#ACCESSING AND MODIFYING CLASS PROPERTIES
'''class car:
    car_model="Skoda Slavia"
    car_year=2022
    car_price=2000000
obj=car()
car.car_price=1700000
obj.car_price=1800000
print("Accessing vales of a class:\n")
print(obj.car_model,obj.car_year,obj.car_price)
print("Modifying object values:")
print(car.car_model,car.car_year,car.car_price)
print("Modifying class members:")
print(car.car_model,car.car_year,car.car_price)'''

'''class panimalar:
    dept="CSE"
    batch="2024-2028"
    subject=["java","dpca","dbms","dm"]
stud1=panimalar()
stud1.dept="cse"
stud1.batch="2024-2028"
stud1.subject="dbms"
print(panimalar.dept,panimalar.batch,panimalar.subject)
print(stud1.dept,stud1.batch,stud1.subject)'''


'''class Laptop:
    brand="hp"
    warrenty_years=2
    def __init__(self,model,color,processor,graphics_card):
        self.model=model
        self.color=color
        self.graphic_card=graphics_card
laptop1=Laptop("hp15s","silver","intel i5","iris 2GB")
laptop2=Laptop("HP pavilion","black","intel i7","nvidea Gforce")
print(laptop1.model,laptop1.color,laptop1.graphic_card)
print(laptop2.model,laptop2.color,laptop2.graphic_card)'''

'''class Bank:
    Bank_name="HDFC Bank"
    def __init__(self,acc_no,acc_holder,acc_balance):
        self.acc_no=acc_no
        self.acc_holder=acc_holder
        self.acc_balance=acc_balance
cust1=Bank(123,"rahul",200000)
cust2=Bank(345,"sana",300000)
print(Bank.Bank_name,cust1.acc_no,cust1.acc_holder,cust1.acc_balance)
print(Bank.Bank_name,cust2.acc_no,cust2.acc_holder,cust2.acc_balance)
'''

class bankk:
    bname='sbi'
    loc='chennai'
    def __init__(self,name,pno,ifsc):
        self.name=name
        self.pno=pno
        self.ifsc=ifsc
    def display(self):
        print(self.name,self.pno,self.ifsc)
    def ch_name(self,new):
        self.name=new
c1=bankk('a',123456788996,1234567899751234)
bankk.display(c1)
bankk.ch_name(c1,'B')
bankk.display(c1)