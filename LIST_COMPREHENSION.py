
# site==>https://www.sanfoundry.com/tough-python-interview-questions-answers/
# 2.https://compsciedu.com/Category/Python
# # 1
# x = ['ab', 'cd']
#
# print(list(map(list, x)))
# print(len(list(map(list, x))))

# # 2
# x = [12, 34]
# print(len(list(map(int, x))))
# print(list(map(int, x)))

# integers cannot be joined

# 3
# x = [12.1, 34.0]
# print(list(map(str, x)))
# print(" ".join(list(map(str, x))))
# print(len(' '.join(list(map(str, x)))))
# 4.
# x = [[0], [1]]
# print(' '.join(list(map(str, x))))
# print(len(' '.join(list(map(str, x)))))

# 5
# x = [[0], [1]]
# print(list(map(str, x)))
# print((' '.join(list(map(str, x)))))
# x = [[0], [1]]
# print((' '.join(list(map(str, x))),))
# x = [[0], [1]]
# # Explanation: We have created a tuple with one string in it.
# print((' '.join(list(map(str, x))),1,3,3))
# # Explanation: We have created a tuple with three string in it.
# print({' '.join(list(map(str, x))),1,3,3})
# # 6
# x = [34, 56]
# print(list(map(int, x)))
# print((''.join(list(map(str, x)))),)
# 7
# x = 'abcd'
# print(list(map(list, x)))
# x = 1234
# print(list(map(list, x)))
# TypeError: 'int' object is not iterable
# x = 1234
# print(list(map(list, x)))

# palindrome
# n=str(input("enter the string"))
# n1=n[::-1]
# print(n1)
# if n==n1:
#     print("palindrome")

# Fathima's Questions


#getting input from user


# user_input = [input("enter the number") for i in range(4)]
# print(user_input)

#lamda
#addition
# f = lambda a1,a2:a1+a2
# print(f(20,20))
#
# #mul
#
# f = lambda a1:a1**2
# print(f(20))
#
# #map
# lst = [1,3,4,5,9,7,65,5,66]
# f = list(map(lambda num:num**2,lst))
# print(f)
#
# lst1 = (5,2,4,8,5,7,9,3,5,2,5,7)
# f = map(lambda num:num**3,lst1)
# print(set(f))
#mcq



# Python Multiple Choice Questions – Mapping Functions
#
# This set of Python Interview Questions & Answers focuses on “Mapping Functions”.
#
# 1. What will be the output of the following Python code?
#
# elements = [0, 1, 2]
# def incr(x):
#     return x+1
# print(list(map(incr,elements)))


# x = ['ab', 'cd']
# print(list(map(lambda x:x.upper(), x)))

x = [12, 34]


# print(len(list(map(len, x))))
# object of type 'int' has no len()
#
# a) 2
# b) 1
# c) error
# d) none of the mentioned


# # x = [12, 34]
# print(len(list(map(int, x))))

# a) 2
# b) 1
# c) error
# d) none of the mentioned


# x = [12, 34]
# print(len(''.join(list(map(str, x)))))

# a) 4
# b) 5
# c) 6
# d) error


#
# x = [[0], [1]]
# print(len(' '.join(list(map(str, x)))))


# def is_positive(num):
#     return num > 0
# numbers = [-1, 3, -5, 7, -9]
# positive_nums = list(filter(is_positive, numbers))
# print(positive_nums)

#
# def add(a, b):
#     return a + b

# numbers1 = [1, 2, 3, 4]
# numbers2 = [5, 6, 7, 8]
# sums = map(add, numbers1, numbers2)
# print(list(sums))
# numbers1 = [1, 2, 3, 4]
# numbers2 = [5, 6, 7, 8]
# sums=list(map(lambda x,y:x+y,numbers1,numbers2))
# print(sums)
# lst=[5,8,7,4]
# prime=[i for i in lst if all(i%y!=0 for y in range(2,i)) ]
# print(prime)
# vowels=['a','e','i','o','u','A','E','I','O','U']
# lst=['apple','banana','grapes','orange']
# re=["".join([i for i in j if i not in vowels])  for j in lst]
#
# print(re)
#
# def is_vowel(char):
#     vowels = 'aeiouAEIOU'
#     return char in vowels
#
# chars = ['a', 'b', 'c', 'd', 'e', 'F', 'G', 'H', 'I', 'j']
# filtered_chars = filter(is_vowel, chars)
# print(list(filtered_chars))
#
#
# result = (lambda x: x * 2)(5)
# print(result)
# a) 5
# b) 10
# c) 25
# d) 15

