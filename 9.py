# Q. Write a program to find the second largest number in a given list of integers.
# Then, perform the following tasks:
# Remove all occurrences of the second largest number from the list.
# Calculate the sum of the remaining numbers in the list.
# Sort the modified list in ascending order and print it.
from numpy.ma.extras import average

# lst = [56, 62, 70, 31, 2, 4, 70, 13, 29, 4, 9, 62, 45]
# lst=[7,7,8,1,2,3,4,4,5]
# print(lst)
# lst1=[i for i in lst if i!=max(lst)]
# print(f'Second largest number is{max(lst1)}')
# lst2=[i for i in lst if i!=max(lst1)]
# print(lst2)
# print(sum(lst2))
# lst2.sort()
# print(lst2)


# Bank domain:

# Design a program for the bank domain where there are unlimited denominations of coins (e.g., 1, 2, 5, 10).
# The program takes an amount as input (e.g., 7) and calculates the minimum number of coins needed to sum up to that amount.
# For instance, if the input is 7, the output should be 2,
# as the minimum number of coins to make 7 is 2 (using one 5-coin and one 2-coin).

# coins = [10, 5, 2, 1]
# # amt = int(input("Enter the amount: "))
# sum=7
# lst= min([i+j+k+l for i in range(0,10) for j in range(0,10) for k in range(0,10) for l in range(0,10) if i*10+j*5+k*2+l*1==sum])
#
# print(lst)

# 3. Write a Python script using list comprehension to perform the following
# tasks on a given list of strings:

# Create a new list containing the length of each string in the original list--

# if the string contains the letter 'e' and its length is greater than 3.
    # Create another list containing the square of each length from
    # the first list. --
    # Filter this second list to keep only values that are even.
    # Print the final list of squares that are even.

# string_lst = ["apple", "banana", "cucumber", "mango", "pineapple"]
# len_lst=[len(i) for i in string_lst]
# print(len_lst)
# lst1=[len(i)**2 for i in string_lst if 'e' in i and len(i)>3]
# print(lst1)
# lst2=[i for i in lst1 if i%2==0]
# print(lst2)

# . Write a Python script to find all perfect numbers in the range from 1 to
# 10000 and add them to a list. Then, calculate the sum and the average of
# these perfect numbers. Additionally, determine and print the smallest and
# largest perfect numbers within this range.
# lst=[]
# for i in range(1,10000):
#     sum1=0
#     for j in range(1,i):
#         if i%j==0:
#             sum1+=j
#     if sum1==i:
#         lst.append(i)
# print(lst)
#
#
# print(f'sum is {sum(lst)}')
# print(f'average is{average (lst)}')
# print(f'min value is {min(lst)}')
# print(f'max value is {max(lst)}')

# 1. Write a Python script to find all prime numbers in the range from 1 to 100
# and add them to a list. Then, calculate the sum and the average of these
# prime numbers, and print the list of prime numbers, the sum, and the
# average.
# lst=[]
# for i in range(1,100):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#     if count==0:
#         lst.append(i)
# print(lst)
# print(sum(lst))
# # print(sum(lst)/len(lst))
# print(average(lst))

# 3. Write a Python script using list comprehension to perform the following tasks on a given list of integers:

# Create a new list containing the squares of all odd numbers from the original list
# Create another list containing the cubes of all even numbers from the original list.
# Combine these two lists into a single list and sort it in descending order.
# Print the final sorted list.

lst = [3, 5, 7, 6, 17, 14, 26, 25, 33, 28, 52, 63, 77, 80]
lst_odd=[i**2 for i in lst if i %2!=0]
print(lst_odd)
lst_even=[i**3 for i in lst if i %2==0]
print(lst_even)
lst_add=lst_odd+lst_even
lst_add.sort(reverse=True)
print(lst_add)

