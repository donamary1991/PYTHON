1. Write a Python script to find all prime numbers in the range from 1 to 100
# and add them to a list. Then, calculate the sum and the average of these
# prime numbers, and print the list of prime numbers, the sum, and the
# average.



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

