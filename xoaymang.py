t = int(input())
for v in range(t):
    n, k = map(int, input().split())
    a = []
    while len(a) < n:
        a.extend(list(map(int, input().split())))
    for i in range(k, n):
        print(a[i], end = ' ')
    for i in range(0, k):
        print(a[i], end = ' ')
    print()
    