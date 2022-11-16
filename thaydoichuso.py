def RePl(a, b, s):
    s = str(s)
    s = s.replace(str(a), str(b))
    return int(s)


n = int(input())
while n > 0:
    n -= 1
    a = []
    while len(a) < 4:
        a.extend(list(map(str, input().strip().split())))
    u = min(a[0], a[1])
    v = max(a[0], a[1])
    print(RePl(v, u, a[2])+RePl(v, u, a[3]), end=' ')
    print(RePl(u, v, a[2])+RePl(u, v, a[3]))
