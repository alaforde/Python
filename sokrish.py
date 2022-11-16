def gt(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s
t = int(input())
for v in range(t):
    n = input()
    sum = 0
    for i in n:
        sum += gt(int(i))
    if sum == int(n):
        print("Yes")
    else:
        print("No")