a=input()
s=input()
if len(set(a))==len(set(s))==1:
    print(len(s)-len(a)+1)
else:
    l=len(s)
    lena=len(a)
    final=0
    from collections import *
    ad=defaultdict(lambda:0)
    for c in a:
        ad[c]=1
    d=defaultdict(lambda:[])
    for i in range(l):
        if ad[s[i]]:
            d[s[i]].append(i)
    for e in d[a[0]]:
        t=e;ind=1
        if l-t<lena:
            break
        while 1:
            if s[t+1]!=a[ind]:
                break
            if ind==lena-1:
                final+=1
                break
            t+=1
            ind+=1
    print(final)
