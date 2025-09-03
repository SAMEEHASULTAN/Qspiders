#Program  to check if 2 to the power
def two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n // 2
    return n == 1
two(23)
def check(n):
    if n&(n-1)==0:
        print("yes")
    else:
        print("No")
#program to print 1 to 20
n=1
while(n<=20):
    print(n)
    n=n+1
#program to print 10 to 1 in while loop
n=10
while(n>=0):
    print(n)
    n=n-1
#multiplication table
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(num,"X",i,"=",num*i)
#program to print sum of numbers from 1 to 100
n=0
for i in range(1,101):
    n=n+i
print("Sum of numbers from 1 to 100:",n)
#print all odd numbers from 1 to 50
print("odd numbers between 1 to 50:")
for i in range(1,51):
    if i%2!=0:
        print(i)
#program each character in string
nu=input("enter string:")
for i in nu:
    print(i)
#foctorial of given number
n=int(input("enter a number to find factorial:"))
r=1
for i in range(1,n+1):
    r=r*i
print("Factorial of ",n,":",r)
#to print 3X3 #
for i in range(1,4):
    for j in range(1,4):
        print("#",end=" ")
    print()
#to break loop if num is divisible by a number--> 7
k=int(input("enter number:"))
for i in range(1,k+1):
    if i%8==0:
        break
    print(i)

#continue statement if even number
n=int(input("enter number:"))
for i in range(1,n+1):
    if n%2==0:
        continue
    print(i)



