from collections import defaultdict
for _ in range(int(input())):
    n,s=input().split()
    n=int(n)
    d=defaultdict(lambda:'.')
    d[1]=s[0]
    l=len(s)
    j=1
    s+='&'*3
    for i in range(l):
        if s[i]=='(':
            j*=2
        elif s[i]==')':
            j=j//2
            if j%2==0:
                j+=1
        else:
            d[j]=s[i]
            if s[i+1]!='(' and s[i+1]!=')':
                j+=1

    level=defaultdict(lambda:[])
    class node:
        def __init__(self,d,ind,level):
            self.d=d
            self.ind=ind
            self.level=level
        l,r=None,None
    root=node(s[0],1,0)
    def add(nodelist):
        next=[]
        for e in nodelist:
            ind=e.ind
            level[e.level].append(e.d)
            if d[2*ind]!='.':
                e.l=node(d[2*ind],2*ind,e.level-1)
                next.append(e.l)
            if d[2*ind+1]!='.':
                e.r=node(d[2*ind+1],2*ind+1,e.level+1)
                next.append(e.r)
        if next==[]:
            return
        add(next)
    add([root])
    for k in level.keys():
        level[k].sort()
    if level[n]:
        print(''.join(level[n]))
    else:
        print('Common Gandhijee!')
