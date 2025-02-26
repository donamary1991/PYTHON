# Pinne 2 string il inn special characters remove chyth single string avan
str1="dona!mary@george"
str2="varghese$Jacob&v"
a='!@$&'

for i in (str1+str2):
    if i not in a:
        print(i,end='')
