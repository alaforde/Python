while True:
    a = list(int(i) for i in input().split())
    if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0:
        break
    cnt = 0
    while(a[0] != a[1] or a[1] != a[2] or a[2] != a[3]):
        cnt += 1
        b = a[0]
        a[0] = abs(a[0]-a[1])
        a[1] = abs(a[1]-a[2])
        a[2] = abs(a[2]-a[3])
        a[3] = abs(a[3]-b)
    print(cnt)