for _ in range(int(input())):
    s = input()
    z = []
    i = 0
    for c in s:
        if c == 'Z':
            z.append(i)
        i += 1
    # from front
    i = 0
    for c in s:
        if c == 'O':
            f = i
            break
        i += 1
    count = 0
    for e in z:
        if e > f:
            count += (e - f)
            f += 1

    # towards last
    i = len(s) - 1
    for c in s[::-1]:
        if c == 'O':
            break
        i -= 1
    co = 0
    for e in z[::-1]:
        if e < i:
            co += (i - e)
            i -= 1
    print(min(co, count))
