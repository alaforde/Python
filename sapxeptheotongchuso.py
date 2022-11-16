def summary(n):
    s, sum = str(n), 0
    for i in s:
        sum += int(i)
    return sum*100000000000000000000+n

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    a.sort(key = summary)
    print(*a)