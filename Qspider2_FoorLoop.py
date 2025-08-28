#FOR LOOP
#21.wap to print all integers present in a list
l=[1,2,3,4]
for i in range(0,len(l)):
      print(l[i])

#22.wap to find the length of homogenous tuple without len()
t=(1,2,3,4,5,6,7)
length=0
for i in t:
      length=length+1
print("length of tuple:",length)

#23.wap to extract all the even numbers present in a list
lst = input("Enter numbers separated by space: ").split()
lst2 = []
for i in range(0, len(lst)):
    if int(lst[i]) % 2 == 0: 
        lst2.append(int(lst[i]))
print("List with even numbers:", lst2)

#24.wapto remove duplicate from list
lst=input("enter a list of values seperated by space").split()
lst1=[]
for i in range(0,len(lst)):
      if lst[i] not in lst1:
            lst1.append(lst[i])
print("List after removing duplicates:",lst1)

#25.wap to reverse a string without using slicing
s = input("Enter a string: ")
rev = ""
i = len(s)-1
while i>=0:
    rev+=s[i]
    i-=1
print("Reversed string:", rev)

#26.wap to get the following output using len function
#s='power star'
#out={'power':5,'star':4}
s=input("enter a string of values seperated by spaces:").split()
dic={}
for i in range(0,len(s)):
      dic[s[i]]=len(s[i])
print("output:",dic)

#27.wap to get the following output
#s='power star'
#out={'power':'rewop','star':'rats'}
s=input("enter a string of values seperated by spaces:").split()
dic={}
for i in range(0,len(s)):
      dic[s[i]]=(s[i][::-1])
print("output:",dic)

#28.wap to get the following output
#In='push maadi kushi padi'
#out={'push':'ph','maadi':'a','kushi':'s','padi':'pi'}
str1=input("Enter string:").split()
dist1={}
for s in str1:
      n=len(s)
      if n%2==0:
            dist1[s]=s[0]+s[-1]
      else:
            dist1[s]=s[n//2]
print(dist1)

