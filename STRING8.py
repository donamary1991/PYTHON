str = "aabbbccccdddddeeffgggggg"
dic={}
for i in str:
    if i not in dic:
        dic[i]=1
    else :
        dic[i]+=1
print(dic)
m=max(dic.values())
for i,j in dic.items():
    if j==m:
        print(i)
