# PYTHON
# SET A
# 1. Write a Python script to find all prime numbers in the range from 1 to 100
# and add them to a list. Then, calculate the sum and the average of these
# prime numbers, and print the list of prime numbers, the sum, and the
# average.
# count=0
# lst=[]
# for i in range(1,101):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#
#     if count ==0 :
#         lst.append(i)
#
# print(lst)
# s=sum(lst)
# l=len(lst)
# a=s/l
# print(s)
# print(a)


count=0
lst=[]
for i in range(2,100):
    count = 0
    for j in range(2,i):

        if i%j==0:
            count=1
            break

    if count==0:
        lst.append(i)
print(lst)
s=sum(lst)
print(sum(lst))
print(s/len(lst))




***********************************************************************************************
# 2. Write a program to find the second largest number in a given list of integers.
# Then, perform the following tasks:
# Remove all occurrences of the second largest number from the list.
# Calculate the sum of the remaining numbers in the list.
# Sort the modified list in ascending order and print it.
lst=[2,5,4,7,9,1,6,8,8]
# lst1=[]
# lst.sort(reverse=True)
# print(lst[1])
# s=lst[1]
# for i in lst:
#     if i != s:
#      lst1.append(i)
# print(lst1)
# print(sum(lst1))
# lst1.sort()
# print(lst1)
lar=max(lst)
print(lar)
lst_without_lar=[]
lst_final=[]
for i in lst:
    if i != lar:
        lst_without_lar.append(i)
print(lst_without_lar)
lst_without_lar.sort()
for i in lst_without_lar:
 if i!=max(lst_without_lar):
     lst_final.append(i)


print(sum(lst_final))
lst_final.sort()
print(lst_final)






*******************************************************************************************************************************************************
# 3. Write a Python script using list comprehension to perform the following
# tasks on a given list of integers:
# Create a new list containing the squares of all odd numbers from the original
# list.
# Create another list containing the cubes of all even numbers from the
# original list.
# Combine these two lists into a single list and sort it in descending order.
# Print the final sorted list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst=[i**2 for i in numbers ]
# print(lst)
# lst1=[i**3 for i in numbers if i%2==0]
# print(lst1)
# lst3= lst + lst1
# lst3.sort(reverse=True)
# print(lst3)
lst_odd=[i**2 for i in numbers if i%2!=0]
print(lst_odd)
lst_even=[i**3 for i in numbers if i %2==0]
print(lst_even)
lst_com=lst_odd+lst_even
lst_com.sort(reverse=True)
print(lst_com)
