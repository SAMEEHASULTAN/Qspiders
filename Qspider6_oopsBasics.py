#class,object,object members and cls members
class School:
    sname="eben"#
    pname="Jj"
    playground=3
    loc="kalyan"
'''s1=School()
print(dir(School))
s1.name="ashmin"
print(s1)#memory address
s1.rollno=1
s1.age=12
s1.classes=7
s2=School()
s1.name="ahaan"
s1.rollno=2
s1.age=13
s1.classes=8'''

'''s1.playground=2
print(s1.playground)
School.playground=4
print(School.playground)'''
#To get multiple user input
def const(self,name,rollno,age,classes):
    self.name=name
    self.rollno=rollno
    self.age=age
    self.classes=classes
s1=School()
const(s1,"asp",1,10,3)
print(s1.name,s1.rollno,s1.age,s1.classes)
print(School.sname)

"""if we want to pass aruments to init func directly we can pass it the time of object creation itself"""
""""""
