import math

def prime(n):
    i = 5
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    else:
        while i*i < n:
            if n % i == 0 or n % (i+2) == 0:
                return False
            i += 6
        return True

n, m = map(int, input().strip().split())
a = []
for i in range(n):
    a.append([])
    while len(a[i]) < m:
        a[i].extend(list(map(int, input().strip().split())))
for i in range(n):
    for j in range(m):
        if(prime(a[i][j])):
            print("1", end = " ")
        else:
            print("0", end = " ")
    print()