s=input()
a=s[::-1]
n=len(s)
if len(set(list(s)))==1:
    print(0)
elif s!=a:
    print(n)
else:
    print(n-1)
