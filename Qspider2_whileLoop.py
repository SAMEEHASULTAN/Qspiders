#26-08-2025
#WHILE LOOP
#15.wap to print python 5 times
n=5
while(n>0):
    print("python")
    n=n-1

#16.wap to print n natural numbers
nu=input("Enter a number:")
n=int(nu)
i=1
while(i<=n):
    print(i)
    i=i+1

#17.wap to print  multiplication of n
n=int(input("Enter a number:"))
i=1
while(i<=10):
         print(i,'X',n,'=',i*n)
         i=i+1

#18.wap to togglr a string
s=input("Enter a string: ")
result=""
i=0
while i<len(s):
    if s[i].isupper():
        result+=s[i].lower()
    elif s[i].islower():
        result+=s[i].upper()
    else:
        result+=s[i]
    i += 1
print("Toggled string:", result)





#19.wap to reverse the given number
n = int(input("Enter a number: "))
num = n
rev = 0
while num > 0:
    digit=num%10      
    rev=rev*10+digit  
    num=num//10        
print("Reversed number:", rev)



#20.wap to find the sum of individual digits of a number
n=int(input("Enter a number:"))
num=n
rev=0
while(num>0):
       digit=num%10
       rev=rev+digit
       num=num//10
print("sum of digits:",rev)