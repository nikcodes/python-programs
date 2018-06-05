a=[int(i) for i in input().split()]
n=len(a)

s=0
ans=0

for i in  range(n):
    a[i]+=s
    if a[i]:
        ans+=1
    s-=a[i]

print(ans)
