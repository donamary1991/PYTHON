#      1
#    1 2 1
#  1 2 3 2 1
# 1 2 3 4 3 2 1
# n=int(input("enter the number"))
# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")
#     print()
n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=' ')
    for k in range(0,i):
        print(k+1,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=' ')
    print()

**************************************************************************
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
# #
# for i in range(4,0,-1):
#     for j in range(0,i):
#         print("*", end=" ")
#     print()
# for i in range(2,5):
#     for j in range(i,0,-1):
#         print("*", end=" ")
#     print()

for i in range(1,5):
    for j in range(4,i-1,-1):
        print('*',end=' ')
    print()
for i in range(2,5):
    for j in range(1,i+1):
        print('*', end=' ')
    print()
******************************************************************************
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# for i in range(3,0,-1):
#     for j in range(0,i):
#         print(i, end=" ")
#     print()
for i in range(1,5):
    for j in range(1,i+1):
     print(i,end=' ')
    print()
for i in range(3,0,-1):
    for j in range(0,i):
        print(i,end=' ')
    print()



**************************************************************************************
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 
for i in range(1,6):
    for j in range(1,6):
     print(j,end=' ')
    print()
**************************************************************************************
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
************************************************************************************
# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5
#
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print("5", end=' ')
#     print()
for i in range(1,6):
    for j in range(5,i-1,-1):
        print("5",end=' ')
    print()

************************************************************************************************
 # 0 1 2 3 4 5
 # 0 1 2 3 4
 # 0 1 2 3
 # 0 1 2
 # 0 1
for i in range(5,0,-1):
    for j in range(0,i+1):
        print(j, end=' ')
    print()
***********************************************************************************************
# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11 12 13  14 15
# k=1
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(k,end=' ')
#         k+=1
#     print()
k=1
for i in range(1,7):
    for j in range(1,i):
        print(k,end=' ')
        k+=1
    print()
*******************************************************************************************************
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
    *************************************************************************************************************
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


for i in range(1,6):
    for j in range(1,i+1):
     print(i, end=" ")
    print()

