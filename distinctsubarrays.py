n=int(input())
a=[int(i) for i in input().split()]
k=len(set(a))
from collections import *
l=0;r=0;dis=0;final=0
d=defaultdict(lambda:0)
for i in range(n):
    if d[a[i]]==0:
        dis+=1
    d[a[i]]+=1
    if dis==k:
        final+=n-i
        while d[a[l]]>1:
            d[a[l]]-=1
            final+=n-i
            l+=1
        d[a[l]]=0
        l+=1
        dis-=1
print(final)
