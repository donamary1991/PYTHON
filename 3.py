# Oru  string etavum kuduthal repeat letter countstr
str1='ababcabcdabcde'
str=''
for i in str1:
    if i not in str:
        str+=i
print(len(str))

# Oru  string etavum kuduthal repeat letter count
str1='aababcabcdabcde'
dic={}
for i in str1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

l=max(dic.values())
for i in dic:
    if dic[i]==l:
        print(i)

str=''

