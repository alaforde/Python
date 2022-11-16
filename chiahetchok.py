a, k, n = map(int, input().split())
if k - a%k + a > n:
    print("-1")
else:
    b = (a//k) + 1
    if (b*k) <= n:
        c = b*k - a
        while c <= n - a:
            print(c, end = " ")
            c += k