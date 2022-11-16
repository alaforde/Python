t = int(input())
for v in range(t):
    n = int(input())
    a = [True]*(n+1)
    b = []
    a[0] = a[1] = False
    for i in range(4, n+1, 2):
        a[i] = False
    for i in range(3, n+1, 2):
        if a[i] == True:
            b.append(i)
            j = 2*i
            while j < n:
                a[j] = False
                j = j+i
    for x in b:
        if x < int(str(x)[::-1]) and b.count(int(str(x)[::-1])):
            print(x, str(x)[::-1], end = ' ')
    print()
