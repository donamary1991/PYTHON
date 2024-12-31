n = int(input())
s = set(map(int, input().split()))
step=int(input())
for i in range(step):
 op=input()
 lst=op.split()
 print(lst)
 if lst[0]=='pop':
     s.pop()

 elif lst[0] =='remove':
     s.remove(int(lst[1]))

 elif lst[0] == 'discard':
     s.discard(int(lst[1]))


 print(sum(s))
