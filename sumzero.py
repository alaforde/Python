t = int(input())
for v in range(t):
    n = int(input())
    a = []
    while len(a) < n:
        a.extend(list(map(int, input().strip().split())))
    a = sorted(a)
    cnt = 0
    for i in range(len(a)):
        f = i+1
        l = n-1
        while f < l:
            if a[f] + a[l] + a[i] < 0:
                f += 1
            elif a[f] + a[l] + a[i] > 0:
                l -= 1
            else:
                cnt += 1
                i += 1
    print(cnt) 