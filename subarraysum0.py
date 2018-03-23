for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[a[0]]
    for e in a[1:]:
        b.append(b[-1]+e)
    if 0 in b:
        print('Yes')
    else:
        if len(set(b))<n:
            print('Yes')
        else:
            print('No')
