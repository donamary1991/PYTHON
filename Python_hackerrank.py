# 1. Write a Python program to print "Hello, World!".
# print("Hello, World!")
# 2. Write a program to
# take input from the user and print it.
# string=input("Enter your name?")
# print(string)
#
# 3. Write a Python program to check if a number is even or odd.
# name=int(input("Enter the number"))
# if name%2==0:
#     print("Even")
# else:
#     print("Odd")

# 4. Write a program to find the largest of three numbers.
# a=input("Enter the number1")
# b=input("Enter the number2")
# c=input("Enter the number3")
# if a>b and a>c:
#         print("a is greater")
# elif b>a and b>c:
#     print("b is greater")
# else:
#     print("c is greater")

# maximum=max([input("enter the number") for i in range(3) ])
# print("maximum is ",maximum)

# 5. Write a Python program to calculate the sum of all numbers in a list.
lst=[1,2,3,4,5]
print(sum(lst))

# 6. Write a program to reverse a string.
# string="Leverage the power of Artificial Intelligence"
# rev_str=''
# for i in string:
#     rev_str=i+rev_str
# print(rev_str)

# 7. Write a program to check if a string is a palindrome.
# string=str(input("Enter the string:"))
# pal_check=string[-1::-1]
# if string==pal_check:
#     print("palindrome")
# else :
#     print("not a palindrome")

# 8. Write a Python program to count the number of vowels in a string.
# string="seek ad hide"
# vowels="aeiou"
# count=0
# for i in string:
#     if i in vowels:
#         count+=1
# print("Number of vowels is",count)

# 9. Write a Python program to print the multiplication table of a given number.
# num=int(input("enter the number"))
# for i in range(11):
#      print(f'{i} * 10 = {i*10}')
# 10. Write a program to find the factorial of a number using a loop
# num=int(input("enter the number"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)



str="anoa"
str1=""
for i in str:
 str1=i+str1
if str1==str:
    print("palindrome")

a=0
print(a)
b=1
print(b)
for i in range(10):
 c=a+b
 print(c,end=' ')
 a,b=b,c

