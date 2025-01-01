# Write a program to accept a number and check whether its a perfect number or not.

# a perfect number is a positive integer that is equal to the sum of its positive proper divisors,
# that is, divisors excluding the number itself.
# For instance, 6 has proper divisors 1, 2 and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.

num=int(input("enter the number to check whether its a perfect number or not"))
sum=0
for j in range(1,num):
     if(num%j==0):
         sum+=j


if(num==sum):
    print(num,"is a perfect number")


-------------------------------------------------------------------------------------------------
# Python program to check if a given number is an Armstrong number
# Armstrong number is a number that is equal to the sum of cubes of its digits.
#  1^3 + 5^3 + 3^3 equals 153.
num=int(input("enter the number"))
sum=0
num1=num
# 1634
l=len(str(num1))
while(num1>0):
    p=num1%10
    sum+=p**l
    num1//=10
if(sum==num):
    print(num,"is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
---------------------------------------------------------------------------------
  #3. Count the total number of digits in a number
num=int(input("enter the number"))
count=0
while(num>0):
    num //= 10
    count+=1

print(count)
---------------------------------------------------------------------------
# Python program to display all numbers within a range except the prime numbers.
# for i in range(2,11):
#  for j in range(2,i):
#      if(i%j==0):
#          print(i)
#          break

for i in range(2,11):
    for j in range(2,i):
        if i%j==0:
            print(i)
            break

---------------------------------------------------------------------------
# Print numbers divisible by 3 or 5 from 1 to 20 using a for loop




for i in range(1,21):
    if (i%3==0)| (i%5==0):
        print(i)




------------------------------------------------------------------------
# Print numbers from 1 to 10. If a number is divisible by 4, stop the loop using a for loop and break statement:
for i in range(1,11):
    if (i%4)==0:
        break
    else:
        print(i)
-------------------------------------------------------------------------------------------------------------------------
# Write a python program to read four numbers (representing the four octets of an IP) and print the next five IP address
# Eg:
# Input:
# 192 168 255 252
# ----------Output---------
# 192 168 255 253
# 192 168 255 254
# 192 168 255 255
# 192 169 0 0
# 192 169 0 1
num1=int(input("enter the octet1"))
num2=int(input("enter the octet2"))
num3=int(input("enter the octet3"))
num4=int(input("enter the octet4"))
if((1<=num1<=255) and ( 0<=num2<=255) and (0<=num3<=255) and (0<=num4<=255)):
 for i in range(1,6):
     num4+=1
     if(num4>255):
        num4=(num4%255)-1
        num3+=1
        if (num3 > 255):
            num3 = (num3 % 255) - 1
            num2 += 1
            if (num2 > 255):
                num2 = (num2 % 255) - 1
                num1 += 1
                if (num1 > 255):
                    print("No more available IP's")
                    break
     print("IP"+str(i)+":"+" "+str(num1) + "." + str(num2) + "." + str(num3) + "." + str(num4))

else:
    print("invalid input")
---------------------------------------------------------------------------------------------------------------------------
first_octet = int(input("Enter the first octet: "))

second_octet = int(input("Enter the second octet: "))

third_octet = int(input("Enter the third octet: "))

forth_octet = int(input("Enter the forth octet: "))

octet_start = forth_octet + 1

octet_end = forth_octet + 6

if (1 <= first_octet <= 255) and (0 <= second_octet <= 255) and (0 <= third_octet <= 255) and (0 <= forth_octet <= 255):

   for ip in range(octet_start, octet_end):

       forth_octet = forth_octet + 1

       if forth_octet > 255:

           forth_octet = (forth_octet % 255) - 1

           third_octet = third_octet + 1

           if third_octet > 255:

               third_octet = (third_octet % 255) - 1

               second_octet = second_octet + 1

               if second_octet > 255:

                   second_octet = (second_octet % 255) - 1

                   first_octet = first_octet + 1

                   if first_octet > 255:

                       print("No more available IP!")

                       break

       print(str(first_octet) + "." + str(second_octet) + "." + str(third_octet) + "." + str(forth_octet))

else:

   print("Invalid input!")
-------------------------------------------------------------------------------------------
# a, b, c = 0, 0, 0 . Write a python program to print all permutations using those three variables
a, b,c = 'a', 'b', 'c'
for i in (a,b,c):
    for j in (a,b,c):
        for k in (a,b,c):
            print(str(i)+str(j)+str(k),end=',')


----------------------------------------------------------------------------------------------
# Python program that accepts a word from the user and reverses it.
word=str(input("enter the string"))
l=len(word)
str=word[::-1]
print(str)
for i in range(l,0,-1):
    print(word[i-1],end='')


--------------------------------------------------------------------------------------------------
# Python program to check the validity of password input by users.

# Primary conditions for password validation:
#
#     Minimum 8 characters.
#     The alphabet must be between [a-z]
#     At least one alphabet should be of Upper Case [A-Z]
#     At least 1 number or digit between [0-9].
#     At least 1 character from [ _ or @ or $ ].
password=str(input("enter the password"))
l=len(password)
upper_count=0
num_count=0
char_count=0
lower_count=0
for i in password:
    if ('A'<=i<='Z'):
        upper_count+=1
        # print("ok_u")
    if('0'<=i<='9'):
        num_count+=1
        # print("ok_n")
    if(i=='_')|(i=='@')|(i=='$'):
        char_count+=1
        # print("ok_char")
    if (i <= 'a' )& (i >= 'z'):
        lower_count+=1
        # print("ok_l")
if((l>=8)&(upper_count>=1)&(lower_count>=0)&(char_count>=1)&(num_count>=1)):
    print("Password is Strong")
else:
    print("Conditions are not satisfied\nPrimary conditions for password validation:\n"
          "1.Minimum 8 characters.\n"
          "2.The alphabet must be between [a-z]"
          "3.At least one alphabet should be of Upper Case [A-Z]\n"
          "4. At least 1 number or digit between [0-9].\n"
          "5.At least 1 character from [ _ or @ or $ ].")
--------------------------------------------------------------------------------------------------------
