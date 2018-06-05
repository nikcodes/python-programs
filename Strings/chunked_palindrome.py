'''

Given a string, the task is to return the length of its longest possible chunked palindrome.
It means a palindrome formed by substring in the case when it is not formed by characters of the string.



Input : ghiabcdefhelloadamhelloabcdefghi 
Output : 7
(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)

Input : merchant
Output : 1
(merchant)

Input : antaprezatepzapreanta
Output : 11
(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)

Input : geeksforgeeks
Output : 3
(geeks)(for)(geeks)

'''

s=input()
n=len(s)

def f(s,n):
    if n==0:
        return 0
    if n==1:
        return 1

    for i in range(n//2):
        if s[:i+1]==s[n-i-1:]:
            return 2+f(s[i+1:n-i-1],n-2*i-2)
    return 1

print(f(s,n))
