from collections import *
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    k=int(input())
    d=defaultdict(lambda:0)
    for e in a:
        d[e] += 1
    a=set(a)
    if k==0:
        c=0
        for ke,v in d.items():
            if v>1:
                c+=1
        print(c)
    else:
        for e in a:
            d[e]=1
        visited=defaultdict(lambda:1)
        c=0
        for e in a:
            if visited[e]:
                visited[e]=0
                if d[e+k]:
                    c+=1
        print(c)
