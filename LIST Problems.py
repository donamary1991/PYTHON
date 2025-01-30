# 1
# x=['ab','cd']
# for i in x:
#     x.append(i.upper())
# print(x)

# 2
# for i in range(10):
#     if i==5:
#         break
#     else:
#         print(i)
# else:
#     print("Here")

#
# 3.
# total=0
# for i in range(1,6):
#     if i % 2==0:
#         total+=i
# print(total)

#
# 4.
# k = [print(i) for i in 'my_string' if i not in "aeiou"]
# print(k)

# 5.
# lst=[j for i in range(2,8) for j in range(i*2, 50, i)]
# print(lst)


# 6. Write a list comprehension for producing a list of numbers between 1 and 1000 that are divisible by 3.
# a) [x in range(1, 1000) if x%3==0]
# b) [x for x in range(1000) if x%3==0]
# c) [x%3 for x in range(1, 1000)]
# d) [x%3=0 for x in range(1, 1000)]
# lst=[x for x in range(1000) if x%3==0]
# print(lst)


# 7.
# n=50
# if n>20:
#     if n>35:
#         print("ok")
#         if n>65:
#             print("good")
#         elif n>45:
#             print("average")
#         else:
#             print("no output")
# 8
# p={2,-1,5}
# for a in p.values():
#     print(a)
# # 9
# for i in range(0):
#     print(i)

# # 10
# p=5678
# for i in p:
#     print(i)
#     # p not itaerable

# 11
# places=['bangalore','mumbai','delhi']
#
# places1=places
# # Effect on Data: Any modification made to places1 will also affect places (and vice versa)
# # because both variables point to the same object in memory.
# places2=places[:]
# # Effect on Data: Modifying places2 does not affect places, and vice versa, because they are two separate objects in memory.
# places1[1]="pune"
# places2[2]="Hyderabad"
# print(places)

# 12
# d={0:'a',1:'b',2:'c'}
# for i in d:
#     print(i)

# 13
# x=int(7)+int('9')
# print(x)

# 14
# print(a+b)
# a=5
# b=8
# define b4 expression


# # 15
# python_list=[1,2,3,4,5,6,7,8,9]
# for k in python_list:
#     if k==7:
#       pass
#     print("passbook",k)

# 16
# n=7
# c=0
# # 6,11
# # 6,5
# while n:
#     if (n>5):
#         c=c+n-1
#         n=n-1
#     else:
#         break
# print(n)
# print(c)

# 17\

# a=[[1,2,3],[4,5,6],[7,8,9]]
# print(a[1])
# 18

# i=0
# while i<5:
#     print(i)
#     i+=1
#     # 1,2,
#     if i==3:
#         break
#     else:
#         print(0)
#19
# strin="fhg kdajvk knkj"
# str1="ghvgshudgv"
# for i in ' '.join(strin.split()):
#  print(i)
# 20
# a=['ldfvsd','adfd','gdfvsd']
# b=''.join(list(map(str,a)))
# print(b)
# 21
# a=[[1,2,3],[4,5,6],[7,8,9]]
# lst=[a[row][1] for row in [0,1,2]]
# print(lst)

numberGames={}
numberGames[(1,2,4)]=8
numberGames[(4,2,1)]=10
numberGames[(1,2)]=12
# The tuples (1, 2, 4), (4, 2, 1), and (1, 2) are used as keys in the dictionary.
# Values assigned to these keys are 8, 10, and 12, respectively.
sum=0
for k in numberGames:
    sum+=numberGames[k]
print(len(numberGames)+sum)
