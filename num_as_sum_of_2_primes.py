class Solution:

    def primesum(self, n):
        global prime
        prime = []
        p = {i: 1 for i in range(2, n + 1)}
        spf = {}
        pl = 0

        for i in range(2, n + 1):
            if p[i]:
                prime.append(i)
                pl += 1

            for j in range(pl):
                if prime[j] * i > n:
                    break
                p[prime[j] * i] = 0
                spf[prime[j] * i] = prime[j]

    def f(self,n):
        d = {e: 1 for e in prime}
        for e in d:
            if n - e in d:
                return str(e) + ' + ' + str(n - e) + ' = ' + str(n)

o=Solution()
o.primesum(58)
print(o.f(58))
