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



