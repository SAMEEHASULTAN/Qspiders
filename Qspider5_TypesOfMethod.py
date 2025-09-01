#TYPES OF METHODS
#object method
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



#30-08-2025
#class method
class Hospital():
    Hname="ABC"
    loc="gandhimarket"
    phno=834222344
    fees='500rs'
    def __init__(self,name,pid,problem,phno):
        self.name=name
        self.pid=pid
        self.problem=problem
        self.phno=phno
    def disp(self):
        print(self.name,self.pid,self.problem,self.phno)
    def ch_name(self,new):
        self.name=new
    #classmethod-->access
    @classmethod
    def display(cls):
        print(cls.Hname,cls.loc,cls.phno,cls.fees)
    #classmethod-->modification of loc
    @classmethod
    def ch_Hname(cls,new):
        cls.Hname=new
p1=Hospital("P1",12,"COLD",2346765555)
p1.disp()
Hospital.display()
Hospital.ch_Hname('DEF')
Hospital.display()



#static method
class College():
    cname="Panimalar Engineering College"
    loc="chennai"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print(self.name,self.roll_no)
    def ch_roll_no(self,new):
        self.roll_no=new
    @classmethod
    def disp(cls):
        print(cls.cname,cls.loc)
    @classmethod
    def ch_loc(cls,new):
        cls.loc=new
    @staticmethod
    def msg():
        print("Welcome to Panimalar Engineering College")
st1=College('Neona',58)
st2=College('Krishna',78)
print("before modification:")
College.disp()
st1.display()
print("after modification:")
College.ch_loc('Kolkatha')
st1.ch_roll_no(56)
st1.display()
College.disp()
#static method call
College.msg()
st1.msg()