# f = lambda x:x if x % 2 == 0 else None
# result = f(2)
# print(result)
# a) Returns the number if it is even, otherwise None
# b) Returns None if the number is even, otherwise the number
# c) Returns the square of the number if it is even, otherwise None
# d) Returns the number if it is odd, otherwise None

#
# names = ["Alice", "Bob", "Charlie", "David"]
# names.sort()
# print(names)
# strs = ["geeks", "code", "ide", "practice"]
# strs.sort()
# print(strs)
# lst=[(i[::-1]) for i in strs ]
# print(lst)
# print("".join(reversed("dona mary george")))
# lst=[sorted(i) for i in strs ]
# print(lst)
# lst=[sorted(i[::-1]) for i in strs ]
# print(lst)
# lst=["".join(sorted(i[::-1])) for i in strs ]
# print(lst)

# sorted_names = sorted(names, key=lambda x: x[-1])
# print(sorted_names)
# f=lambda x: x[-1]
# print(f(names))
#
# func = lambda x: x[1:]
# result = func("Python")
# print(result)
# print(result)
# a) “ython”
# b) “Python”
# c) “P”
# d) “y”




# students = ['Alice', 'Bob', 'Charlie', 'David']
# sorted_students = sorted(students, key=lambda x: len(x))
# print(sorted_students)

# l=[-2, 4]
# m=map(lambda x:x*2, l)
# print(m)
# a) [-4, 16]
# b) Address of m
# c) Error
# d)
# print(bool(0))
# # bool(0) is False and bool(1) is True
# f=lambda x:bool(x%2)
# print(f(20), f(21))

# a) False True
# b) False False
# c) True True
# d) True False


# l=[1, -2, -3, 4, 5]
# def f1(x):
#     return x<2
# m1=filter(f1, l)
# print(list(m1))
# #
# a) [1, 4, 5 ]
# b) Error
# c) [-2, -3]
# d) [1, -2, -3]
#
# l=[1, 2, 3, 4, 5]
# m=map(lambda x:2**x, l)
# print(list(m))
#
# a) [1, 4, 9, 16, 25 ]
# b) [2, 4, 8, 16, 32 ]
# c) [1, 0, 1, 0, 1]
# d) Error


#to print cube of number from 100 to 200

# lst = [i**3 for i in range(10,21)]
# print(lst)
#
# # eg number even calculate square if odd calculate cube
#
# lst = [i**2 if i%2==0 else i**3 for i in range(1,101)]
# print(lst)
# #
# lst=[(i**2,"even") if i %2==0 else (i**3,"odd") for i in range(1,11)]
# print(lst)
# lst = [(i,'even') if i%2==0 else (i,'odd') for i in range(1,101)]
# print(lst)

# lst = ['apple','banana','cherry']
# vowel = 'aeiouAEIOU'
# lst1 = [''.join([i for i in word if i not in vowel])for word in lst]
# print(lst1)
# a=[[1,2.3],[2,3,4],[4,5,1]]
# print(a[1])
# a=165
# # a='165'
# b=sum(list(map(int,str(a))))
# print(b)
# A=[[1,2,3],[4,5,6],[7,8,9]]
# lst=[A[row][1] for row in (0,1,2)]
# print(lst)
# a={}
# a[1,2,4]=8
# a[(4,2,1)]=10
# a[(1,2)]=12
# sum=0
# for k in a:
#     sum+=a[k]
# print(len(a)+sum)
# array=[2,5,3,5]
# lst=[]
# for i in array:
#     if i not in lst:
#         lst.append(i)
#     else:
#         j=i
#         break
# k=-1
# for i in lst:
#     k+=1
#     if i==j:
#         break
# print(k)

