# n=int(input("enter the number"))
#
# print(*range(1,n),sep="")
# n1=int(input("enter the number"))
# n2=int(input("enter the number"))
# print(n1+n2)
n1=input("enter the number")
print(n1.split())
print(map(int,n1.split()))
print(list(map(int,n1.split())))


arr= [int(n) for n in input().split()]
# print(len(arr))
m=max(arr)
c=None
for j in arr:
 if j==m:
    pass
 elif c==None:
     c=j
 elif j>c:
     c=j

print(c)

n = int(input())

student_marks = {}

for _ in range(n):
    name,*line = input().split()
    print(name)
    print(line)

    scores = list(map(float, line))


    student_marks[name] = scores
print(student_marks)
query_name = input()
#
l1 = list(student_marks[query_name])
print(l1)
addition = sum(l1)
#
result = addition / len(l1)

print('%.2f' % result)



for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end=' ')
    print(' ')



