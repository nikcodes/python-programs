n=int(input())
a=[int(i) for i in input().split()]
l=0
r=n-1
cs=0
if n>a[-1]:
    a.append(n)
elif n<a[0]:
    a.insert(0,n)
else:
    while l<=r:
        m=(l+r)//2
        if a[m]==n:
            a.insert(m+1,n)
            cs=1
            break
        if a[m]>=n and a[m-1]<=n:
            a.insert(m,n)
            break
        if a[m]<=n and a[m+1]>=n:
            a.insert(m+1,n)
            break
        if a[m]>n:
            r=m-1f
        else:
            l=m+1
print(a)
