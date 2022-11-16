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
n, x = map(int, input().split())
for i in range(n+1):
    print(x, end = ' ')
    x += b[i]