# Write a Python program that takes two numbers as input
# from the user and performs arithmetic operations
# (addition, subtraction, multiplication, division, and modulus) on them.
# Display the results of each operation.


a=int(input("enter the number1"))
b= int(input("enter the number2"))
print("sum is",a+b)
print("difference is ",a-b)
print("quotient is ",a/b)
print("product is",a*b)
print("modulus is",a%b)
****************************************************************************************
# Write a function to calculate the factorial of a number recursively
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
print(factorial(int(input("enter the number"))))
********************************************************************************************
mother_string=str(input("enter the string from where valid strings can be generated\n"))
l=int(input("enter the length of the required string to be generated\n"))


def generate_string(s,l):
  if(l==0):
    flag=0
    if(((s[0]>='a') & (s[0]<='z'))|((s[0]>='A') & (s[0]<='Z'))|(s[0]=='_')&(s[0]!=' ')):
      strng=s
      for c in s:
          if (((c >= 'a') & (c <= 'z')) | ((c >= 'A') & (c <= 'Z')) | (c == '_') | (
                  (c >= '0') & (c <= '9'))) & ((c != " ")):
              flag = 1
          if (strng == 'False' or strng == 'None' or strng == 'True' or strng == 'and' or strng == 'as' or strng ==
                'assert' or strng == 'async' or strng == 'await'):
              flag = 0
              break
          if (strng == 'break' or strng == 'class' or strng == 'continue' or strng == 'def' or strng == 'del' or strng ==
                  'elif' or strng == 'else' or strng == 'except'):
              flag = 0
              break
          if (strng == 'finally' or strng == 'for' or strng == 'from' or strng == 'global' or strng == 'if' or strng ==
              'import' or strng == 'in' or strng == 'is'):
              flag = 0
              break
          if (strng == 'lambda' or strng == 'nonlocal' or strng == 'not' or strng == 'or' or strng == 'pass' or strng ==
              'raise' or strng == 'return' or strng == 'try'):
              flag = 0
              break
          if (strng == 'while' or strng == 'with' or strng == 'yield' ):
              flag = 0
              break



    if(flag==1):
      print(s,end=',')


  else:
   for i in mother_string:
     generate_string(s+i,l-1)
generate_string('',l)
********************************************************************************************************************************************
# Write a Python program to check if a given string is a valid identifier or not.
# An identifier is valid if it starts with a letter (a-z, A-Z) or an underscore (_) followed by zero or more letters, underscores,
# or digits (0-9).
s=str(input("enter the string"))
flag=0
if(((s[0]>='a') & (s[0]<='z'))|((s[0]>='A') & (s[0]<='Z'))|(s[0]=='_')&(s[0]!=' ')):


    for c in s:
        if (((c >= 'a') & (c<= 'z')) | ((c>= 'A') & (c  <= 'Z')) | (c  == '_') | (
                (c  >= '0') & (c  <= '9')))&((c  !=" ")):
            flag=1

        else:
            print(s, "is not  an identifier")
            flag=0
            break


else:
    print(s,"is an invalid identifier")
if(flag==1):
    print(s, "is  an identifier")
***************************************************************************************************************************************************
# Create a Python program that prompts the user to enter their age
# and checks if they are eligible to vote. Use logical operators
# to check if the age is greater than or equal to 18 and less than or equal to 120.
# Print a message indicating whether the person can vote or not.
age=int(input("enter your age"))
if((age>=18) & (age<=120)):
    print("person can vote")
else:
    print("person cannot vote")
***********************************************************************************************************************************************
# Write a Python program that takes three numbers as input from the user
# and prints out the maximum and minimum numbers in the list.
a=int(input("enter the number1"))
b= int(input("enter the number2"))
c = int(input("enter the number3"))

if a>b and a>c:
    print(a,"is GREATER")
elif b>a and b>c:
    print(b,"is GREATER")
else:
    print(c, "is GREATER")

if a<b and a<c:
    print(a,"is the minimum")
elif b<a and b<c:
    print(b,"is the minimum")
else:
    print(c, "is the mminimum")


******************************************************************************************************************************************
# Write a program that takes inputs  from user and
# prints the multiplication table of that number
num=int(input("enter the number"))
for i in range(1,10):
    print(num,"*",i,"=",num*i)
*******************************************************************************************************************************************
# Create a Python program that prompts the user to enter two numbers.
# Compare the numbers using comparison operators (>, <, ==, !=, >=, <=)
# and print out the result of each comparison.


a=int(input("enter the number1"))
b= int(input("enter the number2"))
if(a>b):
    print(a,"is greater than ",b)
elif(a<b):
    print(a, "is less than ",b)
elif(a==b):
    print(a,"is equal to ",b)
if(a!=b):
    print(a, "is not equal to ",b)
if(a>=b):
    print(a, "is greater than or equal to ", b)
elif(a<=b):
    print(a, "is less than or equal to ", b)

*****************************************************************************************************************************************
# Write a Python program that takes three numbers as input from the user
# and prints out the sum of those numbers.
a=int(input("enter the number1"))
b= int(input("enter the number2"))
c= int(input("enter the number3"))
sum=a+b+c
print(sum)
**********************************************************************************************************************************
# Write a Python program to check if a given string is a valid identifier or not.
# An identifier is valid
# if it starts with a letter (a-z, A-Z) or an underscore (_) followed by zero or more letters,
# underscores, or digits (0-9)
s=str(input("enter the string"))
flag=0
if(((s[0]>='a') & (s[0]<='z'))|((s[0]>='A') & (s[0]<='Z'))|(s[0]=='_')&(s[0]!=' ')):
    strng=s
    for c in s:
        if (((c >= 'a') & (c <= 'z')) | ((c >= 'A') & (c <= 'Z')) | (c == '_') | (
                (c >= '0') & (c <= '9'))) & ((c != " ")):
            flag = 1
        if (strng == 'False' or strng == 'None' or strng == 'True' or strng == 'and' or strng == 'as' or strng ==
              'assert' or strng == 'async' or strng == 'await'):
            flag = 0
            break
        if (strng == 'break' or strng == 'class' or strng == 'continue' or strng == 'def' or strng == 'del' or strng ==
                'elif' or strng == 'else' or strng == 'except'):
            flag = 0
            break
        if (strng == 'finally' or strng == 'for' or strng == 'from' or strng == 'global' or strng == 'if' or strng ==
            'import' or strng == 'in' or strng == 'is'):
            flag = 0
            break
        if (strng == 'lambda' or strng == 'nonlocal' or strng == 'not' or strng == 'or' or strng == 'pass' or strng ==
            'raise' or strng == 'return' or strng == 'try'):
            flag = 0
            break
        if (strng == 'while' or strng == 'with' or strng == 'yield' ):
            flag = 0
            break
        else:
            if(flag==0):
             print(s, "is not  an identifier")
             break


else:
    print(s,"is an invalid identifier")
if(flag==1):
    print(s, "is  an identifier")
else:
    print(s, "is an invalid identifier")

***********************************************************************************************************************************************
