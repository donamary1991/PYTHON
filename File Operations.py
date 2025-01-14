# 1a) Write a Python program to perform read and write operations on a file.
# str=input("enter the string")
# f=open("write2","w")
# f.write(str)
# f.close()
# # closing the file is required
# f1=open("write2","r")
# data=f1.read()
# print(data)


# 2Write a Python program to perform read and write operations on a file.

# filename =input("Enter the file name : ")
# f1=open(filename,'w')
# f1.write('Computer science Engineering\n')
# f1.write('Elecronics and Communication Engineering\n')
# f1.write('Civil Engineering\n')
# f1.close()
# f2=open(filename,'r')
# data=f2.read()
# print(data)
# f2.close()


# data=f2.readline()
# data=f2.readlines()

# 3.Write a Python program to copy the contents of one file to another file.

# filename1 = input("Enter the file name 1: ")
# f1 = open(filename1,'w')
# f1.write('Computer science Engineering\n')
# f1.write('Elecronics and Communication Engineering\n')
# f1.write('Civil Engineering\n')
# f1.close()
# f2 = open(filename1,'r')
# data1 = f2.read()
# print(data1)
# f2.close()
# filename2 = input("Enter the file name 2: ")
# f3 = open(filename2,'w')
# f3.write(data1)
# f3.close()
# f3 = open(filename2,'r')
# data2 = f3.read()
# print(data2)
# f3.close()

# 4) Write a Python program to count frequency of characters in a given file.

#
# filename = input("Enter a file name : ")
# f1 = open(filename,'w')
# f1.write('Computer science Engineering\n')
# f1.write('Elecronics and Communication Engineering\n')
# f1.write('Civil Engineering\n')
# f1.close()
# f1 = open(filename,'r')
# data = f1.read()
# a =list(set(data))
# print(sorted(a))
# print(a)
# f1.close()
# for i in a:
#  # print("{} as occured {} times".format(i,data.count(i)))
#  print(f"{i} occured {data.count(i)} times")

# ['c', 'C', 'p', 'l', 'g', 't', 'o', 'u', 'i', 'd', 's', 'v', '\n', ' ', 'r', 'e', 'E', 'n', 'a', 'm']
# i as occured 12 times
# v as occured 1 times
# a as occured 2 times
# r as occured 5 times
# C as occured 3 times
#
#  as occured 3 times
# p as occured 1 times
# m as occured 3 times
# l as occured 2 times
# o as occured 4 times
# n as occured 14 times
#   as occured 6 times
# g as occured 6 times
# d as occured 1 times
# c as occured 5 times
# u as occured 2 times
# s as occured 2 times
# E as occured 4 times
# e as occured 10 times
# t as occured 2 times
# 5
# d="dona mary george"
# print(d[6:1:-4])
# #
# d1=list(set(d))
# for i in d1:
#   print(f"{d.count(i)} {i}")
# #
# # print(d1)
# print(sorted(d))
# # 6
#
# r = range(-25,10,1)
# print(type(r))
# print(r)
# for i in r:
#  print(i,end = ' ')
#
# #  7 generate:1 5 9 13 17
r = range(1,21,4)
for i in r:
 print(i,end = ' ')

#  8The following list describes operator precedence in Python:page No:E2 ==pg:30
# () ==> Parenthesis
# ** ==> exponential operator
# ~,- ==> Bitwise complement operator,unary minus operator
# *,/,%,// ==> multiplication,division,modulo,floor division
# +,- ==> addition,subtraction
# <<,>> ==> Left and Right Shift
# & ==> bitwise And
# ^ ==> Bitwise X-OR
# | ==> Bitwise OR
# <,<=,>,>=,==, != ==> Relational or Comparison operators
# =,+=,-=,*=... ==> Assignment operators
# is , is not ==> Identity Operators
# in , not in ==> Membership operators
# not ==> Logical not
# and ==> Logical and
# or ==> Logical or
# x=['ab','cd']
# lst=list(map(lambda x:x.upper(),x))
# print(lst)
