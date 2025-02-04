# Write a program that uses a for loop to print numbers from 1 to 10, but breaks the loop when the number is 5.
for i in range(2,11):
 flag=0
 if (i == 5):
    break
 else:
    for j in range(2,i):
         if i%j==0:
          flag=1

    if flag==0:
            print(f'{i}  is prime\n')


 # Write a program that iterates over a list of integers and breaks the loop when a negative number is encountered.
lst=[1,2,9,-3,8,9]
for i in lst:
    if i >=0:
        print(i)
    else:
        break



# Write a program that prints all even numbers from 1 to 10 using a While loop and continue statement.
i=1
while(i<=10):

    if(i % 2)==0:
        print(i)
        i+=1
    else:
        i+=1
        continue


# Write a program that prints the sum of all positive numbers in a list using a for loop and continue statement.\
lst=[1,2,3,-8,5,-7,6,4]
sum=0
for i in lst:
    if i>=0:
        sum+=i
    else:
        continue
print(sum)
# Write a simple program that includes a pass statement in a for loop.
sum=0
for i in range(1,11):
    if i%2 ==0:
        sum+=i
    else:
        pass
        sum+=i
print(sum)
# Write a Python function that uses break to exit early if a certain condition is met while iterating through a list.
lst=[1,7,6,-2,8,4]
for i in lst:
    if i <0:
        break
    else:
        print(i)
# Write a program that uses continue to skip over certain iterations in a loop that processes a list of strings,
# skipping strings shorter than 3 characters.
strings = ["a", "abc", "defg", "hi", "jkl"]
for i in strings:
    if len(i)>=3:
        print(i)
    else:
        continue
# Write a Python function that processes a list of numbers,
# using continue to skip processing for numbers less than 5.
lst=[7,8,6,1,3,5,-9,4]
for i in lst:
    if i >=5:
        print(i)
    else:
        continue
# Write a program that uses break and continue in a nested loop to find
# and print the first pair of numbers (i, j) where i * j is greater than 10.
for i in range(1,11):
    for j in range(1,11):
        if i*j >10:
            print((i,j))
            break
        else:
            continue
# Write a program that uses break and continue in a nested loop to find
# and print the first pair of numbers (i, j) where i * j is greater than 10.
for i in range(1,11):
    for j in range(1,11):
        if i*j >10:
            print((i,j))
            break
        else:
            continue
