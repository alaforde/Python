def gcd(a, b):
    if a % b == 0: 
        return b
    return gcd(b, a%b)
n, k = map(int, input().strip().split())
a = 10**(k-1)
b = 10**k
cnt = 0
for i in range(a, b):
    if gcd(i, n) == 1:
        print(i, end = ' ')
        cnt += 1
        if cnt % 10 == 0:
            print()