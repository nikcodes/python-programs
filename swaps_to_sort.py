a=[int(i) for i in input().split()]
b=sorted(a)
l=len(a)
db={}
for i in range(l):
    db[b[i]]=i
from collections import *
check=defaultdict(lambda:1)
s=0
ideal={}
for i in range(l):
    ideal[i]=db[a[i]]

for i in range(l):
    j=i
    count=0
    if check[i]:
        check[i]=0
        while i != ideal[j]:
            count+=1
            j=ideal[j]
            check[j]=0
        s+=count

print(s)
