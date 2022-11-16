from math import log2

def change(n, s):
    if len(s) % n != 0:
        for i in range(n - len(s) % n):
            s = '0' + s
    k = 0
    res = ''
    for i in range(len(s)):
        k += int(s[i]) * 2 ** (n - 1 - i % n)
        if (i + 1) % n == 0:
            if   k > 9:     res += chr(k + 55)
            else:           res += str(k)
            k = 0
    return res
t = int(input())
for i in range(t):
    n = int(input())
    n = (int)(log2(n))
    s = input()
    print(change(n, s))
    