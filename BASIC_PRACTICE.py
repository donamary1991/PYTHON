# 1. Write a Python program to find the second largest number in a list.
# lst=[9,5,8,7,9,6]
# lst=list(set(lst))
# print(lst)
# lst.sort(reverse=True)
# print(lst)
# print(lst[1])
# # 2. Write a program to remove duplicates from a list.
# lst=[9,5,8,7,9,6]
# lst=list(set(lst))
# 3. Write a Python program to find the GCD of two numbers.

# def fact(num):
#     factors=[]
#     for j in range(1,num):
#         if num % j==0:
#             factors.append(j)
#     return factors
# fact1=fact(15)
#
# fact2=fact(20)
# print(fact1)
# print(fact2)
# GCD=list(set(fact1) & set(fact2))
# print(max(GCD))

# 4. Write a Python program to check if two strings are anagrams.
# str1='form'
# str2='from'
# lst1=set(sorted(str1.lower()))
# print(lst1)
# lst2=set(sorted(str2.lower()))
# print(lst2)
# if lst1==lst2:
#     print("anagram")
# else:
#     print("not anagram")
# 5. Write a program to generate Fibonacci numbers up to n.
# a=0
# b=1
# num1=int(input("enter the number"))
# print(a)
# print(b)
#
# for i in range(num1):
#     c=a+b
#     print(c)
#     a,b=b,c


# 6. Write a Python program to sort a list of dictionaries by a key.
# lst=[{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}]
# new_list = sorted(lst, key=lambda d: d['age'])
# print(new_list)

# 7. Write a Python program to find all prime numbers within a range.
# num=int(input("enter the number"))
# for i in range(2,num+1):
#     count=0
#     for j in range(1,i):
#         if i%j==0:
#             count+=1
#
#     if count==1:
#         print(i)

# 8. Write a program to flatten a nested list.
#    Example:
#    Input: [[1, 2, [3]], [4, 5]]
#    Output: [1, 2, 3, 4, 5]
lst=[[1, 2, [3]], [4, 5]]
flatten=[]
for i in lst:
    if type(i) is list:
        for j in  i:
            if type(j) is list:
                for k in j:
                    flatten.append(k)
            else:
                flatten.append(j)
    else:
        flatten.append(i)
print(flatten)

# 9. Write a program to find the sum of digits of a number.
num=int(input("enter the number"))
sum1=0
while num>0:
    sum1=sum1+num%10

    num=num//10
print(sum1)
# 1. Write a Python program to print your name and age.
# print(f'My Name is {str(input("enter the name"))} and age is {int(input("enter the age"))}')
# 2. Write a Python program to find the type of a variable.
num=10
print(f'type is {type(num)}')

# # 3. Write a program to demonstrate the use of logical operators (and, or, not).
# a=True
# b=False
# print(a and b)
# print(a or b)
# print(not a)
# 4. Write a Python program to calculate the square root of a number.
# num=input("enter the number")
# square_root=pow(4,0.5)
# print(square_root)
# # 5. Write a program to print the sum of two user-provided numbers.
# a=int(input("enter num1"))
# b=int(input("enter num2"))
# summ=a+b
# print(summ)
# 6. Write a Python program to swap the values of two variables using a temporary variable.
# a=5
# b=4
# a,b=b,a
# print(a,b)
# 7. Write a program to calculate the cube of a number.
# num=int(input("enter the num"))
# cube=pow(num,3)
# print(cube)
# 8. Write a Python program to check if a number is divisible by 5.
# num=int(input("enter the num"))
# if num%5==0:
#     print("divisible by 5")
# 9. Write a program to demonstrate the use of the is and in operators.
a=5
b=5
lst=[5,6,8]
if a is b:
    print("same to same")
if a in lst:
    print("included")
# 10. Write a Python program to print "Python is Fun!" five times using a loop.
for i in range(5):
    print("Python is Fun!")


