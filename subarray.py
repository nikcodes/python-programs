n = int(input())
a = [int(i) for i in input().split()]
for i in range(n):
    if a[i]%2:
        a[i]=-1
    else:
        a[i]=1
b=[a[0]]
for e in a[1:]:
    b.append(b[-1]+e)
c=b.count(0)
from collections import *
d=defaultdict(lambda:0)
for e in b:
    d[e]+=1
for v in d.values():
    t=v*(v-1)//2
    c+=t
print(c)
