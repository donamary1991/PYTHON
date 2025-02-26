
# Input : test_list = [4, 5, 5, 5, 5, 6, 6, 7, 8, 2, 2, 10]
# Output : 3
# Explanation : 5, 6 and 2 has identical element as their next element.
a= [4, 5, 5, 5, 5, 6, 6, 7, 8, 2, 2, 10]
dic={}
for i in range(0,len(a)):
    if a[i]==a[i-1]:
        print(a[i])
        if a[i] not in dic:
         dic[a[i]]=2
        else:
         dic[a[i]]+=1
print(dic)

