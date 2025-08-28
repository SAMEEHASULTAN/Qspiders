#26-08-2025
#CONDITIONAL STATEMEMENTS
#1.program to square a num only if it is even
n=int(input("Enter a number:"))
if(n%2==0):
        print(n*n)

#2.wheter a charctelis a vowel or not
n=input("enter a character:")
if n in "aeiouAEIOU":
    print("character is vowel")
else:
    print("not a vowel")

#3.Ascii value of a character only if it is uppercase
n=input("Enter a character")
if n.isupper():
    print(ord(n))

#4.the cube of a number only if it is divisible by 9 or 6
n=int(input("Enter a number"))
if n%9==0 or n%6==0:
    print(n*n*n)

#5.whether a data is mutable
n=input("Enter a data")
na=input("enter another data:")
if id(n)!=id(na):
      print("data is immutable")
else:
      print("Immutable")



#6.whether given character is digit or not
n=input("Enter a character:")
if n.isdigit():
    print("its a digit.")
else:
    print("not a digit.")

#7.wheter a given character is special or not
n=input("enter a character:")
if n.isalnum() :
    print(" not special character or scpace")
else:
    print("a special character")

#8.given strig is palindrome
n=input("enter a string:")
if n[::-1]==n:
    print("palindrome")
else:
    print("not a palindrome")

#9.whether char is uppercase,lowercase,digit,or special char
n=input("Enter a character:")
if n.isupper():
    print("charcter is in upperrcase")
elif n.islower():
    print("character is in lowercase")
elif n.isdigit():
    print("character is a number")
else:
    print("special character")

#10.check if integer is single digits or double digit or 3 digits
n=int(input("enter a number:"))
if n>-9 and n<9:
    print("Its a single digit")
elif n>-99 and n<99:
    print("Its a single digit ")
elif n>-999 and n<999:
    print("Its a triple digit")



#11.wap to check relation between two integer
n=int(input("enter a number:"))
na=int(input("enter a number:"))
if n>na:
      print(n,' greater than ',na)
elif na>n:
    print(na,' greater than ',n)
else:
      print(n,' equals to ',na)  


#12.TO LOGIN INTO THE INSTAGRAM WITH VAID USERNAME AND PASSWORD(enter word nly if the username is valid)
username=input("Enter your instagram username:")
if (len(username)>3 and len(username)<30 )and (username.isalpha() or username.isdigit() or username.isalnum())or(username in ['_','.']):
        password=input("enter a valid password:")
        if (len(password)>6) and (password.isalnum() or password.isdigit()) or (password in ['@','#' , '$', '%', '&']):
            print("YOUR INSTAGRAM VALID USERNAME AND PASSWORD IS:")
            print("USERNAME:",username)
            print("PASSWORD:",password) 
        else:
            print("try again with a valid password")
else:
      print("You entered a invalid username")


# 13.Program to print the middle value of a list only if it is string

my_list=input("Enter a list of values seperted by space: ").split()
n=len(my_list)
middle_index=n//2 
middle_value=my_list[middle_index]
if isinstance(middle_value,str):#isinstance() is a built-in function used to check if an object is of a specified type (class)
    print("Middle value is a string:",middle_value)
else:
    print("Middle value is not a string")


#14.to print the reversed sting ony if it is starting with vowel,ending with consonant and having middle value
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
if len(s) % 2 == 1:  # must have a middle character
    if s[0] in vowels and s[-1].isalpha() and s[-1] not in vowels:
        print("Reversed string:", s[::-1])
    else:
        print("String does not meet the conditions.")
else:
    print("String must have a middle character (odd length).")

