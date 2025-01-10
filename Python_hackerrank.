num=int(input())
if num % 2 != 0 :
    print("weird")
else:
    if num in range(2,6):
        print("not_weird")
    elif num in range(6,21):
        print("weird")
    elif num>20:
        print("not_weird")



def wrap(string, max_width):
    str = ''
    count = 0
    string+='\n'
    for i in string:
        str += i
        count += 1
        if(count==max_width)or(i=='\n') :
          print(str)
          count=0
          str=''


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


n1=int(input())
lst1=[]
lst2=[]
for i in range(n1):
    lst1.append(input())

set1=set(lst1)
print(set1)

n2=int(input())
for i in range(n2):
    lst2.append(input())

set2=set(lst2)
print(set2)
set3=set1 ^ set2
print(len(set3))



def swap_case(s):
    str=''
    for i in s:
        if i.isupper():
            i=i.lower()
            str+=i
        elif i.islower():
            str+=i.upper()
        else:
            str+=i
    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


def merge_the_tools(string, k):
    str=''
    for i in string:
        str+=i
        if len(str)==k:
            str1 = ''
            for j in str:
              if j not in str1:
                str1+=j
            print(str1)
            str=''
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

def split_and_join(line):
  a=line.split()
  print(a)
  b="-".join(a)
  print(b)
line=input("enter the string")
split_and_join(line)

# if __name__ == '__main__':
students = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

pmn = min(students, key=lambda x: x[1])
print(pmn)


lst=[int(i) for i in input().split()]
lst.sort(reverse=True)
# set1=set(lst)
# lst1=list(set1)
# lst1.sort(reverse=True)
# print(lst1[1])
x=max(lst)
for i in lst:
    if i==x:
        lst.remove(i)
        break
print(lst[1])


