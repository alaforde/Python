t = int(input())
for v in range(t):
    n = int(input())
    a = []
    b = []
    ok = True
    while len(a) < n:
        a.extend(list(map(int, input().strip().split())))
    while len(b) < n:
        b.extend(list(map(int, input().strip().split())))
    a = sorted(a)
    b = sorted(b)
    for i in range(n):
        if a[i] > b[i]:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
    
        