s=input()
a=s[::-1]
n=len(s)
if s!=a:
    print(n)
else:
    c=0;m=0
    for e in s:
        if e!=s[-1]:
            break
        c+=1
    m=max(m,n-c)
    c=0
    for e in s[::-1]:
        if e!=s[0]:
            break
        c+=1
    print(max(m,n-c))
