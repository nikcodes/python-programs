n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]

b=[i for i in range(n) if a[i]<0]
l=len(b)

bp=0

i,j=0,k-1
printed=0

while j<n:
    if bp==l:
        break

    if b[bp]>j:
        print(0,end=' ')

    elif i<=b[bp]<=j:
        if b[bp] == i:
            print(a[i],end=' ')
            bp+=1

        else:
            print(a[b[bp]],end=' ')

    printed+=1
    i+=1
    j+=1

for _ in range(n-k+1-printed):
    print(0,end=' ')
