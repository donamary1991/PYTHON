# Oru string number extract cheythit sum kandupidikan
str1="apple3banana5orange5"
a='123456789'
lst=[]
for i in str1:
    if i in a:
        lst.append(int(i))
print(sum(lst))
