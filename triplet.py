a = [True]*(1000000)
b = []
a[0] = a[1] = False
for i in range(2, 1000000):
    if (a[i] == True):
        b.append(i)
        j = i*2
        while j < 1000000:
            a[j] = False
            j += i
t = int(input())
for v in range(t):
    n = int(input())
    i = 0
    ans = 0
    while b[i]+6 < n:
        if b[i+1] == b[i]+2 and b[i+2] == b[i]+6:
               ans += 1
        if b[i+1] == b[i]+4 and b[i+2] == b[i]+6:
               ans += 1
        i += 1
    print(ans)