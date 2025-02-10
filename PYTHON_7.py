age=int(input("enter the age\n"))
gender=str(input("enter gender m/f\n"))
wage=0
No_of_days=int(input("enter the number of days"))
if((age>=18)&(age<30))& (gender=='F'):
   wage=750*No_of_days
elif((age>=18)&(age<30))& (gender=='M'):
 wage=700*No_of_days
elif((age>=30)&(age<=40))& (gender=='F'):
    wage=850*No_of_days
elif ((age >= 30) & (age <= 40))& (gender=='M'):
 wage=800*No_of_days
else:
    print("condition not satisfied")
print(wage)
#************************************************************
# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.
print("Each unit will cost rs100 and discount of 10% if the cost of purchased quantity is more than 1000")
quantity=int(input("enter the quantity"))
total_cost=quantity*100
if (total_cost>1000):
    discounted_price=total_cost-(total_cost*.10)
    print("TOTAL COST IS",discounted_price)
else:
    print("discount is not applicable")
    print(total_cost)
#*****************************************************************
# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
def grade(n):
    if n<25:
        grade='F'
    elif 25<=n<=45:
        grade='E'
    elif 45<=n<50:
        grade='D'
    elif 50 <= n <60:
        grade = 'C'
    elif 60<=n<80:
        grade='B'
    elif n>=80:
        grade='A'
    else:
        print("invalid entry")
    return grade
print("enter marks and print the corresponding grade.\n")
n=int(input("enter the mark"))
Grade=grade(n)
print(Grade)


#************************************************************
# Write a program to find greatest number among three numbers
lst=[]
for i in range(3):
    n=int(input("enter the number"))
    lst.append(n)

max1=0
# for i in lst:
#     if i>max1:
#         max1=i
#     else:
#         continue
# print(max1)
print(max(lst))
****************************************************************
year=int(input("enter the year"))

if(year%4==0):

    if((year % 100 != 0)|(year % 400 == 0)):

        print(year,"is a leap year")
    else:
        print(year, "is not a leap year")
else:
    print(year,"is not a leap year")
#****************************************************************
n1=int(input("enter the number"))
n2=int(input("enter the number2"))
operator=input("enter the operator")
def operations(n1,n2,operator):
    if operator=="+":
        result=n1+n2
    elif operator=='-':
        result=n1-n2
    elif operator=="*":
        result=n1*n2
    elif operator=="/":
        result=n1//n2
    return result
res=operations(n1,n2,operator)
print(n1,operator,n2,"=",res)
#*****************************************************************
def mon(place):
    if place == '1':
        monument="RedFort"
    elif place == '2':
        monument="Taj Mahal"
    elif place == '3':
        monument=  "Jal Mahal"
    return monument
place=input("enter the number corresponding to place to find the monument corresponding to it\n 1.Delhi 2.Agra 3.Jaipur\nenter the number")
monument=mon(place)
print(monument)
#**********************************************************************
# Take values of length and breadth of a rectangle from user and check if it is square or not.
length=int(input("enter the length"))
breadth=int(input("enter the breadth"))
if(length==breadth):
    print("it's a square")
else:
    print("invalid")
#**************************************************************
print("this program is to find whether sides of triange belongs to an equilateral or isosceles or scalene")
side1=int(input("enter side1"))
side2=int(input("enter side"))
side3=int(input("enter side3"))
if (side1==side2==side3):
    print("sides belongs to an equilateral triangle")
elif((side1==side2)|(side2==side3)|(side1==side3)):
    print("sides belongs to an isosceles triangle")
elif((side1 != side2) & (side2 != side3) & (side1 != side3)):
    print("sides belongs to a scalene triangle")






