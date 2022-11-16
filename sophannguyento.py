from math import log
from bisect import bisect_left
import sys
MAXN = 2*1e7


def gen_primes():
    primes = []
    primes_product = 1
    for n in range(2, 10**10):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
        if is_prime:
            primes.append(n)
            primes_product *= n
            if primes_product > MAXN:
                break
    return primes


primes = gen_primes()


def gen_hcn():
    hcn = [(1, 1, [])]
    for i in range(len(primes)):
        new_hcn = []
        for el in hcn:
            new_hcn.append(el)
            if len(el[2]) < i:
                continue
            e_max = el[2][i-1] if i >= 1 else int(log(MAXN, 2))
            n = el[0]
            for e in range(1, e_max+1):
                n *= primes[i]
                if n > MAXN:
                    break
                div = el[1] * (e+1)
                exponents = el[2] + [e]
                new_hcn.append((n, div, exponents))
        new_hcn.sort()
        hcn = [(1, 1, [])]
        for el in new_hcn:
            if el[1] > hcn[-1][1]:
                hcn.append(el)
    return hcn


hcn = gen_hcn()
a = []
for i in hcn:
    a.append(i[0])
t = int(input())
for _ in sys.stdin:
    x = int(_)
    print(a[bisect_left(a, x)])

