#01-09-2025
#basic program
#swap 2 variable without 3rd variable
'''a=int(input())
b=int(input())
print(a,b)
a,b=b,a
print(a,b)

#method 2
a=int(input())
b=int(input())
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)'''


#shaloow and deep copy
'''import copy
l=[1,2,3,[4,5]]
l2=copy.deepcopy(l)
print(l)
print(id(l))
print(l2)
print(id(l2))

l3=l
print(l3)
print(id(l3))
l[3]+=[5,6]
print("after modification:")
print("normal list:")
print(l)
print(id(l))
print("deep copy:")
print(l2)
print(id(l2))
print("shallow copy:")
print(l3)
print(id(l3))'''
'''changing the values of nested list will reflected in original list  and
 shallow copy list as both points to same variable  but deepcopy just copies the base values of original list  but 
 created in diff address hence changes in nested list wont reflect'''

#priramid of stars
'''for i in range(1,5):
    print(f"{'* '*i:^10}")
#method 2
for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end='')
    for k in range(i):
            print("* ",end="")
    print()'''


#palindrome number without string conversion
'''num=int(input())
temp=num
sum=0
digit=0
while temp!=0:
    digit=temp%10
    sum=(sum*10)+digit
    temp=temp//10
if sum==num:
    print("palindrome")
else:
    print("not palindrome")'''

#3.prime number in a range
num=int(input("Enter num:"))
for i in range(1,num+1):
  if num>1:
    for j in range(2,int(num*0.5)+1):
        if i%j==0:
            break
    else:
            print(i,"is PRIME")
#missing number in list containing num from 
def find_missing(nums):
    n = len(nums) + 1
    return n*(n+1)//2 - sum(nums)